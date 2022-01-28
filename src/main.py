"""! @brief
[file description]
"""

##
# @mainpage
# @author Kyle Jennings, Zarek Lazowski, William Dorosk
# @date January 11th, 2022

import pyb
import utime
from enc_driver import EncoderConfig
from motor_driver import MotorConfig
from servo import Servo
from pid_controller import PID


def main():
    # initialize the encoder and motor drivers
    m_config = MotorConfig('PA10', 'PB4', 'PB5', pyb.Timer(3))
    e_config = EncoderConfig('PC6', 'PC7', pyb.Timer(8))

    # initialize the servo
    servo = Servo(m_config, e_config)
    servo.enable_motor()
    servo.zero()

    # initialize the pid controller
    # 11488 is 1/3 of the encoder
    setpoint = 11488
    pid = PID(setpoint, input('Enter Kp: '))

    # initialize encoder and time data lists
    encoder_data = []
    time_data = []

    # five seconds for each third of the encoder
    for _ in range(3):
        # set the timeout to 5 seconds
        timeout = utime.ticks_add(utime.ticks_ms(), 5000)
        while utime.ticks_diff(timeout, utime.ticks_ms()) > 0:
            # get the error and adjust the duty cycle
            servo.set_duty_cycle(pid.update(servo.get_error(11488)))

            # get the encoder data and time data
            encoder_data.append(servo.read())
            time_data.append(utime.ticks_ms())

            utime.sleep_ms(10)

        # move the encoder to the next third
        pid.set_setpoint(pid.setpoint + setpoint)

    # print the encoder data and time data
    pid.print_data(encoder_data, time_data)

    servo.disable_motor()
    

if __name__ == '__main__':
    print('Starting main...')
    main()
