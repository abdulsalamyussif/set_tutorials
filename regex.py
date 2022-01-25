import re

hand = open('learn.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        #print(line)
        for wrd in line:
            wrd = line.split()
            w = wrd[1]
            w = w.split('.')
            person = w[0]
            person = person.split('@')
        print(person[0])


x = 'my 3 fAVOrite numbers are 19 and 21'

y = re.findall('[0-9]+', x)
#print(y)  
y = re.findall('[AEIOU]+', x)
print(y) 

#Greedy matching Regular expression
pro = 'From: this thing :character'
pra = re.findall('^F.+:', pro)
#print(pra)

#Non Greedy matching
pro = 'From: this thing :character'
pra = re.findall('^F.+?:', pro)
#print(pra)

#fing turning string extraction
xi = 'From: Stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
yi = re.findall('^From \S+@\S+', xi)
#print(yi)
xa = 'From: Stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
ya = re.findall('^From (\S+@\S+)', xa)
#print(ya)
xq = 'From: Stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
yq = re.findall('^From .*@([^ ]*)', xq)
#print(yq)

#Regex version 
xp = 'From: Stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
yp = re.findall('^@([^ ]*)', xp)
#print(yp)

mess = 'We just received $10.00 for cookies'
extr = re.findall('\$[0 - 9.]+', mess)
print(extr)


