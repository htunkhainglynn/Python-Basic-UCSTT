class Base:
    def __init__(self, name):
        self._name = name


class Sub(Base):
    def show(self):
        print('Name is ', self._name)


obj = Sub('KoKo')
obj.show()







