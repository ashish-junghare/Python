class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Ammount):
        self.Name = Name
        self.Ammount = int(Ammount)

    def display(self):
        print("Name is: ", self.Name)
        print("Amount is: ", self.Ammount)

    def deposit(self, depo):
        self.Ammount = self.Ammount + depo

    def withdraw(self, depo):
        depo = 0
        self.Ammount = self.Ammount - depo

    def CalculateInterest(self, time):
        SI = (self.Ammount * BankAccount.ROI*time) / 100
        print("Simple Interest is: ", SI)


def main():
    obj1 = BankAccount("Ashish", "10000")
    obj1.display()
    obj1.deposit(3000)
    obj1.display()
    obj1.withdraw(2000)
    obj1.display()
    obj1.CalculateInterest(2)


if __name__ == "__main__":
    main()