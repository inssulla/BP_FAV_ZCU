import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime
from matplotlib import pyplot as plt

TEST_DURATION = 30
BOUNCETIME = 0.5

## 4 mics HW484 demo (green, red, blue, yellow)
## GPIO pinout: https://pinout.xyz
## connect mics to the following pins
micGREEN_pin = 20
micRED_pin = 21
micBLUE_pin = 16
micYELLOW_pin = 12

# Suppress warnings
GPIO.setwarnings(False)

# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BCM)

# Set MIC pin as input (4 mics demo)
GPIO.setup(micGREEN_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(micRED_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(micBLUE_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(micYELLOW_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def get_now():
    return datetime.now().timestamp()

events = []
t0 = get_now()
last = t0

def save_event(mic, t):
    global last, events

    if t-last > BOUNCETIME:
        events.append((mic, t))
        last = t
        print(f'Event: {mic} at {t-t0}')


def green_event(channel):
    save_event('green', get_now())

def red_event(channel):
    save_event('red', get_now())

def blue_event(channel):
    save_event('blue', get_now())

def yellow_event(channel):
    save_event('yellow', get_now())

GPIO.add_event_detect(micGREEN_pin, GPIO.FALLING, callback=green_event, bouncetime=200)
GPIO.add_event_detect(micRED_pin, GPIO.FALLING, callback=red_event, bouncetime=200)
GPIO.add_event_detect(micBLUE_pin, GPIO.FALLING, callback=blue_event, bouncetime=200)
GPIO.add_event_detect(micYELLOW_pin, GPIO.FALLING, callback=yellow_event, bouncetime=200)

for i in range(TEST_DURATION):
    sleep(1)

tS = get_now()

print(f'Num events: {len(events)}')

plt.plot([t0, tS], [0, 0], 'k-')
for mic, t in events:
    plt.plot([t, t], [0, 1], '-', color=mic, linewidth=1)
    
plt.xticks([t0, tS], [t0, tS])
plt.grid()

plt.savefig('mics_event.png')

