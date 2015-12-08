__author__ = 'Jo'


from gopigo import *
import time


class Pigo():

    sweep = [0] * 180
    FARDISTANCE = 90
    MIN_DISTANCE = 60
    turned_right_last = True

    status = {"ismoving" : False, "servo" : 90, "leftspeed" : 175,
              "rightspeed" : 175, "dist" : 100, "volt" : 2}

    def __init__(self):
        print "I'm alive"

    def fwd(self):
        self.status["ismoving"] = True
        print "lets a go"
        for x in range(3):
            self.fwd()


    def servoSweep(self):
        enable_servo()
        for ang in range(20,160,3):
            servo(ang)
            time.sleep(.1)
            self.sweep[ang] = us_dist(15)

    def checkDist(self):
        servo(90)
        time.sleep(1)
        self.status['dist'] = us_dist(15)
        if dist > MIN_DISTANCE:
            print('Forward is fine with me', dist)
            return True
        else:
            return False



    def safeDrive(self):
        self.fwd()
        counter = 0
        while self.checkDist:
            if counter % 10:
                print "driving safe!"
            counter += 1
        self.stop()

    def stop(self):
        self.status["ismoving"] = False
        print "EMERGENCY STOP"
        for x in range(3):
            self.stop()


    def isTherePath(self):
        print "Is there any path?"
        counter=0
        for ang in range(20,160,3):
            if self.vision[ang] > self.MIN_DISTANCE:
                counter+=1
            else:
                print "let's restart"
                counter=0
            if counter == 10:
                print "found an option"
                return True
        return False




    def turnTo(self, angle):
        turntime = .2
        BIGTURN = .5
        if angle < 50 or angle > 120:
            print "We're going to need a big turn"
            turntime = BIGTURN
        if angle < 90:
            print "Turning right"
            self.right_rot()
            time.sleep(turntime)
            self.stop()
        else:
            print "Turning left"
            self.left_rot()
            time.sleep(turntime)
            self.stop()



    def findAngle(self):

        if ang<90 and self.turned_right_last == False:
            enable_encoders()
            enc_tgt(1,1,ang/15)
            right_rot()
            self.turned_right_last = True
            time.sleep(1)
            safeDrive(self)
            print "right " + str(ang)
        elif ang>90 and self.turned_right_last == True:
            enable_encoders()
            enc_tgt(1,1,ang/15)
            left_rot()
            self.turned_right_last = False
            time.sleep(1)
            safeDrive(self)
            print "left " + str(ang)


    def turnRound(self):
        print "no option in current view"
        if self.turned_right_last == True:
            enable_encoders()
            enc_tgt(1,1,9)
            left_rot()
            self.turned_right_last = False
            time.sleep(1)
            safeDrive(self)
            print "no options must turn 90 degrees to the left"
        else:
            enable_encoders()
            enc_tgt(1,1,9)
            right_rot()
            self.turned_right_last = True
            time.sleep(1)
            safeDrive(self)
            print "no options must turn 90 degrees to the right"



tina = Pigo()

while True :
    if tina.servoSweep():
        tina.safeDrive()
    else:
        if tina.isTherePath():
            tina.turnTo(tina.findAngle())
        else:
            tina.turnRound()

tina.stop()