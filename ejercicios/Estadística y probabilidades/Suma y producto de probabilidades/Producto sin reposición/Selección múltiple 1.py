{"cantidad_opciones":1, "cantidad_disponible":50}

if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    colores = ['roja', 'amarilla', 'azul', 'rosa', 'verde', 'negra', 'blanca']
    shuffle(colores)
    color_1, color_2 = colores[0], colores[1]
    plurales = {'roja':'rojas', 'amarilla':'amarillas', 'azul':'azules', 'rosa':'rosadas', 'verde':'verdes', 'negra':'negras', 'blanca':'blancas'}
    cantidad_1, cantidad_2 = Racional(randrange(4,10)), Racional(randrange(4,10))
    total = cantidad_1 + cantidad_2
    #================================Aquí va el enunciado================================================================
    enunciado = enunciado = f'En una caja hay {cantidad_1} pelotas solo {plurales[color_1]} y {cantidad_2} solo {plurales[color_2]}. Si se sacan dos pelotas, una después de la otra, ¿Cuál es la probabilidad de que la primera sea {color_1} y la segunda {color_2}?'
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(cantidad_1/total * cantidad_2/(total-1))
    contenido_2 =        Matematica(cantidad_1/total * cantidad_2/total)
    contenido_3 =        Matematica((cantidad_1+cantidad_2)/total)
    contenido_4 =        Matematica((cantidad_1*cantidad_2)/total)
    contenido_5 =        Matematica((cantidad_1+cantidad_2)/total**2)
    enunciado_oculto = [opcion,cantidad_1,cantidad_2]

