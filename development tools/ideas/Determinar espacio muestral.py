opcion = choice([1,2,3,4,5,6,7,8,9])

if opcion==1:
    #================================Aquí va el enunciado================================================================
    enunciado = "Se lanza un dado normal de 6 caras numeradas de 1 a 6. El espacio muestral de este evento es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = r"\{1, 2, 3, 4, 5, 6\}"
    contenido_2 = r"\{1, 2, 3, 4, 5\}"
    contenido_3 = r"\{1, 2, 3, 4\}"
    contenido_4 = r"\{1, 2, 3\}"
    contenido_5 = r"\{1, 2\}"





elif opcion==2:
    #================================Aquí va el enunciado================================================================
    enunciado = "Se lanzan dos dados normales de 6 caras numeradas de 1 a 6. El espacio muestral de este evento es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = r"\{"
    for i in [1,2,3,4,5,6]:
        for j in [1,2,3,4,5,6]:
            contenido_correcto += f"({i},{j}), "
    contenido_correcto = contenido_correcto[:-2]+r"\}"

    contenido_2 = r"\{"
    for i in [1,2,3,4,5]:
        for j in [1,2,3,4,5,6]:
            contenido_2 += f"({i},{j}), "
    contenido_2 = contenido_2[:-2]+r"\}"

    contenido_3 = r"\{"
    for i in [1,2,3]:
        for j in [1,2,3,4,5,6,7]:
            contenido_3 += f"({i},{j}), "
    contenido_3 = contenido_3[:-2]+r"\}"

    contenido_4 = r"\{"
    for i in [1,2,3,4,5,6]:
        contenido_4 += f"({i},{i}), "
    contenido_4 = contenido_4[:-2]+r"\}"

    contenido_5 = r"\{"
    for i in [1]:
        for j in [1,2,3,4,5,6]:
            contenido_5 += f"({i},{j}), "
    contenido_5 = contenido_5[:-2]+r"\}"





elif opcion==3:
    #================================Aquí va el enunciado================================================================
    enunciado = "Se lanza una moneda. El espacio muestral de este evento es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = r"\{cara, sello\}"
    contenido_2 = r"\{cara\}"
    contenido_3 = r"\{sello\}"
    contenido_4 = r"\{(sello,cara), (cara,sello), (sello,sello), (cara,cara)\}"
    contenido_5 = r"\{(sello,cara), (sello,sello), (cara,cara)\}"




elif opcion==4:
    #================================Aquí va el enunciado================================================================
    enunciado = "Se lanzan dos monedas. El espacio muestral de este evento es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = r"\{(sello,cara), (cara,sello), (sello,sello), (cara,cara)\}"
    contenido_2 = r"\{cara\}"
    contenido_3 = r"\{sello\}"
    contenido_4 = r"\{cara, sello\}"
    contenido_5 = r"\{(sello,cara), (sello,sello), (cara,cara)\}"





elif opcion==5:
    #================================Aquí va el enunciado================================================================
    enunciado = "Se responde una pregunta de selección múltiple de 4 alternativas al azar. El espacio muestral de este evento es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = r"\{A, B, C, D\}"
    contenido_2 = r"\{A, B, C, D, E\}"
    contenido_3 = r"\{"+choice(["A","B","C","D","E"])+r"\}"
    contenido_4 = r"\{"+choice(["A","B","C","D","E"])+r"\}"
    contenido_5 = r"\{"+choice(["A","B","C","D","E"])+r"\}"





elif opcion==6:
    #================================Aquí va el enunciado================================================================
    enunciado = "Se responde una pregunta de selección múltiple de 5 alternativas al azar. El espacio muestral de este evento es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = r"\{A, B, C, D, E\}"
    contenido_2 = r"\{A, B, C, D\}"
    contenido_3 = r"\{"+choice(["A","B","C","D","E"])+r"\}"
    contenido_4 = r"\{"+choice(["A","B","C","D","E"])+r"\}"
    contenido_5 = r"\{"+choice(["A","B","C","D","E"])+r"\}"





elif opcion==7:
    #================================Aquí va el enunciado================================================================
    enunciado = "Se elige uno de los colores de la bandera chilena. El espacio muestral de este evento es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = r"\{rojo, blanco, azul\}"
    contenido_2 = r"\{rojo, blanco, azul, negro, amarillo, verde, rosa\}"
    contenido_3 = r"\{rojo\}"
    contenido_4 = r"\{blanco\}"
    contenido_5 = r"\{azul\}"





elif opcion==8:
    #================================Aquí va el enunciado================================================================
    enunciado = "Se lanza un dado normal y una moneda. El espacio meustral de este evento es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = r"\{"
    for i in [1,2,3,4,5,6]:
        for j in ["cara", "sello"]:
            contenido_correcto += f"({i},{j}), "
    contenido_correcto = contenido_correcto[:-2]+r"\}"

    contenido_2 = r"\{"
    for i in [1,2,3,4,5,6]:
        for j in [1,2,3,4,5,6]:
            contenido_2 += f"({i},{j}), "
    contenido_2 = contenido_2[:-2]+r"\}"

    contenido_3 = r"\{"
    for i in ["cara", "sello"]:
        for j in ["cara", "sello"]:
            contenido_3 += f"({i},{j}), "
    contenido_3 = contenido_3[:-2]+r"\}"

    contenido_4 = r"\{"
    for i in [1,2,3,4,5,6, "cara", "sello"]:
        for j in ["cara", "sello"]:
            contenido_4 += f"({i},{j}), "
    contenido_4 = contenido_4[:-2]+r"\}"

    contenido_5 = r"\{"
    for i in [1,2,3,4,5,6]:
        for j in [1,2,3,4,5,6, "cara", "sello"]:
            contenido_5 += f"({i},{j}), "
    contenido_5 = contenido_5[:-2]+r"\}"




elif opcion==9:
    numeros = "123456789"
    shuffle(numeros)
    numeros = sorted(numeros[:3])
    numero_1 = numeros[0]
    numero_2 = numeros[1]
    numero_3 = numeros[2]

    #================================Aquí va el enunciado================================================================
    enunciado = f"Se construye un número de 3 dígitos (sin repeticiones) con las cifras {numero_1}, {numero_2} y {numero_3} colocándolas al azar. El espacio muestral de este evento es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = r"\{"
    for i in numero_1+numero_2+numero_3:
        for j in (numero_1+numero_2+numero_3).replace(i,""):
            for k in (numero_1+numero_2+numero_3).replace(i,"").replace(k,""):
                contenido_correcto += f"{i}{j}{k} ,"
    contenido_correcto = contenido_correcto[:-2]+r"\}"

    contenido_2 = r"\{"
    for i in numero_1+numero_2+numero_3:
        for j in numero_1+numero_2+numero_3:
            for k in numero_1+numero_2+numero_3:
                contenido_2 += f"{i}{j}{k} ,"
    contenido_2 = contenido_2[:-2]+r"\}"#Consideró las repeticiones

    contenido_3 = r"\{"
    for i in numero_1+numero_2+numero_3:
        contenido_3 += f"{i} ,"
        for j in numero_1+numero_2+numero_3:
            contenido_3 += f"{i}{j} ,"
            for k in numero_1+numero_2+numero_3:
                contenido_3 += f"{i}{j}{k} ,"
    contenido_3 = contenido_3[:-2]+r"\}"#Consideró los números de 1 dígito

    contenido_4 = r"\{"
    for i in numero_1+numero_2+numero_3:
        contenido_4 += f"{i}{j} ,"
        for j in numero_1+numero_2+numero_3:
            for k in numero_1+numero_2+numero_3:
                contenido_4 += f"{i}{j}{k} ,"
    contenido_4 = contenido_4[:-2]+r"\}"#Consideró los números de 2 dígitos

    contenido_5 = r"\{"
    for i in numero_1+numero_2+numero_3:
        contenido_3 += f"{i} ,"
        for j in numero_1+numero_2+numero_3:
            contenido_5 += f"{i}{j} ,"
            for k in numero_1+numero_2+numero_3:
                contenido_5 += f"{i}{j}{k} ,"
    contenido_5 = contenido_5[:-2]+r"\}"#Consideró los números de 1 dígito y los de 2 dígitos







enunciado_oculto = opcion
