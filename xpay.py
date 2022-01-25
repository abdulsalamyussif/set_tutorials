def computepay():
    fh = float(input('Enter hours: '))
    fr = float(input('Enter rate: '))
    if fh > 40:
        reg = fh * fr
        otp = (fh - 40)*(fr * 0.5)
        pay = reg + otp
    else:
        pay = fh * fr

    return pay
print('Pay',computepay())