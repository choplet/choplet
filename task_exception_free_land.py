import math

def get_free_land(land, grya):
    LAND_S = int(land[0] * 100)
    GRYA_S = grya[0] * grya[1]
    LAND_SHIR0 = int(land[1][0])
    LAND_DLIN0 = int(land[1][2])
    X = math.sqrt(LAND_S / LAND_SHIR0 * LAND_DLIN0)
    LAND_SHIR, LAND_DLIN = LAND_SHIR0 * X, LAND_DLIN0 * X
    print(LAND_SHIR, LAND_DLIN)

    if (grya[0] > LAND_SHIR or grya[1] > LAND_DLIN) or LAND_S < GRYA_S :
        if land[0] == 0:
                raise ValueError('Не задана площадь участка')
        else:
            raise ValueError('Размер грядки больше размера участка')
    elif grya[0] == 0 or grya[1] == 0:
            raise ValueError('Не задана площадь грядки')


    else:
        non_shir = LAND_SHIR % grya[0]

        non_dlin = LAND_DLIN % grya[1]
        ostatok = non_shir * LAND_SHIR + non_dlin * (LAND_DLIN - non_shir)
    return ostatok, non_shir, non_dlin

print(get_free_land((100, "1:1"),(15, 25)))
