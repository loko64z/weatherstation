# coding=utf-8
import time
import temp, led




while True:
    total_temp = 0
    for sensor in temp.sensors:
        sensor_temp = temp.read_temp(sensor)
        #print "{} -- {}".format(sensor["code"],sensor_temp)
        total_temp += sensor_temp
    total_temp = total_temp / len(temp.sensors)
    print u"TEMPERATURE => {} ºC".format(total_temp)
    led.all_off()
    led.show_value(total_temp)

    time.sleep(1)