

def pig_latin(word = input()):
    list_word = word.split(' ')
    new_word = ''
    end = 'ay '
    for i in list_word:
        if '!' not in i:
            new_word += i[1:] + i[0] + end
        else:
            new_word +=i
    return new_word

pig_latin()
