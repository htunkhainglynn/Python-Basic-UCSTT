num1 = input('Enter a number')

try:
    num1 = int(num1)
    print('Your number: ', num1)
except ValueError:
    print('Enter a number', ValueError)

num1 = input('Enter a number')
num2 = input('Enter a number')

try:
    num1 = int(num1)
    num2 = int(num2)
    num3 = num1 / num2

except ZeroDivisionError:
    print(ZeroDivisionError)