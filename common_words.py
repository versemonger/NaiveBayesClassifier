fp1 = open('TopWords', 'r')
fp2 = open('100-frequency-words.txt', 'r')
top_words = set([line.strip() for line in fp1])
print top_words
count = 0
for line in fp2:
    for word in line.strip().split():
        print word
        if word in top_words:
            count += 1
print count

