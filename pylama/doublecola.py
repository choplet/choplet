import math

def whoIsNext(names, r):
    nS = int(math.log((r + 4) / 5, 2))
    rank1stSerie = (5 * math.pow(2, nS)) - 4
    dist = int((r - rank1stSerie) / (math.pow(2, nS)))
    return names[dist]

########################################################################

# http://www.codewars.com/kata/551dd1f424b7a4cdae0001f0/train/python
from math import  log, ceil

def whoIsNext(names, r):
    l = len(names)
    
    if l == 1 or r <= l :
        return names[(l==1 and [0] or [r-1])[0]]
    start = 0
    for i in range(int(log(r/l + 1, 2)) + 1):
        start += 2**(i) * l
        if start > r:
            break

    #
    left_count = l * (2 ** (i) -1 )
    remain_number = r - left_count
    #print('start', start, 'Remain', remain_number, '\t\ti:', i)
    index = -1
    if remain_number <= 0:
        return names[0]
    while remain_number >= 0:
        remain_number -= (2**i)
        #print( 'Remain', remain_number, '\t\ti:', index)
        index += 1
    return (names[index])

names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
r = 52
res = "Sheldon"

print(whoIsNext(names, r))
