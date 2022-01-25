fruit = 'pinEApple'
user = fruit.upper()
print(user[0])
print(max(user))
print(min(user))
index = 0
while index < len(user):
    letter = user[index]
    print(index, letter)
    index = index +1
#this for loop and the above while loop all 
#perform the same function
count = 0
for ind, leter in enumerate(user):
    print(ind, leter)
    if leter == 'P':
        count = count + 1
print('There are :',count, 'P in ', user)


#Slicing(pulling part of string out)

drug = 'Amoxasillin tablets'
fletter = drug.find('s')
print(fletter)
final = drug[5:]
print(final)

