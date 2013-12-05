# Chaz Chamberlin
# Fall 2013

# The Basketball game Around the World

import pdb
from random import randint

class AroundtheWorld():
    def __init__(self):
        self.current_location = 'start'
        self.shots = ["start", "right_corner", "right_side",
                 "middle", "left_side", "left_corner", "end"]
        self.shot_percentage = {
            "start": 50,
            "right_corner": 50,
            "right_side": 50,
            "middle": 50,
            "left_corner": 50,
            "left_side": 50,
            "end": 50
        }

    def get_next_location(self, current_location):
        """
        Returns next shot. If current_shot is "end" 
        returns "win"
        """
            return (self.shots[current_location + 1] 
                    if current_location is not "end" else "win")

    def made_shot(self, current_location):
        """
        Shoots a basket and returns whether the player made it
        or not given the shot percentage at that location
        """
        return (randint(1, 100) <= self.shot_percentage[current_location])

    def play():
        current_location = "end"
        shot = False
        while (current_location != "end"):
            shot = self.made_shot(current_location)
            print("Shot at %s: %s" % (current_location, shot))
            if (shot)
                current_location = self.get_next_location(current_location)
        print("You win!")
            
                    

test = AroundtheWorld()
print(test.shot_percentage["right_side"])
for i in range(10):
    print(test.made_shot("start"))
