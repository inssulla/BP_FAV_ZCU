
import argparse
import os
import sys
from threading import Thread

from test_picovoice import Picovoice
from pvrecorder import PvRecorder

# import simulation as s
from simulation import calculate_camera_direction 
from simulation import calculate_solar_direction
import time


class PicovoiceDemo(Thread):
    def __init__(
            self,
            keyword_path,
            context_path,
            access_key,
            device_index,
            porcupine_sensitivity=0.75,
            rhino_sensitivity=0.25):
        super(PicovoiceDemo, self).__init__()

        self._picovoice = Picovoice(
            access_key=access_key,
            keyword_path=keyword_path,
            wake_word_callback=self._wake_word_callback,
            context_path=context_path,
            porcupine_sensitivity=porcupine_sensitivity,
            rhino_sensitivity=rhino_sensitivity)

        self._device_index = device_index
        
        
    # Funkce ktera probehne po KWS
    def _wake_word_callback(self): 
        print('Wake word detected\n')
        self.recorder.stop()
        calculate_camera_direction()
        self.start_time = time.time()
        self.recorder.start()
       
        
        
        
    def run(self):
        self.recorder = None
        try:
            self.recorder = PvRecorder(device_index=self._device_index, frame_length=self._picovoice.frame_length)
            self.recorder.start()
            print('[Listening ...]')
            self.start_time = time.time()
            self.start_time_v2 = 10
            while True:
                pcm = self.recorder.read()
                self._picovoice.process(pcm)

                if (time.time() - self.start_time) > 10:
                    print((time.time() - self.start_time), '+')

                    if (time.time() - self.start_time_v2) > 10:
                        self.recorder.stop()
                        calculate_solar_direction()
                        self.start_time_v2 = time.time()
                        self.recorder.start()
                else:
                    print((time.time() - self.start_time))

        except KeyboardInterrupt:
            sys.stdout.write('\b' * 2)
            print('Stopping ...')
        finally:
            if self.recorder is not None:
                self.recorder.delete()
                
            self._picovoice.delete()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--access_key',
        help='AccessKey obtained from Picovoice Console (https://console.picovoice.ai/)',
        required=False,default ='jmO3cG5bPAg+eCRAa96TgxAzUWU42E+ZY/WzhHBPQAf9JgdLB3WQyg==')

    parser.add_argument('--audio_device_index', help='Index of input audio device.', type=int, default=-1)
    args = parser.parse_args()
    o = PicovoiceDemo(
        os.path.join(os.path.dirname(__file__), 'Keyword.ppn'),
        os.path.join(os.path.dirname(__file__), 'respeaker_raspberry-pi.rhn'),
        args.access_key,
        args.audio_device_index
    )
    o.run()
    

if __name__ == '__main__':        
    main()
    