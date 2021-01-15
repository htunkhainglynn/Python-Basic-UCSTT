student = {
    'name': 'Ko Ko',
    'age': 19,
    'is_boy': True
}

student['birthday'] = 'Jan 8 2001'

print(student)

print(student.get('name'))

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
