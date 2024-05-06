class People:
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


class Doctoral_student(Lecturer, Student):
    def __init__(
        self, firstname: str, lastname: str, salary: int, Courses: list[str] = []
    ) -> None:
        super().__init__(firstname, lastname, salary)
        self.Courses = Courses


def main():
    s1 = Doctoral_student("Dea", "Zurabishvili", 2500)

    print(s1.get_email())


if __name__ == "__main__":
    main()
