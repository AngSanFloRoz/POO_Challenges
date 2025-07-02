import math

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def get_x(self):
        return self.x
    
    def set_x(self, new_x):
        self.x = new_x
        return self.x
    
    def get_y(self):
        return self.y
    
    def set_y(self, new_y):
        self.y = new_y
        return self.y

    def compute_distance(self, another_point) -> float:
        return ((self.x - another_point.x) ** 2 + 
                (self.y - another_point.y) ** 2) ** 0.5

class Line:
    def __init__(self, start_point, end_point, lenght: float):
        self.start_point = start_point
        self.end_point = end_point
        self.lenght = start_point.compute_distance(end_point)

    def get_start_point(self):
        return self.start_point
    
    def set_start_point(self, new_start_point):
        self.set_start_point = new_start_point
        return self.start_point
    
    def get_end_point(self):
        return self.end_point
    
    def set_end_point(self, new_end_point):
        self.set_start_point = new_end_point
        return self.end_point
    
    def get_lenght(self):
        return self.lenght
    
    def set_lenght(self, new_lenght):
        self.lenght = new_lenght
        return self.lenght
    
class Shape:
    def __init__(self, vertices: list[Point]):
        self._vertices = vertices
        self._edges = self._create_edges(vertices)
        self._inner_angles = []
        self.is_regular = False

    def _create_edges(self, vertices):
        return [Line(vertices[i], vertices[(i + 1) % len(vertices)]) for i in range(len(vertices))]

    def compute_area(self):
        raise NotImplementedError

    def compute_perimeter(self):
        return sum(edge.get_length() for edge in self._edges)

    def compute_inner_angles(self):
        raise NotImplementedError


class Triangle(Shape):
    def compute_area(self):
        a, b, c = [edge.get_length() for edge in self._edges]
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    def compute_inner_angles(self):
        a, b, c = [edge.get_length() for edge in self._edges]
        angle_A = math.degrees(math.acos((b**2 + c**2 - a**2)/(2*b*c)))
        angle_B = math.degrees(math.acos((a**2 + c**2 - b**2)/(2*a*c)))
        angle_C = 180 - angle_A - angle_B
        self._inner_angles = [angle_A, angle_B, angle_C]
        return self._inner_angles


class Isosceles(Triangle):
    pass

class Equilateral(Triangle):
    def __init__(self, vertices: list[Point]):
        super().__init__(vertices)
        self.is_regular = True

class Scalene(Triangle):
    pass

class TriRectangle(Triangle):
    pass

class Rectangle(Shape):
    def compute_area(self):
        l1 = self._edges[0].get_length()
        l2 = self._edges[1].get_length()
        return l1 * l2

    def compute_inner_angles(self):
        self._inner_angles = [90.0] * 4
        return self._inner_angles

class Square(Rectangle):
    def __init__(self, vertices: list[Point]):
        super().__init__(vertices)
        self.is_regular = True
