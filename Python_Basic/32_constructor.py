class Student:
    def __init__(self, name, age): # special method
        self.name = name
        self.age = age
        print('Work First')

    def show_data(self):
        print(f'Student1 name: {self.name}, age: {self.age}')
        print('Work Second')


stu1 = Student('Smith', 19)
stu2 = Student('Jason', 20)

stu1.show_data()
stu2.show_data()


