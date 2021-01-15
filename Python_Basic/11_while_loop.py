i = 0
while i <= 5:
    print(i)
    i += 1

print('Done')

i = 0
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1
print('Done')

i = 0
while i < 5:
  i += 1
  if i == 3:
    continue
  print(i)