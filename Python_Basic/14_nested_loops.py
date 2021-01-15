for i in range(3):
    for j in range(3):
        print(f'({i} {j})')

myList = [5, 2, 5, 2, 2]
for i in myList:
    for j in range(i):
        print('x', end='')
    print('')

for i in range(5):
    for j in range(i + 1):
        print('*', end=' ')
    print('')