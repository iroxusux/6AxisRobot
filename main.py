from __future__ import division
import time
import keyboard
import board
import busio

# Import the PCA9685 module.
from Adafruit_Python_PCA9685 import Adafruit_PCA9685


def Main():
    controller = Controller()
    InitializeEnvironment(controller)  

    

def InitializeEnvironment(controller):
    while True:
        try:
            ok_to_run = Detecti2cModule(controller)
            if ok_to_run:
                RobotMain(controller)
        except KeyboardInterrupt:
            print('\n')
            print('########################################')
            print('Keyboard Interrupt Detected.')
            print('Moving To Cleanup & System Exit.')
            print('########################################')
            break
    
    CleanUpEnvironment(controller)
    
    print('########################################')
    print('System Exiting.')
    print('########################################')
    

def CleanUpEnvironment(controller):
    try:
        controller.i2c.unlock()
    except ValueError:
        pass
    controller.i2c.deinit()
    print('########################################')
    print('Clean Up Complete.')
    print('########################################')
    
    
def Detecti2cModule(controller):
    print('########################################')
    print('Scanning For i2c Connection Point.')
    print('########################################')
    
    # Create i2c Instance To Detect Board Before Deploying Data
    i2c_list = controller.i2c.scan()
    
    # Scan i2c Objects For Valid Data
    data_object_found = False
    for i in i2c_list:
        if i is not None:
            data_object_found = True
    
    # Valid Data Found
    if data_object_found:
        print('########################################')
        print('i2c Board Scan Successful.')
        print('########################################')
    
    # No Valid Data Found
    else:
        print('########################################')
        print('i2c Board Scan Failed.')
        print('Please Verify Device Is Plugged In.')
        print('Press Enter To Retry Scan.')
        print('########################################')
        input('')
        
    return(data_object_found)
    

def RobotMain(controller):
    controller.pwm = Adafruit_PCA9685.PCA9685()
    controller.pwm.set_pwm_freq(60)
    HomeRobot(controller)
#     OscillateJoint(pwm, 5, 390, 150, 600, 0.005)
#     OscillateJoint(pwm, 4, 390, 150, 600, 0.005)
#     OscillateJoint(pwm, 3, 390, 150, 600, 0.005)
#     OscillateJoint(pwm, 2, 200, 150, 250, 0.005)
#     OscillateJoint(pwm, 0, 390, 290, 490, 0.005)
    ManualControl(controller.pwm, controller.robot)

def ManualControl(pwm, robot):
    speed = 10
    clock = 0.01
    UpdateAllAxisSpeeds(robot, speed)
    while True:
        time.sleep(clock)
        if keyboard.is_pressed('q'):
            robot.axis1.req_position -= robot.axis1.speed
        elif keyboard.is_pressed('w'):
            robot.axis1.req_position += robot.axis1.speed

        if keyboard.is_pressed('a'):
            robot.axis2.req_position -= robot.axis2.speed
        elif keyboard.is_pressed('s'):
            robot.axis2.req_position += robot.axis2.speed

        if keyboard.is_pressed('z'):
            robot.axis3.req_position -= robot.axis3.speed
        elif keyboard.is_pressed('x'):
            robot.axis3.req_position += robot.axis3.speed

        if keyboard.is_pressed('e'):
            robot.axis4.req_position -= robot.axis4.speed
        elif keyboard.is_pressed('r'):
            robot.axis4.req_position += robot.axis4.speed

        if keyboard.is_pressed('d'):
            robot.axis5.req_position -= robot.axis5.speed
        elif keyboard.is_pressed('f'):
            robot.axis5.req_position += robot.axis5.speed

        if keyboard.is_pressed('c'):
            robot.axis6.req_position -= robot.axis6.speed
        elif keyboard.is_pressed('v'):
            robot.axis6.req_position += robot.axis6.speed

        UpdatePosition(pwm, robot)


def UpdatePosition(pwm, robot):
    UpdateAxis(robot.axis1)
    UpdateAxis(robot.axis2)
    UpdateAxis(robot.axis3)
    UpdateAxis(robot.axis4)
    UpdateAxis(robot.axis5)
    UpdateAxis(robot.axis6)
    pwm.set_pwm(robot.axis1.axis, 0, robot.axis1.position)
    pwm.set_pwm(robot.axis2.axis, 0, robot.axis2.position)
    pwm.set_pwm(robot.axis3.axis, 0, robot.axis3.position)
    pwm.set_pwm(robot.axis4.axis, 0, robot.axis4.position)
    pwm.set_pwm(robot.axis5.axis, 0, robot.axis5.position)
    pwm.set_pwm(robot.axis6.axis, 0, robot.axis6.position)


