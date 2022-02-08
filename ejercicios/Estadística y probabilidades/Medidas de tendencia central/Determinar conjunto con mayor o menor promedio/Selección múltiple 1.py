{"cantidad_opciones":2, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========

conjunto_1 = []
promedio_1 = Racional(0)
for i in range(0,3):
    conjunto_1.append(Racional(randrange(1,20)))
    promedio_1 += conjunto_1[-1]/3
while promedio_1.denominador!=1:
    conjunto_1 = []
    promedio_1 = Racional(0)
    for i in range(0,3):
        conjunto_1.append(Racional(randrange(1,20)))
        promedio_1 += conjunto_1[-1]/3
conjunto_1 = sorted(conjunto_1)

conjunto_2 = []
promedio_2 = Racional(0)
for i in range(0,3):
    conjunto_2.append(Racional(randrange(1,20)))
    promedio_2 += conjunto_2[-1]/3
while promedio_2.denominador!=1:
    conjunto_2 = []
    promedio_2 = Racional(0)
    for i in range(0,3):
        conjunto_2.append(Racional(randrange(1,20)))
        promedio_2 += conjunto_2[-1]/3
conjunto_2 = sorted(conjunto_2)

conjunto_3 = []
promedio_3 = Racional(0)
for i in range(0,3):
    conjunto_3.append(Racional(randrange(1,20)))
    promedio_3 += conjunto_3[-1]/3
while promedio_3.denominador!=1:
    conjunto_3 = []
    promedio_3 = Racional(0)
    for i in range(0,3):
        conjunto_3.append(Racional(randrange(1,20)))
        promedio_3 += conjunto_3[-1]/3
conjunto_3 = sorted(conjunto_3)

conjunto_4 = []
promedio_4 = Racional(0)
for i in range(0,3):
    conjunto_4.append(Racional(randrange(1,20)))
    promedio_4 += conjunto_4[-1]/3
while promedio_4.denominador!=1:
    conjunto_4 = []
    promedio_4 = Racional(0)
    for i in range(0,3):
        conjunto_4.append(Racional(randrange(1,20)))
        promedio_4 += conjunto_4[-1]/3
conjunto_4 = sorted(conjunto_4)

conjunto_5 = []
promedio_5 = Racional(0)
for i in range(0,3):
    conjunto_5.append(Racional(randrange(1,20)))
    promedio_5 += conjunto_5[-1]/3
while promedio_5.denominador!=1:
    conjunto_5 = []
    promedio_5 = Racional(0)
    for i in range(0,3):
        conjunto_5.append(Racional(randrange(1,20)))
        promedio_5 += conjunto_5[-1]/3
conjunto_5 = sorted(conjunto_5)
promedio_1, promedio_2, promedio_3, promedio_4, promedio_5 = int(promedio_1), int(promedio_2), int(promedio_3), int(promedio_4), int(promedio_5)
lista_de_promedios = sorted([promedio_1, promedio_2, promedio_3, promedio_4, promedio_5])
diccionario_promedio_conjunto = {promedio_1:conjunto_1, promedio_2:conjunto_2, promedio_3:conjunto_3, promedio_4:conjunto_4, promedio_5:conjunto_5}



if opcion==1:
    while lista_de_promedios[4]==lista_de_promedios[3]:
        conjunto_1 = []
        promedio_1 = Racional(0)
        for i in range(0,3):
            conjunto_1.append(Racional(randrange(1,20)))
            promedio_1 += conjunto_1[-1]/3
        while promedio_1.denominador!=1:
            conjunto_1 = []
            promedio_1 = Racional(0)
            for i in range(0,3):
                conjunto_1.append(Racional(randrange(1,20)))
                promedio_1 += conjunto_1[-1]/3
        conjunto_1 = sorted(conjunto_1)

        conjunto_2 = []
        promedio_2 = Racional(0)
        for i in range(0,3):
            conjunto_2.append(Racional(randrange(1,20)))
            promedio_2 += conjunto_2[-1]/3
        while promedio_2.denominador!=1:
            conjunto_2 = []
            promedio_2 = Racional(0)
            for i in range(0,3):
                conjunto_2.append(Racional(randrange(1,20)))
                promedio_2 += conjunto_2[-1]/3
        conjunto_2 = sorted(conjunto_2)

        conjunto_3 = []
        promedio_3 = Racional(0)
        for i in range(0,3):
            conjunto_3.append(Racional(randrange(1,20)))
            promedio_3 += conjunto_3[-1]/3
        while promedio_3.denominador!=1:
            conjunto_3 = []
            promedio_3 = Racional(0)
            for i in range(0,3):
                conjunto_3.append(Racional(randrange(1,20)))
                promedio_3 += conjunto_3[-1]/3
        conjunto_3 = sorted(conjunto_3)

        conjunto_4 = []
        promedio_4 = Racional(0)
        for i in range(0,3):
            conjunto_4.append(Racional(randrange(1,20)))
            promedio_4 += conjunto_4[-1]/3
        while promedio_4.denominador!=1:
            conjunto_4 = []
            promedio_4 = Racional(0)
            for i in range(0,3):
                conjunto_4.append(Racional(randrange(1,20)))
                promedio_4 += conjunto_4[-1]/3
        conjunto_4 = sorted(conjunto_4)

        conjunto_5 = []
        promedio_5 = Racional(0)
        for i in range(0,3):
            conjunto_5.append(Racional(randrange(1,20)))
            promedio_5 += conjunto_5[-1]/3
        while promedio_5.denominador!=1:
            conjunto_5 = []
            promedio_5 = Racional(0)
            for i in range(0,3):
                conjunto_5.append(Racional(randrange(1,20)))
                promedio_5 += conjunto_5[-1]/3
        conjunto_5 = sorted(conjunto_5)

        promedio_1, promedio_2, promedio_3, promedio_4, promedio_5 = int(promedio_1), int(promedio_2), int(promedio_3), int(promedio_4), int(promedio_5)
        lista_de_promedios = sorted([promedio_1, promedio_2, promedio_3, promedio_4, promedio_5])
        diccionario_promedio_conjunto = {promedio_1:conjunto_1, promedio_2:conjunto_2, promedio_3:conjunto_3, promedio_4:conjunto_4, promedio_5:conjunto_5}
    #================================Aquí va el enunciado================================================================
    enunciado = "¿Cuál de los siguientes conjuntos de datos tiene el mayor promedio?"

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = f"{diccionario_promedio_conjunto[lista_de_promedios[4]][0]};  {diccionario_promedio_conjunto[lista_de_promedios[4]][1]};  {diccionario_promedio_conjunto[lista_de_promedios[4]][2]}"
    contenido_2 =        f"{diccionario_promedio_conjunto[lista_de_promedios[3]][0]};  {diccionario_promedio_conjunto[lista_de_promedios[3]][1]};  {diccionario_promedio_conjunto[lista_de_promedios[3]][2]}"
    contenido_3 =        f"{diccionario_promedio_conjunto[lista_de_promedios[2]][0]};  {diccionario_promedio_conjunto[lista_de_promedios[2]][1]};  {diccionario_promedio_conjunto[lista_de_promedios[2]][2]}"
    contenido_4 =        f"{diccionario_promedio_conjunto[lista_de_promedios[1]][0]};  {diccionario_promedio_conjunto[lista_de_promedios[1]][1]};  {diccionario_promedio_conjunto[lista_de_promedios[1]][2]}"
    contenido_5 =        f"{diccionario_promedio_conjunto[lista_de_promedios[0]][0]};  {diccionario_promedio_conjunto[lista_de_promedios[0]][1]};  {diccionario_promedio_conjunto[lista_de_promedios[0]][2]}"








if opcion==2:
    while lista_de_promedios[0]==lista_de_promedios[1]:
        conjunto_1 = []
        promedio_1 = Racional(0)
        for i in range(0,3):
            conjunto_1.append(Racional(randrange(1,20)))
            promedio_1 += conjunto_1[-1]/3
        while promedio_1.denominador!=1:
            promedio_1 = Racional(0)
            for i in range(0,3):
                conjunto_1.append(Racional(randrange(1,20)))
                promedio_1 += conjunto_1[-1]/3
        conjunto_1 = sorted(conjunto_1)

        conjunto_2 = []
        promedio_2 = Racional(0)
        for i in range(0,3):
            conjunto_2.append(Racional(randrange(1,20)))
            promedio_2 += conjunto_2[-1]/3
        while promedio_2.denominador!=1:
            promedio_2 = Racional(0)
            for i in range(0,3):
                conjunto_2.append(Racional(randrange(1,20)))
                promedio_2 += conjunto_2[-1]/3
        conjunto_2 = sorted(conjunto_2)

        conjunto_3 = []
        promedio_3 = Racional(0)
        for i in range(0,3):
            conjunto_3.append(Racional(randrange(1,20)))
            promedio_3 += conjunto_3[-1]/3
        while promedio_3.denominador!=1:
            promedio_3 = Racional(0)
            for i in range(0,3):
                conjunto_3.append(Racional(randrange(1,20)))
                promedio_3 += conjunto_3[-1]/3
        conjunto_3 = sorted(conjunto_3)

        conjunto_4 = []
        promedio_4 = Racional(0)
        for i in range(0,3):
            conjunto_4.append(Racional(randrange(1,20)))
            promedio_4 += conjunto_4[-1]/3
        while promedio_4.denominador!=1:
            promedio_4 = Racional(0)
            for i in range(0,3):
                conjunto_4.append(Racional(randrange(1,20)))
                promedio_4 += conjunto_4[-1]/3
        conjunto_4 = sorted(conjunto_4)

        conjunto_5 = []
        promedio_5 = Racional(0)
        for i in range(0,3):
            conjunto_5.append(Racional(randrange(1,20)))
            promedio_5 += conjunto_5[-1]/3
        while promedio_5.denominador!=1:
            promedio_5 = Racional(0)
            for i in range(0,3):
                conjunto_5.append(Racional(randrange(1,20)))
                promedio_5 += conjunto_5[-1]/3
        conjunto_5 = sorted(conjunto_5)
        promedio_1, promedio_2, promedio_3, promedio_4, promedio_5 = int(promedio_1), int(promedio_2), int(promedio_3), int(promedio_4), int(promedio_5)
        lista_de_promedios = sorted([promedio_1, promedio_2, promedio_3, promedio_4, promedio_5])
        diccionario_promedio_conjunto = {promedio_1:conjunto_1, promedio_2:conjunto_2, promedio_3:conjunto_3, promedio_4:conjunto_4, promedio_5:conjunto_5}
    #================================Aquí va el enunciado================================================================
    enunciado = "¿Cuál de los siguientes conjuntos de datos tiene el menor promedio?"

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = f"{diccionario_promedio_conjunto[lista_de_promedios[0]][0]};  {diccionario_promedio_conjunto[lista_de_promedios[0]][1]};  {diccionario_promedio_conjunto[lista_de_promedios[0]][2]}"
    contenido_2 =        f"{diccionario_promedio_conjunto[lista_de_promedios[1]][0]};  {diccionario_promedio_conjunto[lista_de_promedios[1]][1]};  {diccionario_promedio_conjunto[lista_de_promedios[1]][2]}"
    contenido_3 =        f"{diccionario_promedio_conjunto[lista_de_promedios[2]][0]};  {diccionario_promedio_conjunto[lista_de_promedios[2]][1]};  {diccionario_promedio_conjunto[lista_de_promedios[2]][2]}"
    contenido_4 =        f"{diccionario_promedio_conjunto[lista_de_promedios[3]][0]};  {diccionario_promedio_conjunto[lista_de_promedios[3]][1]};  {diccionario_promedio_conjunto[lista_de_promedios[3]][2]}"
    contenido_5 =        f"{diccionario_promedio_conjunto[lista_de_promedios[4]][0]};  {diccionario_promedio_conjunto[lista_de_promedios[4]][1]};  {diccionario_promedio_conjunto[lista_de_promedios[4]][2]}"










enunciado_oculto = sorted(conjunto_1 + conjunto_2 + conjunto_3 + conjunto_4 + conjunto_5)











