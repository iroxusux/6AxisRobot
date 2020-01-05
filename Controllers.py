import busio
import xbox

import Engine
import SainSmartRobot


class RaspberryPiController(object):

    def __init__(self):
        board_imported = False
        try:
            import board
            board_imported = True
        except NotImplementedError:
            print('Board Not Detected. Unable To Create Controller i2c Connection.')

        if board_imported:
            self.i2c = busio.I2C(board.SCL, board.SDA)
        else:
            self.i2c = None
        self.pwm = None
        self.clock = 0.01
        self.robot = []
        self.selected_robot = None
        try:
            self.joy = xbox.Joystick()
            self.enable_joy = True
        except OSError:
            self.joy = None
            self.enable_joy = False
            pass
        self.InitializeEnvironment()

    def InitializeEnvironment(self):
        self.ok_to_run = self.Detecti2cModule()

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

    def Detecti2cModule(self):
        data_object_found = False
        if self.i2c:
            i2c_list = self.i2c.scan()
            for i in i2c_list:
                if i is not None:
                    data_object_found = True
        return(data_object_found)

    def AddRobot(self, name):
        robot = SainSmartRobot.SixAxisRobot()
        robot.name = name
        self.robot.append(robot)

    def RunRobot(self, robot):
        self.selected_robot = robot
        try:
            if self.ok_to_run:
                SainSmartRobot.RobotMain(self)
        except KeyboardInterrupt:
            pass
        self.CleanUpEnvironment()
