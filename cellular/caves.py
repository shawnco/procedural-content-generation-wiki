import pygame, sys, random

# Set up the window
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Cellular Cave Generation')
running = True

# Create a 50x50 grid of cells.
cells = [[0]*50 for _ in range(50)]

# Temporary grid for calculating lives
tempGrid = [[0]*50 for _ in range(50)]

# How likely should a cell be alive at start? Let's say .45
chanceToLive = .45

# Handy neighbor-checking function
def check_neighbors(x,y):
    dead_neighbrors = 0
    live_neighbors = 0
    
    # Collect neighbors into a list for cleaner counting
    neighbors = []
    if x > 0:
        
            
    
    

# Populate the grid
for x in range(0,50):
    for y in range(0,50):
        ran = random.random()
        if ran < .45:
            cells[x][y] = 0
        else:
            cells[x][y] = 1
            
# Iterate 4 times
for i in range(4):
    for x in range(50):
        for y in range(50):
            neighbors = check_neighbors(x,y)
                
    cells = tempGrid

# The display window.
while running:
    # Draw the cells
    for x in range(0,50):
        for y in range(0,50):
            if cells[x][y] == 0:
                pygame.draw.rect(screen, (0,0,0), (x*10, y*10, 10, 10))
            else:
                pygame.draw.rect(screen, (255,255,255), (x*10, y*10, 10, 10))
                
    # Handle quit input
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()
sys.exit()