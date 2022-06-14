import sys
import random
import sqlite3

conn = sqlite3.connect('mini-bank.db')
c = conn.cursor()
create_table = 'CREATE TABLE IF NOT EXISTS mini_bank(id INTEGER, name TEXT NO NULL, password TEXT NO NULL, amount REAL, phone TEXT NO NULL);'
c.execute(create_table)
insert_data = 'INSERT INTO mini_bank(id, name, password, amount, phone) VALUES(?,?,?,?,?);'
select_data = 'SELECT * FROM mini_bank;'
check_phone = 'SELECT id FROM mini_bank WHERE phone=:phone;'
check_password = 'SELECT id FROM mini_bank WHERE password=:password;'
get_password = 'SELECT password FROM mini_bank WHERE id=:id;'
amount = 'SELECT amount FROM mini_bank WHERE id=:id;'
update_amount = 'UPDATE mini_bank set amount=:amount WHERE id=:id;'
my_ph = 'SELECT phone FROM mini_bank WHERE id=:id;' 
phone_amount = 'SELECT amount FROM mini_bank WHERE phone=:phone;'
phone_bal_update = 'UPDATE mini_bank set amount=:amount where phone=:phone;'
my_bal_update = 'UPDATE mini_bank set amount=:amount where id=:id;'
own_data_check = 'SELECT * FROM mini_bank WHERE id=:id;'
get_name = 'SELECT name FROM mini_bank WHERE phone=:phone'

class User:
    def create_account(self):
        phones = []
        name = input('Enter your name:> ')
        all_data = c.execute(select_data).fetchall()
        for i in all_data:
            phones.append(i[4])
        while True:
            phone = input('Enter your phone number:> ')
            while phone in phones:
                print('This number already exists.')
                break
            else:   
                password = input('Enter your password:> ')
                while True:
                    confirm_password = input('Confirm your password:> ')
                    while password != confirm_password:
                        print('Passwords do not match')
                        break
                    else:
                        print('Account create successfully')
                        c.execute(insert_data,(random.randint(000000, 1000000), name, password, 0, phone))
                        conn.commit()
                        break
                break

    def login(self):
        while True:
            phone = input('Enter your phone number:> ')
            password = input('Enter your password:> ')
            names = []
            passwords = []
            phones = []
            all_data = c.execute(select_data)
            all_data = all_data.fetchall()
            for i in all_data:
                names.append(i[1])
                passwords.append(i[2])
                phones.append(i[4])
            while phone not in phones or password not in passwords:
                print('Wrong phone number or password')
                break

            else:
                phone_id = c.execute(check_phone, {'phone':phone})
                pass_id = c.execute(check_password, {'password':password})
                while phone_id != pass_id:
                    print('Wrong phone number or password')
                    break

                else:
                    print('Login Successfully.')
                    name = c.execute(get_name,{'phone':phone}).fetchall()[0][0]
                    print('Hello {}'.format(name))
                    phone_id = c.execute(check_phone, {'phone':phone}).fetchall()[0][0]
                    pass_id = c.execute(check_password, {'password':password}).fetchall()[0][0]
                    balance = c.execute(amount, {'id':phone_id}).fetchall()[0][0]
                    print('Your ammount - {} kyats'.format(balance))
                    while True:
                        user_option = int(input('Enter 1 to deposit. Enter 2 to withdraw. Enter 3 to transfer. Enter 4 to look info. Enter 5 to quit. Enter 6 to logout.'))
                        real_pass = c.execute(get_password,{'id':pass_id}).fetchall()[0][0]
                        if user_option == 1:
                            deposit_money = int(input('Enter amount:> '))
                            while True:
                                confirm_pass = input('Enter password:> ')
                                while confirm_pass != real_pass:
                                    print('Wrong Password')
                                    break
                                else:
                                    balance += deposit_money
                                    c.execute(update_amount, {'amount':balance,'id':phone_id})
                                    print('Successfully Deposit.')
                                    conn.commit()
                                    break
                             
                        elif user_option == 2:
                            flag = True
                            while flag:
                                withdraw_money = float(input('Enter amount:> '))
                                while withdraw_money > balance:
                                    print('Balance Insufficient')
                                    keep_doing = input('Continue? y/n:> ')
                                    if keep_doing.lower() == 'y':
                                        break
                                    elif keep_doing.lower() == 'n':
                                        flag = False
                                        break
                                    else:
                                        print('Wrong Command.')
                                        break
                                else:
                                    while True:
                                        confirm_pass = input('Enter password:> ')
                                        while confirm_pass != real_pass:
                                            print('Wrong Password')
                                            break
                                        else:
                                            if balance == 0:
                                                print('Your balance is 0 kyat')
                                            elif balance < withdraw_money:
                                                print('Not enough balance.')
                                            else:
                                                balance -= withdraw_money
                                                c.execute(update_amount, {'amount':balance,'id':phone_id})
                                                print('Successfully Withdraw .')
                                                conn.commit()
                                                break
                                        break
                                    break

                        elif user_option == 3:
                            while True:
                                all_ph_no = c.execute(select_data).fetchall()
                                ph_no = []
                                for data in all_ph_no:
                                    ph_no.append(data[4])
                                transfer_no = input('Enter phone:> ')
                                while transfer_no not in ph_no:
                                    print('Phone number does not exist.')
                                    break
                                else:
                                    my_phone_no = c.execute(my_ph, {'id':phone_id}).fetchall()[0][0]
                                    transfer_balance = c.execute(phone_amount,{'phone':transfer_no}).fetchall()[0][0]
                                    while True:
                                        transfer_money = float(input('Enter amount:> '))
                                        while balance == 0 or balance < transfer_money:
                                            print('Insufficient balance.')
                                            break
                                        else:
                                            while True:
                                                confirm_pass = input('Enter password:> ')
                                                while confirm_pass != real_pass:
                                                    print('Wrong Password')
                                                    break
                                                else:
                                                    if transfer_no == my_phone_no:
                                                        print('You cannot transfer to yourself.')
                                                        break
                                                    else:
                                                        transfer_balance += transfer_money
                                                        c.execute(phone_bal_update, {'amount':transfer_balance, 'phone':transfer_no})
                                                        balance -= transfer_money
                                                        c.execute(my_bal_update, {'amount':balance, 'id':phone_id})
                                                        print('Successfully Transfer.')
                                                        conn.commit()
                                                        break
                                            break
                                    break
                                    
                        elif user_option == 4:
                            own_data = c.execute(own_data_check, {'id':phone_id})
                            own_data = own_data.fetchall()
                            for data in own_data:
                                print('Name - {}'.format(data[1]))
                                print('Your ID - {}'.format(data[0]))
                                print('Your Money - {} kyats'.format(data[3]))
                                print('Your Phone Number - {}'.format(data[4]))

                        elif user_option == 5:
                            sys.exit('Bye Bye')

                        elif user_option == 6:
                            print('Successfully Logout.')
                            main()
                        else:
                            print('Wrong number')

    def logout(self):
        self.login()

print('***Welcome to Khaing Khaing Pay***') 
global main
def main():
    option = input('Enter 1 to create account. Enter 2 to login:> ')
    try:
        option = int(option)
    except ValueError as e:
        print('Please enter 1 or 2.')
        main()

    user = User()
    if option == 1:
        user.create_account()
        print('Enter phone number and password again to login. ')
        user.login()

    elif option == 2:
        user.login()

    else:
        print('Wrong Command')
        main()    
main()
