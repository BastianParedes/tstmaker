{"cantidad_opciones":2, "cantidad_disponible":50}

if opcion==1:

    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c, d, e = elegir(2,10), elegir(2,10), elegir(2,7), elegir(2,6), elegir(2,4)
    a, b, c, d, e = a, Root(b**2+elegir(-2,6,0), 2), Root(c**3+elegir(-2,6,0), 3), Root(d**4+elegir(-2,6,0), 4), Root(d**5+elegir(-2,6,0), 5)
    lista_de_raices = sorted([a,b,c,d,e])
    while not type(b)==Root or not type(c)==Root or not type(d)==Root or not type(e)==Root or lista_de_raices[3]==lista_de_raices[4]:
        a, b, c, d, e = elegir(2,10), elegir(2,10), elegir(2,7), elegir(2,6), elegir(2,4)
        a, b, c, d, e = a, Root(b**2+elegir(-5,6,0), 2), Root(c**3+elegir(-5,6,0), 3), Root(d**4+elegir(-5,6,0), 4), Root(d**5+elegir(-5,6,0), 5)
        lista_de_raices = sorted([a,b,c,d,e])
    #================================Aquí va el enunciado================================================================
    enunciado = "De los siguientes números, ¿cuál es mayor?"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(lista_de_raices[4])
    contenido_2 = Matematica(lista_de_raices[3])
    contenido_3 = Matematica(lista_de_raices[2])
    contenido_4 = Matematica(lista_de_raices[1])
    contenido_5 = Matematica(lista_de_raices[0])


if opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c, d, e = elegir(2,10), elegir(2,10), elegir(2,7), elegir(2,6), elegir(2,4)
    a, b, c, d, e = a, Root(b**2+elegir(-2,6,0), 2), Root(c**3+elegir(-2,6,0), 3), Root(d**4+elegir(-2,6,0), 4), Root(d**5+elegir(-2,6,0), 5)
    lista_de_raices = sorted([a,b,c,d,e])
    while not type(b)==Root or not type(c)==Root or not type(d)==Root or not type(e)==Root or lista_de_raices[0]==lista_de_raices[1]:
        a, b, c, d, e = elegir(2,10), elegir(2,10), elegir(2,7), elegir(2,6), elegir(2,4)
        a, b, c, d, e = a, Root(b**2+elegir(-5,6,0), 2), Root(c**3+elegir(-5,6,0), 3), Root(d**4+elegir(-5,6,0), 4), Root(d**5+elegir(-5,6,0), 5)
        lista_de_raices = sorted([a,b,c,d,e])
    #================================Aquí va el enunciado================================================================
    enunciado = "De los siguientes números, ¿cuál es menor?"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(lista_de_raices[0])
    contenido_2 = Matematica(lista_de_raices[1])
    contenido_3 = Matematica(lista_de_raices[2])
    contenido_4 = Matematica(lista_de_raices[3])
    contenido_5 = Matematica(lista_de_raices[4])




enunciado_oculto = [a,b,c,d,e]










