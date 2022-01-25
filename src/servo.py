"""! @brief
[file description]
"""

import time
from enc_driver import EncoderDriver, EncoderConfig
from motor_driver import MotorDriver, MotorConfig


class Servo(MotorDriver, EncoderDriver):
    '''!
    Class that combies the functionality of the encoder and motor drivers.
    '''

    gain: float

    def __init__(self, m_config: MotorConfig, e_config: EncoderConfig, gain: float = 0.1) -> None:
        '''!
        Creates a servo object by initializing the motor and encoder drivers.
        @param m_config The motor configuration
        @param e_config The encoder configuration
        '''
        MotorDriver.__init__(self, *m_config.args)
        EncoderDriver.__init__(self, *e_config.args)
        self.gain = gain

    def move_to_point(self, setpoint: int) -> int:
        '''!
        This method moves the servo to the given setpoint.
        There is a timeout of 5 seconds
        @param setpoint The desired setpoint
        '''
        print('Moving to point...', end=' ')

        # enable motor
        self.enable_motor()

        timeout = time.time() + 5

        while time.time() < timeout:
            # set duty cycle according to distance to setpoint and servo gain
            pwm = self.get_error(setpoint) * self.gain
            self.set_duty_cycle(pwm)

        print(f'finished at {self.get_count()}')
