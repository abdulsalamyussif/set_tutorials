#fname = input("Please enter a file name: ")
#try:
#    access = open(fname)
#except:
#    print("file cannot be opened: ", fname)
#    quit()
#count = 0
#for lines in access:
#    lines = lines.rstrip()
#    post = lines.find('@')
#    ed = lines.find(' ', post)
#    if not "From: " in lines:
#        continue
#    count = count +1
#    lines = lines.lstrip()
#    print(lines[post+1:ed])
#print(f'{count} are found in the file.')


enter_file = input('Enter a file: ')
fhand = open(enter_file)
count = 0 
total = 0
for sentences in fhand:
    sentences = sentences.rstrip()
    #sentences = sentences.split()
    #print(sentences)
    if not sentences.startswith('X-DSPAM-Confidence:'):
        continue
    sentences = sentences.split()
    values = sentences[1]
    count = count +1
    total = total + float(values)

    

print('The total is : ', total)
print('The average is : ', total/count)


    
