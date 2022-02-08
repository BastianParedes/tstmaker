{"cantidad_opciones":4, "cantidad_disponible":50}

if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    p1 = Pol("x", elegir(-9,10,0))
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(potencia(p1,3)+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(p1**3)
    contenido_2 =        Matematica(p1**2) #solo eleva a 2
    contenido_3 =        Matematica(3*p1) #multiplica por 3 en lugar de elevar a 3
    contenido_4 =        Matematica(3*p1**2) #eleva a 2 y luego multiplica por 3
    contenido_5 =        Matematica(Pol(lista_de_terminos = list((p1**2)[:-1]) + [(p1**2)[-1]*p1[0]] + [p1[-1]]))
    enunciado_oculto = [opcion, p1]


elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    while True:
        p1 = Pol("x", elegir(-9,10,0), parentesis=True)
        p2 = Pol("x", elegir(-9,10,0), parentesis=True)
        p3 = Pol("x", elegir(-9,10,0), parentesis=True)
        p4 = Pol("x", elegir(-9,10,0), parentesis=True)
        if p1 != p2 != p3 != p4:
            break
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(p1.show + p2.show + "+" + p3.show + p4.show + "=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(p1 * p2 + p3 * p4)
    contenido_2 =        Matematica(Pol(p1[0] , p1[-1] * p2[0] , p2[-1] , p3[0] , p3[-1] * p4[0] , p4[-1], reducir=True)) # Al multiplicar solo lo hace con los términos que están cerca
    contenido_3 =        Matematica(p1*p2) # solo multiplica los terminos de la izquierda
    contenido_4 =        Matematica(p3*p4) # solo multiplica los terminos de la derecha
    contenido_5 =        Matematica(p1*p2*p3*p4) # multiplica los cuatro términos
    enunciado_oculto = [opcion, p1,p2,p3,p4]



elif opcion==3:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    while True:
        n1 = Racional(randrange(2,10))
        n2 = Racional(elegir(-9,10,0,1))
        p1 = Pol("x", elegir(-9,10,0), parentesis=True)
        p2 = Pol("x", elegir(-9,10,0), parentesis=True)
        if n1 != n2 and p1 != p2:
            break

    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(Pol(n1*p1.show, n2*p2.show) + "=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(n1 * p1 + n2 * p2)
    contenido_2 =        Matematica(n1 * p1) #Solo multiplica el primero
    contenido_3 =        Matematica(n2 * p2) #Solo multiplica el segundo
    contenido_4 =        Matematica(n1 * p1 * n2 * p2) # multiplica todo en lugar de sumar
    contenido_5 =        Matematica(Pol(lista_de_terminos=[n1]+p1.lista_de_terminos+[n2]+p2.lista_de_terminos, reducir=True)) # suma todo sin multiplicar
    enunciado_oculto = [opcion, n1, n2, p1, p2]




elif opcion==4:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    while True:
        p1 = Pol("x","y", elegir(-9,10,0), parentesis=True, azar=True)
        p2 = Pol("x","y", elegir(-9,10,0), parentesis=True, azar=True)
        if p1 != p2:
            break
    listaPol = [p1,p2]
    shuffle(listaPol)
    p1,p2 = listaPol[0], listaPol[1]
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(p1.show + p2.show + "=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(p1 * p2)
    contenido_2 =        Matematica(p1 + p2) #suma los términos
    contenido_3 =        Matematica(Pol(lista_de_terminos=(list(p1[:-1]) + [p1[-1]*p2[0]] + list(p2[1:])), reducir=True)) #multiplica solo los de almedio
    contenido_4 =        Matematica(p1**2) #el primero lo eleva a 2
    contenido_5 =        Matematica(p2**2) #el segundo lo eleva a 2
    enunciado_oculto = [opcion, p1 + p2]













