from gopigo import *
import time

__author__ = 'Jo'

class Pigo:

    isMoving = False
    servoPos = 90

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


stamkos = Pigo()
stamkos.fwd()
time.sleep(2)
stamkos.stop()


