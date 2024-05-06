from enum import Enum


class Statuses(Enum):
    AVAILABLE = "available"
    OCCUPIED = "occupied"


class LibraryItem:
    def __init__(self, title: str, subject: str) -> None:
        self.title = title
        self.subject = subject
        self.status = Statuses.AVAILABLE

    def booking(self) -> None:
        if self.status == Statuses.AVAILABLE:
            print(f'Item "{self.title}" booked successfully')
            self.status = Statuses.OCCUPIED
        else:
            print(f'Item "{self.title}" already booked')

    def cancel_booking(self) -> None:
        if self.status == Statuses.OCCUPIED:
            print(f'Booking of item "{self.title}" canceled successfully')
            self.status = Statuses.AVAILABLE
        else:
            print('Item "{self.title}" isn\'t booked yet')


class Book(LibraryItem):
    def __init__(self, title: str, subject: str, ISBN: int, authors: str) -> None:
        super().__init__(title, subject)
        self.ISBN = ISBN
        self.authors = authors


class Magazine(LibraryItem):
    def __init__(
        self,
        title: str,
        subject: str,
        JournalName: str,
        volume: int,
    ) -> None:
        super().__init__(title, subject)
        self.JournalName = JournalName
        self.volume = volume


class CD(LibraryItem):
    def __init__(self, title: str, subject: str = "no subject available") -> None:
        super().__init__(title, subject)

    def booking(self) -> None:
        print("Cannot book a CD")

    def cancel_booking(self) -> None:
        print("Cannot book a CD")


def main():
    b1 = Book(
        title="Romeo and Juliet",
        authors="Shakespeare",
        subject="Romance",
        ISBN=9780671722852,
    )
    m1 = Magazine(
        title=" top 100 trains", subject="trains", JournalName="tu tuuu", volume=22
    )
    cd1 = CD("nadirobis sezoni 3 (chaxmovanebuli)")
    
    b1.booking()
    b1.cancel_booking()

    m1.booking()
    m1.cancel_booking()

    cd1.booking()
    cd1.cancel_booking()


if __name__ == "__main__":
    main()
