import pyaudio
import queue as Queue
import threading
import numpy as np
from gcc_phat import gcc_phat
import math


SOUND_SPEED = 343.2

MIC_DISTANCE_4 = 0.08127
MAX_TDOA_4 = MIC_DISTANCE_4 / float(SOUND_SPEED)


class MicArray(object):


    def __init__(self, rate=16000, channels=4, chunk_size=None):
        self.pyaudio_instance = pyaudio.PyAudio()
        self.queue = Queue.Queue()
        self.quit_event = threading.Event()
        self.channels = channels
        self.sample_rate = rate
        self.chunk_size = chunk_size if chunk_size else rate / 100

        device_index = None
        for i in range(self.pyaudio_instance.get_device_count()):
            dev = self.pyaudio_instance.get_device_info_by_index(i)
            name = dev['name'].encode('utf-8')
            print(i, name, dev['maxInputChannels'], dev['maxOutputChannels'])
            if dev['maxInputChannels'] == self.channels:
                print('Use {}'.format(name))
                device_index = i
                break

        if device_index is None:
            raise Exception('can not find input device with {} channel(s)'.format(self.channels))

        self.stream = self.pyaudio_instance.open(
            input=True,
            start=False,
            format=pyaudio.paInt16,
            channels=self.channels,
            rate=int(self.sample_rate),
            frames_per_buffer=int(self.chunk_size),
            stream_callback=self._callback,
            input_device_index=device_index,
        )


    def _callback(self, in_data, frame_count, time_info, status):
        self.queue.put(in_data)
        return None, pyaudio.paContinue


    def start(self):
        self.queue.queue.clear()
        self.stream.start_stream()


    def read_chunks(self):
        self.quit_event.clear()
        while not self.quit_event.is_set():
            frames = self.queue.get()
            if not frames:
                break

            frames = np.fromstring(frames, dtype='int16')
            yield frames


    def stop(self):
        self.quit_event.set()
        self.stream.stop_stream()
        self.queue.put('')
        

    def __enter__(self):
        self.start()
        return self


    def __exit__(self, type, value, traceback):
        if value:
            return False
        self.stop()


    def get_direction(self, buf):
        best_guess = None
        if self.channels == 4:
            MIC_GROUP_N = 2
            MIC_GROUP = [[0, 2], [1, 3]]

            tau = [0] * MIC_GROUP_N
            theta = [0] * MIC_GROUP_N
            for i, v in enumerate(MIC_GROUP):
                tau[i], _ = gcc_phat(buf[v[0]::4], buf[v[1]::4], fs=self.sample_rate, max_tau=MAX_TDOA_4, interp=1)
                theta[i] = math.asin(tau[i] / MAX_TDOA_4) * 180 / math.pi

            if np.abs(theta[0]) < np.abs(theta[1]):
                if theta[1] > 0:
                    best_guess = (theta[0] + 360) % 360
                else:
                    best_guess = (180 - theta[0])
            else:
                if theta[0] < 0:
                    best_guess = (theta[1] + 360) % 360
                else:
                    best_guess = (180 - theta[1])

                best_guess = (best_guess + 90 + 180) % 360


            best_guess = (-best_guess + 120) % 360

        return best_guess
    
