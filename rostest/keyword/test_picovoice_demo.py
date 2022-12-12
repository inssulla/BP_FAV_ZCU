#
# Copyright 2020-2022 Picovoice Inc.
#
# You may not use this file except in compliance with the license. A copy of the license is located in the "LICENSE"
# file accompanying this source.
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
#

import argparse
import os
import struct
import sys
from threading import Thread

from gpiozero import LED
from test_picovoice import Picovoice
from pvrecorder import PvRecorder

from apa102 import APA102

import json
import rospy
from std_msgs.msg import String


class PicovoiceDemo(Thread):
    def __init__(
            self,
            ros_publisher,
            keyword_path,
            context_path,
            access_key,
            device_index,
            porcupine_sensitivity=0.75,
            rhino_sensitivity=0.25):
        super(PicovoiceDemo, self).__init__()
        
        self.ros_publisher = ros_publisher

        self._picovoice = Picovoice(
            access_key=access_key,
            keyword_path=keyword_path,
            wake_word_callback=self._wake_word_callback,
            context_path=context_path,
            porcupine_sensitivity=porcupine_sensitivity,
            rhino_sensitivity=rhino_sensitivity)

        self._context = self._picovoice.context_info

        self._device_index = device_index


    def _wake_word_callback(self):
        print('[wake word]')
        
        keyword = "Hey robot" 
        structure = {
            "direction": keyword 
        }
        str_structure = json.dumps(structure)
        rospy.loginfo(str_structure)
        self.ros_publisher.publish(str_structure)
        
        print('Publish is Done\n')

    def run(self):
        recorder = None

        try:
            recorder = PvRecorder(device_index=self._device_index, frame_length=self._picovoice.frame_length)
            recorder.start()

            # print(self._context)

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
    
    ros_publisher = rospy.Publisher('/mics/keyword_detected', String, queue_size=10)
    rospy.init_node('keyword_detected', anonymous=True)

    o = PicovoiceDemo(
        ros_publisher,
        os.path.join(os.path.dirname(__file__), 'Keyword.ppn'),
        os.path.join(os.path.dirname(__file__), 'respeaker_raspberry-pi.rhn'),
        args.access_key,
        args.audio_device_index
    )
    o.run()


if __name__ == '__main__':        
    main()
