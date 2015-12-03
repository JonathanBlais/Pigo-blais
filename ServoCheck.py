__author__ = 'Jo'


from gopigo import *


class Pigo():

    sweep = [0] * 180
    FARDISTANCE = 90
    MIN_DISTANCE = 60

    status = {"ismoving" : False, "servo" : 90, "leftspeed" : 175,
              "rightspeed" : 175, "dist" : 100, "volt" : 2}

    def fwd(self):
        self.status["ismoving"] = True
        print "lets a go"
        for x in range(3):
            self.fwd()


    def servoSweep(self):
        enable_servo()
        for ang in range(20,160,5)
            servo(ang)
            time.sleep(.1)
            self.sweep[ang] = us_dist(15)

    def checkDist(self):
        servo(90)
            time.sleep(1)
            dist = us_dist(15)
            if dist > MIN_DISTANCE:
                print('Forward is fine with me', dist)
                return True
            else:
                return False



    def safeDrive(self):
        self.fwd()
        counter = 0
        while self.checkDist():
            if counter % 10:
                print "driving safe!"
            counter += 1
        self.stop()

    def stop(self):
        self.status["ismoving"] = False
        print "EMERGENCY STOP"
        for x in range(3):
            self.stop()





while True :
    if tina.checkDist()
        tina.safeDrive()
    else:
        tina.servoSweep()
        if tina.isTherePath():
            tina.turnto(tina.findAngle())
        else:
            tina.turnAround()