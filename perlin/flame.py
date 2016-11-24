import perlin, pygame, math, sys

# Our noise object
noise = perlin.Perlin()

# Setup to get the Pygame window going.
pygame.init()
screen = pygame.display.set_mode((250, 250))
pygame.display.set_caption('Procedural Flame')

# Generate our grid
grid = [[0]*25 for _ in range(25)]

# Fill the grid
for x in range(25):
    for y in range(25):
        #grid[x][y] = abs(noise.getNoise(x/2, y/4, 1))
        val = noise.getNoise(x/4, y/2, 1)
        print(val)
        if val < .5:
            grid[x][y] = (255,0,0)
        else:
            grid[x][y] = (0,0,255)

# The display loop
while True:
    for x in range(0,25):
        for y in range(0,25):
            #pygame.draw.rect(screen, (math.floor(255*grid[x][y]), math.floor(255*grid[x][y]), math.floor(255*grid[x][y])), (10*x,10*y,10,10))
            pygame.draw.rect(screen, grid[x][y], (10*x, 10*y, 10, 10))
    pygame.display.update()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()