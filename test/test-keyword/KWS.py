
import argparse
import os
import sys
from threading import Thread

from test_picovoice import Picovoice
from pvrecorder import PvRecorder


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
        
        
        
    def run(self):
        recorder = None
        try:
            recorder = PvRecorder(device_index=self._device_index, frame_length=self._picovoice.frame_length)
            recorder.start()
            print('[Listening ...]')
            while True:
                pcm = recorder.read()
                self._picovoice.process(pcm)
        except KeyboardInterrupt:
            sys.stdout.write('\b' * 2)
            print('Stopping ...')
        finally:
            if recorder is not None:
                recorder.delete()
                
            self._picovoice.delete()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--access_key',
        help='AccessKey obtained from Picovoice Console (https://console.picovoice.ai/)',
        required=True)

    parser.add_argument('--audio_device_index', help='Index of input audio device.', type=int, default=-1)
    args = parser.parse_args()
    o = PicovoiceDemo(
        os.path.join(os.path.dirname(__file__), 'Bot.ppn'),
        os.path.join(os.path.dirname(__file__), 'respeaker_raspberry-pi.rhn'),
        args.access_key,
        args.audio_device_index
    )
    o.run()
    

if __name__ == '__main__':        
    main()
    