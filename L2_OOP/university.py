class People:
    """
    The code defines classes for People, Lecturer, and Student
    with methods to get their email addresses
    and demonstrates their usage in the main function.
    """

    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname

    def get_email(self) -> str:
        return f"{self.firstname}.{self.lastname}.uni@btu.edu.ge"


class Lecturer(People):
    def __init__(self, firstname: str, lastname: str, salary: int) -> None:
        super().__init__(firstname, lastname)
        self.salary = salary

    def get_email(self) -> str:
        return f"{self.firstname}.{self.lastname}@btu.edu.ge"


class Student(People):
    def __init__(self, firstname: str, lastname: str, Courses: list[str] = []) -> None:
        super().__init__(firstname, lastname)
        self.Courses = Courses

    def get_email(self) -> str:
        return f"{self.firstname}.{self.lastname}.1@btu.edu.ge"


def main():
    s1 = Student("Giorgi", "Berishvili")
    l1 = Lecturer("Lika", "Svanidze", 5000)
    p1 = People("Leonardo", "Dicaprio")
    print(s1.get_email())
    print(l1.get_email())
    print(p1.get_email())


if __name__ == "__main__":
    main()
