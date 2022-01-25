"""! @brief
[file description]
"""

##
# @mainpage
# @author Kyle Jennings, Zarek Lazowski, William Dorosk
# @date January 11th, 2022

import pyb
import time
from enc_driver import EncoderDriver, EncoderConfig
from motor_driver import MotorDriver, MotorConfig


class Servo(MotorDriver, EncoderDriver):
    '''!
    Class that combies the functionality of the encoder and motor drivers.
    '''

    def __init__(self, m_config: MotorConfig, e_config: EncoderConfig) -> None:
        '''!
        Creates a servo object by initializing the motor and encoder drivers.
        @param m_config The motor configuration
        @param e_config The encoder configuration
        '''
        MotorDriver.__init__(self, *m_config.args)
        EncoderDriver.__init__(self, *e_config.args)

    def move_to_point(self, setpoint: int) -> None:
        '''!
        This method moves the servo to the given setpoint.
        @param setpoint The desired setpoint
        '''
        print('Moving to point...', end=' ')

        # enable motor
        self._motor.enable_motor()

        if init_state := self._encoder.get_count() < setpoint:
            # move clockwise
            self._motor.set_duty_cycle(100)
        else:
            # move counter-clockwise
            self._motor.set_duty_cycle(-100)

        while init_state == self._encoder.get_count < setpoint:
            # wait until the motor has moved to the setpoint
            time.sleep(0.01)

        print(f'finished at {self._encoder.get_count()}')
        return setpoint - self._encoder.get_count()


def main():
    m_config = MotorConfig('PA10', 'PB4', 'PB5', pyb.Timer(3))
    e_config = EncoderConfig('PB6', 'PB7', pyb.Timer(8))

    servo = Servo(m_config, e_config)

    servo.move_to_point(servo.get_count() + 1000)
    servo.move_to_point(servo.get_count() - 1000)


if __name__ == '__main__':
    print('Starting main...')
    main()
