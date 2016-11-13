import perlin
import sys
import pygame
import math

# What's the width of a given block? This will determine most other visual settings.
SIZE = 50

# Setup to get the Pygame window going.
pygame.init()
screen = pygame.display.set_mode((10*SIZE, 10*SIZE))
pygame.display.set_caption('Biome Generation')

# What's the size we 

# Our example will be a 50*50 grid.
grid = [[0]*SIZE]*SIZE

# There will be three biomes in the terrain: desert, grass, and snowy. Each one is represented by its own color.
biomes = {
    0: (255,255,0), # Yellow
    1: (38,108,46),   # Vibrant reen
    2: (255,255,255) # White
}

# Assign a randomly chosen value to be the seed. We'll use this as the z value.
seed = 101.0

# Import an instance of our Perlin noise generator.
noise = perlin.Perlin()

# Iterate through each grid element and assign it a value.
for x in range(0,SIZE):
    for y in range(0, SIZE):
        # Dividing by 2 is done because if you pass Perlin whole numbers (like 1.0, 2.0, etc.)
        # You'll get nothing but 0's, which isn't very interesting.
        value = abs(noise.getNoise(x/2,y/2,seed))
        if value < .1:
            grid[x][y] = 0
        elif value < .85:
            grid[x][y] = 1
        else:
            grid[x][y] = 2
#        print(x,y,value)
        

# Blit everything to the screen
screen = pygame.Surface(screen.get_size())
screen.blit(screen, (0, 0))
pygame.display.flip()

# Event loop
while 1:
    
#    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,0,0), (10,10,50,50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(screen, (0, 0))
    pygame.display.flip()