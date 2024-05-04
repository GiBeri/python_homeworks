class Bank_Account:
    """class for bank account"""

    def __init__(self, __account_name: str, __balance: int = 0) -> None:
        self.__account_name = __account_name
        self.__balance = __balance

    def get_account_name(self) -> str:
        return self.__account_name

    def set_account_name(self, name: str):
        self.__account_name = name

    account_name = property(get_account_name, set_account_name)

    def deposit(self, amount: int):
        self.__balance += amount

    def withdraw(self, amount: int):
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


account1 = Bank_Account(input("enter your fullname:"))


def main():
    print(
        f"hello {account1.get_account_name()}, your current balance is {account1.get_balance()}"
    )

    def money():
        x = input("enter 0 to deposit, enter 1 to withdraw: ")
        if x == "0":
            account1.deposit(int(input("enter amount to deposit: ")))
            print(
                f"successfully deposited to your account, your current balance is {account1.get_balance()}"
            )
        elif x == "1":
            account1.withdraw(int(input("enter amount to withdraw: ")))
            print(
                f"successfully withdrew to your account, your current balance is {account1.get_balance()}"
            )

    while True:
        money()


if __name__ == "__main__":
    main()
