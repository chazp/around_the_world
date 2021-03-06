Around the World Simulation
===========================
![](https://raw.github.com/chazp/around_the_world/master/pictures/AroundtheWorld.PNG)

## Rules ##
Around the World is a basketball game consisting of six shot locations (the picture shows seven. The amount of shots and location vary). The goal is to make it "around" the three-point line first by making baskets. If you shoot and make the shot, move to the next position and continue shooting. If you miss the shot, play continues with next person and you stay where you are. Or, if you miss the shot you can "chance" it and shoot again. If you make your "chance" shot you continue as normal, but if you miss your "chance" shot you start over at the first shot location.

Complete rules:
http://en.wikipedia.org/wiki/Variations_of_basketball#Around_the_World

## Simulation ##
This program simulates games of Around the World in order to determine whether a player with a specific shot percentage should always chance it, never chance it, or only chance it for the first half of the shots. 

The data table shows the average number of turns per game if the person playing 
has the given shot percentage and the three options on whether they should "chance"
it or not

For each shot percentage and variation on "chance", 100,000 games were simulated.

![](https://raw.github.com/chazp/around_the_world/master/pictures/Data1.png)

![](https://raw.github.com/chazp/around_the_world/master/pictures/Data2.png)

The data and graph show that a person whose shot is **below 60% should never "chance" it.** A person who shoots **between 60% and 80% should "chance" it for the first half of the shots.** A player shooting **above 80% should always "chance" it** (though at that point all three options are very close).

