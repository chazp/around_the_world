# Chaz Chamberlin
# Fall 2013

# The Basketball game Around the World

import pdb
import sys
from random import randint

class AroundtheWorld():
    def __init__(self):
        self.chance_it, self.shot_percentage = self._get_command_argument()
        self.chance_first_half = False
        self.shots = ["start", "right_corner", "right_side",
                 "middle", "left_side", "left_corner", "end"]
        self.shot_percentage_location = {
            "start": 90,
            "right_corner": self.shot_percentage,
            "right_side": self.shot_percentage,
            "middle": self.shot_percentage,
            "left_corner": self.shot_percentage,
            "left_side": self.shot_percentage,
            "end": 90
        }
            
    def _get_command_argument(self):
        chance = ""
        if (len(sys.argv) < 3):
            print("Error. Parameters: chance it (all|half|none) and shot percentage (0 - 100)")
            exit(0)
        if (sys.argv[1] in ("all", "half", "none")):
            chance = sys.argv[1]
        else:
            raise Exception("invalid parameter")
        
        return chance, int(sys.argv[2])
        
            
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
        return (randint(1, 100) <= self.shot_percentage_location[current_location])

    def on_first_half(self, current_location):
        """
        Returns true if player is still on a shot
        on the first half of the court.
        Assumes "middle" shot is on second half.
        """
        return (self.shots.index(current_location) < 7)
        

    def play(self):
        current_location = "start"
        turns = 0
        shot = False

        while (current_location != "win"):
            shot = self.made_shot(current_location)
            if (self.chance_it == "all" or (self.chance_it == "half" and self.on_first_half(current_location))):
                shot = shot or self.made_shot(current_location) # shoot again
            turns += 1
            if (shot):
                current_location = self.get_next_location(current_location)
            elif (self.chance_it == "all" or (self.chance_it == "half" and self.on_first_half(current_location))): # player chanced it and missed both
                current_location = "start"
        return turns
            
                    

test = AroundtheWorld()
runs = 100000
total = 0.0

for i in range(runs):
    total += test.play()
print(total / runs)



