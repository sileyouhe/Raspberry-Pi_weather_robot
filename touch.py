import get_weather
import get_recommend
import time
#VCC-接电源正---36
#GND---接地---34
#out---信号输出---32

import RPi.GPIO as GPIO


def touch():
    pin_power = 36  # 电源口，这里让cpu输出1代替电源
    pin_in = 32  # 触摸开关后会输出1或0，在这个口读取给CPU使用
    count = 5
    flag = 0  # flag=0跑天气脚本，flag=1跑搭配脚本

    GPIO.setmode(GPIO.BOARD)
    #设置电源口为输出口，向电源口输出1
    GPIO.setup(pin_power, GPIO.OUT)
    GPIO.setup(pin_in, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


    GPIO.output(pin_power, GPIO.HIGH)

    #触摸按键脚本：先跑天气API
    while True:
        GPIO.wait_for_edge(pin_in, GPIO.RISING)
        if flag == 0:
            get_weather.GetTianqi()
            flag = 1
        else:
            get_recommend.getDapei()
            flag = 0
        count = count-1

    GPIO.cleanup()


if __name__ == '__main__':
    time.sleep(10)
    touch()
