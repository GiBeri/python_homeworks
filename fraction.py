class Fraction:
    """class for fractions"""

    def __init__(self, top: int, bottom: int) -> None:
        self.top = top
        self.bottom = bottom

    def __str__(self) -> str:
        return f"{self.top}/{self.bottom}"

    def total_sum(self, other: "Fraction") -> str:
        new_top = self.top * other.bottom + other.top * self.bottom
        new_bottom = self.bottom * other.bottom
        return f"{new_top}/{new_bottom}"

    def inverse(self):
        return f"{self.bottom}/{self.top}"


def main():
    obj1 = Fraction(5, 6)
    obj2 = Fraction(3, 4)
    print(obj1.total_sum(obj2))
    print(obj2.inverse)


if __name__ == "__main__":
    main()
