{"cantidad_opciones":5, "cantidad_disponible":50}


if opcion == 1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    n1 = Racional(randrange(1, 1000), choice([90, 900, 990]), True)
    while n1.parte_decimal_no_periodica=="" or n1.parte_decimal_periodica=="":
        n1 = Racional(randrange(1, 1000), choice([90, 900, 990]), True)

    n2 = Racional(randrange(1, 1000), choice([90, 900, 990]), True)
    while n2.parte_decimal_no_periodica=="" or n2.parte_decimal_periodica=="":
        n2 = Racional(randrange(1, 1000), choice([90, 900, 990]), True)
    n = Racional(n1+n2, 1, True)

    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(n1+"+"+n2+"=")

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(n)
    contenido_2 = Matematica(Racional(Racional(n1.parte_entera+"."+str(int(n1.parte_decimal_no_periodica)+int(n1.parte_decimal_periodica))) + Racional(n2.parte_entera+"."+str(int(n2.parte_decimal_no_periodica)+int(n2.parte_decimal_periodica))), 1, True))
    contenido_3 = Matematica(Racional(f"{int(n1.parte_entera) + int(n2.parte_entera)}.{int(n1.parte_decimal_no_periodica) + int(n2.parte_decimal_no_periodica)}{int(n1.parte_decimal_periodica) + int(n2.parte_decimal_periodica)}", 1, True))
    contenido_4 = Matematica(f"{int(n1.parte_entera) + int(n2.parte_entera)},{int(n1.parte_decimal_no_periodica) + int(n2.parte_decimal_no_periodica)}{linea(int(n1.parte_decimal_periodica) + int(n2.parte_decimal_periodica), azar=False)}")
    contenido_5 = Matematica(f"{int(n1.parte_entera) + int(n2.parte_entera)},{linea(int(n1.parte_decimal_no_periodica + n1.parte_decimal_periodica) + int(n2.parte_decimal_no_periodica + n2.parte_decimal_periodica), azar=False)}")



elif opcion == 2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    n1 = Racional(randrange(1, 1000), choice([9, 99]), True)
    while n1.parte_decimal_no_periodica!="" or n1.parte_decimal_periodica=="":
        n1 = Racional(randrange(1, 1000), choice([9, 99]), True)

    n2 = Racional(randrange(1, 1000), choice([9, 99]), True)
    while n2.parte_decimal_no_periodica!="" or n2.parte_decimal_periodica=="":
        n2 = Racional(randrange(1, 1000), choice([9, 99]), True)
    n = Racional(n1+n2, 1, True)

    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(n1+"+"+n2+"=")

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(n)
    contenido_2 = Matematica(Racional(Racional(n1.parte_entera+"."+n1.parte_decimal_periodica) + Racional((n2.parte_entera+"."+n2.parte_decimal_periodica)),1,True))
    contenido_3 = Matematica(Racional(f"{int(n1.parte_entera) + int(n2.parte_entera)}.{int(n1.parte_decimal_periodica) + int(n2.parte_decimal_periodica)}",1,True))
    contenido_4 = Matematica(f"{int(n1.parte_entera) + int(n2.parte_entera)},{linea(int(n1.parte_decimal_periodica) + int(n2.parte_decimal_periodica), azar=False)}")
    contenido_5 = Matematica(int(n1.parte_entera+n1.parte_decimal_periodica) + int(n2.parte_entera+n2.parte_decimal_periodica))



