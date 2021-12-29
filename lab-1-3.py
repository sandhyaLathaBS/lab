a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newList = list()
for val in a:
    if val < 6:
        newList.append(val)

print(newList)
