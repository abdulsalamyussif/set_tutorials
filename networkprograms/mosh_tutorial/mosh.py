import math

name = input('what is your name? ')
color = input('What is your favorite color? ')

#print(f'{name} likes {color}')

x = 2.8
print(math.floor(x))
has_down_payment = True

byer = input('Buyer type: ')
price = 1000000
if has_down_payment:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f'Down payment: ${down_payment}')
if byer == 'good credit':
    print('deposit 10%')
    print('Amount: ',0.10*price )
else:
    print('you must deposit 20%')
    print('Amount:', 0.20 * price)
    
namee = input('Enter name: ')

if len(namee) < 3:
    print('Name must be more than 3 letters long')
elif len(namee) > 50:
    print('Name can be a maximum of 50 characters')
else:
    print('Name looks good!')