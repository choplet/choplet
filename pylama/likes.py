'''
Описание
Вы, вероятно, знаете, как в вконтакте устроена система лайков картинок, постов и других вещей. Вам нужно организовать текст, который будет отображаться с таким элементом.

Функция принимает массив, который содержит имена людей, лайкнувших что-либо. Она должна возвращать сгенерированную строку, как в примерах ниже:

Например:
Вход	Выход
[]

"no one likes this"

["Peter"]

"Peter likes this"

["Jacob", "Alex"]

"Jacob and Alex like this"

["Max", "John", "Mark"]

"Max, John and Mark like this"

["Alex", "Jacob", "Mark", "Max"]

"Alex, Jacob and 2 others like this"

Для 4 и более людей отображается только первые 2 имени, остальные отображаются цифрой лайкнувших людей, за исключением первых двух.
'''
def likes( listt):
    if not listt:
        print('no one likes this')
    elif len(listt)==1:
        print('{} likes this'.format(listt[0]))
    elif len(listt)==2:
        print('{} and {} like this'.format(listt[0], listt[1]))
    elif len(listt)==3:
        print('{}, {} and {} like this'.format(listt[0], listt[1], listt[2]))
    else:
        other_likes = len(listt) - 2
        print('{}, {} and {} others like this'.format(listt[0], listt[1], other_likes))



def likes(names):
    # your code here

    textToReturn = ""

    if (len(names) == 0):
        textToReturn = "no one likes this"
    elif (len(names) == 1):
        textToReturn = str(names[0]) + " likes this"
    elif (len(names) > 1 and len(names) < 4):
        for name in range(0, len(names) - 1):
            textToReturn = textToReturn + names[name] + ", "
        textToReturn = textToReturn[:-2]
        textToReturn = textToReturn + " and " + str(names[len(names) - 1]) + " like this"
    else:
        for name in range(0, 2):
            textToReturn = textToReturn + names[name] + ", "
        textToReturn = textToReturn[:-2]
        textToReturn = textToReturn + " and " + str(len(names)-2) + " others like this"
    return textToReturn


print(likes([]))
print(likes(['Alex']))
print(likes(['Alex','Bob']))
print(likes(['Alex','Bob', 'Sam']))
print(likes(['Alex','Bob', 'Sam', 'Pete']))
