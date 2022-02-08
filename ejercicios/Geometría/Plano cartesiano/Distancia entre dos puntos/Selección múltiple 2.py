{"cantidad_opciones":2, "cantidad_disponible":50}


#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
while True:
    pEnunciado = Par(elegir(-10,10, 0), elegir(-10,10, 0))
    listaP = [
    Par(randrange(-10, 10), randrange(-10, 10)),
    Par(randrange(-10, 10), randrange(-10, 10)),
    Par(randrange(-10, 10), randrange(-10, 10)),
    Par(randrange(-10, 10), randrange(-10, 10)),
    Par(randrange(-10, 10), randrange(-10, 10)),
    ]

    listaDistancias = []
    for p in listaP:
        distancia = pEnunciado.distancia(p)
        distancia.par = p
        listaDistancias.append(distancia)

    listaDistancias = sorted(listaDistancias)
    if listaDistancias[0] != listaDistancias[1] and listaDistancias[-2] != listaDistancias[-1]:
        break

if opcion == 1:
    #================================Aquí va el enunciado================================================================
    enunciado = f"De los siguientes puntos, el que está más lejos del punto {Matematica(pEnunciado)} es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(listaDistancias[-1].par)
    contenido_2 = Matematica(listaDistancias[-2].par) # Relleno
    contenido_3 = Matematica(listaDistancias[-3].par) # Relleno
    contenido_4 = Matematica(listaDistancias[-4].par) # Relleno
    contenido_5 = Matematica(listaDistancias[-5].par) # Elige el más cercano


elif opcion == 2:
    #================================Aquí va el enunciado================================================================
    enunciado = f"De los siguientes puntos, el que está más cerca del punto {Matematica(pEnunciado)} es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(listaDistancias[0].par)
    contenido_2 = Matematica(listaDistancias[1].par) # Relleno
    contenido_3 = Matematica(listaDistancias[2].par) # Relleno
    contenido_4 = Matematica(listaDistancias[3].par) # Relleno
    contenido_5 = Matematica(listaDistancias[4].par) # Elige el más lejano


enunciado_oculto = pEnunciado












