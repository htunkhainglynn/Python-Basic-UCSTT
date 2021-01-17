class Alive:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs

    def legs_count(self):
        print(f'{self.name} has {self.legs} legs')

    def talk(self):
        print(f'{self.name}')

    def sleep(self):
        pass


class Animal(Alive):

    def __init__(self, name, legs, sleep_type):
        super().__init__(name, legs)
        self.sleep_ype = sleep_type

    def talk(self):
        print(f'{self.name} meows you')

    def sleep(self):
        print(f'{self.name} sleeps like {self.sleep_ype}')


class Human(Alive):

    def __init__(self, name, legs, sleep_type):
        super().__init__(name, legs)
        self.sleep_ype = sleep_type

    def talk(self):
        print(f'{self.name} loves you')

    def sleep(self):
        print(f'{self.name} sleeps like {self.sleep_ype}')


alien = Alive('Groot', 2)
alien.talk()
alien.legs_count()

human = Human('KoKo', 2, 'KhawKhaw')
human.talk()
human.legs_count()
human.sleep()

dog = Animal('Bob', 4, 'Zzzz')
dog.talk()
dog.legs_count()
dog.sleep()
