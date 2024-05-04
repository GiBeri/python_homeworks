class Car:
    """class for cars"""

    def __init__(self, color: str, model: str, make_year: int, fuel_type: str) -> None:
        self.color = color
        self.model = model
        self.make_year = make_year
        self.fuel_type = fuel_type
        self.name = f"{self.make_year, self.model}"

    def sell(self):
        print(f"sold{self.name}")

    def buy(self):
        print(f"bought{self.name}")

    def rent(self):
        print(f"rented{self.name}")

    def insurance(self):
        print(f"insured{self.name}")


def main():
    obj1 = Car("Red", "Mercedes", 2015, "Gas")
    obj2 = Car("Blue", "BMW", 2013, "Gas")
    obj3 = Car("Orange", "Audi", 2009, "Diesel")

    obj1.rent()
    obj2.insurance()
    obj3.buy()


if __name__ == "__main__":
    main()
