grade = input("enter a grade: ")
try:
    Ival = int(grade)
except:
    Ival = -1
if Ival > 0:
    print("Nice work!, your grade is more than zero, you had : ",Ival)
else:
    print("Note a number, Try again🤢❌❌")

    