from __future__ import division
import time
import keyboard

import Engine

import irox_tools

# Import the PCA9685 module.
from Adafruit_Python_PCA9685 import Adafruit_PCA9685


def RobotMain(controller):
    controller.pwm = Adafruit_PCA9685.PCA9685()
    controller.pwm.set_pwm_freq(60)
    HomeRobot(controller.pwm, controller.robot1)
    while True:
        print('########################################')
        print('Please Select Mode:')
        print('[a]: Demo')
        print('[b]: Manual')
        print('[c]: Run Path')
        print('########################################')
        response = input()
        print(response)
        if response == ('a' or 'A'):
            RunRoutine(controller, controller.robot1.path[0])
        elif response == ('b' or 'B'):
            ManualControl(controller)
        elif response == ('c' or 'C'):
            path_to_run = SelectPath(controller.robot1.paths)
            if path_to_run:
                RunRoutine(controller, path_to_run)
        else:
            print('Invalid Option')


def RunRoutine(controller, path):
    robot = controller.robot1
    pwm = controller.pwm
    routine_complete = False
    while not routine_complete:
        for i in path['Path']:
            step_complete = False
            while not step_complete:
                time.sleep(controller.clock)
                speed = i[0]
                UpdateAllAxisSpeeds(robot, speed)
                robot.axis1.req_position = i[2][0]
                robot.axis2.req_position = i[2][1]
                robot.axis3.req_position = i[2][2]
                robot.axis4.req_position = i[2][3]
                robot.axis5.req_position = i[2][4]
                robot.axis6.req_position = i[2][5]
                robot.gripper.req_position = i[2][6]
                UpdatePosition(pwm, robot)
                if (robot.axis1.complete and robot.axis2.complete and robot.axis3.complete
                    and robot.axis4.complete and robot.axis5.complete and robot.axis6.complete
                        and robot.gripper.complete):
                    time.sleep(i[1])
                    step_complete = True
            routine_complete = True


def SelectPath(paths):
    print('########################################')
    print('Select Path To Run:')
    for i, v in enumerate(paths):
        print('[{}]: {}'.format(i, v['Name']))
    print('########################################')
    try:
        response = int(input("Type a number:"))
        return paths[response]
    except ValueError:
        print("Value is not a whole number.")
    return None


def CompileDemoRoutine():
    path = {
        'Name': 'Demo Path',
        'Path': [],
        }
    demo_speed = 10
    demo_dwell = .1
    point_data = (390, 500, 180, 390, 390, 390, 195)  # Set
    path['Path'].append(AssembleTeachPoint(point_data, demo_speed, demo_dwell))
    point_data = (390, 500, 180, 390, 390, 390, 342)  # Set
    path['Path'].append(AssembleTeachPoint(point_data, demo_speed, demo_dwell))
    point_data = (390, 500, 180, 390, 390, 390, 195)  # Set
    path['Path'].append(AssembleTeachPoint(point_data, demo_speed, demo_dwell))
    point_data = (390, 500, 180, 390, 390, 390, 342)  # Set
    path['Path'].append(AssembleTeachPoint(point_data, demo_speed, demo_dwell))
    point_data = (390, 500, 180, 390, 390, 390, 195)  # Set
    path['Path'].append(AssembleTeachPoint(point_data, demo_speed, demo_dwell))
    point_data = (390, 380, 320, 390, 390, 390, 195)  # Set
    path['Path'].append(AssembleTeachPoint(point_data, demo_speed, demo_dwell))
    point_data = (390, 380, 320, 390, 390, 390, 195)  # Set
    path['Path'].append(AssembleTeachPoint(point_data, demo_speed, demo_dwell))
    point_data = (390, 380, 320, 410, 390, 589, 195)  # Set
    path['Path'].append(AssembleTeachPoint(point_data, demo_speed, demo_dwell))
    point_data = (390, 380, 300, 370, 240, 169, 195)  # Set
    path['Path'].append(AssembleTeachPoint(point_data, demo_speed, demo_dwell))
    point_data = (380, 310, 320, 370, 240, 169, 195)  # Set
    path['Path'].append(AssembleTeachPoint(point_data, demo_speed, demo_dwell))
    point_data = (380, 310, 340, 370, 270, 169, 242)  # Set
    path['Path'].append(AssembleTeachPoint(point_data, demo_speed, demo_dwell))
    point_data = (380, 310, 340, 370, 270, 169, 340)  # Set
    path['Path'].append(AssembleTeachPoint(point_data, demo_speed, demo_dwell))
    point_data = (380, 460, 180, 370, 270, 169, 340)  # Set
    path['Path'].append(AssembleTeachPoint(point_data, demo_speed, demo_dwell))
    point_data = (380, 460, 180, 610, 190, 169, 340)  # Set
    path['Path'].append(AssembleTeachPoint(point_data, demo_speed, demo_dwell))
    point_data = (380, 460, 180, 160, 180, 589, 340)  # Set
    path['Path'].append(AssembleTeachPoint(point_data, demo_speed, demo_dwell))
    point_data = (270, 290, 370, 160, 190, 589, 340)  # Set
    path['Path'].append(AssembleTeachPoint(point_data, demo_speed, demo_dwell))
    point_data = (390, 410, 190, 380, 360, 589, 340)  # Set
    path['Path'].append(AssembleTeachPoint(point_data, demo_speed, demo_dwell))
    point_data = (550, 250, 420, 170, 180, 147, 340)  # Set
    path['Path'].append(AssembleTeachPoint(point_data, demo_speed, demo_dwell))
    point_data = (390, 410, 190, 380, 360, 589, 340)  # Set
    path['Path'].append(AssembleTeachPoint(point_data, demo_speed, demo_dwell))
    point_data = (380, 310, 340, 370, 270, 169, 340)  # Set
    path['Path'].append(AssembleTeachPoint(point_data, demo_speed, demo_dwell))
    point_data = (380, 310, 340, 370, 270, 169, 242)  # Set
    path['Path'].append(AssembleTeachPoint(point_data, demo_speed, demo_dwell))
    point_data = (380, 310, 320, 370, 240, 169, 195)  # Set
    path['Path'].append(AssembleTeachPoint(point_data, demo_speed, demo_dwell))
    point_data = (390, 380, 300, 370, 240, 169, 195)  # Set
    path['Path'].append(AssembleTeachPoint(point_data, demo_speed, demo_dwell))
    point_data = (390, 380, 320, 410, 390, 589, 195)  # Set
    path['Path'].append(AssembleTeachPoint(point_data, demo_speed, demo_dwell))
    point_data = (390, 380, 320, 390, 390, 390, 195)  # Set
    path['Path'].append(AssembleTeachPoint(point_data, demo_speed, demo_dwell))
    point_data = (390, 380, 320, 390, 390, 390, 195)  # Set
    path['Path'].append(AssembleTeachPoint(point_data, demo_speed, demo_dwell))
    point_data = (390, 500, 180, 390, 390, 390, 195)  # Set
    path['Path'].append(AssembleTeachPoint(point_data, demo_speed, demo_dwell))
    return path


