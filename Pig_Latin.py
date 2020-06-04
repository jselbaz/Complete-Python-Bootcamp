def pig_latin(word):
    first_letter = word[0]
    if first_letter in 'aeiou':
        print(word+'ay')
    else:
        print(word[1:]+word[0]+'ay')

pig_latin('word')
pig_latin('apple')
