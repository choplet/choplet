def bin2dec(l):
    l = str(l)
    b = [int(i) for i in l]
    lenn = len(b) - 1
    itog = 0
    
    for i in b:
        itog = itog + (i * (2**lenn))
        lenn-=1
    return (itog)


def oct2dec(l):
    l = str(l)
    b = [int(i) for i in l]
    lenn = len(b) - 1
    itog = 0
    
    for i in b:
        itog = itog + (i * (8**lenn))
        lenn-=1
    return (itog)
    

def hex2dec(l):
    hexx = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,'9':9, 
     'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15, 'g':16}
    c = [c for c in l] 
    lenn = len(c)-1
    itog = 0
    for i in c:
        itog = itog + (hexx[i] * (16**lenn))
        lenn-=1
    return (itog)


    

def dec2hex(l):
    d = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9',
         10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    q = l
    result = ""
    while q != 0:
        r = q % 16
        q = q // 16
        result += d[r]
    return (result)


def bin2dec(l):

    q = l
    result = ""
    while q != 0:
        r = q % 2
        q = q // 2
        result += str( r)
    return (result[::-1])


def oct2dec(l):

    q = l
    result = ""
    while q != 0:
        r = q % 8
        q = q // 8
        result += str( r)
    return (result[::-1])
    
 



