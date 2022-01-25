#REVERSING THE ORTHER OF A NUMBER
#number = int(input('Enter Number to reverse: '))
#original_number = number
#reverse_number = 0
#while number > 0:
#    digit = number % 10
#    number = number // 10
#    print(digit, end=" ")

def hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf
print('Please enter 2#s to find their HCF: ')
num1 = int(input('Enter #1: '))
num2 = int(input('Enter #2: '))
print(hcf(num1, num2))



    
