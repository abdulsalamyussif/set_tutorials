students = list()
students.append('Sakinatu')
students.append('Ghassan')
students.append(99)
students.append('cookie')
students.insert(99, 100)
print(students)
print('sakinatu' in students)
print('salam' not in students)

numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)

print('The largest value is: ',max(numlist))
print('The smallest value is: ',min(numlist))
average = sum(numlist)/len(numlist)
print('Average: ', average)