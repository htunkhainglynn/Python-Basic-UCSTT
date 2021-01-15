def c_to_f(a):
    return (a * (9 / 5)) + 32


def f_to_c(a):
    return (a * 1.8) + 32


degree = float(input('Enter degree who what to exchange'))
func = int(input('Enter 1 to change Celsius to Fahrenheit\n'
                 'Enter 2 to change Fahrenheit to Celsius'))

if func == 1:
    cel2fah = c_to_f(degree)
    print(cel2fah)
else:
    fah2cel = f_to_c(degree)
    print(fah2cel)

####################################
# function to function


def square(a):
    return a**2


def cube(a):
    return a**3


def fun2fun(fun, n):
    return fun(n)


fun2fun = fun2fun(square, 3)
print(fun2fun)

