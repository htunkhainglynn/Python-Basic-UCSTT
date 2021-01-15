emojis ={
    ':)': '☺',
    ':(': '☹',
    'B)': '😎',
    ':D': '😁',
    ':P': '😜',
    '<3': '❤'
}

message = input('> ')
message = message.split(' ')
output = ''

for word in message:
    output += emojis.get(word, word) + ' '
print(output)