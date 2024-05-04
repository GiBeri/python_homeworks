import math


class Point:
    """class for points"""

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def find_distance(self) -> int:
        hypotenuse = math.sqrt(self.x**2 + self.y**2)
        return int(hypotenuse)

def main():
    point1 = Point(3, 4)
    point2 = Point(6, 9)

    print(point1.find_distance())
    print(point2.find_distance())

if __name__ == "__main__":
    main()