import statistics

data = []
while len(data) < 10:
    num = input('Enter Number: ')
    if num == '':
        continue
    num = float(num)
    data.append(num)



mean = statistics.mean(data)
mode = statistics.mode(data)
median = statistics.mode(data)

print(f'The median is {median}')
print(f'The mean is {mean}')
print(f'The mode is {mode}')