def ManualControl(controller):
    robot = controller.robot1
    pwm = controller.pwm
    clock = controller.clock
    joy = controller.joy
    joy_set = True
    joy_set_ons = False
    exit_manual = False
    speed = 10
    UpdateAllAxisSpeeds(robot, speed)
    while not exit_manual:
        time.sleep(clock)
        a = robot.axis1.position
        b = robot.axis2.position
        c = robot.axis3.position
        d = robot.axis4.position
        e = robot.axis5.position
        f = robot.axis6.position
        g = robot.gripper.position
        robot.full_position = (a, b, c, d, e, f, g)

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

        if keyboard.is_pressed('1'):
            robot.gripper.req_position -= robot.gripper.speed
        elif keyboard.is_pressed('2'):
            robot.gripper.req_position += robot.gripper.speed

        if controller.enable_joy:
            left_stick = joy.leftStick()
            right_stick = joy.rightStick()
            joy_set, joy_set_ons = irox_tools.Toggle(joy_set, joy.Y(), joy_set_ons)
            if joy_set:
                robot.axis1.req_position += (int(left_stick[0]*robot.axis1.speed))
                robot.axis2.req_position += (int(left_stick[1]*robot.axis2.speed))
                robot.axis3.req_position += (int(right_stick[0]*robot.axis3.speed))
                robot.axis4.req_position += (int(right_stick[1]*robot.axis4.speed))
            if not joy_set:
                robot.axis5.req_position += (int(left_stick[0]*robot.axis5.speed))
                robot.axis6.req_position += (int(left_stick[1]*robot.axis6.speed))
                robot.gripper.req_position += (int(right_stick[0]*robot.gripper.speed))

        if keyboard.is_pressed('0'):
            print('Robot Current Axis Points: 1:{} 2:{} 3:{} 4:{} 5:{} 6:{} 7:{}'.format(a,b,c,d,e,f,g))

        if keyboard.is_pressed('h'):
            print('########################################')
            print('Send Robot To Home? [y]')
            print('########################################')
            response = input()
            if response == ('y' or 'Y'):
                HomeRobot(pwm, robot)

        if keyboard.is_pressed('t'):
            print('########################################')
            print('Enter Teach Mode? [y]')
            print('########################################')
            response = input()
            if response == ('y' or 'Y'):
                robot.teach_mode = True
                print('########################################')
                print('Enter Path Name:')
                print('########################################')
                name = input()
                path = {
                'Name': name,
                'Path': [],
                }
                robot.paths.append(path)
                robot.current_teach_path = name

        if robot.teach_mode:
            PathTeaching(controller)

        if keyboard.is_pressed('esc'):
            exit_manual = True

        UpdatePosition(pwm, robot)


