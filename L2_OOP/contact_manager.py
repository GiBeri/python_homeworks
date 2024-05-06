class Contacts:
    def __init__(self, name: str, phone: int) -> None:
        self.name = name
        self.phone = phone


class MailSender:
    def __init__(self, email: str) -> None:
        self.email = email

    def send_mail(self):
        print(f"your mail sent to: {self.email}")


class Friend(Contacts, MailSender):
    def __init__(self, name: str, phone: int, email: str) -> None:
        super().__init__(name, phone)
        MailSender.__init__(self, email)


class Family(Contacts, MailSender):
    def __init__(self, name: str, phone: int, email: str, birthdate: str) -> None:
        super().__init__(name, phone)
        MailSender.__init__(self, email)
        self.birthdate = birthdate


def main():
    fr1 = Friend("Jemali", 599695249, "jemali.@gmail.com")
    fa1 = Family("Alesqi", 599695289, "aleksi.@gmail.com", "01/31/2003")

    fr1.send_mail()
    fa1.send_mail()


if __name__ == "__main__":
    main()
