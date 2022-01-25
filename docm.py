fname = open('use.txt', 'r')
doc = dict()
for lines in fname:
    wordsss = lines.split()
    for word in wordsss:
        doc[word] = doc.get(word, 0) + 1

counting_words = list()
for k, v in doc.items():
    counting_words.append((k, v))

counting_words = sorted(counting_words, reverse=True)

for v, k in counting_words[:10]:
    print(k, v)

   

