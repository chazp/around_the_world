# Chaz Chamberlin
# Fall 2013

# The Basketball game Around the World

import pdb
from random import randint

class AroundtheWorld():
    def __init__(self):
        self.current_location = 'start'
        self.chance_it = False
        self.shots = ["start", "right_corner", "right_side",
                 "middle", "left_side", "left_corner", "end"]
        self.shot_percentage = {
            "start": 90,
            "right_corner": 70,
            "right_side": 70,
            "middle": 70,
            "left_corner": 70,
            "left_side": 70,
            "end": 90
        }

    def get_next_location(self, current_location):
        """
        Returns next shot. If current_shot is "end" 
        returns "win"
        """
        current_index = self.shots.index(current_location)
        return(self.shots[current_index + 1] if (current_location != "end") else 'win')

    def made_shot(self, current_location):
        """
        Shoots a basket and returns whether the player made it
        or not given the shot percentage at that location
        """
        return (randint(1, 100) <= self.shot_percentage[current_location])

    def play(self):
        current_location = "start"
        turns = 0
        shot = False
        print("Are you chancing it?: %s" % self.chance_it)
        while (current_location != "win"):
            shot = self.made_shot(current_location)
            if (self.chance_it):
                shot = shot or self.made_shot(current_location) # shoot again
            print("You shoot at %s. Results: %s" % (current_location, shot))
            turns += 1
            if (shot):
                current_location = self.get_next_location(current_location)
            elif (self.chance_it): # player chanced it and missed both
                current_location = "start"
        print("You win in only %d turns!" % turns)
            
                    

test = AroundtheWorld()
test.play()
