class Factorial:
    def __init__(self, num):
        self.num = num

    def CalcFactorial(self):
        factorial = 1
        while self.num > 1:
            factorial *= self.num
            self.num -= 1
        return factorial
