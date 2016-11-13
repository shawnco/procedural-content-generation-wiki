import perlin

# Create our generator.    
noise = Perlin();

# Let the user play with the algorithm.
print('Try it out! Enter three floating point numbers.')
print('Note: Try not to enter all integer numbers, otherwise you will get zero as output.')
print('That is a known part of Perlin noise''s functionality.')
x = float(input('X-coordinate: '))
y = float(input('Y-coordinate: '))
z = float(input('Z-coordinate: '))
ans = noise.getNoise(x,y,z)
print('Output: {}'.format(ans))