text = 'Sed vitae justo malesuada, commodo libero eu, bibendum mauris.'

words = text.split()
fin_words = []

for word in words:
    if 'o' in word:
        print(word)
    else:
        fin_words.append(word)

print(' '.join(fin_words))            

