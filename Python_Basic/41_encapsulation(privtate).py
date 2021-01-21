class Dog:
    __name = 'Bob'  # Dog class attributes
    __age = 1
    __color = 'red'
    __height = 2

    def modify_data(self, name, age, color, height):  # normal method
        self.__name = name
        self.__age = age
        self.__color = color
        self.__height = height

    def show_data(self):
        print(self.__name, self.__age, self.__color, self.__height)


dog = Dog()
dog.show_data()
dog.modify_data('John', 4, 'white', 2)
dog.show_data()
