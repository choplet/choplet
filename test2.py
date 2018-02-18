
def get_quadrant_number(x,y):

    if x * y == 0:
        raise ValueError
    elif x * y > 0:
        if x > 0:
            return(1)
        else:
            return(3)
    elif x * y < 0:
        if x < 0:
            return(2)
        else:
            return(4)




print(get_quadrant_number(-1,-1))
