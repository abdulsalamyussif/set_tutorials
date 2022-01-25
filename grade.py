score = input('Enter Score: ')
try:
    score = float(score)
except:
    print('Please enter a valid range value (0.0 - 1.0)')
else:
    if score > 0.0 and score < 1.0:
        if score >= 0.9:
            print('A')
            quit()
        elif score >= 0.8:
            print('B')
            quit()
        elif score >= 0.7:
            print('C')
            quit()
        elif score >= 0.6:
            print('C')
            quit()
        elif score < 0.6:
            print('F')
            quit()
    else:
        print('value out of the range. Please enter a range between 0.0 - 1.0')
    