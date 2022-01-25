sentence = 'Ghassan is a school boy'
words = sentence.split()
print(words)
print(len(words))
print(words[4])
for word in words:
    if 'i' in word:
        continue
    print(word)

sender_information = 'From: abdulsalamyussif.asy@gmail.com Sat 11:30pm '

words_in_email = sender_information.split()
email = words_in_email[1]
nam = email.split('@')
print(nam[0])
        