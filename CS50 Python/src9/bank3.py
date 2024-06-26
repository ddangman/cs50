# Uses class


class Account:
    def __init__(self):
        self._balance = 0 # please treat as _private

    # property is an instance variable protected by setter and getter
    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n


def main():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    print("Balance after deposit:", account.balance)
    account.withdraw(25)
    print("Balance after withdraw:", account.balance)
    try:
        # balance property protected against direct change
        account.balance(5000)
        print("Balance after direct change:", account.balance)
    except TypeError:
        print("direct change to balance not allowed")



if __name__ == "__main__":
    main()
