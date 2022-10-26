"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Employee:
    def __init__(self, _name, _pay, _commission=None):
        self.name = _name
        self.pay = _pay
        self.commission = _commission

    def get_pay(self):
        if self.commission:
            return self.pay.get_pay() + self.commission.commission_pay()
        return self.pay.get_pay()

    def __str__(self):
        commission_str = ""
        if self.commission:
            commission_str = self.commission.__str__()
        return f"{self.name} works on a {self.pay.__str__()}{commission_str}. Their total pay is {self.get_pay()}."


class ContractPay:
    def __init__(self, _pay):
        self.pay = _pay

    def __str__(self):
        pass

    def get_pay(self):
        return self.pay


class SalaryContract(ContractPay):
    def __init__(self, _pay):
        super().__init__(_pay)

    def __str__(self):
        return f"monthly salary of {self.pay}"


class HourlyContract(ContractPay):
    def __init__(self, _hourly_pay, _hours):
        super().__init__(_hourly_pay * _hours)
        self.hourly_pay = _hourly_pay
        self.hours = _hours

    def __str__(self):
        return f"contract of {self.hours} hours at {self.hourly_pay}/hour"


class Commission:
    def __init__(self, _amount):
        self.amount = _amount

    def __str__(self):
        return " and receives a"

    def commission_pay(self):
        return self.amount


class BonusCommission(Commission):
    def __init__(self, _amount):
        super().__init__(_amount)

    def __str__(self):
        return f"{super().__str__()} bonus commission of {self.amount}"


class ContractCommission(Commission):
    def __init__(self, _amount, _number_of_contracts):
        super().__init__(_amount)
        self.number_of_contracts = _number_of_contracts

    def __str__(self):
        return f"{super().__str__()} commission for {self.number_of_contracts} contract(s) at {self.amount}/contract"

    def commission_pay(self):
        return self.amount * self.number_of_contracts


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee("Billie", SalaryContract(4000))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee("Charlie", HourlyContract(25, 100))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee("Renee", SalaryContract(3000), ContractCommission(200, 4))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee("Jan", HourlyContract(25, 150), ContractCommission(220, 3))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee("Robbie", SalaryContract(2000), BonusCommission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee("Ariel", HourlyContract(30, 120), BonusCommission(600))
