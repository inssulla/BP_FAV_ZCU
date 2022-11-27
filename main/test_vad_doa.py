
import sys
import webrtcvad
import time
import math
import numpy as np
import threading
import multiprocessing
#from pixel_ring import pixel_ring
#from test_lights import leds
from test_direction import MicArray

import apa102
from gpiozero import LED


RATE = 16000
CHANNELS = 4
VAD_FRAMES = 10     # ms
DOA_FRAMES = 200    # ms

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

driver = apa102.APA102(num_led=12)
power = LED(5)
#power.on()


def rounding(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier

def max_value(lst):
    for value in lst:
        count = lst.count(value)
        if count > 1:
            return value
        
    return lst[-1]

def buffer(direction, b1, b2):
    
    bool = False
    b1.append(direction)
    if len(b1) == 3:
        # Find max count of value
        bool = True
        max_value_b1 = max_value(b1)
        b2.append(max_value_b1)   
        b1.clear() 
    
    # Find and return max val from b2
    if len(b2) > 1 and bool == True:
        bool = False
        max_value_b2 = max_value(b2)
        if len(b2) == 3:
            del b2[0]    
        return max_value_b2


def set_color(color, direction, b):
    
    if b != direction: # turn off lights when another direction
        driver.clear_strip()
    
    power.on()
    position = int(rounding((direction + 15) % 360 / 15)) % 24 
    if position != 0 and (position % 2) == 0:
        position = int(position / 2) 
        driver.set_pixel(position, color[0], color[1], color[2])
        driver.set_pixel(position - 1, color[0], color[1], color[2])
    else:    
        position = int(position / 2)
        driver.set_pixel(position, color[0], color[1], color[2])
    
    driver.show()
        
        
def turn_off_leds():
    time.sleep(2) # 2 secs
    power.off()


def main():
    vad = webrtcvad.Vad(3)

    speech_count = 0
    chunks = []
    doa_chunks = int(DOA_FRAMES / VAD_FRAMES)
    
    b1 = [] # buffer 1
    b2 = [] # buffer 2
    b = 0   # previous direction
    
    # Turn off leds 
    proc = multiprocessing.Process(target=turn_off_leds)
    proc.start()
    
    try:
        with MicArray(RATE, CHANNELS, RATE * VAD_FRAMES / 1000)  as mic:
            for chunk in mic.read_chunks():
                # Use single channel audio to detect voice activity
                if vad.is_speech(chunk[0::CHANNELS].tobytes(), RATE):
                    speech_count += 1
                
                chunks.append(chunk)
                if len(chunks) == doa_chunks:
                    
                    if speech_count > (doa_chunks / 2):
                        
                        # Restart multiprocessing
                        proc.terminate()
                        time.sleep(0.05)
                        proc = multiprocessing.Process(target=turn_off_leds)
                        proc.start()
                        
                        frames = np.concatenate(chunks)
                        direction = mic.get_direction(frames)
                        set_color(COLORS_RGB['blue'], direction, b)
                        print('\n{}'.format(int(direction)))
                        
                        position = int(rounding((direction + 15) % 360 / 15) % 24 )
                        #print(position)
                        
                        buf = buffer(direction, b1, b2) # Filtered direction (For motor)
                        b = direction
                        #print(buf, b1, b2)
                        #print(buf)
                        
                    speech_count = 0
                    chunks = []

    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
