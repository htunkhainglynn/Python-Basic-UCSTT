student = {
    'name': 'Ko Ko',
    'age': 19,
    'is_boy': True
}

student['name'] = 'Ma Ma'

print(student)

print(student.get('name'))


a = {'name':[0, 1, 2, 3, 4]}
print(a['name'][3])

#######################################

num_mapping ={
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five'
}

number = input('Enter number: ')
output = ''

for data in number:
    output += num_mapping.get(data, '!') + ' '
print(output)
