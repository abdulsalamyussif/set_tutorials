friends = ['Sakinatu', 'Ridwan', 'Osman', 'Mohammed']
for friend in friends:
    print('How are the holidays', friend)
print('All messages sent successfully!')

age_total = 0
oldest = 0
ages = [29, 23, 24, 25, 27]
names = ['salam', 'hamza']
for age in ages:
    age_total = age_total + age
    if age == 29:
        print(names[0], "is",age)

print(age_total)

for i in ages:
    if i> oldest:
        oldest = i
print(oldest)

found = False
print('Before: ', found)
for value in [9, 10, 12,3, 51,74,15]:
    if value == 3:
        found = True
        break
    print(found, value)
print('After', found)

smallest = None
for value in [3,9,4,87,2,6]:
    if smallest is None: 
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('The smmalest # is: ', smallest)