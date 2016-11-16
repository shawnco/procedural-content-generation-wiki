import perlin, sys, math, pygame

# The coordinates of the top left corner being displayed.
top = 0
left = 0
depth = 0

# Setup to get the Pygame window going.
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Procedural Galaxy')

# We will see 10x10 blocks at any given time.
grid = [[0]*10]*10

# There will be three star colors: red, yellow, and blue.
star_colors = {
    0: (255,0,0), # Red
    1: (213,213,0), # Yellow
    2: (0,0,255) # Blue
}

# Stars come in three sizes: dwarf, normal, and giant.
star_sizes = {
    0: 5,
    1: 10,
    2: 25
}

# We have two noise generators: first for finding the star size, one for finding the star color.
color_noise = perlin.Perlin()
size_noise = perlin.Perlin()

# Ask the user what seed to use for the simulation.
seed = float(input('Enter the numerical seed: '))


#screen.fill((255,255,255))
pygame.display.flip()
# Game loop
running = True
while running:
    # Clear the screen
    screen.fill((255,255,255))
    
    # Run through and determine the sizes and colors of the stars.
    for x in range(left, 10+left):
        for y in range(top, 10+top):
            size = abs(size_noise.getNoise(x*seed*.25, y*seed*.5, depth*seed))
            # We don't want the entire thing filled with stars. Let's make some empty space.
            if size >= .15:
                if size < .45:
                    star_size = 1
                elif size < .75:
                    star_size = 0
                else:
                    star_size = 2

                # Now get the star color. Half yellow, the other half split red and blue.
                color = abs(color_noise.getNoise(x*seed, y*seed*.25, depth*seed*.5))
                if color < .5:
                    star_color = 1
                elif color < .65:
                    star_color = 0
                else:
                    star_color = 2

                # Let's make this more visually interesting by offsetting the stars from the center of their slots.
                offset_x = math.floor(size_noise.getNoise(x/4, y/4, depth)*20)
                offset_y = math.floor(size_noise.getNoise(x/2, y/2, depth)*20)
                # Draw the star at the center of its given slot.
                pygame.draw.circle(screen, star_colors[star_color], (offset_x+25+(x-left)*50, offset_y+25+(y-top)*50), star_sizes[star_size], 0)

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
            elif e.key == pygame.K_q:
                depth = depth - 1
            elif e.key == pygame.K_e:
                depth = depth + 1
        if e.type == pygame.QUIT:
            running = False

    pygame.display.flip()
pygame.quit()
sys.exit()