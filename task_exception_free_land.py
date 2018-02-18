import math

def get_free_land(land, grya):

    X = math.sqrt(int(land[0]) * 100 / (int(land[1][0]) * int(land[1][2])))
    LAND_SHIR = X * int(land[1][0])

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
