doc = input('Enter a file: ')
fhand  = open(doc)

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigword = None
bigcount = None
for word, count in counts.items():
    if bigword is None or count > bigcount:
        bigword = word
        bigcount = count

print( bigword, bigcount)