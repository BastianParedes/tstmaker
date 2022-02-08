{"cantidad_opciones":3, "cantidad_disponible":50}

if opcion==1:
    #===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
    f = randrange(2, 17)
    g = randrange(2, 17)
    while not f<g:
        f = randrange(2, 17)
        g = randrange(2, 17)
    #===============================================Aquí va el número del ejercicio y el enunciado.
    enunciado = f"El mínimo común múltiplo entre {f} y {g} es"
    #===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
    contenido_correcto = MCM(f, g)
    contenido_2 = MCD(f, g)
    contenido_3 = min(f, g)
    contenido_4 = max(f, g)
    contenido_5 = f*g



elif opcion==2:
    #===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
    f = randrange(2, 17)
    g = randrange(2, 17)
    h = randrange(2, 17)
    while not f<g<h:
        f = randrange(2, 17)
        g = randrange(2, 17)
        h = randrange(2, 17)
        
    #===============================================Aquí va el número del ejercicio y el enunciado.
    enunciado = f"El mínimo común múltiplo entre {f}, {g} y {h} es"
    #===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
    contenido_correcto = Matematica(MCM(f, g, h))
    contenido_2 = MCD(f, g, h)
    contenido_3 = min(f, g, h)
    contenido_4 = max(f, g, h)
    contenido_5 = f*g*h



elif opcion==3:
    #===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
    f = randrange(2, 17)
    g = randrange(2, 17)
    h = randrange(2, 17)
    i = randrange(2, 17)
    while not f<g<h<i:
        f = randrange(2, 17)
        g = randrange(2, 17)
        h = randrange(2, 17)
        i = randrange(2, 17)
    #===============================================Aquí va el número del ejercicio y el enunciado.
    enunciado = f"El mínimo común múltiplo entre {f}, {g}, {h} y {i} es"
    #===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
    contenido_correcto = Matematica(MCM(f, g, h, i))
    contenido_2 = MCD(f, g, h, i)
    contenido_3 = min(f, g, h, i)
    contenido_4 = max(f, g, h, i)
    contenido_5 = f*g*h*i






enunciado_oculto = enunciado










