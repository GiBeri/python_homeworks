class Cat:
    def eat(self) -> None:
        print("cat eats fish")

    def talk(self) -> None:
        print("cat meows")

    def walk(self) -> None:
        print("cat runs at 20 km/h")


class Dog:
    def eat(self) -> None:
        print("dog eats dog")

    def talk(self) -> None:
        print("dog barks")

    def walk(self) -> None:
        print("dog runs at 30 km/h")


def main():
    luna = Dog()
    fofo = Cat()
    luna.eat()
    fofo.eat()


if __name__ == "__main__":
    main()
