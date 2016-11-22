import turtle

# The window we'll be drawing on.
screen = turtle.Screen()

# Our drawing agent.
t = turtle.Turtle()
t.penup()
t.setheading(90)
t.goto(0,-250)
t.pendown()
t.speed(0)

# This list holds the pushed locations with their corresponding angle.
locations = []

# The string holding our completed rules.
finish = ''

# The dict for our production rules.
production_rules = {
    'X': 'F-[[X]+X]+F[+FX]-X',
    'F': 'FF'
}

# The input string we are given.
start = 'X'

# Iterate through and create our L-system
iterations = 6
for i in range(0,iterations):
    finish = ''
    for s in start:
        if s in production_rules:
            finish = finish + production_rules[s]
        else:
            finish = finish + s
    start = finish

# Process the rules
for s in start:
    if s is 'F':
        t.forward(5)
    elif s is '+':
        t.left(25)
    elif s is '-':
        t.right(25)
    # Push/pop location
    elif s is '[':
        locations.append([t.xcor(), t.ycor(), t.heading()])
    elif s is ']':
        t.penup()
        pos = locations.pop()
        t.goto(pos[0], pos[1])
        t.setheading(pos[2])
        t.pendown()

# Don't let the window close immediately.
turtle.done()