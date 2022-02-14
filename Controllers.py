import busio
import xbox

import SainSmartRobot

from Adafruit_Python_PCA9685 import Adafruit_PCA9685


class RaspberryPiController(object):

    def __init__(self):

        # Attempt To Connect To I2C Adafruit 9685 Board
        try:
            import board
            print('I2C Board Connection Established.')
            self.i2c = busio.I2C(board.SCL, board.SDA)
            print('I2C Board Connection Persist Complete.')
            self.ok_to_run = False
            self.DetectI2CModule()  # Read I2C Pins To Validate Active Connection Before Continuing
            if self.ok_to_run is True:
                print('I2C Board Valid Controller Detected.')
            # Create Instance Of PCA Controller
            self.pwm = Adafruit_PCA9685.PCA9685()
            print('PCA Object Created.')
            self.pwm.set_pwm_freq(60)
            print('PWM Frequency Set.')
        except NotImplementedError:
            print('Board Not Detected. Unable To Create Controller I2C Connection.')
            print('Check I2C Is Enabled Using The Terminal.')
            print('sudo raspi-config.')

        # Detect XBox Controller Plugin
        try:
            self.joy = xbox.Joystick()
            self.enable_joy = True
            print('XBox Controller Detected & Enabled')
        except OSError:
            self.joy = None
            self.enable_joy = False
            print('No XBox Controller Detected. Controller Fucntion Not Enabled.')
            print('Reboot Controller To Retry Connection')

        print('Local Clock Update Frequency Set')
        self.clock = 0.05  # Set Internal Clock For Localized Update Speeds
        print('Robot Controller Driver Connected')
        self.robot = SainSmartRobot.SixAxisRobot(self)
        print('Running Robot...')
        self.RunRobot()

    def CleanUpEnvironment(self):
        if self.i2c:
            try:
                self.i2c.unlock()
            except ValueError:
                pass
            self.i2c.deinit()
        try:
            self.joy.close()
        except AttributeError:
            pass

    def DetectI2CModule(self):
        if self.i2c:
            i2c_list = self.i2c.scan()
            for i in i2c_list:
                if i is not None:
                    self.ok_to_run = True
                    return

    def RunRobot(self):
        if self.ok_to_run:
            self.robot.main()
        self.CleanUpEnvironment()
