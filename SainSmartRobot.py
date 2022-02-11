from __future__ import division
import time
import keyboard

import irox_tools


def RunRoutine(controller, path):
    robot = controller.selected_robot
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


def PathTeaching(controller):
    robot = controller.selected_robot
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
                for i in controller.selected_robot.paths:
                    print(i)
                    if i['Name'] == robot.current_teach_path:
                        i['Path'].append(
                            AssembleTeachPoint(controller.selected_robot.full_position, speed_response, dwell_response))
                        print(i['Path'])


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


TEACH_MODE_SPEED = 1


class SixAxisRobot(object):

    def __init__(self, controller):
        self.controller = controller
        self.clock_rpi = controller.clock
        self.__refresh_time__ = 0
        self.axis1 = SingleAxis(self.controller, 150, 600, 390, 0)  # Set
        self.axis2 = SingleAxis(self.controller, 230, 590, 500, 1)  # Set
        self.axis3 = SingleAxis(self.controller, 180, 550, 200, 2)  # Set
        self.axis4 = SingleAxis(self.controller, 160, 610, 390, 3)  # Set
        self.axis5 = SingleAxis(self.controller, 150, 500, 390, 4)  # Set
        self.axis6 = SingleAxis(self.controller, 147, 589, 390, 5)  # Set
        self.gripper = SingleAxis(self.controller, 195, 342, 200, 6)
        self.teach_mode = False
        self.paths = []
        self.current_teach_path = ''

    @property
    def homed(self):
        if (self.axis1.homed is True and
                self.axis2.homed is True and
                self.axis3.homed is True and
                self.axis4.homed is True and
                self.axis5.homed is True and
                self.axis6.homed is True and
                self.gripper.homed is True):
            return True
        else:
            return False

    @property
    def full_position(self):
        return (self.axis1.actual_position,
                self.axis2.actual_position,
                self.axis3.actual_position,
                self.axis4.actual_position,
                self.axis5.actual_position,
                self.axis6.actual_position,
                self.gripper.actual_position)

    # Main Process Loop For SixAxis Robot
    def main(self):
        exit_loop = False
        while exit_loop is False:
            if self.__refresh_time__ < time.time():
                self.__refresh_time__ = time.time() + self.clock_rpi
                self.fcn_home()  # Request All Axis Home Command
                self.manual_control()  # Monitor Manual Control Commands
                # Always Keep This As Last Function For Main Loop
                self.__update_all_axis__()
                if keyboard.is_pressed('esc'):
                    exit_loop = True
        self.fcn_shutdown()  # Shutdown Axis On Exit Run

    # After Internal Scan, Scan Each Axis For Updates
    def __update_all_axis__(self):
        self.axis1.main_loop()
        self.axis2.main_loop()
        self.axis3.main_loop()
        self.axis4.main_loop()
        self.axis5.main_loop()
        self.axis6.main_loop()
        self.gripper.main_loop()

    # Set Home Position On Robot
    # All Servo Axis Will Move To Predefined Home Position And Register Position To Home Value
    def fcn_home(self):
        if self.homed is True:  # Don't Home Axis Unless Required By Axis
            return
        self.axis1.request_home
        self.axis2.request_home
        self.axis3.request_home
        self.axis4.request_home
        self.axis5.request_home
        self.axis6.request_home
        self.gripper.request_home

    # Shut Down Robot Servos
    # Unexpected Motion May Occur As Physical Weight Of Robot
    # May Push Through Servos (There Are No Mechanical Brakes On This Device)
    def fcn_shutdown(self):
        self.UpdateAllAxisSpeeds(0)
        self.axis1.request_shutdown
        self.axis2.request_shutdown
        self.axis3.request_shutdown
        self.axis4.request_shutdown
        self.axis5.request_shutdown
        self.axis6.request_shutdown
        self.gripper.request_shutdown

    def manual_control(self):
        self.UpdateAllAxisSpeeds(TEACH_MODE_SPEED)
        self.__keyboard_commands__()
        self.__joy_commands__()
        return

    def __keyboard_commands__(self):
        # Axis 1
        if keyboard.is_pressed('q'):
            self.axis1.fcn_jog_forward()
        elif keyboard.is_pressed('w'):
            self.axis1.fcn_jog_reverse()

        # Axis 2
        if keyboard.is_pressed('a'):
            self.axis2.fcn_jog_forward()
        elif keyboard.is_pressed('s'):
            self.axis2.fcn_jog_reverse()

        # Axis 3
        if keyboard.is_pressed('z'):
            self.axis3.fcn_jog_forward()
        elif keyboard.is_pressed('x'):
            self.axis3.fcn_jog_reverse()

        # Axis 4
        if keyboard.is_pressed('e'):
            self.axis4.fcn_jog_forward()
        elif keyboard.is_pressed('r'):
            self.axis4.fcn_jog_reverse()

        # Axis 5
        if keyboard.is_pressed('d'):
            self.axis5.fcn_jog_forward()
        elif keyboard.is_pressed('f'):
            self.axis5.fcn_jog_reverse()

        # Axis 6
        if keyboard.is_pressed('c'):
            self.axis6.fcn_jog_forward()
        elif keyboard.is_pressed('v'):
            self.axis6.fcn_jog_reverse()

        # Gripper
        if keyboard.is_pressed('t'):
            self.gripper.fcn_jog_forward()
        elif keyboard.is_pressed('y'):
            self.gripper.fcn_jog_reverse()

    def __joy_commands__(self):
        if self.controller.enable_joy:
            left_stick = self.controller.joy.leftStick()
            right_stick = self.controller.joy.rightStick()
            print((left_stick[0]), (left_stick[1]))
            if self.controller.joy.leftTrigger() < 0.5:
                self.axis1.requested_position += (int(left_stick[0] * self.axis1.speed))
                self.axis2.requested_position += (int(left_stick[1] * self.axis2.speed))
                self.axis3.requested_position += (int(right_stick[0] * self.axis3.speed))
                self.axis4.requested_position += (int(right_stick[1] * self.axis4.speed))
            if self.controller.joy.leftTrigger() >= 0.5:
                self.axis5.requested_position += (int(left_stick[0] * self.axis5.speed))
                self.axis6.requested_position += (int(left_stick[1] * self.axis6.speed))
                self.gripper.requested_position += (int(right_stick[0] * self.gripper.speed))


    # Static Method To Update SingleAxis Speed Reference
    @staticmethod
    def UpdateAxisSpeed(axis: "SingleAxis", speed: "int"):
        axis.speed = speed

    # Update All Axis Speed References
    def UpdateAllAxisSpeeds(self, speed):
        self.UpdateAxisSpeed(self.axis1, speed)
        self.UpdateAxisSpeed(self.axis2, speed)
        self.UpdateAxisSpeed(self.axis3, speed)
        self.UpdateAxisSpeed(self.axis4, speed)
        self.UpdateAxisSpeed(self.axis5, speed)
        self.UpdateAxisSpeed(self.axis6, speed)
        self.UpdateAxisSpeed(self.gripper, speed)


