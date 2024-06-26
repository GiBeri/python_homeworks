class Celsius:
    """class for temperature"""

    def __init__(self, __temperature: int) -> None:
        self.__temperature = __temperature

    def get_temp(self) -> int:
        """
        :return: temperature
        """
        return self.__temperature

    def set_temp(self, temperature: int) -> None:
        """sets temperature

        :param temperature: new temperature
        """
        self.__temperature = temperature

    def del_temp(self) -> None:
        """delete temperature"""

        del self.__temperature

    temperature = property(get_temp, set_temp, del_temp)


def main():
    obj1 = Celsius(30)
    obj2 = Celsius(25)

    print(obj1.temperature)
    obj1.temperature = 35
    print(obj1.temperature)
    print(obj2.temperature)
    del obj2.temperature


if __name__ == "__main__":
    main()
