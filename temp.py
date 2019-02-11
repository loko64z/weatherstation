import os
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')


# TODO get temperature sensors from API call
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


