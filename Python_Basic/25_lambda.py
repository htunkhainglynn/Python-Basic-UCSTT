a = lambda x, y: x * y

print(a(2, 3))

b = lambda x, y, *args, z, **kwargs: print(x, y, z, args, kwargs)

b(1, 2, 3, 4, z=5, k=6, l=7)

print(b)