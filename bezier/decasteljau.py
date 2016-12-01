import pygame, math, sys

# The set of coordinates to display and generate the Bezier curve for
coords = [
    (10, 50),
    (250, 400),
    (350, 100),
    (480, 480)
]

# Set up our Pygame window.
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Bezier Curve')
screen.fill((255,255,255))

for c in coords:
    pygame.draw.circle(screen, (0,0,0), c, 4, 0)

def draw_curve(points, t):
    if(len(points) is 1):
        p = (round(points[0][0]), round(points[0][1]))
        pygame.draw.circle(screen, (255,0,0), p, 4, 0)
    else:
        length = len(points)-1
        new_points = [(0,0) for _ in range(length)]
        for i in range(len(new_points)):
            x = (1-t) * points[i][0] + t * points[i+1][0]
            y = (1-t) * points[i][1] + t * points[i+1][1]
            new_points[i] = (x,y)
        draw_curve(new_points, t)
        
draw_curve(coords, .2)

while True:
    pygame.display.update()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()