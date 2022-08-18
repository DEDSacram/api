# 0 kreveta
# 1 zivorodka
# 2 mercovka
# 3 parma zraloci
# 4 rostlina
# 5 danio
# 6 sekavec
# 7 neonka
# 8 hlemyzd
# 9 tercovec
# 10 skalara
# 11 krunyrovec
# 12 parma cerna

#skip
# 0 kreveta
# 6 sekavec
# 8 hlemyzd

import collections

Fishy = [[2, 7, 11, 4],
         [11, 7, 4, 8],
         [3, 9, 0, 8], 
         [2, 3, 11, 8]]


def Calc_Score(Grid):
    skore = 0
    count_mercovka = 0
    count_tercovec = 0
    count_parmac = 0
    count_skalara = 0
    count_krunyrovec = 0
    count_rostlina = 0

    for sloupec in range(len(Grid)):
        for radek in range(len(Grid[sloupec])):
            if Grid[sloupec][radek] == None:
                continue
            count = 0
            list = []
            match Grid[sloupec][radek]:
                case 0:
                    if(sloupec-1 >=0):
                        if radek+1 < 4:
                            list.append(Grid[sloupec-1][radek+1])
                        if radek-1 >= 0:
                            list.append(Grid[sloupec-1][radek-1])
                    if(sloupec+1 < 4):
                        if radek+1 < 4:
                            list.append(Grid[sloupec+1][radek+1])
                        if radek-1 >= 0:
                            list.append(Grid[sloupec+1][radek-1])
                    counter = collections.Counter(filter(lambda element: element != None, list))
                    common = counter.most_common(1)
                    if(common):
                        if counter.most_common(1)[0][1] > 1:
                            skore += 6
                case 6:
                    if sloupec-1 >= 0:
                        list.append(Grid[sloupec-1][radek])
                    if sloupec+1 < 4:
                        list.append(Grid[sloupec+1][radek])
                    if radek+1 < 4:
                        list.append(Grid[sloupec][radek+1])
                    if radek-1 >= 0:
                        list.append(Grid[sloupec][radek-1])
                    if(len(set(filter(lambda element: element != None, list))) >= 3):
                        skore += 5
                case 8:
                    if sloupec-1 >= 0:
                        list.append(Grid[sloupec-1][radek])
                    if sloupec+1 < 4:
                        list.append(Grid[sloupec+1][radek])
                    if radek+1 < 4:
                        list.append(Grid[sloupec][radek+1])
                    if radek-1 >= 0:
                        list.append(Grid[sloupec][radek-1])
                    counter = collections.Counter(filter(lambda element: element != None, list))
                    common = counter.most_common(1)
                    if(common):
                        if counter.most_common(1)[0][1] > 1:
                            skore += 5
                case default:
                    pass


    for sloupec in range(4):
        for radek in range(4):
            if Grid[sloupec][radek] == None:
                continue
            match Grid[sloupec][radek]:
                case 1:
                    try:   
                        if Grid[sloupec+1][radek-1] == Grid[sloupec][radek]:
                            skore += 5
                            Grid[sloupec+1][radek-1] = None
                            if Grid[sloupec+2][radek-2] == Grid[sloupec][radek]:
                                skore += 6
                                Grid[sloupec+2][radek-2] = None
                    except:
                        pass
                    Grid[sloupec][radek] = None
                case 2:
                    if Grid[0][0] == Grid[sloupec][radek]:
                        count_mercovka+= 1 
                        Grid[0][0] = None
                    if Grid[0][3] == Grid[sloupec][radek]:
                        count_mercovka+=1
                        Grid[0][3] = None
                    if Grid[3][0] == Grid[sloupec][radek]:
                        count_mercovka+=1
                        Grid[3][0] = None
                    if Grid[3][3] == Grid[sloupec][radek]:
                        count_mercovka+=1
                        Grid[3][3] = None

                        for y in range(1, 3):
                            for x in range(1,3):
                                if(Grid[y][x] == Grid[sloupec][radek]):
                                        count_mercovka+=1
                                        Grid[y][x] = None
                                
                    Grid[sloupec][radek] = None
                case 3:
                    try:
                        if Grid[sloupec+1][radek+1] == Grid[sloupec][radek]:
                            skore += 5
                            Grid[sloupec+1][radek+1] = None
                            if Grid[sloupec+2][radek+2] == Grid[sloupec][radek]:
                                skore += 6
                                Grid[sloupec+2][radek+2] = None
                    
                    except:
                        pass
                    Grid[sloupec][radek] = None
                case 4:
                    count_rostlina += 1
                case 5:
                    try: 
                        if Grid[sloupec][radek+1] == Grid[sloupec][radek]:
                            skore += 5
                            Grid[sloupec][radek+1] = None
                            if Grid[sloupec][radek+2] == Grid[sloupec][radek]:
                                skore += 6
                                Grid[sloupec][radek+2] = None
                    except:
                        pass
                    Grid[sloupec][radek] = None
                case 7:
                    try:
                        if Grid[sloupec+1][radek] == Grid[sloupec][radek]:
                            skore += 5
                            Grid[sloupec+1][radek] = None
                            if Grid[sloupec+2][radek] == Grid[sloupec][radek]:
                                skore += 6
                                Grid[sloupec+2][radek] = None
                    except:
                        pass
                    Grid[sloupec][radek] = None
                case 9:
                    for y in range(1, 3):
                        for x in range(1,3):
                            if(Grid[y][x] == Grid[sloupec][radek]):
                                    count_tercovec+=1
                                    Grid[y][x] = None
                    Grid[sloupec][radek] = None
                case 10:
                    count_skalara += 1
                    Grid[sloupec][radek] == None
                case 11:
                    if sloupec == 1 or sloupec == 3:
                        count_krunyrovec +=1
                    Grid[sloupec][radek] = None
                case 12:
                    if(Grid[1][0] == Grid[sloupec][radek]):
                        count_parmac += 1
                        Grid[1][0] = None
                    if(Grid[2][0] == Grid[sloupec][radek]):
                        count_parmac += 1
                        Grid[2][0] = None
                    if(Grid[0][1] == Grid[sloupec][radek]):
                        count_parmac += 1
                        Grid[0][1] = None
                    if(Grid[0][2] == Grid[sloupec][radek]):
                        count_parmac += 1
                        Grid[0][2] = None
                    if(Grid[3][2] == Grid[sloupec][radek]):
                        count_parmac += 1
                        Grid[3][2] = None
                    if(Grid[3][1] == Grid[sloupec][radek]):
                        count_parmac += 1
                        Grid[3][1] = None
                    if(Grid[1][3] == Grid[sloupec][radek]):
                        count_parmac += 1
                        Grid[1][3] = None
                    if(Grid[2][3] == Grid[sloupec][radek]):
                        count_parmac += 1
                        Grid[2][3] = None
                    Grid[sloupec][radek] = None
                case default:
                    pass
    if(count_mercovka > 2):
        skore += 11
    elif count_mercovka == 2:
        skore += 5

    if(count_tercovec > 2):
        skore += 12
    elif count_tercovec >= 1:
        skore += 4

    if(count_parmac > 2):
        skore += 10
    elif count_parmac == 2:
        skore += 5

    if(count_skalara > 3):
        skore += 13
    elif count_skalara == 1:
        skore += 5

    if(count_krunyrovec > 1):
            skore += 6

    if(count_rostlina > 6):
        skore += 13
    elif count_rostlina > 3:
        skore += 7
    elif count_rostlina > 1:
        skore += 3
  
    # OLD
    # for sloupec in range(len(Grid)):
    #         for radek in range(len(Grid[sloupec])):
    #             if Grid[sloupec][radek] == None:
    #                 continue
    #             count = 0
    #             list = []
    #             match Grid[sloupec][radek]:
    #                 case 0:
    #                     if(sloupec-1 >=0):
    #                         if radek+1 < 4:
    #                             list.append(Grid[sloupec-1][radek+1])
    #                         if radek-1 >= 0:
    #                             list.append(Grid[sloupec-1][radek-1])
    #                     if(sloupec+1 < 4):
    #                         if radek+1 < 4:
    #                             list.append(Grid[sloupec+1][radek+1])
    #                         if radek-1 >= 0:
    #                             list.append(Grid[sloupec+1][radek-1])
    #                     counter = collections.Counter(filter(lambda element: element != None, list))
    #                     common = counter.most_common(1)
    #                     if(common):
    #                         if counter.most_common(1)[0][1] > 1:
    #                             skore += 6
    #                 case 6:
    #                     if sloupec-1 >= 0:
    #                         list.append(Grid[sloupec-1][radek])
    #                     if sloupec+1 < 4:
    #                         list.append(Grid[sloupec+1][radek])
    #                     if radek+1 < 4:
    #                         list.append(Grid[sloupec][radek+1])
    #                     if radek-1 >= 0:
    #                         list.append(Grid[sloupec][radek-1])
    #                     if(len(set(filter(lambda element: element != None, list))) >= 3):
    #                         skore += 5
    #                 case 8:
    #                     if sloupec-1 >= 0:
    #                         list.append(Grid[sloupec-1][radek])
    #                     if sloupec+1 < 4:
    #                         list.append(Grid[sloupec+1][radek])
    #                     if radek+1 < 4:
    #                         list.append(Grid[sloupec][radek+1])
    #                     if radek-1 >= 0:
    #                         list.append(Grid[sloupec][radek-1])
    #                     counter = collections.Counter(filter(lambda element: element != None, list))
    #                     common = counter.most_common(1)
    #                     if(common):
    #                         if counter.most_common(1)[0][1] > 1:
    #                             skore += 5
    #                 case default:
    #                     pass

   # print(count_rostlina,count_tercovec,count_krunyrovec,count_mercovka,count_parmac,count_skalara)

    return skore



print(Calc_Score(Fishy))



