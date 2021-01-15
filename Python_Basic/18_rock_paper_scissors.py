import random

computer = c = 0
player = p = 0
data = ['Rock', 'Paper', 'Scissors']

print('Score Computer: {0} Player: {1}'.format(c, p))

run = True
while run:
    computer_choice = random.choice(data)
    player_choice = input('Enter Rock or Paper or Scissors or Quit: ')

    if computer_choice == player_choice:
        print('Tie')

    elif player_choice.lower() == 'rock':
        if computer_choice == 'Scissors':
            print('You Win')
            p += 1
        else:
            print('Computer Win')
            c += 1

    elif player_choice.lower() == 'paper':
        if computer_choice == 'rock':
            print('You Win')
            p += 1
        else:
            print('Computer Win')
            c += 1

    elif player_choice.lower() == 'scissors':
        if computer_choice == 'paper':
            print('You Win')
            p += 1
        else:
            print('Computer Win')
            c += 1

    elif player_choice.lower() == 'quit':
        break
    else:
        print('Wrong Command')

    print('Player: ', player_choice)
    print('Computer: ', computer_choice)
    print("")
    print('Score Computer: {0} Player: {1}'.format(c, p))
    print("")