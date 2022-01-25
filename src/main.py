"""! @brief
[file description]
"""

##
# @mainpage
# @author Kyle Jennings, Zarek Lazowski, William Dorosk
# @date January 11th, 2022

import pyb
import time
from enc_driver import EncoderConfig
from motor_driver import MotorConfig
from servo import Servo


def main():
    m_config = MotorConfig('PA10', 'PB4', 'PB5', pyb.Timer(3))
    e_config = EncoderConfig('PC6', 'PC7', pyb.Timer(8, prescaler=1, period=100000))

    servo = Servo(m_config, e_config, 0.00625)
    
    print(servo._e_pin1)
    print(servo._e_pin2)
    print(servo._e_ch1)
    print(servo._e_ch2)
    print(servo._e_tim)

    while True:
        print(servo.get_count())
        time.sleep(0.5)
    

if __name__ == '__main__':
    print('Starting main...')
    main()
