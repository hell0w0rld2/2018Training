#!/usr/bin/env python3
'''
    This is a demo program showing how to use Mecanum control with the
    RobotDrive class.
'''

import wpilib
import wpilib.drive.differentialdrive as dd

import commandbased
import ctre


#main robot

class MyRobot(commandbased.CommandBasedRobot):
    def robotInit(self):
        self.motors = {}
        self.motors['leftMotor'] = ctre.WPI_TalonSRX(0)
        self.motors['rightMotor'] = ctre.WPI_TalonSRX(1)
        self.driveTrain = dd.DifferentialDrive(**self.motors)
        self.driveController = wpilib.XboxController(0)

    def teleopInit(self):
        print("Test Mode")
        dc = self.driveController
        while self.isOperatorControl():
            leftSide = dc.getRawAxis(0)
            rightSide = dc.getRawAxis(1)
            self.driveTrain.tankDrive(leftSide, rightSide)
            
        print("Test Done")
            





#code to help run the robot

#import sys       
def exit(retval):
    pass
#    sys.exit(retval)

if __name__ == '__main__':
    try:
        print(wpilib._impl.main.exit)
    except:
        wpilib._impl.main.exit = exit
    wpilib.run(MyRobot,physics_enabled=True)