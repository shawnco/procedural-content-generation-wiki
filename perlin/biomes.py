import perlin, sys, math, pygame

# The coordinates of the top left corner being displayed.
top = 0
left = 0

# Setup to get the Pygame window going.
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Biome Generation')

# We will see 50x50 blocks at any given time.
grid = [[0]*50]*50

# There will be three biomes in the terrain: desert, grass, and snowy. Each one is represented by its own color.
biome_colors = {
    0: (255,255,0), # Yellow
    1: (38,108,46),   # Forest green
    2: (255,255,255) # White
}

# Import an instance of our Perlin noise generator.
noise = perlin.Perlin()

# Ask the user what seed to use for the simulation.
seed = float(input('Enter the numerical seed: '))


screen.fill((255,255,255))
pygame.display.flip()
# Game loop
running = True
while running:
    # Iterate through the biome list and determine the biome.
    for x in range(left, 50+left):
        for y in range(top, 50+top):
            ans = abs(noise.getNoise(x/2, y/2, seed))
            if ans < .25:   # Deserts should be relatively uncommon
                color = biome_colors[0]
            elif ans < .85: # Grass should be the most common biome
                color = biome_colors[1]
            else:           # Snowy areas should also be uncommon
                color = biome_colors[2]
            pygame.draw.rect(screen, color, ((x-left)*10, (y-top)*10, 10, 10))

    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_w:
                top = top-1
            elif e.key == pygame.K_s:
                top = top+1
            elif e.key == pygame.K_a:
                left = left - 1
            elif e.key == pygame.K_d:
                left = left + 1
        if e.type == pygame.QUIT:
            running = False

    pygame.display.flip()
pygame.quit()
sys.exit()