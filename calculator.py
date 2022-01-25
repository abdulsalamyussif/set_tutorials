import math, statistics

basics = 1
others = 2

result = 0


print('1 for basics: ')
print('2 for others: ')
lower_higher_order_operations = int(input('Select: '))
if lower_higher_order_operations == basics:
    try:
        f_num = int(input('Enter first Number: '))
        l_num = int(input('Enter second Number: '))
    except:
        print('Please enter a number!')
        quit()

    print('kindly select the operation to perform: ')

    print('a - addition')
    print('s - subtration')
    print('m - multiplication')
    print('d - division')
    operation = input('Kindly enter the operation: ').lower()


    if operation == 'a':
        result = f_num + l_num
    elif operation == 's':
        result = f_num - l_num
    elif operation == 'm':
        result = f_num * l_num
    elif operation =='d':
        result = f_num/ l_num
    else:
        print('Please Enter the right operation. ')
    print(f'Answer: {result}')
elif lower_higher_order_operations ==others:
    print('Exp - power')
    print('Sqrt - square root')
    print('Combi - combination' )
    print('Perm - permutation')
    operation = input('Kindly enter the operation: ').lower()



    #code for exponential, square root, permutation and combination
    userinput = int(input('Enter number: '))
    signs = ['Power', 'Root', 'Permutation', 'Combination']
    for nameofoperation in signs: 
        nameofoperation = nameofoperation.lower()


    if operation == 'sqrt':
        result = math.sqrt(userinput)
    elif operation == 'exp':
        print(f'{userinput} To what power? 2 or 3 or 4...')
        power = int(input('Please enter power: '))
        result = math.pow(userinput, power)
    elif operation == 'comb':
        if userinput < 0:
            print('Sorry!. factorial for negatives does not exist')
            quit()
        elif userinput == 0:
            print('The factorial for 0 is 1')
            quit()
        elif userinput > 0:
            print(f'{userinput} to what combination? 1 or 2 or 3...')
            r = int(input('Please enter r for the number of ways: '))
            result = math.comb(userinput,r )
        else:
            print('Please enter a number')
    elif operation == 'perm':
        print(f'{userinput} to what permutation? 1 or 2 or 3....')
        r = int(input('Please enter r for the number of ways: '))
        result = math.perm(userinput, r)
    else:
        print('Please enter one of the above operations')
else:
    print('Please enter 1 or 2: ')

print(f'Answer: {result}')




