a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even = []
for x in a:
    if (x % 2 == 0):
        even.append(x)
    else:
        continue
print(even)

b = list(filter(lambda x: x % 2 == 0, a))
print(b)
