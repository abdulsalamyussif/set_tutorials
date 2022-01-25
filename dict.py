records = dict()
records['ama'] = 89
records['akosua'] = 78
records['oppong'] = 84
records['salomey'] = 45
print(records['oppong'])

counts = dict()

names = ['yussif', 'yussif','ama', 'sakina', 'sakina', 'Ama', 'sakina', 'sly', 'ridwan']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
#print(counts)
    
#another way of making the histogram with 
# giving the same results

#freq = dict()
concepts = ['mean','SD', 
'probability', 
'integration', 'permutation',
 'summation', 'mean', 
 'probability'] 

#for concept in concepts:
 #   freq[concept] = freq.get(concept, 0) +1
#print(freq)

#freq_words = dict()
#fhand = input('Enter a file: ')
#file_open = open(fhand)
#for lines in file_open :
    #lines = lines.rstrip()
    #print(lines)
    #for words in lines:
        #words = words.split()
#print(words)
        #if words not in freq_words:
            #freq_words[words] = 1
        #else:
            #freq_words[words] = freq_words[words]+1
#print(freq_words)

#user = dict()
#print('Please enter a line of text: ')
#line = input(' ')
#words = line.split()

#print('Words: ', words)

#print('Counting>>>>')
#for word in words:
 #   user[word] = user.get(word, 0) +1
#print('Users: ', user)


#doc = open('learn.txt')
#countss = dict()
#word_high = 0
#for lines in doc:
#    lines = lines.rstrip()
#    lines = lines.split()
    #for wordss in lines:
     #   countss[wordss] = countss.get(wordss, 0) + 1
      #  if countss[wordss] > word_high :
       #     word_high = countss[wordss]
    #print(wordss,word_high)





        #print('Histogram: ', countss)


std = dict()
print('Please enter a line: ')
usr = input('< ')
usr = usr.split()
#print(usr)
cnt = 0

for wrds in usr:
    std[wrds] = std.get(wrds, 0) +1
    if std[wrds] > cnt :
        cnt = std[wrds] 
        print('Most common word is: ',wrds)
        print(std.keys())
        print(std.items())
        print(std.values())
print('Frequency is : ',cnt) 
