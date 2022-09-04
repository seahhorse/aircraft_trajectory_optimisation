import numpy as np
import math

class Point:
    def __init__(self, *position):
        self.x, self.y, self.z = position

        '''
        6 total discrete movement options (E W N S U D)
        '''
        self.actions = {0: [1,0,0], 
                        1: [-1,0,0],
                        2: [0,1,0],
                        3: [0,-1,0],
                        4: [0,0,1],
                        5: [0,0,-1]}

        self.drift_heading = 2 * np.random.rand(3) - 1

    def __str__(self):
        return f"Point ({self.x}, {self.y}, {self.z})"

    def __sub__(self, other):
        return abs(self.x-other.x) + abs(self.y-other.y) + abs(self.z-other.z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def location(self):
        return np.array([self.x, self.y, self.z])

    def move(self, x=False, y=False, z=False):
        self.x += x
        self.y += y
        self.z += z
        return self

    def drift(self):
        dx, dy, dz = np.random.normal(self.drift_heading, 1, 3).astype(int)
        return self.move(dx,dy,dz)

    def within_bounds(self, *boundaries):
        # Remain within the boundaries
        x_bound, y_bound, z_bound = boundaries
        within = self.x in range(0,x_bound) and self.y in range(0,y_bound) and self.z in range(0,z_bound)
        self.x = min(x_bound-1, max(0, self.x))
        self.y = min(y_bound-1, max(0, self.y))
        self.z = min(z_bound-1, max(0, self.z))
        return within

    def action(self, choice=-1):
        if choice != -1:
            return self.move(*self.actions.get(choice, -1))
        else:
            return self.action(np.random.randint(0, 6))

    def vector(self, other):
        if self == other:
            return np.array([0,0,0])
        vect = other.location() - self.location()
        return vect / math.sqrt(sum(vect*vect)) 
    
    def copy(self):
        return Point(self.x, self.y, self.z)