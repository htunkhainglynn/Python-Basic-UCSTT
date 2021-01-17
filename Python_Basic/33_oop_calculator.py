class Calculator:
    def __init__(self, nu1, nu2):
        self.num1 = nu1
        self.num2 = nu2

    def add(self):
        add = self.num1 + self.num2
        return add

    def sub(self):
        sub = self.num1 - self.num2
        return sub

    def multiply(self):
        mul = self.num1 * self.num2
        return mul

    def div(self):
        div = self.num1 / self.num2
        return div


no1 = int(input('Enter number 1: '))
no2 = int(input('Enter number 2: '))
cal = Calculator(no1, no2)
print('Add result', cal.add())
print('Sub result', cal.sub())
print('Multiply result', cal.multiply())
print('Div result', cal.div())
