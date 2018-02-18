
import math
def get_free_land(land, grya):

    land_dlin = land[0] * land[1][1]
    land_shir = land[0] * land[1][3]


    if s_bed == 0:
        raise ValueError('Не задана площадь грядки')
    elif s_land == 0:
        raise ValueError('Не задана площадь участка')
    elif s_land < s_bed:
        raise ValueError('Размер грядки больше размера участка')
    else:
        s_lost = s_land % s_bed
    return s_lost


#print(get_free_land((6, "1:5"), (3000, 20)))

#(100, "1:1")
#(15, 25)

#100 = x * x
#100 = 3x * 2x

#100 = 10 * 10 (1:1)

def get_part(land, grya):

    X = math.sqrt(int(land[0]) * 100 / (int(land[1][0]) * int(land[1][2])))
    LAND_SHIR = X * int(land[1][0])
    print (LAND_SHIR)
    LAND_DLIN = X * int(land[1][2])
    S_LAND = land[0] * 100
    S_GRYA = grya[0] * grya[1]
    if (grya[0] > LAND_SHIR or grya[1] > LAND_DLIN) or S_LAND < S_GRYA :
        if land[0] == 0:
                raise ValueError('Не задана площадь участка')
        else:
            raise ValueError('Размер грядки больше размера участка')
    elif grya[0] == 0 or grya[1] == 0:
            raise ValueError('Не задана площадь грядки')


    else:
        non_shir = LAND_SHIR % grya[0]

        non_dlin = LAND_DLIN % grya[1]
        ostatok = non_shir * grya[1] + non_dlin * grya[0]

    return ostatok

 #land_shir, land_dlin

print(get_part((100, "1:1"),(5, 0)))
