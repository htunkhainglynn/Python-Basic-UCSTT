for i in range(9):
    print(i)
print('--------------------------------')

for i in range(10):
    if i == 5:
        break
    print(i)
print('--------------------------------')

for i in range(10):
    if i == 5:
        continue
    print(i)
print('--------------------------------')

name = 'Htun Khaing Lynn'
for i in name:
    print(i)
print('--------------------------------')

for i in range(0, 10, 2):
    print(i)
print('--------------------------------')

number = ['a', 'b', 'c', 'd', 'e']
for a, b in enumerate(number):
    print(a, b)

