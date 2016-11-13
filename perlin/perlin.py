# Port of Ken Perlin's noise algorithm to Python.
# Original implementation in Java
# Available at http://http://mrl.nyu.edu/~perlin/noise/

import math;

class Perlin():
    p = [0]*512
    permutations = [151,160,137,91,90,15,
   131,13,201,95,96,53,194,233,7,225,140,36,103,30,69,142,8,99,37,240,21,10,23,
   190, 6,148,247,120,234,75,0,26,197,62,94,252,219,203,117,35,11,32,57,177,33,
   88,237,149,56,87,174,20,125,136,171,168, 68,175,74,165,71,134,139,48,27,166,
   77,146,158,231,83,111,229,122,60,211,133,230,220,105,92,41,55,46,245,40,244,
   102,143,54, 65,25,63,161, 1,216,80,73,209,76,132,187,208, 89,18,169,200,196,
   135,130,116,188,159,86,164,100,109,198,173,186, 3,64,52,217,226,250,124,123,
   5,202,38,147,118,126,255,82,85,212,207,206,59,227,47,16,58,17,182,189,28,42,
   223,183,170,213,119,248,152, 2,44,154,163, 70,221,153,101,155,167, 43,172,9,
   129,22,39,253, 19,98,108,110,79,113,224,232,178,185, 112,104,218,246,97,228,
   251,34,242,193,238,210,144,12,191,179,162,241, 81,51,145,235,249,14,239,107,
   49,192,214, 31,181,199,106,157,184, 84,204,176,115,121,50,45,127, 4,150,254,
   138,236,205,93,222,114,67,29,24,72,243,141,128,195,78,66,215,61,156,180]
   
    def __init__(self):
        # Populate the p list
        # This is where the heart of the apparent randomness lies.
        for i in range(0,256):
            self.p[i] = self.permutations[i]
            self.p[256+i] = self.permutations[i]
           
    def getNoise(self, x, y, z):    
       # Get the point's grid location.
       X = int(math.floor(x)) & 255
       Y = int(math.floor(y)) & 255
       Z = int(math.floor(z)) & 255
       
       # Get the location of the point in its respective cube.
       x -= math.floor(x)
       y -= math.floor(y)
       z -= math.floor(z)
       
       # Get the fade function. Fade function makes it so you don't go from 0 to 1
       # In a linear fashion, but rather in a way that is more varied.
       u = self.fade(x)
       v = self.fade(y)
       w = self.fade(z)
       
       # Simulate the six faces of a cube.
       A = self.p[X]+Y
       AA = self.p[A]+Z
       AB = self.p[A+1]+Z
       B = self.p[X+1]+Y
       BA = self.p[B]+Z
       BB = self.p[B+1]+Z
       
       # Compute the values at the corners of the cube and average them out.
       return self.lerp(w, self.lerp(v, self.lerp(u, self.grad(self.p[AA  ], x  , y  , z   ),
                                                     self.grad(self.p[BA  ], x-1, y  , z   )),
                                        self.lerp(u, self.grad(self.p[AB  ], x  , y-1, z   ),
                                                     self.grad(self.p[BB  ], x-1, y-1, z   ))),
                           self.lerp(v, self.lerp(u, self.grad(self.p[AA+1], x  , y  , z-1 ),
                                                     self.grad(self.p[BA+1], x-1, y  , z-1 )),
                                        self.lerp(u, self.grad(self.p[AB+1], x  , y-1, z-1 ),
                                                     self.grad(self.p[BB+1], x-1, y-1, z-1 ))));

   
    def fade(self, t):
        return t * t * t * (t * (t * 6 - 15) + 10)
    
    def lerp(self, t, a, b):
        return a + t * (b - a)
    
    def grad(self, hash, x, y, z):        
        h = hash & 15
        # Ternary logic is hard to read, so I expanded it to if-elses.
        if h < 8:
            u = x
        else:
            u = y
        if h < 4:
            v = y
        else:
            if h == 12 or h == 14:
                v = x
            else:
                v = z
        if h & 1 == 0:
            result = u
        else:
            result = -u
        if h & 2 == 0:
            result += v
        else:
            result += -v
#        print(u,v,result)
        return result