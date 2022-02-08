{"cantidad_opciones":2, "cantidad_disponible":50}


if opcion==1:
    #===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
    f1, f2 = Racional(randrange(2, 21),randrange(2, 21)), Racional(randrange(2, 21),randrange(2, 21))
    while f1.denominador==1 or f2.denominador==1 or f1.denominador==f2.denominador:
        f1, f2 = Racional(randrange(2, 21),randrange(2, 21)), Racional(randrange(2, 21),randrange(2, 21))
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(f1 + "+" + f2 + "=")
    #===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
    contenido_correcto = Matematica(f1+f2)
    contenido_2 = Matematica(Racional(f1.numerador+f2.numerador, f1.denominador+f2.denominador))
    contenido_3 = Matematica(f1*f2)
    contenido_4 = Matematica(Racional(f1.numerador+f2.numerador,f1.denominador*f2.denominador))
    contenido_5 = Matematica(Racional(f1.numerador*f2.numerador,f1.numerador*f2.denominador+f2.numerador*f1.denominador))


elif opcion==2:
    #===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
    f1, f2 = Racional(randrange(2, 21),randrange(2, 21)), Racional(randrange(2, 21),randrange(2, 21))
    while f1.denominador==1 or f2.denominador==1 or f1.denominador==f2.denominador or f1-f2<=0:
        f1, f2 = Racional(randrange(2, 21),randrange(2, 21)), Racional(randrange(2, 21),randrange(2, 21))
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(f1 + "-" + f2 + "=")
    #===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
    contenido_correcto = Matematica(f1-f2)
    contenido_2 = Matematica(Racional(abs(f1.numerador-f2.numerador), abs(f1.denominador-f2.denominador)))
    contenido_3 = Matematica(f1*f2)
    contenido_4 = Matematica(Racional(abs(f1.numerador-f2.numerador),f1.denominador*f2.denominador))
    contenido_5 = Matematica(Racional(f1.numerador*f2.numerador,abs(f1.numerador*f2.denominador-f2.numerador*f1.denominador)))



enunciado_oculto = [f1, f2, opcion]










