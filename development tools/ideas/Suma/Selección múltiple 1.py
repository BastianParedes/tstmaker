{"cantidad_opciones":2, "cantidad_disponible":50}


if opcion==1:
    opcion_b = choice([1,2])
    if opcion_b == 1:#MEJORARRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        colores = ['roja', 'amarilla', 'azul', 'rosa', 'verde', 'negra', 'blanca']
        shuffle(colores)
        color_1, color_2 = colores[0], colores[1]
        plurales = {'roja':'rojas', 'amarilla':'amarillas', 'azul':'azules', 'rosa':'rosadas', 'verde':'verdes', 'negra':'negras', 'blanca':'blancas'}
        cantidad_1, cantidad_2 = Racional(randrange(4,10)), Racional(randrange(4,10))
        total = cantidad_1 + cantidad_2
        #================================Aquí va el enunciado================================================================
        enunciado = f'En una caja hay {cantidad_1} pelotas solo {plurales[color_1]} y {cantidad_2} solo {plurales[color_2]}. Si se saca una pelota al azar, la probabilidad de que sea {color_1} o {color_2} es'
        #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
        contenido_correcto = Matematica(cantidad_1/total + cantidad_2/total)
        contenido_2 =        Matematica(cantidad_1/total * cantidad_2/total)
        contenido_3 =        Matematica(cantidad_1 * cantidad_2 / total)
        contenido_4 =        Matematica((cantidad_1 + cantidad_2) / total**3)
        contenido_5 =        Matematica(min([cantidad_1/cantidad_2 , cantidad_2/cantidad_1]))
        enunciado_oculto = [opcion, opcion_b, sorted([cantidad_1,cantidad_2])]
    elif opcion_b == 2:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        colores = ['roja', 'amarilla', 'azul', 'rosa', 'verde', 'negra', 'blanca']
        shuffle(colores)
        color_1, color_2, color_3 = colores[0], colores[1], colores[2]
        plurales = {'roja':'rojas', 'amarilla':'amarillas', 'azul':'azules', 'rosa':'rosadas', 'verde':'verdes', 'negra':'negras', 'blanca':'blancas'}
        cantidad_1, cantidad_2, cantidad_3 = Racional(randrange(4,10)), Racional(randrange(4,10)), Racional(randrange(4,10))
        total = cantidad_1 + cantidad_2 + cantidad_3
        #================================Aquí va el enunciado================================================================
        enunciado = f'En una caja hay {cantidad_1} pelotas solo {plurales[color_1]}, {cantidad_2} solo {plurales[color_2]} y {cantidad_3} solo {plurales[color_3]}. Si se saca una pelota al azar, la probabilidad de que sea {color_1} o {color_2} es'
        #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
        contenido_correcto = Matematica(cantidad_1/total + cantidad_2 / total)
        contenido_2 =        Matematica(cantidad_1/total * cantidad_2/total * cantidad_3/total)
        contenido_3 =        Matematica(cantidad_1 * cantidad_2 * cantidad_3 / total)
        contenido_4 =        Matematica((cantidad_1 + cantidad_2 + cantidad_3) / total**3)
        contenido_5 =        Matematica(cantidad_1 * cantidad_2 / cantidad_3)
        enunciado_oculto = [opcion, opcion_b, sorted([cantidad_1,cantidad_2,cantidad_3])]




elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    idiomas = ['español', 'inglés', 'portugués', 'japonés', 'ruso', 'italiano', 'francés']
    shuffle(idiomas)
    idioma_1, idioma_2 = idiomas[0], idiomas[1]
    while True:
        cantidad_1, cantidad_2 = Racional(randrange(5,11)), Racional(randrange(5,11))
        if cantidad_1 != cantidad_2:
            break
    menor = min([cantidad_1, cantidad_2])
    cantidad_ambos = Racional(randrange(int(menor/4), int(menor/2)))
    cantidad_ninguno = Racional(randrange(5,11))
    total = cantidad_1 + cantidad_2 - cantidad_ambos + cantidad_ninguno
    #================================Aquí va el enunciado================================================================
    enunciado = f'En una escuela de idiomas hay {total} estudiantes, de los cuales {cantidad_1} hablan {idioma_1}, {cantidad_2} hablan {idioma_2} y {cantidad_ambos} hablan ambos idiomas. Si se escoge un estudiante al azar, la probabilidad de que hable por lo menos uno de los idiomas mencionados es'
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(cantidad_1/total + cantidad_2/total - cantidad_ambos/total)
    contenido_2 =        Matematica(cantidad_1/total + cantidad_2/total)
    contenido_3 =        Matematica(cantidad_1/total + cantidad_2/total - (cantidad_1/total)*(cantidad_2/total))
    contenido_4 =        Matematica(min([ (cantidad_1+cantidad_2)/total , total/(cantidad_1+cantidad_2) ]))
    contenido_5 =        Matematica(cantidad_ambos/total)
    enunciado_oculto = [cantidad_1 , cantidad_2 , cantidad_ambos]



