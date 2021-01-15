# positional_arguments
# arbitrary arguments (end of positional arguments)
# keyword only arguments
# keyword arguments

def pos(name, age):
    print(name, age)


pos('KoKo', 17)


def arb(*args):
    print(args)


arb('KoKo', 19, 5.8, 'Computer')


def kwo(a, b, *args, d):
    print(a, b, args, d)


kwo(1, 2, 3, 4, 5, 6, d=7)


def kw(a, b, c, *args, d, **kwargs):
    print(a, b, c, args, d, kwargs)


kw(1, 2, 3, 4, 5, 6, d=7, e=8, f=9, g=10)
