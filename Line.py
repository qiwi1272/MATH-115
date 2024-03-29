import math
from Point import Point

class Line:
    def  __init__(self, a:Point, b:Point) -> None:
        self.a = a
        self.b = b
        self.m = self.get_slope()
        self.y_int = self.get_y_intercept()
        
    #distance formula
    def get_distance(self):
        """Returns the distance between two points"""
        #___ Algebra clarity, ignore ___#
        a = self.a
        b = self.b
        #___ end ___#

        # Get difference of x, y values.
        a_avg = a.x - b.x
        b_avg = a.y - b.y

        # Pythagorean theorem: a^2 + b^2 = c^2
        # Therefore,  a_avg^2 + b_avg^2 = distance^2
        total_dist_squared = a_avg**2 + b_avg**2

        # Pythagorean theorem:  Square root of distance^2 to distance
        if total_dist_squared == 1 or total_dist_squared == -1:
            print(f'+-{total_dist_squared}')
        distance = math.sqrt(total_dist_squared)

        return distance

    #midpoint formula
    def midpoint(self) -> Point:
        """Returns the middle point between two points"""
        #___ Algebra clarity, ignore ___#
        a = self.a
        b = self.b
        #___ end ___#

        # pretty fuckin simple bud
        a_mid = (a.x + b.x)/2
        b_mid = (a.y + b.y)/2

        midpoint  = Point(a_mid, b_mid)

        return midpoint
    


    
    def get_slope(self):
        # difference in y / difference in x
        return (b.y - a.y) / (b.x - a.x)
    
    def get_y_intercept(self):
        # use slope to solve for b
        return a.y - (a.x * self.m)
    
a  = Point(5, 12)
b = Point(-6, -5)
L = Line(a, b)
M = L.midpoint()
#print(M.x, M.y)
print(L.m, L.y_int)