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
from motor_driver import MotorConfig, MotorDriver
from servo import Servo


def main():
    # motor = MotorDriver('PA10', 'PB4', 'PB5', pyb.Timer(3))
    # motor.enable_motor()
    # motor.set_duty_cycle(25)
    
    # time.sleep(5)

    # motor.disable_motor()



    m_config = MotorConfig('PA10', 'PB4', 'PB5', pyb.Timer(3))
    e_config = EncoderConfig('PC6', 'PC7', pyb.Timer(8))

    servo = Servo(m_config, e_config)
    servo.enable_motor()
    servo.zero()

    servo.move_to_point(31000)
    servo.move_to_point(17000)

    servo.disable_motor()
    

if __name__ == '__main__':
    main()
