for i in range(0, 500):
    for j in range(0, 500):
        somme = i + j
        if 0 <= somme <= 999:
            chiffres_i = sorted(str(i))
            chiffres_j = sorted(str(j))
            chiffres_somme = sorted(str(somme))
            if chiffres_i == chiffres_j == chiffres_somme:
                print ("Les nombres sont :", i, j, somme)