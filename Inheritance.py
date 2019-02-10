#!/usr/bin/python

#!Inheritance

class Cook:
    def make_tacos(self):
        print("The cook made Tacos Today")

    def make_tortillas(self):
        print("The cook decided to make tortillas, AGAIN!!!!")

    def make_surprise(self):
        print("The cook decided to surprise us today, YEEEE!!!!!")


myCook = Cook()
myCook.make_tacos()
myCook.make_tortillas()
myCook.make_surprise()

#!Specific Cook

class IndianCook:
    def make_tacos(self):
        print("Our indian cook made Tacos Today")

    def make_chicken(self):
        print("Our Indian cook decided to make chicken, AGAIN!!!!")

    def make_surprise(self):
        print("Our Indian cook decided to surprise us today, YEEEE!!!!!")

    def make_ribs(self):
        print("Our Indian cook prepared some ribs for us today")

myindiancook = IndianCook()
myindiancook.make_tacos()

#!Inherit
class JapaneseCook(IndianCook):
    def make_sashimi(self):
        print("My Japanese Cook made incredible Sashimi")

    def make_sushi(self):
        print("My Japanese Cook made tantalising sushi today")

myjapanesecook = JapaneseCook()
myjapanesecook.make_sashimi()



#!Go ahead and test it out!!!!
