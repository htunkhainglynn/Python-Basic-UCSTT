import sys
import random

global users
users = {'id': [123456, 987654],'name': ['ag ag', 'ng ng'], 'password': ['234', '567'], 'amount': [5000, 10000]}

class User:
    def create_account(self):
        name = input('Enter your name:> ')
        password = input('Enter your password:> ')
        while True:
            confirm_password = input('Confirm your password:> ')
            while password != confirm_password:
                print('Passwords do not match')
                break
            else:
                print('Account create successfully')
                users['id'].append(random.randint(000000, 1000000))
                users['name'].append(name)
                users['password'].append(password)
                users['amount'].append(0)
                break

    def login(self):
        while True:
            name = input('Enter your name:> ')
            password = input('Enter your password:> ')

            while name not in users['name'] or password not in users['password']:
                print('Wrong user name or password')
                break

            else:
                while users['name'].index(name) != users['password'].index(password):
                    print('Wrong user name or password')
                    break

                else:
                    print('Login Successfully.')
                    print('Hello {}'.format(users['name'][users['name'].index(name)]))
                    balance = users['amount'][users['name'].index(name)]
                    print('Your ammount - {} kyats'.format(balance))
                    while True:
                        user_option = int(input('Enter 1 to deposit. Enter 2 to withdraw. Enter 3 to transfer. Enter 4 to look info. Enter 5 to quit. Enter 6 to logout.'))
                        if user_option == 1:
                            deposit_money = int(input('Enter amount:> '))
                            balance += deposit_money
                            print('Successfully Deposit.')
                             
                        elif user_option == 2:
                            withdraw_money = int(input('Enter amount:> '))
                            if balance == 0:
                                print('Your balance is 0 kyat')
                            else:
                                balance -= withdraw_money
                                print('Successfully Withdraw .')

                        elif user_option == 3:
                            transfer_money = int(input('Enter amount:> '))
                            transfer_id = int(input('Enter id:> '))
                            if balance == 0:
                                print('Your money is 0 kyat')
                            elif transfer_id == users['id'][users['name'].index(name)]:
                                print('You cannot transfer to yourself.')
                            else:
                                users['amount'][users['id'].index(transfer_id)] + transfer_money
                                balance -= transfer_money
                                print('Successfully Transfer.')
                            
                        elif user_option == 4:
                            print('Name - {}'.format(users['name'][users['name'].index(name)]))
                            print('Your ID - {}'.format(users['id'][users['name'].index(name)]))
                            print('Your Money - {} kyats'.format(balance))

                        elif user_option == 5:
                            sys.exit('Bye Bye')

                        elif user_option == 6:
                            print('Successfully Logout.')
                            self.logout()

                        else:
                            print('Wrong number')
                    break

    def logout(self):
        self.login()

print('***Welcome to UCSTT ICT Club Bank***')
option = int(input('Enter 1 to create account. Enter 2 to login:> '))
if option == 1:
    user = User()
    user.create_account()
    print('Enter username and password again to login. ')
    user.login()

elif option == 2:
    user = User()
    user.login()

else:
    print('Wrong Commend')