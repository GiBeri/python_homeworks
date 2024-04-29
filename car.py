class Car:
    def __init__(self, color: str, model: str, makeYear: int, fuelType: str) -> None:
        self.color = color
        self.model = model
        self.makeYear = makeYear
        self.fuelType = fuelType
        self.name = self.makeYear + self.model

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
    obj2 = Car("Orange", "Audi", 2009, "Diesel")


if __name__ == "__main__":
    main()
