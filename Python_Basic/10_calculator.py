num1 = input('Enter number 1: ')
num2 = input('Enter number 2: ')
operator = input('*****\n'
                  'Enter + to add\n'
                  'Enter - to sub\n'
                  'Enter * to multiply\n'
                  'Enter / to div\n'
                  'Enter % to find remainder\n'
                  '*****\n'
                  )
try:
    num1 = int(num1)
    num2 = int(num2)

    if operator == '+':
        print((num1 + num2))
    elif operator == '-':
        print(num1 - num2)
    elif operator == '*':
        print(num1 * num2)
    elif operator == '/':
        try:
            num1 = int(num1)
            num2 = int(num2)
            print(num1 / num2)

        except ZeroDivisionError:
            print(ZeroDivisionError)
    else:
        print(num1 % num2)

except ValueError:
    print('Please enter a number', ValueError)