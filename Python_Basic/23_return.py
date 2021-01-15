def test(name):
    greet = 'Hello ' + name
    return greet


z = test('Ko Ko')
print(z)

########################################


def cal(no1, no2):
    add = no1 + no2
    mul = no1 * no2
    return add, mul


num1 = input('Enter number 1: ')
num2 = input('Enter number 2: ')

# type casting
num1 = int(num1)
num2 = int(num2)

a, b = cal(num1, num2)
print(f'sum is {a},mul is {b}')
