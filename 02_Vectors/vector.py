import math

class Vector:

    def __init__(self, values):
        self.values = list(values)

    def __repr__(self):
        return f"Vector({self.values})"

    def __len__(self):
        return len(self.values)

    def __getitem__(self, index):
        return self.values[index]

    def __add__(self, other):
        return Vector([a+b for a, b in zip(self.values, other.values)])
        
    def __sub__(self, other):
        return Vector([a-b for a,b in zip(self.values, other.values)])
    
    def __mul__(self, scalar):
        return Vector([x * scalar for x in self.values])
    
    def dot(self, other):
        return sum ([x*y for x, y in zip(self.values, other.values)])
    
    def magnitude(self):
        return math.sqrt (sum(x * x for x in self.values))
    
    def __neg__(self):
        return Vector([-x for x in self.values])

    def __eq__(self, other):
        return self.values == other.values

    def __iter__(self):
        return iter(self.values)
    
    def __setitem__(self, index, value):
         self.values[index] = value

    def __contains__(self, value):
        return value in self.values

    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    
    def normalize(self):
        magnitude = self.magnitude()

        if magnitude == 0:
            raise ValueError("Cannot normalize a zero vector.")

        return Vector([x / magnitude for x in self.values])

    def distance(self, other):
        difference = self - other
        return difference.magnitude()

    def copy(self):
        return Vector(self.values)


    def cross(self, other):
        if len(self) != 3 or len(other) != 3:
            raise ValueError("Cross product only works for 3D vectors.")
        
        x1, y1, z1 = self.values
        x2, y2, z2 = other.values


        return Vector([
            y1*z2 - z1*y2,
            z1*x2 - x1*z2,
            x1*y2 - y1*x2
        ])
    

    def angle(self, other):

        dot = self.dot(other)

        m1 = self.magnitude()
        m2 = other.magnitude()

        if m1 == 0 or m2 == 0:
            raise ValueError("Cannot compute angle with a zero vector.")
        
        cos_theta = dot / (m1 * m2)

        cos_theta = max(-1, min(1, cos_theta))

        return math.degrees(math.acos(cos_theta))