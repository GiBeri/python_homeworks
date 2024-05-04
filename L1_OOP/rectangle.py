class Rectangle:
    """class for rectangle"""

    def __init__(self, height: int, width: int, color: str) -> None:
        self.height = height
        self.width = width
        self.color = color

    def get_perimeter(self):
        return self.height * 2 + self.width * 2

    def get_area(self):
        return self.height * self.width


def main():
    obj1 = Rectangle(1, 5, "blue")
    obj2 = Rectangle(3, 3, "green")
    obj3 = Rectangle(3, 7, "purple")

    print(obj1.get_area(), obj2.get_perimeter, obj3.get_area)


if __name__ == "__main__":
    main()
