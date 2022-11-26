
import sys
import webrtcvad
import time
import math
import numpy as np
#from pixel_ring import pixel_ring
#from test_lights import leds
from test_direction import MicArray

import apa102
from gpiozero import LED


RATE = 16000
CHANNELS = 4
VAD_FRAMES = 10     # ms
DOA_FRAMES = 200    # ms

driver = apa102.APA102(num_led=12)
power = LED(5)
#power.on()

COLORS_RGB = dict(
        blue=(0, 0, 255),
        green=(0, 255, 0),
        orange=(255, 128, 0),
        pink=(255, 51, 153),
        purple=(128, 0, 128),
        red=(255, 0, 0),
        white=(255, 255, 255),
        yellow=(255, 255, 51),
    )

def rounding(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier

def set_color(color, direction):
    power.on()
    # for i in range(12):
    #     driver.set_pixel(i, color[0], color[1], color[2])
    position = int(rounding((direction + 15) % 360 / 15)) % 24 
    if position != 0 and (position % 2) == 0:
        position = int(position / 2) 
        driver.set_pixel(position, color[0], color[1], color[2])
        driver.set_pixel(position - 1, color[0], color[1], color[2])
    else:    
        position = int(position / 2)
        driver.set_pixel(position, color[0], color[1], color[2])
    
    driver.show()
    time.sleep(0.1)
    power.off()
    driver.clear_strip()

def main():
    vad = webrtcvad.Vad(1)

    speech_count = 0
    chunks = []
    doa_chunks = int(DOA_FRAMES / VAD_FRAMES)

    COLORS_RGB = dict(
        blue=(0, 0, 255),
        green=(0, 255, 0),
        orange=(255, 128, 0),
        pink=(255, 51, 153),
        purple=(128, 0, 128),
        red=(255, 0, 0),
        white=(255, 255, 255),
        yellow=(255, 255, 51),
    )
    
    try:
        with MicArray(RATE, CHANNELS, RATE * VAD_FRAMES / 1000)  as mic:
            for chunk in mic.read_chunks():
                # Use single channel audio to detect voice activity
                if vad.is_speech(chunk[0::CHANNELS].tobytes(), RATE):
                    speech_count += 1

                chunks.append(chunk)
                if len(chunks) == doa_chunks:
                    if speech_count > (doa_chunks / 2):
                        frames = np.concatenate(chunks)
                        direction = mic.get_direction(frames)
                        set_color(COLORS_RGB['blue'], direction)
                        print('\n{}'.format(int(direction)))
                        
                        position = int(rounding((direction + 15) % 360 / 15) % 24 )
                        print(position)
                        

                    speech_count = 0
                    chunks = []

    except KeyboardInterrupt:
        pass
        
   # pixel_ring.off()


if __name__ == '__main__':
    main()
