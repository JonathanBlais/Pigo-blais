from gopigo import *
import time

__author__ = 'Jo'

class Pigo:

    ########
    ######## BASIC STATUS AND METHODS
    ########

    status = {"ismoving": False, "servo": 90, "leftspeed": 175,
              "rightspeed": 175}

    def __init__(self):
        print "I'm such a robot. beep. beep."

    def stop(self):
        self.isMoving = False
        while stop() != 1:
            time.sleep(.1)
            print "Yikes, looks like I can't stop!"

    def fwd(self):
        self.isMoving = True
        while fwd() != 1:
            time.sleep(.1)
            print "Sorry boss, can't seem to get moving"


    ########
    ######## ADVANCED METHODS
    ########

########
######## MAIN APP STARTS HERE
########

stamkos = Pigo()
stamkos.fwd()
time.sleep(2)
stamkos.stop()


