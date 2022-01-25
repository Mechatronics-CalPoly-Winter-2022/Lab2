"""! @brief
[file description]
"""

##
# @mainpage
# @author Kyle Jennings, Zarek Lazowski, William Dorosk
# @date January 11th, 2022

import pyb
from enc_driver import EncoderConfig
from motor_driver import MotorConfig
from servo import Servo


def main():
    m_config = MotorConfig('PA10', 'PB4', 'PB5', pyb.Timer(3))
    e_config = EncoderConfig('PC6', 'PC7', pyb.Timer(8))

    servo = Servo(m_config, e_config, 0.00625)

    servo.enable_motor()
    servo.set_duty_cycle(50)


if __name__ == '__main__':
    print('Starting main...')
    main()
