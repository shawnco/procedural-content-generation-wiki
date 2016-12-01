import pygame, sys, math

# The set of coordinates to display and generate the Bezier curve for
coords = [
    (10, 50),
    (250, 400),
    (350, 100),
    (480, 480)
]

# The number of coordinates
n = 4


# Set up our Pygame window.
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Bezier Curve')
screen.fill((255,255,255))

# Do the binomial in its own function to make code cleaner.
def binomial(n,k):
    return math.factorial(n)/(math.factorial(k) * math.factorial(n-k))

# Do the polynomial in its own function to make code cleaner.
def polynomial(t,n,k):
    return ((1-t)**(n-k))*(t**k)

# Display our curve
running = True
while running:
    # Draw our dots
    for c in coords:
        pygame.draw.circle(screen, (0,0,0), c, 4, 0 )
        
    last_point = coords[0]
    # Generate our curve
    for i in range(1,100):
        if i is 1:
            print('########')
        t = i/100.0
        final_x = 0.0
        final_y = 0.0
        for k in range(n):
            final_x += binomial(n,k) * polynomial(t,n,k)*coords[k][0]
            final_y += binomial(n,k) * polynomial(t,n,k)*coords[k][1]
        new_point = (round(final_x), round(final_y))
        pygame.draw.line(screen, (0,0,0), last_point, new_point, 1 )
        last_point = new_point
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            
    pygame.display.update()
pygame.quit()
sys.exit()