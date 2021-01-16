import random

# generate a random floating point number
a = random.random()
print('using random.random()', a)

# generate a random integer
b = random.randint(0, 10)  # start stop
print('using random.randint()', b)

# generate a random integer
c = random.randrange(0, 10, 2)  # start stop step
print('using random.randrange()', c)

# randomly choice a data from list
words = ['a', 'b', 'c', 'd', 'e', 'f']
d = random.choice(words)
print('using random.choice', d)

# generate a random seed
random.seed(0)
for i in range(4):
    print('using random.seed()', random.random())

# shuffle data in list
random.shuffle(words)
print('using random.shuffle()', words)

# randomly choice data in list/ tuple/ set respect to the second parameter
print('using random.sample()', random.sample(words, 5))

# generate a random floating point number
print('using random.uniform()', random.uniform(1, 3))

# generate a random floating point number
print('using random.triangular()', random.triangular(1, 3, 0.5))
