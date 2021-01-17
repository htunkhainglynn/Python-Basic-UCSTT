class Animal:
    def leg_count(self): # normal method
        self.leg = 2
        self.hand = 2


dog = Animal()
dog.leg_count()
print(f'Dog has {dog.leg} legs')
print(f'Dog has {dog.hand} hands')

chicken = Animal()
chicken.leg_count()
chicken.leg = 2
chicken.hand = 0
print(f'Chicken has {chicken.leg} legs')
print(f'Chicken has {chicken.hand} hands')
