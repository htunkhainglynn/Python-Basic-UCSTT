sublist = ['myanmar', 'eng', 'math', 'physics']

# remove and add
sublist[-1] = 'algorithm'
print(sublist)
rm = 'algorithm'
sublist.remove(rm)
print('After using remove\n', sublist)

# pop
sublist.pop(0) #it needs index number
print('After using pop\n', sublist)

# del
del sublist[0]
print('After using del\n', sublist)

# append
sublist.append(99)
print('After appending\n', sublist)
print(len(sublist))

###########################################

# max
num_list = [100, 1203, 102, 192, 2321]
print('after using max\n', max(num_list))
print('after using min\n', min(num_list))
num_list.reverse()
print('after using reverse\n', num_list)
my_index = num_list.index(102)
print('After using index\n', my_index)
addition = sum(num_list)
print('after using sum\n', addition)
num_list.sort()
print('after using sort\n', num_list)
num_list.sort(reverse=True)
print('After using sort reverse', num_list)

########################################

# testing sentences
string_list = ['apple', 'banana', 'zoo', 'orange']

string_list.sort()
print(string_list)

string_list.sort(key=len, reverse=True)
print('after using len sort\n', string_list)

# using loops
for element in string_list:
    if element == 'zoo':
        print('zoo')
    else:
        print('Not found')

#############################################

num_list = [1, 2, 3, 4, 5, 6, 7]

for i in num_list:
    print(i+3)

for integer in num_list[:3]:
    num_list.remove(integer)
    print('removing...', integer)

print(num_list)

##############################

num_list = []

for i in range(1, 10):
    data = i**2
    num_list.append(data)
    print('appending...', data)

print(num_list)
