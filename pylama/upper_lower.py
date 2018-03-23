def up_low(word):
    new_word = ''
    for i in word:
        if i == i.lower():
            new_word += i.upper()
        else:
            new_word += i.lower()
    return new_word

print(up_low('wOrd word'))
