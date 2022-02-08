{"cantidad_opciones":2, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========


conjunto_1 = []
promedio_1 = Racional(0)
for i in range(0,3):
    conjunto_1.append(Racional(randrange(1,20)))
    promedio_1 += conjunto_1[-1]/3
varianza_1 = Racional(0)
for dato in conjunto_1:
    varianza_1 += (dato-promedio_1)**2/3
while varianza_1.denominador!=1:
    conjunto_1 = []
    promedio_1 = Racional(0)
    for i in range(0,3):
        conjunto_1.append(Racional(randrange(1,20)))
        promedio_1 += conjunto_1[-1]/3
    varianza_1 = Racional(0)
    for dato in conjunto_1:
        varianza_1 += (dato-promedio_1)**2/3
conjunto_1 = sorted(conjunto_1)


conjunto_2 = []
promedio_2 = Racional(0)
for i in range(0,3):
    conjunto_2.append(Racional(randrange(1,20)))
    promedio_2 += conjunto_2[-1]/3
varianza_2 = Racional(0)
for dato in conjunto_2:
    varianza_2 += (dato-promedio_2)**2/3
while varianza_2.denominador!=1:
    conjunto_2 = []
    promedio_2 = Racional(0)
    for i in range(0,3):
        conjunto_2.append(Racional(randrange(1,20)))
        promedio_2 += conjunto_2[-1]/3
    varianza_2 = Racional(0)
    for dato in conjunto_2:
        varianza_2 += (dato-promedio_2)**2/3
conjunto_2 = sorted(conjunto_2)


conjunto_3 = []
promedio_3 = Racional(0)
for i in range(0,3):
    conjunto_3.append(Racional(randrange(1,20)))
    promedio_3 += conjunto_3[-1]/3
varianza_3 = Racional(0)
for dato in conjunto_3:
    varianza_3 += (dato-promedio_3)**2/3
while varianza_3.denominador!=1:
    conjunto_3 = []
    promedio_3 = Racional(0)
    for i in range(0,3):
        conjunto_3.append(Racional(randrange(1,20)))
        promedio_3 += conjunto_3[-1]/3
    varianza_3 = Racional(0)
    for dato in conjunto_3:
        varianza_3 += (dato-promedio_3)**2/3
conjunto_3 = sorted(conjunto_3)


conjunto_4 = []
promedio_4 = Racional(0)
for i in range(0,3):
    conjunto_4.append(Racional(randrange(1,20)))
    promedio_4 += conjunto_4[-1]/3
varianza_4 = Racional(0)
for dato in conjunto_4:
    varianza_4 += (dato-promedio_4)**2/3
while varianza_4.denominador!=1:
    conjunto_4 = []
    promedio_4 = Racional(0)
    for i in range(0,3):
        conjunto_4.append(Racional(randrange(1,20)))
        promedio_4 += conjunto_4[-1]/3
    varianza_4 = Racional(0)
    for dato in conjunto_4:
        varianza_4 += (dato-promedio_4)**2/3
conjunto_4 = sorted(conjunto_4)


conjunto_5 = []
promedio_5 = Racional(0)
for i in range(0,3):
    conjunto_5.append(Racional(randrange(1,20)))
    promedio_5 += conjunto_5[-1]/3
varianza_5 = Racional(0)
for dato in conjunto_5:
    varianza_5 += (dato-promedio_5)**2/3
while varianza_5.denominador!=1:
    conjunto_5 = []
    promedio_5 = Racional(0)
    for i in range(0,3):
        conjunto_5.append(Racional(randrange(1,20)))
        promedio_5 += conjunto_5[-1]/3
    varianza_5 = Racional(0)
    for dato in conjunto_5:
        varianza_5 += (dato-promedio_5)**2/3
conjunto_5 = sorted(conjunto_5)





varianza_1, varianza_2, varianza_3, varianza_4, varianza_5 = int(varianza_1), int(varianza_2), int(varianza_3), int(varianza_4), int(varianza_5)
lista_de_varianzas = sorted([varianza_1, varianza_2, varianza_3, varianza_4, varianza_5])
diccionario_varianza_conjunto = {varianza_1:conjunto_1, varianza_2:conjunto_2, varianza_3:conjunto_3, varianza_4:conjunto_4, varianza_5:conjunto_5}



if opcion==1:
    while lista_de_varianzas[4]==lista_de_varianzas[3] or lista_de_varianzas[4]<1:
        conjunto_1 = []
        promedio_1 = Racional(0)
        for i in range(0,3):
            conjunto_1.append(Racional(randrange(1,20)))
            promedio_1 += conjunto_1[-1]/3
        varianza_1 = Racional(0)
        for dato in conjunto_1:
            varianza_1 += (dato-promedio_1)**2/3
        while varianza_1.denominador!=1:
            conjunto_1 = []
            promedio_1 = Racional(0)
            for i in range(0,3):
                conjunto_1.append(Racional(randrange(1,20)))
                promedio_1 += conjunto_1[-1]/3
            varianza_1 = Racional(0)
            for dato in conjunto_1:
                varianza_1 += (dato-promedio_1)**2/3
        conjunto_1 = sorted(conjunto_1)


        conjunto_2 = []
        promedio_2 = Racional(0)
        for i in range(0,3):
            conjunto_2.append(Racional(randrange(1,20)))
            promedio_2 += conjunto_2[-1]/3
        varianza_2 = Racional(0)
        for dato in conjunto_2:
            varianza_2 += (dato-promedio_2)**2/3
        while varianza_2.denominador!=1:
            conjunto_2 = []
            promedio_2 = Racional(0)
            for i in range(0,3):
                conjunto_2.append(Racional(randrange(1,20)))
                promedio_2 += conjunto_2[-1]/3
            varianza_2 = Racional(0)
            for dato in conjunto_2:
                varianza_2 += (dato-promedio_2)**2/3
        conjunto_2 = sorted(conjunto_2)


        conjunto_3 = []
        promedio_3 = Racional(0)
        for i in range(0,3):
            conjunto_3.append(Racional(randrange(1,20)))
            promedio_3 += conjunto_3[-1]/3
        varianza_3 = Racional(0)
        for dato in conjunto_3:
            varianza_3 += (dato-promedio_3)**2/3
        while varianza_3.denominador!=1:
            conjunto_3 = []
            promedio_3 = Racional(0)
            for i in range(0,3):
                conjunto_3.append(Racional(randrange(1,20)))
                promedio_3 += conjunto_3[-1]/3
            varianza_3 = Racional(0)
            for dato in conjunto_3:
                varianza_3 += (dato-promedio_3)**2/3
        conjunto_3 = sorted(conjunto_3)


        conjunto_4 = []
        promedio_4 = Racional(0)
        for i in range(0,3):
            conjunto_4.append(Racional(randrange(1,20)))
            promedio_4 += conjunto_4[-1]/3
        varianza_4 = Racional(0)
        for dato in conjunto_4:
            varianza_4 += (dato-promedio_4)**2/3
        while varianza_4.denominador!=1:
            conjunto_4 = []
            promedio_4 = Racional(0)
            for i in range(0,3):
                conjunto_4.append(Racional(randrange(1,20)))
                promedio_4 += conjunto_4[-1]/3
            varianza_4 = Racional(0)
            for dato in conjunto_4:
                varianza_4 += (dato-promedio_4)**2/3
        conjunto_4 = sorted(conjunto_4)


        conjunto_5 = []
        promedio_5 = Racional(0)
        for i in range(0,3):
            conjunto_5.append(Racional(randrange(1,20)))
            promedio_5 += conjunto_5[-1]/3
        varianza_5 = Racional(0)
        for dato in conjunto_5:
            varianza_5 += (dato-promedio_5)**2/3
        while varianza_5.denominador!=1:
            conjunto_5 = []
            promedio_5 = Racional(0)
            for i in range(0,3):
                conjunto_5.append(Racional(randrange(1,20)))
                promedio_5 += conjunto_5[-1]/3
            varianza_5 = Racional(0)
            for dato in conjunto_5:
                varianza_5 += (dato-promedio_5)**2/3
        conjunto_5 = sorted(conjunto_5)



        varianza_1, varianza_2, varianza_3, varianza_4, varianza_5 = int(varianza_1), int(varianza_2), int(varianza_3), int(varianza_4), int(varianza_5)
        lista_de_varianzas = sorted([varianza_1, varianza_2, varianza_3, varianza_4, varianza_5])
        diccionario_varianza_conjunto = {varianza_1:conjunto_1, varianza_2:conjunto_2, varianza_3:conjunto_3, varianza_4:conjunto_4, varianza_5:conjunto_5}
    #================================Aquí va el enunciado================================================================
    enunciado = choice([
        "¿Cuál de los siguientes conjuntos de datos es menos homogéneo?",
        "¿Cuál de los siguientes conjuntos de datos es más heterogéneo?",
        "¿Cuál de los siguientes conjuntos de datos es más disperso?",
        f"¿Cuál de los siguientes conjuntos es peor representado por su {choice(['media aritmética', 'promedio'])}?"
    ])


    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = f"{diccionario_varianza_conjunto[lista_de_varianzas[4]][0]};  {diccionario_varianza_conjunto[lista_de_varianzas[4]][1]};  {diccionario_varianza_conjunto[lista_de_varianzas[4]][2]}"
    contenido_2 =        f"{diccionario_varianza_conjunto[lista_de_varianzas[3]][0]};  {diccionario_varianza_conjunto[lista_de_varianzas[3]][1]};  {diccionario_varianza_conjunto[lista_de_varianzas[3]][2]}"
    contenido_3 =        f"{diccionario_varianza_conjunto[lista_de_varianzas[2]][0]};  {diccionario_varianza_conjunto[lista_de_varianzas[2]][1]};  {diccionario_varianza_conjunto[lista_de_varianzas[2]][2]}"
    contenido_4 =        f"{diccionario_varianza_conjunto[lista_de_varianzas[1]][0]};  {diccionario_varianza_conjunto[lista_de_varianzas[1]][1]};  {diccionario_varianza_conjunto[lista_de_varianzas[1]][2]}"
    contenido_5 =        f"{diccionario_varianza_conjunto[lista_de_varianzas[0]][0]};  {diccionario_varianza_conjunto[lista_de_varianzas[0]][1]};  {diccionario_varianza_conjunto[lista_de_varianzas[0]][2]}"








if opcion==2:
    while lista_de_varianzas[0]==lista_de_varianzas[1] or lista_de_varianzas[0]<1:
        conjunto_1 = []
        promedio_1 = Racional(0)
        for i in range(0,3):
            conjunto_1.append(Racional(randrange(1,20)))
            promedio_1 += conjunto_1[-1]/3
        varianza_1 = Racional(0)
        for dato in conjunto_1:
            varianza_1 += (dato-promedio_1)**2/3
        while varianza_1.denominador!=1:
            conjunto_1 = []
            promedio_1 = Racional(0)
            for i in range(0,3):
                conjunto_1.append(Racional(randrange(1,20)))
                promedio_1 += conjunto_1[-1]/3
            varianza_1 = Racional(0)
            for dato in conjunto_1:
                varianza_1 += (dato-promedio_1)**2/3
        conjunto_1 = sorted(conjunto_1)


        conjunto_2 = []
        promedio_2 = Racional(0)
        for i in range(0,3):
            conjunto_2.append(Racional(randrange(1,20)))
            promedio_2 += conjunto_2[-1]/3
        varianza_2 = Racional(0)
        for dato in conjunto_2:
            varianza_2 += (dato-promedio_2)**2/3
        while varianza_2.denominador!=1:
            conjunto_2 = []
            promedio_2 = Racional(0)
            for i in range(0,3):
                conjunto_2.append(Racional(randrange(1,20)))
                promedio_2 += conjunto_2[-1]/3
            varianza_2 = Racional(0)
            for dato in conjunto_2:
                varianza_2 += (dato-promedio_2)**2/3
        conjunto_2 = sorted(conjunto_2)


        conjunto_3 = []
        promedio_3 = Racional(0)
        for i in range(0,3):
            conjunto_3.append(Racional(randrange(1,20)))
            promedio_3 += conjunto_3[-1]/3
        varianza_3 = Racional(0)
        for dato in conjunto_3:
            varianza_3 += (dato-promedio_3)**2/3
        while varianza_3.denominador!=1:
            conjunto_3 = []
            promedio_3 = Racional(0)
            for i in range(0,3):
                conjunto_3.append(Racional(randrange(1,20)))
                promedio_3 += conjunto_3[-1]/3
            varianza_3 = Racional(0)
            for dato in conjunto_3:
                varianza_3 += (dato-promedio_3)**2/3
        conjunto_3 = sorted(conjunto_3)


        conjunto_4 = []
        promedio_4 = Racional(0)
        for i in range(0,3):
            conjunto_4.append(Racional(randrange(1,20)))
            promedio_4 += conjunto_4[-1]/3
        varianza_4 = Racional(0)
        for dato in conjunto_4:
            varianza_4 += (dato-promedio_4)**2/3
        while varianza_4.denominador!=1:
            conjunto_4 = []
            promedio_4 = Racional(0)
            for i in range(0,3):
                conjunto_4.append(Racional(randrange(1,20)))
                promedio_4 += conjunto_4[-1]/3
            varianza_4 = Racional(0)
            for dato in conjunto_4:
                varianza_4 += (dato-promedio_4)**2/3
        conjunto_4 = sorted(conjunto_4)


        conjunto_5 = []
        promedio_5 = Racional(0)
        for i in range(0,3):
            conjunto_5.append(Racional(randrange(1,20)))
            promedio_5 += conjunto_5[-1]/3
        varianza_5 = Racional(0)
        for dato in conjunto_5:
            varianza_5 += (dato-promedio_5)**2/3
        while varianza_5.denominador!=1:
            conjunto_5 = []
            promedio_5 = Racional(0)
            for i in range(0,3):
                conjunto_5.append(Racional(randrange(1,20)))
                promedio_5 += conjunto_5[-1]/3
            varianza_5 = Racional(0)
            for dato in conjunto_5:
                varianza_5 += (dato-promedio_5)**2/3
        conjunto_5 = sorted(conjunto_5)



        varianza_1, varianza_2, varianza_3, varianza_4, varianza_5 = int(varianza_1), int(varianza_2), int(varianza_3), int(varianza_4), int(varianza_5)
        lista_de_varianzas = sorted([varianza_1, varianza_2, varianza_3, varianza_4, varianza_5])
        diccionario_varianza_conjunto = {varianza_1:conjunto_1, varianza_2:conjunto_2, varianza_3:conjunto_3, varianza_4:conjunto_4, varianza_5:conjunto_5}
    #================================Aquí va el enunciado================================================================
    enunciado = choice([
        "¿Cuál de los siguientes conjuntos de datos es más homogéneo?",
        "¿Cuál de los siguientes conjuntos de datos es menos heterogéneo?",
        "¿Cuál de los siguientes conjuntos de datos es menos disperso?",
        f"¿Cuál de los siguientes conjuntos es mejor representado por su {choice(['media aritmética', 'promedio'])}?"
    ])


    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = f"{diccionario_varianza_conjunto[lista_de_varianzas[0]][0]};  {diccionario_varianza_conjunto[lista_de_varianzas[0]][1]};  {diccionario_varianza_conjunto[lista_de_varianzas[0]][2]}"
    contenido_2 =        f"{diccionario_varianza_conjunto[lista_de_varianzas[1]][0]};  {diccionario_varianza_conjunto[lista_de_varianzas[1]][1]};  {diccionario_varianza_conjunto[lista_de_varianzas[1]][2]}"
    contenido_3 =        f"{diccionario_varianza_conjunto[lista_de_varianzas[2]][0]};  {diccionario_varianza_conjunto[lista_de_varianzas[2]][1]};  {diccionario_varianza_conjunto[lista_de_varianzas[2]][2]}"
    contenido_4 =        f"{diccionario_varianza_conjunto[lista_de_varianzas[3]][0]};  {diccionario_varianza_conjunto[lista_de_varianzas[3]][1]};  {diccionario_varianza_conjunto[lista_de_varianzas[3]][2]}"
    contenido_5 =        f"{diccionario_varianza_conjunto[lista_de_varianzas[4]][0]};  {diccionario_varianza_conjunto[lista_de_varianzas[4]][1]};  {diccionario_varianza_conjunto[lista_de_varianzas[4]][2]}"




enunciado_oculto = sorted(conjunto_1 + conjunto_2 + conjunto_3 + conjunto_4 + conjunto_5)











