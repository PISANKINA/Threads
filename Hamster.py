import names

from FactorialCalculator import Factorial


class Hamster:
    def __init__(self, name, count_hair):
        self.name = name
        self.count_hair = count_hair


class HamsterGenerator:
    def __init__(self, count_hair):
        self.count_hair = count_hair

    def CreateHamster(self):
        name = names.get_full_name()
        factorial = Factorial(self.count_hair)

        result = factorial.CalcFactorial()

        return Hamster(name, result)
