import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# TODO get the led data from API call
RED = 18
BLUE = 23
GREEN = 24

leds = [RED,BLUE,GREEN]


def setup_led(pin):
    GPIO.setup(pin, GPIO.OUT)


def led_on(pin):
    GPIO.output(pin, GPIO.HIGH)


def led_off(pin):
    GPIO.output(pin, GPIO.LOW)


def all_off():
    [led_off(led) for led in leds]


def all_on():
    [led_on(led) for led in leds]


for led in leds:
    setup_led(led)

def show_value(total_temp):
    if total_temp < 20:
        led_on(BLUE)
    elif total_temp <= 27:
        led_on(GREEN)
    else:
        led_on(RED)

