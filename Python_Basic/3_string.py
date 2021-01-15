# length of a stringS
a = 'hello'
print(len(a))

# check string
name = "Htun Khaing Lynn"
print('Khaing' in name)
print('Ko' in name)
print('Ko' not in name)

# string slicing
x = 'Hello World'
   # 012345678910 <-- index
  #-11-10-9-8-7-6-5-4-3-2-1
print(x[1])
print(x[:]) #same as original string
print(x[:5]) #slice from start
print(x[2:]) #slice to end
print(x[2:5]) #slice from 2 to 5
print(x[2:10:2]) #start stop step
print(x[:]) #last word
print(x[::-1]) #reverse the string
print(x[-11:-2]) #negative slicing

# useful string methods
x = 'I love Python'
y = ' JavaScrip is not Java '

print(x.lower()) #change to lower
print(x.upper()) #change to upper
print(x.find('I')) #return its index
print(y.strip()) #remove blanks from start and end of string
print(y.replace('J', 'C')) #replace J with C
print(x.split(" ")) #return a list

# Concatenate string
a = 'Hello'
b = 'World'
c = a + b

print(c)

# format
name = 'Htun Khaing Lynn'
age = 19
height = 172.72

my_bio = 'My name is {}. I am {} years old. My height is {}'.format(name, age, height)
my_bio_2 = f'My name is {name}. I am {age} years old. My height is {height}'
print(my_bio)
print(my_bio_2)
