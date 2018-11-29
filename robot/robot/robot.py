#!/usr/bin/env python3
'''
    This is a demo program showing how to use Mecanum control with the
    RobotDrive class.
'''

import wpilib
import commandbased
import ctre

#main robot

class MyRobot(commandbased.CommandBasedRobot):
    def robotInit(self):
        self.motors = {}
        self.motors['leftMotor'] = ctre.WPI_TalonSRX(0)
        self.motors['rightMotor'] = ctre.WPI_TalonSRX(1)
        
    def testInit(self):
        print("Test Mode")
        while self.isTest():
            self.motors['leftMotor'].set(-50)
            self.motors['rightMotor'].set(100)
        print("Done")
     
    #Made by Matthew McFarland, the Great Wizard of 
    def teleopPeriodic(self):
        self.drive.tankDrive(0)
   








#code to run the robot

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