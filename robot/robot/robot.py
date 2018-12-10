#!/usr/bin/env python3
'''
    This is a demo program showing how to use Mecanum control with the
    RobotDrive class.
'''

#add 'team3200' module to the search path
import os
import sys
sys.path.insert(0, os.getcwd() + "\\..")
import team3200
import wpilib

import commandbased

import subsystems.driveTrain

#main robot

class MyRobot(commandbased.CommandBasedRobot):
    
    def robotInit(self):
        team3200.getRobot = lambda x=0:self
        self.dtSub = subsystems.driveTrain.DriveTrainSub()
        self.driveController = wpilib.XboxController(0)

#    def teleopInit(self):
#        print("Test Mode")
#        dc = self.driveController
#        while self.isOperatorControl():
#            leftSide = dc.getRawAxis(0)
#            rightSide = dc.getRawAxis(1)
#        
#            self.dtSub.setTankDrive(leftSide,rightSide)
#            
#        print("Test Done")
            

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
    
    #fixes simulation rerun errors.
    #todo verify this causes no issues on robot
    wpilib.DriverStation._reset()
    
    wpilib.run(MyRobot,physics_enabled=True)