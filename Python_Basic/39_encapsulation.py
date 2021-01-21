class MyClass:
    def __init__(self, a, b, c):
        self.a = a
        self._b = b
        self.__c = c

    def value_c(self):
        print(self.__c)


my_class = MyClass('I am Public', 'I am Protected', 'I am Private')
print(my_class.a, my_class._b)
my_class.value_c()
