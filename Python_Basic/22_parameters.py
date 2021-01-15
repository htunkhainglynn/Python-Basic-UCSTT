def greet(name):
    print(f'Hello {name}')


greet('KoKo')


def add(no1, no2):
    result = no1 + no2
    print('Result = ', result)


num1 = input('Enter number 1: ')
num2 = input('Enter number 2: ')

# type casting
num1 = int(num1)
num2 = int(num2)

add(num1, num2)
