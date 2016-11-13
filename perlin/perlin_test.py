import perlin

# Create our generator.    
noise = perlin.Perlin();

# Let the user play with the algorithm.
print('Try it out! Enter three floating point numbers.')
print('Note: Try not to enter all integer numbers, otherwise you will get zero as output.')
print('That is a known part of Perlin noise''s functionality.')

# Keep going until the user doesn't want to.
again = True
while(again):
    x = float(input('X-coordinate: '))
    y = float(input('Y-coordinate: '))
    z = float(input('Z-coordinate: '))
    ans = noise.getNoise(x,y,z)
    print('Output: {}'.format(ans))
    
    query = raw_input('Try again? Y/N: ')
    if(query == 'N' or query == 'n'):
        again = False