def PathTeaching(controller):
    robot = controller.robot1
    if robot.teach_mode:
        if keyboard.is_pressed('ins'):
            print('########################################')
            print('Add Teach Point? [y]')
            print('########################################')
            response = input()
            if response == ('y' or 'Y'):
                print('########################################')
                print('Enter Move Speed [1 - 10]')
                print('########################################')
                try:
                    speed_response = int(input("Type a number:"))
                except ValueError:
                    print("Value is not a whole number.")
                if speed_response > 10:
                    speed_response = 10
                if speed_response < 1:
                    speed_response = 1
                print('########################################')
                print('Enter Dwell Time [0.1 - 5]')
                print('########################################')
                try:
                    dwell_response = float(input("Type a number:"))
                except ValueError:
                    print("Value is not a number.")
                if dwell_response > 5.0:
                    dwell_response = 5.0
                if dwell_response < 0.1:
                    dwell_response = 0.1
                for i in controller.robot1.paths:
                    print(i)
                    if i['Name'] == robot.current_teach_path:
                        i['Path'].append(AssembleTeachPoint(controller.robot1.full_position, speed_response, dwell_response))
                        print(i['Path'])


def UpdatePosition(pwm, robot):
    UpdateAxis(robot.axis1)
    UpdateAxis(robot.axis2)
    UpdateAxis(robot.axis3)
    UpdateAxis(robot.axis4)
    UpdateAxis(robot.axis5)
    UpdateAxis(robot.axis6)
    UpdateAxis(robot.gripper)
    pwm.set_pwm(robot.axis1.axis, 0, robot.axis1.position)
    pwm.set_pwm(robot.axis2.axis, 0, robot.axis2.position)
    pwm.set_pwm(robot.axis3.axis, 0, robot.axis3.position)
    pwm.set_pwm(robot.axis4.axis, 0, robot.axis4.position)
    pwm.set_pwm(robot.axis5.axis, 0, robot.axis5.position)
    pwm.set_pwm(robot.axis6.axis, 0, robot.axis6.position)
    pwm.set_pwm(robot.gripper.axis, 0, robot.gripper.position)


def UpdateAxis(axis):
    axis.complete = False
    if axis.req_position != axis.position:
        if axis.req_position > axis.high_limit:
            axis.req_position = axis.high_limit
        if axis.req_position < axis.low_limit:
            axis.req_position = axis.low_limit
    if axis.req_position > axis.position:
        axis.position += axis.speed
        if axis.position > axis.req_position:
            axis.position = axis.req_position
#         axis.position = axis.req_position
    if axis.req_position < axis.position:
        axis.position -= axis.speed
        if axis.position < axis.req_position:
            axis.position = axis.req_position
    if axis.req_position == axis.position:
        axis.complete = True
#     axis.req_position = axis.position


def UpdateAllAxisSpeeds(robot, speed):
    robot.axis1.speed = speed
    robot.axis2.speed = speed
    robot.axis3.speed = speed
    robot.axis4.speed = speed
    robot.axis5.speed = speed
    robot.axis6.speed = speed
    robot.gripper.speed = speed


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
    pwm.set_pwm(robot.gripper.axis, 0, robot.gripper.home)
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
    robot.gripper.position = robot.gripper.home
    robot.gripper.req_position = robot.gripper.position
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
            current -= 1
        if direction == 1 and current < max_sweep:
            print('Rotating Counterclockwise...{}'.format(current))
            current += 1
    print('Oscillation Complete...')
    print('########################################')


def AssembleTeachPoint(point_data, speed, dwell_time):
    return (speed, dwell_time, point_data)


class SixAxisRobot(object):

    def __init__(self):
        self.axis1 = SingleAxis('Axis 1', 150, 600, 390, 0)  # Set
        self.axis2 = SingleAxis('Axis 2', 230, 590, 500, 1)  # Set
        self.axis3 = SingleAxis('Axis 3', 180, 550, 200, 2)  # Set
        self.axis4 = SingleAxis('Axis 4', 160, 610, 390, 3)  # Set
        self.axis5 = SingleAxis('Axis 5', 150, 500, 390, 4)  # Set
        self.axis6 = SingleAxis('Axis 6', 147, 589, 390, 5)  # Set
        self.gripper = SingleAxis('Gripper', 195, 342, 200, 6)
        self.full_position = (0, 0, 0, 0, 0, 0, 0)
        self.teach_mode = False
        self.paths = []
        self.current_teach_path = ''


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
        self.complete = True
