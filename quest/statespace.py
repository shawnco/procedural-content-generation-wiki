'''

Here is an example of a simple randomized quest generator. In this example, the
player wants to get enough animal skins to eventually upgrade to better swords.
As they do so, they unlock better regions of the world and eventually face the
final boss, which is a dragon.

'''

import random

# Simple example class for a Player
class Player:
    def __init__(self):
        self.current_town = ''
        self.animal_skins = 0
        self.sword = 0
        self.level = 0
        
# Cut-offs for how many animal skins you need to purchase the next sword type
sword_levels = [0, 10, 25, 50, 100]

# Three cities per region. The player travels between these regions, collecting
# animal skins. Once they've reached or exceeded the needed amount, they buy the
# next level sword then proceed to the next area. The final level is the dragon's
# lair.
regions = [
    ['Firsttown', 'Twoville', 'Threehold'],
    ['Fourwinds', 'Fivegates,', 'Sixtown'],
    ['Sevenhouse', 'Eighttown', 'Nineham'],
    ['Tentown', 'Elevensville', 'Twelveham'],
    ['Dragonslair']
]

player = Player()
while player.level < 4:
    # Go to a random town at your level
    start = random.randint(0,2)
    if regions[player.level][start] == player.current_town:
        # Add one and modulo to ensure no repeition
        player.current_town = regions[player.level][(start + 1) % 3]
    else:    
        player.current_town = regions[player.level][start]
    
    skins = random.randint(1,5)
    player.animal_skins = player.animal_skins + skins
    print('Capture {} skins at {}'.format(skins, player.current_town))
    
    # If you have enough skins to get the next level sword, purchase and hunt
    # At new places
    if player.animal_skins >= sword_levels[player.level + 1]:
        print('Advance sword to level {} for a cost of {} skins!'.format(player.level, player.animal_skins))
        player.level = player.level + 1
        player.animal_skins = 0
print('Fight the dragon at Dragonslair')        