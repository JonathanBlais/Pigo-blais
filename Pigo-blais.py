#GOPIGO AUTONOMOUS, INSTANTIATED CLASS
#GOPIGO API: http://www.dexterindustries.com/GoPiGo/programming/python-programming-for-the-raspberry-pi-gopigo/

from gopigo import *
import time

#Global variable on how close an object is allowed to be
STOP_DIST = 50

class Pigo:

    ########
    ######## BASIC STATUS AND METHODS
    ########

    status = {"ismoving": False, "servo": 90, "leftspeed": 175,
              "rightspeed": 175, "dist": 100}

    def __init__(self):
        print "I'm such a robot. beep. beep."
        self.checkDist()

    def stop(self):
        self.status["ismoving"] = False
        print "Whoaaaa there."
        for x in range(3):
            stop()

    def fwd(self):
        self.status["ismoving"] = True
        print "Let's get going!"
        for x in range(3):
            fwd()

    def bwd(self):
        self.status["ismoving"] = True
        print "Back, back it up!"
        for x in range(3):
            bwd()


    #Check if conditions are safe to continue operating
    def keepGoing(self):
        if self.status['dist'] < STOP_DIST:
            print "Obstacle detected. Stopping."
            return False
        elif volt() > 14 or volt() < 6:
            print "Unsafe voltage detected: " + str(volt())
            return False
        else:
            return True


    def checkDist(self):
        self.status['dist'] = us_dist(15)
        print "I see something" + str(self.status["dist"]) + "mm away."
        if not self.keepGoing():
            print "EMERGENCY STOP FROM THE CHECK DISTANCE"
            self.stop()


########
######## ADVANCED METHODS
########


    def safeDrive(self):
        self.fwd()
        while self.keepGoing():
            self.checkDist()
        self.stop()

    def servoSweep(self):
        for ang in range(20, 160, 5):
            servo(ang)
            time.sleep(.1)

    def dance(self):
        print "I just want to DANCE!"
        if self.keepGoing():
            self.circleRight()
            self.circleLeft()
            self.shuffle
            self.servoShake()
            self.blink()


########
######## MAIN APP STARTS HERE
########
tina = Pigo()
while tina.keepGoing():
    tina.fwd()
    time.sleep(2)
    tina.stop()

tina.stop()
