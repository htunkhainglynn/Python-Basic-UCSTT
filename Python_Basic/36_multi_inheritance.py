# multiple inheritance

class First:
    def fpass(self):
        print('Passed first year')


class Second:
    def spass(self):
        print('Passed second year')


class Third:
    def tpass(self):
        print('Passed third year')


class Final:
    def fipass(self):
        print('Passed final year')


class Graduate(First, Second, Third, Final):
    def grad(self):
        print('Graduated')


stu = Graduate()
stu.fpass()
stu.spass()
stu.tpass()
stu.fpass()
stu.fipass()
stu.grad()


# multiple level inheritance
class S1():
    def square(self, x):
        return x ** 2


class S2(S1):
    def cube(self, x):
        return x ** 3


class S3(S2):
    def fourth(self, x):
        return x ** 4


stage = S3()
print('Square is', stage.square(2))
print('Cube is', stage.cube(2))
print('Fourth is', stage.fourth(2))