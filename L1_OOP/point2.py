import math


class Point:
    """class for points"""

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x},{self.y})"

    def find_point_distance(self, other: "Point"):
        point_distance = math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)
        return int(point_distance)


def main():
    a = Point(int(input("enter x value for a: ")), int(input("enter y value for a: ")))
    b = Point(int(input("enter x value for b: ")), int(input("enter y value for b: ")))
    print(a.find_point_distance(b))


if __name__ == "__main__":
    main()
