guess_number = 9
guess_limit = 3
number_of_guess = 0
while number_of_guess < guess_limit:
    guess = int(input('Make a guess: '))
    number_of_guess += 1
    if guess == guess_number:
        print('You won!')
        break
else:
    print('Sorry you failed!')

