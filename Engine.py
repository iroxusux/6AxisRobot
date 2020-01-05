import json

import SainSmartRobot


def RunEngine(controller, queue):
    controller.selected_robot = controller.robot[0]
    controller.RunRobot(queue)


def SavePathData(controller):
    with open('PathData.txt', 'w') as a:
        json.dump(controller)


def LoadPathData(controller):
    try:
        with open('PathData.txt', 'r') as a:
            data = json.load(a)
            controller = data
    except FileNotFoundError:
        controller.selected_robot.paths.append(SainSmartRobot.CompileDemoRoutine())
