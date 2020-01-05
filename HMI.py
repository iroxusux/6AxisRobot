import SainSmartRobot


class HMI(object):
    def __init__(self, ui):
        self.ui = ui
        self.Input = HMIInputs()
        self.Output = HMIOutputs()
        self.InitializeHMI()

    def InitializeHMI(self):
        self.Input.Navigation_Req = 0
        self.Output.StatusText = 'Ready.'
        self.ProcessEvents()

    def ProcessEvents(self):
        self.ChangeScreen()
        self.HouseKeeping()

    def ChangeScreen(self):
        if self.Input.Navigation_Req != -1:
            self.Output.GoToScreen = self.Input.Navigation_Req
        self.Output.StatusText = 'Ready.'

    def HouseKeeping(self):
        self.Input.UpdateInputs(self)
        self.Output.UpdateOutputs(self)

    def ProcessData(self, processor):
        self.robot = processor.controller.selected_robot


class HMIInputs(object):
    def __init__(self):
        self.Navigation_Req = -1

    def UpdateInputs(self, HMI):
        self.Navigation_Req = -1


class HMIOutputs(object):
    def __init__(self):
        self.StatusText = ''
        self.GoToScreen = -1
        self.robot = SainSmartRobot.SixAxisRobot()

    def UpdateOutputs(self, HMI):
        if self.StatusText != '':
            try:
                HMI.ui.System_Status_Text.setText(self.StatusText)
            except TypeError:
                print('Text Type Error. Not Valid String')

        if self.GoToScreen != -1:
            try:
                HMI.ui.stackedWidget.setCurrentIndex(HMI.Output.GoToScreen)
            except TypeError:
                print('Integer Type Error. Not Valid Integer: {}'.format(HMI.Input.Navigation_Req))
                self.GoToScreen = -1

    def UpdateRobotScreen(self, HMI):
        HMI.ui.Axis1_Current_Pos_LCD = self.robot.axis1.position
        HMI.ui.Axis2_Current_Pos_LCD = self.robot.axis2.position
        HMI.ui.Axis3_Current_Pos_LCD = self.robot.axis3.position
        HMI.ui.Axis4_Current_Pos_LCD = self.robot.axis4.position
        HMI.ui.Axis5_Current_Pos_LCD = self.robot.axis5.position
        HMI.ui.Axis6_Current_Pos_LCD = self.robot.axis6.position
        HMI.ui.Axis7_Current_Pos_LCD = self.robot.gripper.position

        HMI.ui.Axis1_Low_Limit_LCD = self.robot.axis1.low_limit
        HMI.ui.Axis2_Low_Limit_LCD = self.robot.axis2.low_limit
        HMI.ui.Axis3_Low_Limit_LCD = self.robot.axis3.low_limit
        HMI.ui.Axis4_Low_Limit_LCD = self.robot.axis4.low_limit
        HMI.ui.Axis5_Low_Limit_LCD = self.robot.axis5.low_limit
        HMI.ui.Axis6_Low_Limit_LCD = self.robot.axis6.low_limit
        HMI.ui.Axis7_Low_Limit_LCD = self.robot.gripper.low_limit

        HMI.ui.Axis1_high_Limit_LCD = self.robot.axis1.high_limit
        HMI.ui.Axis2_high_Limit_LCD = self.robot.axis2.high_limit
        HMI.ui.Axis3_high_Limit_LCD = self.robot.axis3.high_limit
        HMI.ui.Axis4_high_Limit_LCD = self.robot.axis4.high_limit
        HMI.ui.Axis5_high_Limit_LCD = self.robot.axis5.high_limit
        HMI.ui.Axis6_high_Limit_LCD = self.robot.axis6.high_limit
        HMI.ui.Axis7_high_Limit_LCD = self.robot.gripper.high_limit
