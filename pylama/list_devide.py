def mass(list):
    chet = 0
    nechet = 0
    for i in list:
        if i % 2 != 0:
            nechet +=1
        else:
            chet +=1


    if chet == 1:
        for i in list:
            if i % 2 == 0:
                return i
    else:
        for i in list:
            if i % 2 != 0:
                return i


print (mass([160, 3, 1719, 19, 11, 13, -21]))
