import random
import sys

while True:
    print('***Welcome to number guessing game***')
    name = input('Enter your name: ')
    age = int(input('Enter your age, age must be greater than 18: '))
    while age >= 18:
        print('***Hello {}***'.format(name))
        play_money = int(input('Enter your money: '))
        while play_money > 0:
            while True:
                random_num = random.randint(10, 99)
                guess_num = int(input('Enter you guess number: '))
                amount = int(input('Enter your playing amount: '))
                if play_money >= amount:
                    if random_num == guess_num:
                        print('You won\n')
                        print('Your number: {} Computer number: {}'.format(guess_num, random_num))
                        play_money = (play_money - amount) + (amount * 2)
                        print('Your left money: ',play_money)
                    else:
                        print('You lose')
                        print('Your number: {} Computer number: {}'.format(guess_num, random_num))
                        play_money = play_money - amount
                        print('Your left money: ', play_money)

                    if play_money == 0:
                        sys.exit('You have no money')
                    leave = int(input('Enter 0 to continue, any number to quit: '))
                    if leave != 0:
                        sys.exit('Bye Bye')
                    continue
                else:
                    print('***Your amount is greater than your play money***')
                    break
            break
    else:
        print('Sorry age must be 18\n')