def UpdateAxis(axis):
    if axis.req_position != axis.position:
        if axis.req_position > axis.high_limit:
            axis.req_position = axis.high_limit
        if axis.req_position < axis.low_limit:
            axis.req_position = axis.low_limit
        axis.position = axis.req_position
        print(axis, axis.position)
    if axis.req_position == axis.position:
        axis.complete = True
    axis.req_position = axis.position


def UpdateAllAxisSpeeds(robot, speed):
    robot.axis1.speed = speed
    robot.axis2.speed = speed
    robot.axis3.speed = speed
    robot.axis4.speed = speed
    robot.axis5.speed = speed
    robot.axis6.speed = speed


def HomeRobot(pwm, robot):
    print('########################################')
    print('Homing Robot. Please Wait...')
    time.sleep(0.5)
    # Use Delay Timer To Dwell Any Residule Servo Motion
    pwm.set_pwm(robot.axis1.axis, 0, robot.axis1.home)
    pwm.set_pwm(robot.axis2.axis, 0, robot.axis2.home)
    pwm.set_pwm(robot.axis3.axis, 0, robot.axis3.home)
    pwm.set_pwm(robot.axis4.axis, 0, robot.axis4.home)
    pwm.set_pwm(robot.axis5.axis, 0, robot.axis5.home)
    pwm.set_pwm(robot.axis6.axis, 0, robot.axis6.home)
    time.sleep(0.5)
    # Use Delay Timer To Dwell Any Residule Servo Motion
    print('Assigning Current Position...')
    robot.axis1.position = robot.axis1.home
    robot.axis1.req_position = robot.axis1.position
    robot.axis2.position = robot.axis2.home
    robot.axis2.req_position = robot.axis2.position
    robot.axis3.position = robot.axis3.home
    robot.axis3req_position = robot.axis3.position
    robot.axis4.position = robot.axis4.home
    robot.axis4.req_position = robot.axis4.position
    robot.axis5.position = robot.axis5.home
    robot.axis5.req_position = robot.axis5.position
    robot.axis6.position = robot.axis6.home
    robot.axis6.req_position = robot.axis6.position
    time.sleep(0.5)
    # Use Delay Timer To Dwell Any Residule Servo Motion
    print('Homing Complete.')
    print('########################################')


def OscillateJoint(pwm, joint, origin, min_sweep, max_sweep, rate):
    print('########################################')
    print('Beginning Oscillation...')
    current = origin
    direction = 0
    complete = False
    while not complete:
        if current <= min_sweep and direction == 0:
            direction = 1
        if current >= max_sweep and direction == 1:
            HomeRobot(pwm)
            complete = True
            continue

        time.sleep(rate)  # Sleep For Rate
        pwm.set_pwm(joint, 0, current)  # Move Axis To Requested Position

        if direction == 0 and current > min_sweep:
            print('Rotating Clockwise...{}'.format(current))
            current -=1
        if direction == 1 and current < max_sweep:
            print('Rotating Counterclockwise...{}'.format(current))
            current +=1
    print('Oscillation Complete...')
    print('########################################')
    
    
class Controller(object):
    
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.pwm = None
        self.robot1 = SixAxisRobot()
        self.robot2 = SixAxisRobot() # Reserved For Future Use


class SixAxisRobot(object):

    def __init__(self):
        self.axis1 = SingleAxis('Axis 1', 150, 600, 390, 0) # Set
        self.axis2 = SingleAxis('Axis 2', 230, 590, 500, 1) # Set
        self.axis3 = SingleAxis('Axis 3', 180, 240, 200, 2) # Set
        self.axis4 = SingleAxis('Axis 4', 160, 610, 390, 3) # Set
        self.axis5 = SingleAxis('Axis 5', 150, 500, 390, 4) # Set
        self.axis6 = SingleAxis('Axis 6', 170, 570, 390, 5) # Set


class SingleAxis(object):

    def __init__(self, name, low_limit, high_limit, home, axis):
        self.name = name
        self.low_limit = low_limit
        self.high_limit = high_limit
        self.home = home
        self.axis = axis
        self.position = 0
        self.req_position = 0
        self.speed = 0
        self.positioning_complete = True


if __name__ == "__main__":
    Main()
