class Mammal(object):
    def __init__(self, mammal_name):
        print(mammal_name, 'is a warm-blooded animal.')


class Dog(Mammal):
    def __init__(self):
        print('Dog has four legs.')
        super().__init__('Dog')


d1 = Dog()