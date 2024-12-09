from enum import Enum
from math import sqrt

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_to(self, other: 'Point') -> float:
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

class Colour(Enum):
    RED = 'Red'
    GREEN = 'Green'
    BLUE = 'Blue'
    YELLOW = 'Yellow'
    BLACK = 'Black'

class Polynom:
    def __init__(self, points: list[Point], colour: Colour):
        self.points = points
        self.colour = colour

    def perimeter(self) -> float:
        if len(self.points) < 2:
            return 0
        perimeter = 0
        for i in range(len(self.points)):
            perimeter += self.points[i].distance_to(self.points[(i + 1) % len(self.points)])
        return perimeter

    def longest_diagonal(self) -> float:
        if len(self.points) < 2:
            return 0
        max_diagonal = 0
        for i in range(len(self.points)):
            for j in range(i + 1, len(self.points)):
                diagonal_length = self.points[i].distance_to(self.points[j])
                max_diagonal = max(max_diagonal, diagonal_length)
        return max_diagonal

    def sort_by_x(self):
        self.points.sort(key=lambda point: point.x)

    def sort_by_y(self):
        self.points.sort(key=lambda point: point.y)

    def __repr__(self):
        return f"Polynom(points={self.points}, colour={self.colour.value})"

if __name__ == "__main__":
    points = [Point(0, 0), Point(3, 4), Point(6, 0)]
    polynom = Polynom(points, Colour.RED)

    print("Багатокутник:", polynom)
    print("Периметр:", polynom.perimeter())
    print("Найдовша діагональ:", polynom.longest_diagonal())

    polynom.sort_by_x()
    print("Сортування за x:", polynom.points)

    polynom.sort_by_y()
    print("Сортування за y:", polynom.points)