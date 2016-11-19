import perlin, sys, math, pygame

# The coordinates of the top left corner being displayed.
top = 0
left = 0
depth = 0

# Setup to get the Pygame window going.
pygame.init()
screen = pygame.display.set_mode((500, 550))
pygame.display.set_caption('Procedural Galaxy')
font = pygame.font.SysFont('Arial', 25)
small_font = pygame.font.SysFont('Arial', 16)

# View modes: galaxy, solarsystem, and planet
view_mode = 'galaxy'

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

# We have three noise generators: first for finding the star size, one for finding the star color, one for finding planet colors
color_noise = perlin.Perlin()
size_noise = perlin.Perlin()
planet_noise = perlin.Perlin()

# Ask the user what seed to use for the simulation.
seed = float(input('Enter the numerical seed: '))   

#screen.fill((255,255,255))
pygame.display.flip()
# Game loop
running = True
while running:
    # Clear the screen
    screen.fill((0,0,0))
    
    # Show the galaxy screen
    if view_mode is 'galaxy':
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

        # Draw a white square around the current grid we're on.
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_y < 500:
            pygame.draw.rect(screen, (255,255,255), ((mouse_x - (mouse_x % 50)), (mouse_y - (mouse_y % 50)), 50, 50), 1 )
            
        # Show the instructions at the bottom of the screen.
        screen.blit(font.render('X: ' + str(top) , True, (255,255,255)), (0,500))
        screen.blit(font.render('Y: ' + str(left), True, (255,255,255)), (100,500))
        screen.blit(font.render('Z: ' + str(depth), True, (255,255,255)), (200,500))
        screen.blit(small_font.render('WASDQE to move', True, (255,255,255)), (350,500))
    
    # Show the solar system screen
    elif view_mode is 'solarsystem':
        # Reacquire the color of the star
        color = abs(color_noise.getNoise(click_x*seed, click_y*seed*.25, depth*seed*.5))
        if color < .5:
            star_color = 1
        elif color < .65:
            star_color = 0
        else:
            star_color = 2
        pygame.draw.circle(screen, star_colors[star_color], (0,250), 50, 0)
        
        # Bigger stars should have more planets.
        planet_count = round(abs(size_noise.getNoise(click_x*seed*.25, click_y*seed*.5, depth*seed))*10)
        if planet_count > 5:
            planet_count = 5
            
        for p in range(0,planet_count):     
            # Make the color of the planets gradually change the further you get from the parent star.
            pygame.draw.circle(screen, (math.floor(star_colors[star_color][0]/(planet_count-p+1)), math.floor(star_colors[star_color][1]/(planet_count-p+1)), math.floor(star_colors[star_color][2]/(planet_count-p+1))), (100+(p*75), 250), 25, 0)
        
        # Show the instructions at the bottom of the screen.
        screen.blit(font.render('X: ' + str(int(click_x)), True, (255,255,255)), (0,500))
        screen.blit(font.render('Y: ' + str(int(click_y)), True, (255,255,255)), (100,500))
        screen.blit(font.render('Z: ' + str(int(depth)), True, (255,255,255)), (200,500))
        screen.blit(small_font.render('Z to return to galaxy view', True, (255,255,255)), (300,500))

    else:
        print('There has been an error.')
                        
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            if view_mode is 'galaxy':
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
            elif e.key == pygame.K_z and view_mode is 'solarsystem':
                view_mode = 'galaxy'
        elif e.type == pygame.MOUSEBUTTONDOWN:            
            # Swap the view as needed.
            if mouse_y < 500 and view_mode is 'galaxy':
                # Find the grid location of the mouse click.
                click_x = left + (mouse_x - (mouse_x % 50))/50
                click_y = top + (mouse_y - (mouse_y % 50))/50
                
                # Swap to solar system view ONLY if there's a star there.
                size = abs(size_noise.getNoise(click_x*seed*.25, click_y*seed*.5, depth*seed))
                if size >= .15:
                    view_mode = 'solarsystem'
        elif e.type == pygame.QUIT:
            running = False

    pygame.display.flip()
pygame.quit()
sys.exit()