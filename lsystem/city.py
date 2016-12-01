import pygame

# Parameterized production rules can't be easily represented as dictionaries.
# Therefore they're written here as functions.
def production_rules(rule, params):
    if rule is 'house':
        if params == 6:
            return [['church', 0], ['house', params+1]]
        elif params == 10:
            return [['school', 0], ['house', 1]]
        else:
            return [['house', params+1], ['house', params+2]]
    elif rule is 'town_hall':
        if params == 0:
            return [['town_hall', 1], ['shop', 0], ['house', params+1]]
        else:
            return [['shop', 0], ['house', params+1]]
    else:
        return [[rule, params]]    
    
# The initial state
start = [['town_hall', 0]]
end = []

# Loop through and do the generating.
iterations = 5

for i in range(0,iterations):
    end = []
    for s in start:
        result = production_rules(s[0], s[1])
        for r in result:
            end.append(r)
    start = end

# Colors for the different buildings
building_colors = {
    'town_hall': (126,126,126),
    'shop': (0,255,0),
    'church': (0,0,255),
    'school': (255,0,0),
    'house': (0,0,0)
}

# Heights for the buildings
building_heights = {
    'house': 10,
    'church': 20,
    'school': 40,
    'shop': 50,
    'town_hall': 100
}

# We will start drawing from (10, 10)
x = 10
y = 10

# Set up the screen and draw the city.
pygame.init()
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption('L-System City')
running = True
screen.fill((255,255,255))
while running:
    for s in start:
        pygame.draw.rect(screen, building_colors[s[0]], (x, y, 10, building_heights[s[0]]))
        x += 15
        if x >= 970:
            x = 10
            y += 60    
    
    
#    for s in start:
#        pygame.draw.rect(screen, building_colors[s[0]], (i*20, 250, 10, building_heights[s[0]]))
#        i = i + 1
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()
sys.exit()