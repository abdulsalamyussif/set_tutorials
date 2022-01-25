numbers = [2, 3, 4, 8, 4, 2, 8, 3, 3, 4, 9,]
uniques = []

for num in numbers:
    if not num in uniques:
        uniques.append(num)
print(uniques)

       