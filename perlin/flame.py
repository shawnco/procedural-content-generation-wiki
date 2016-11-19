import perlin, pygame, math

# Our noise object
noise = perlin.Perlin()

# Setup to get the Pygame window going.
pygame.init()
screen = pygame.display.set_mode((500, 550))
pygame.display.set_caption('Procedural Galaxy')
pygame.display.flip()

# The display loop
while True:
    #screen.fill((0,0,0))
    for x in range(0,500):
        for y in range(0,500):
            val = abs(noise.getNoise(x/2, y/2, 100.0))
            print(math.floor(val*255), math.floor(255*val), math.floor(255*val))
            pygame.draw.rect(screen, (math.floor(val*255), math.floor(255*val), math.floor(255*val)), (x,y,1,1))