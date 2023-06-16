class Salary:
    def calculate(self, hours):
        return self.rate * hours
    # define Salary class and associated methods here


class Promotable:
    def promote(self, rate, increase):
        return rate + increase
    # define Promotable class and associated methods here


# Do NOT change the code below:
class Employee(Salary, Promotable):
    def __init__(self, rate: float):
        self.rate = rate

    def weekly_salary(self) -> float:
        return self.calculate(40)
