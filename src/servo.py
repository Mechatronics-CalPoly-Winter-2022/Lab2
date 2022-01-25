"""! @brief
[file description]
"""

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

        error = self.get_error(setpoint)
        if error > 0:
            self.set_duty_cycle(100)
        elif error < 0:
            self.set_duty_cycle(-100)
        else:
            return

        while abs(self.get_error(setpoint)) > 1:
            pass