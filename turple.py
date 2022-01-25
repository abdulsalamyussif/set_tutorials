ids = (829, 3782, 2937,829, 3782, 829)
cnt = ids.count(829)
#print(cnt)
#print(ids.index(3782))
(x, y) = (99, 100)
#print(x)

#di = dict()

#di['ali'] = 90
#di['usuf'] = 95
#di['cwen'] = 78
#for (k, v) in di.items():
    #print(k, v)

#tur = di.items()
#print(tur)
#comparing turples...follows the same way trend as strings
#print(('am', 'us', 'ly') > ('an', 'us', 'yl'))
#print(('am', 'us', 'la') < ('am', 'us', 'lA'))

#sorting of turples 

#clients = {'a': 45, 'b': 98, 'c': 78, 'e': 76, 'f': 67, 'd': 56}
#print(clients.items())

#print(sorted(clients.items()))

#for k, v in sorted(clients.items()):
    #print(k, v)

#sorting by their values and not the keys
#usr = list()
#for ke, va in clients.items():
 #   usr.append((va, ke))
#print(usr)



data = [(10, 'd'), (15, 'b'), (23, 'c'), (34, 'f')]
#usr = sorted(usr, reverse=True)
#print(usr)

#finding the top ten most common words in a text

fname = input('Enter a file: ')
if len(fname) < 1: fname = 'learn.txt'
fhand = open(fname)

users = dict()
for line in fhand:
    #line = line.rstrip()
    words = line.split()
    for word in words:
        users[word] = users.get(word, 0) + 1

scores = list()
for k, v in users.items():
    scores.append((v, k))

scores = sorted(scores, reverse=True)

for v, k in scores[:10]:
    print(k, v)



