guess_number = 7
guess_limit = 3
count = 0
score = 6

while count != guess_limit:
    count = count + 1
    try:
        user_input = input('Make a guess: ')
        if user_input == 'done': break
        user_input = int(user_input)
    except:
        print('Please enter a number')
    else:
    
        if user_input > guess_number:
            print('Your guess is bigger than guess number')
            if user_input % 2==0:
                print('The guess number is not even')
        else:
            if count == guess_limit: break
        if user_input == guess_number:
            score = score + 2
            print('You won!')
            break
        else:
            score = score - 2
            print('You failed. Try again.')
if (user_input - guess_number) >= 0 or (user_input - guess_number)<=0 :
    print('Your input was an actual number')
else:
    print('You did not enter an actual number')
if score > 0:
    print('Your score is : ', score, 'congratulation!')
else:
    print("You don't have any score")

