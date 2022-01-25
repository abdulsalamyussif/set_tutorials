num = str(int(input('Enter: ')))
reversed_num = num[::-1]
if num == reversed_num:
    print('It is a palindrome number')
else:
    print('The number is not a palindrome number')

sum_of_digits = 0
for digits in num:
    if int(num) > 0 and int(num) < 999:
        sum_of_digits = sum_of_digits + int(digits)
    else:
        print('Please enter a number between 0 and 999: ')
        print('Therefore no sum for the number entered!')
        break
print(f'The sum of the digits is {sum_of_digits}')