class SingleAxis(object):

    def __init__(self, controller, low_limit, high_limit, home_position, axis):
        self.controller = controller
        self.low_limit = low_limit
        self.high_limit = high_limit
        self.home_position = home_position
        self.axis = axis
        self.actual_position = 0
        self.requested_position = 0
        self.speed = 0

        # Servo Homing
        self.__request_home__ = False
        self.__homing_in_progress__ = False
        self.__homed__ = False

        # Servo Shutdown
        self.__request_shutdown__ = False
        self._shutdown_ = False

        # Servo Move Data
        self.busy = False
        self._move_in_progress_ = False

    @property
    def request_home(self):
        self.__fcn_home__()

    @property
    def request_shutdown(self):
        self.__fcn_shutdown__()


    @property
    def homed(self):
        return self.__homed__

    # Only Allow Home Status To Be Set By Local Class (Hence Homing Memory)
    # Homed Status Is Process Crucial, We Don't Want Outside Influences Changing This Data
    @homed.setter
    def homed(self, val: "bool"):
        self.__homed__ = val

    def main_loop(self):
        self.__check_limits__()  # Monitor Servo Axis Position Requests Against Limits
        self.__fcn_assert_move__()  # Assert Requested Moves To Servo

    # Assert Home Command To Specific Axis
    # Dwell Time To Allow Servo Time To Fully Move Into Position Before Defining Position
    # Then Redefine Current Position With Commanded Home Position
    def __fcn_home__(self):
        self.controller.pwm.set_pwm(self.axis, 0, self.home_position)  # Set Controller Command For Current Position
        self.actual_position = self.requested_position = self.home_position
        time.sleep(1)  # Dwell Servo Motion
        self.__homed__ = True

    # Shut Down Robot Servo
    # Unexpected Motion May Occur As Physical Weight Of Robot
    # May Push Through Servo (There Are No Mechanical Brakes On This Device)
    # Setting Requested Position As 0 Sets Disabled For SUNFOUNDER SF0180 Servos
    def __fcn_shutdown__(self):
        self.controller.pwm.set_pwm(self.axis, 0, 0)  # Set Controller Command For Current Position
        time.sleep(1)  # Dwell Servo Motion
        self.actual_position = 0
        self.__homed__ = False

    # Check Request Position Commands Against Preset Servo Limits
    # If Command Is Out Of Limits, Set Hard Limits To Servo Position Request
    def __check_limits__(self):
        # Protect From Over Travel Values
        if self.requested_position > self.high_limit:
            self.requested_position = self.high_limit
            return
        if self.requested_position < self.low_limit:
            self.requested_position = self.low_limit
            return

    # Helper Function
    # Request Simple Jog Forward Command To Servo By Updating Requested Position
    def fcn_jog_forward(self):
        self.requested_position += self.speed

    # Helper Function

    # Helper Function
    # Request Simple Jog Reverse Command To Servo By Updating Requested Position
    def fcn_jog_reverse(self):
        self.requested_position -= self.speed

    # Assert Requested Move For This Servo To The PWM Controller
    def __fcn_assert_move__(self):
        if self.requested_position == self.actual_position:  # No Requests Were Made - Return As Not Busy
            self.busy = False
            return
        self.busy = True
        self.actual_position = self.__calculate_pwm_offset__()  # Set Our Actual Position Before Moving To It
        self.controller.pwm.set_pwm(self.axis, 0, self.actual_position)  # Set Controller Command For Current Position

    def __calculate_pwm_offset__(self):
        position_offset = self.requested_position - self.actual_position
        if abs(position_offset) > self.speed:
            return self.actual_position + self.speed if position_offset > 0 else self.actual_position + self.speed*-1
        else:
            return self.actual_position + position_offset



