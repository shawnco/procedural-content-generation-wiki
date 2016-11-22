import perlin, pygame, math, sys

# Our noise object
noise = perlin.Perlin()

# Setup to get the Pygame window going.
pygame.init()
screen = pygame.display.set_mode((250, 250))
pygame.display.set_caption('Procedural Galaxy')
pygame.display.flip()

# The display loop
while True:
    for x in range(0,250):
        for y in range(0,250):
            pygame.draw.rect(screen, (255,0,0), (x,y,1,1))
    #screen.fill((0,0,0))
#    for x in range(0,250):
#        for y in range(0,250):
#            val = abs(noise.getNoise(x/2, y/2, 100.0))
#            print(math.floor(val*255), math.floor(255*val), math.floor(255*val))
#            pygame.draw.rect(screen, (126,126,126), (x,y,1,1))
#            pygame.draw.rect(screen, (math.floor(val*255), math.floor(255*val), math.floor(255*val)), (x,y,1,1))
    pygame.display.flip()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()