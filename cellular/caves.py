import pygame, sys, random

# Set up the window
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Cellular Cave Generation')
running = True

# Temporary grid for calculating lives
tempGrid = [[0]*50 for _ in range(50)]

# How likely should a cell be alive at start? Let's say .45
chanceToLive = .45

# Handy neighbor-checking function
def check_neighbors(x,y):
    live_neighbors = 0
    
    # Collect neighbors into a list for cleaner counting
    neighbors = []       
    for a in range(-1, 1):
        for b in range(-1, 1):
            neighbors.append(cells[x+a][y+b])
        
    for n in neighbors:
        if n is 1:
            live_neighbors += 1
    
    return live_neighbors
    
# Create a 50x50 grid of cells.
cells = [[0]*50 for _ in range(50)]

# Populate the grid
def populate():
    global cells
    for x in range(0,50):
        for y in range(0,50):
            ran = random.random()
            if ran < .45:
                cells[x][y] = 0
            else:
                cells[x][y] = 1
            
# Run a generation
def do_generation():
    global cells
    # Run the live-die function
    for i in range(4):
        tempGrid = [[0]*50 for _ in range(50)]
        for x in range(50):
            for y in range(50):
                neighbors = check_neighbors(x,y)

                # Apply the rules
                if cells[x][y] is 1 and neighbors < 2:
                    tempGrid[x][y] = 0
                elif cells[x][y] is 1 and (neighbors is 2 or neighbors is 3):
                    tempGrid[x][y] = 1
                elif cells[x][y] is 1 and neighbors > 3:
                    tempGrid[x][y] = 0
                elif cells[x][y] is 0 and neighbors is 3:
                    tempGrid[x][y] = 1
        cells = tempGrid
            
def display():        
    for x in range(0,50):
        for y in range(0,50):
            if cells[x][y] is 1:
                pygame.draw.rect(screen, (0,0,0), (x*10, y*10, 10, 10))
            else:
                pygame.draw.rect(screen, (255,255,255), (x*10, y*10, 10, 10))
    pygame.display.update()
    
# Our first population
populate()
# Do the display
display()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif e.type == pygame.MOUSEBUTTONDOWN:
            if e.button is 1:
                # Advance a generation
                do_generation()
                display()
            elif e.button is 3:
                # Restart
                populate()
                display()