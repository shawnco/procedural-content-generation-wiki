import pygame, sys

# The production rules is a dictionary of graph fragments and their replacements.
# Each node type will have its own phrase and its own color.

class Node:
    def __init__(self, phrase):
        self.phrase = phrase
        self.children = []
    
    def addChildren(self, add):
        self.children.append(add)

# The production rules list phrases and things to replace them with. Commas indicate nodes that are children of the parent.
# Semicolons indicate a new branch.
rules = {
    'start': [['fight troll'],['fight boss']],
    'fight troll': [['enter dungeon/swim in river']],
    'fight boss': [['fight troll'],['unlock castle'],['enter castle'],['fight big troll'],['fight king']]
}

# Colors to differentiate the different types of dungeons
colors = {
    'begin': (192,0,0),
    'start': (0,0,0),
    'fight troll': (255,0,0),
    'fight boss': (0,255,0),
    'enter dungeon': (255,255,0),
    'swim in river': (0,0,255),
    'unlock castle': (255,0,255),
    'enter castle': (124,0,0),
    'fight big troll': (0,124,0),
    'fight king': (0,255,255)
    
}

# Just as a means of getting things started.
graph = ['start']

# Iterate some times.
for i in range(4):
    temp = []
    for g in graph:
        if g in rules:
            for r in rules[g]:
                for e in r:
                    temp.append(e)
        else:
            temp.append(g)
    graph = temp
            
print(graph)

'''
Building the graph
* create the begin node
* for each string in the array:
    * if there is a / in the name, split it into two nodes and append them both as children of the previous node
        * make the prevNode list these
    * else append this as a child of the previous node
        * make the prevNode list these
    
    
'''

# Create the begin node
nodes = Node('begin')
prevNodes = [nodes]
for g in graph:
    print(g, prevNodes)
    if '/' in g:
        actions = g.split('/')
        length = len(actions)
        new_nodes = []
        for l in range(length):
            new_nodes.append( Node(actions[1]) )
            for p in prevNodes:
                p.addChildren(new_nodes[l])
        prevNodes = []
        for n in new_nodes:
            prevNodes.append(n)
    else:
        for p in prevNodes:
            new_node = Node(g)
            p.addChildren(new_node)
        prevNodes = [new_node]
        
def showChildren(node, level):
    print('{} {}'.format('*'*level, node.phrase))
    for c in node.children:
        showChildren(c, level+1)
showChildren(nodes, 1)

# Display!
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Bezier Curve')
screen.fill((255,255,255))

def drawNodes(node, x, y, parentXY):
    pygame.draw.rect(screen, colors[node.phrase], (x,y,10,10))
    pygame.draw.line(screen, (0,0,0), parentXY, (x,y), 1)
    child_x = x + 20
    child_y = y
    for c in node.children:
        drawNodes(c, child_x, child_y, (x,y))
        child_y += 20
drawNodes(nodes, 10, 10, (0,10))
        

pygame.display.update()
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
