from datetime import datetime


def converter(message):
    """
    This function converts emojis from emoji signs. If there is no emoji signs, it returns original text
    :param message:
    :return: change emoji signs to emojis
    """

    emojis = {
        ':)': '☺',
        ':(': '☹',
        'B)': '😎',
        ':D': '😁',
        ':P': '😜',
        '<3': '❤'
    }

    message = message.split(' ')
    output = ''

    for word in message:
        output += emojis.get(word, word) + ' '
    return output


def send_message(conv_func, message, *, sent_time=datetime.utcnow()):
    result = converter(msg)
    return result, sent_time


msg = input('Send message...')
msg, sentTime = send_message(converter, msg)
print(f'{msg} at {sentTime}')
