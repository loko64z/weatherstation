import os
import time

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


RED = 18
BLUE = 23
GREEN = 24


leds = [RED,BLUE, GREEN]

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')



temp_sensor1 = {"code":"SENSOR1", "path":'/sys/bus/w1/devices/28-02131ddb0daa/w1_slave'}
temp_sensor2 = {"code":"SENSOR2", "path":'/sys/bus/w1/devices/28-02131def4caa/w1_slave'}

sensors = [temp_sensor1, temp_sensor2]

def temp_raw(sensor):
    with open(sensor, 'r') as f:
        lines = f.readlines()
    return lines


def read_temp(sensor):

    lines = temp_raw(sensor["path"])
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = temp_raw(sensor["path"])

    temp_output = lines[1].find('t=')

    if temp_output != -1:
        temp_string = lines[1].strip()[temp_output + 2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c


def setup_led(pin):
    GPIO.setup(pin, GPIO.OUT)


def led_on(pin):
    print "LED {} ON".format(pin)
    GPIO.output(pin, GPIO.HIGH)

def led_off(pin):
    print "LED {} OFF".format(pin)
    GPIO.output(pin, GPIO.LOW)

def all_off():
    for led in leds:
        led_off(led)

def all_on():
    for led in leds:
        led_on(led)


for led in leds:
    setup_led(led)

while True:
    total_temp = 0
    for sensor in sensors:
        sensor_temp = read_temp(sensor)
        #print "{} -- {}".format(sensor["code"],sensor_temp)
        total_temp += sensor_temp
    total_temp = total_temp / len(sensors)
    print "TEMPERATURA => {}".format(total_temp)
    all_off()
    if total_temp < 20:
        led_on(BLUE)
    elif total_temp <= 27:
        led_on(GREEN)
    else:
        led_on(RED)
    time.sleep(1)