elif opcion == 3:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    n1 = Racional(randrange(1, 1000), choice([9, 99]), True)
    while n1.parte_decimal_no_periodica!="" or n1.parte_decimal_periodica=="":
        n1 = Racional(randrange(1, 1000), choice([9, 99]), True)

    n2 = Racional(randrange(1, 1000), choice([90, 900, 990]), True)
    while n2.parte_decimal_no_periodica=="" or n2.parte_decimal_periodica=="":
        n2 = Racional(randrange(1, 1000), choice([90, 900, 990]), True)
    n = Racional(n1+n2, 1, True)

    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(n1+"+"+n2+"=")

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(n)
    contenido_2 = Matematica(Racional(Racional(n1.parte_entera+"."+n1.parte_decimal_periodica) + Racional(n2.parte_entera+"."+n2.parte_decimal_no_periodica+n2.parte_decimal_periodica),1,True))
    contenido_3 = Matematica(Racional(f"{int(n1.parte_entera) + int(n2.parte_entera)}.{n2.parte_decimal_no_periodica}{int(n1.parte_decimal_periodica) + int(n2.parte_decimal_periodica)}",1,True))
    contenido_4 = Matematica(f"{int(n1.parte_entera) + int(n2.parte_entera)},{n2.parte_decimal_no_periodica}{linea(int(n1.parte_decimal_periodica) + int(n2.parte_decimal_periodica), azar=False)}")
    contenido_5 = Matematica(f"{int(n1.parte_entera) + int(n2.parte_entera)},{linea(int(n1.parte_decimal_periodica) + int(n2.parte_decimal_no_periodica + n2.parte_decimal_periodica), azar=False)}")



elif opcion == 4:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    n1 = Racional(randrange(1, 100), choice([10, 100]), True)
    while not 1<=len(n1.parte_decimal_no_periodica)<=2 or n1.parte_decimal_periodica!="":
        n1 = Racional(randrange(1, 100), choice([10, 100]), True)

    n2 = Racional(randrange(1, 1000), choice([90, 900, 990]), True)
    while n2.parte_decimal_no_periodica=="" or n2.parte_decimal_periodica=="":
        n2 = Racional(randrange(1, 1000), choice([90, 900, 990]), True)
    n = Racional(n1+n2, 1, True)

    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(n1+"+"+n2+"=")

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(n)
    contenido_2 = Matematica(Racional(Racional(n1.parte_entera+"."+n1.parte_decimal_no_periodica) + Racional(n2.parte_entera+"."+n2.parte_decimal_no_periodica+n2.parte_decimal_periodica),1,True))
    contenido_3 = Matematica(Racional(f"{int(n1.parte_entera) + int(n2.parte_entera)}.{int(n1.parte_decimal_no_periodica) + int(n2.parte_decimal_no_periodica)}{n2.parte_decimal_periodica}",1,True))
    contenido_4 = Matematica(f"{int(n1.parte_entera) + int(n2.parte_entera)},{int(n1.parte_decimal_no_periodica) + int(n2.parte_decimal_no_periodica)}{linea(n2.parte_decimal_periodica, azar=False)}")
    contenido_5 = Matematica(f"{int(n1.parte_entera) + int(n2.parte_entera)},{linea(int(n1.parte_decimal_no_periodica) + int(n2.parte_decimal_no_periodica + n2.parte_decimal_periodica), azar=False)}")



elif opcion == 5:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    n1 = Racional(randrange(1, 100), choice([10, 100]), True)
    while not 1<=len(n1.parte_decimal_no_periodica)<=2 or n1.parte_decimal_periodica!="":
        n1 = Racional(randrange(1, 100), choice([10, 100]), True)

    n2 = Racional(randrange(1, 1000), choice([9, 99]), True)
    while n2.parte_decimal_no_periodica!="" or n2.parte_decimal_periodica=="":
        n2 = Racional(randrange(1, 1000), choice([9, 99]), True)
    n = Racional(n1+n2, 1, True)

    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(n1+"+"+n2+"=")

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(n)
    contenido_2 = Matematica(Racional(Racional(n1.parte_entera+"."+n1.parte_decimal_no_periodica) + Racional(n2.parte_entera+"."+n2.parte_decimal_periodica),1,True))
    contenido_3 = Matematica(Racional(f"{int(n1.parte_entera) + int(n2.parte_entera)}.{n1.parte_decimal_no_periodica}{n2.parte_decimal_periodica}",1,True))
    contenido_4 = Matematica(f"{int(n1.parte_entera) + int(n2.parte_entera)},{n1.parte_decimal_no_periodica}{linea(n2.parte_decimal_periodica, azar=False)}")
    contenido_5 = Matematica(f"{int(n1.parte_entera) + int(n2.parte_entera)},{linea(int(n1.parte_decimal_no_periodica) + int(n2.parte_decimal_periodica), azar=False)}")

enunciado_oculto = enunciado










