{"cantidad_opciones":3, "cantidad_disponible":50}


if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    b = Racional(choice([2,3,5,7]))
    e = Racional(randrange(2, 4))
    #================================Aquí va el enunciado================================================================
    enunciado = "La descomposición en potencias de "+Matematica(Racional(b**e))+" es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(potencia(b,e))
    contenido_2 = Matematica(b)
    contenido_3 = Matematica(e)
    contenido_4 = Matematica(potencia(e,b))
    contenido_5 = Matematica(b+por()+e)



elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    b1, b2 = Racional(choice([2,3,5,7])), Racional(choice([2,3,5,7]))
    e1, e2 = Racional(randrange(2, 4)), Racional(randrange(2, 4))
    while b1==b2:
        b1, b2 = Racional(choice([2,3,5,7])), Racional(choice([2,3,5,7]))
        e1, e2 = Racional(randrange(2, 4)), Racional(randrange(2, 4))
    #================================Aquí va el enunciado================================================================
    enunciado = "La descomposición en potencias de "+Matematica(Racional(b1**e1*b2**e2))+" es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(potencia(b1,e1)+por()+potencia(b2,e2))
    contenido_2 = Matematica("("+b1+por()+e1+")"+por()+"("+b2+por()+e2+")")
    contenido_3 = Matematica(e1+por()+b1+por()+e2+por()+b2)
    contenido_4 = Matematica(potencia(e1,b1)+por()+potencia(e2,b2))
    contenido_5 = Matematica(b1+"+"+e1+"+"+b2+"+"+e2)



elif opcion==3:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    b1, b2, b3 = Racional(choice([2,3,5,7])), Racional(choice([2,3,5,7])), Racional(choice([2,3,5,7]))
    e1, e2, e3 = Racional(randrange(2, 4)), Racional(randrange(2, 4)), Racional(randrange(2, 4))
    while b1==b2 or b1==b3 or b2==b3:
        b1, b2, b3 = Racional(choice([2,3,5,7])), Racional(choice([2,3,5,7])), Racional(choice([2,3,5,7]))
        e1, e2, e3 = Racional(randrange(2, 4)), Racional(randrange(2, 4)), Racional(randrange(2, 4))
    #================================Aquí va el enunciado================================================================
    enunciado = "La descomposición en potencias de "+Matematica(Racional(b1**e1*b2**e2*b3**e3))+" es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(potencia(b1,e1)+por()+potencia(b2,e2)+por()+potencia(b3,e3))
    contenido_2 = Matematica("("+b1+por()+e1+")"+por()+"("+b2+por()+e2+")"+por()+"("+b3+por()+e3+")")
    contenido_3 = Matematica(e1+por()+b1+por()+e2+por()+b2+por()+e3+por()+b3)
    contenido_4 = Matematica(potencia(e1,b1)+por()+potencia(e2,b2)+por()+potencia(e3,b3))
    contenido_5 = Matematica(b1+"+"+e1+"+"+b2+"+"+e2)




enunciado_oculto = enunciado










