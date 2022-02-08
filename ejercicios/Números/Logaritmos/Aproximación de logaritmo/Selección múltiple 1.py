{"cantidad_opciones":4, "cantidad_disponible":50}

if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, d = Racional(randrange(2, 6)), Racional(randrange(2, 6)), Racional(randrange(2, 5))
    while a.numerador%b.numerador==0 or b.numerador%a.numerador==0:
        a, b, d = Racional(randrange(2, 6)), Racional(randrange(2, 6)), Racional(randrange(2, 5))
    logaritmo_redondeado = Racional(round(math.log(a.numerador,b.numerador),1))
    #================================Aquí va el enunciado================================================================
    enunciado = "Si "+Matematica(logaritmo(a, b)+r"\approx"+logaritmo_redondeado)+" entonces, de las siguientes alternativas, la mejor aproximación de "+Matematica(logaritmo(a*b**d.numerador, b))+" es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto  = Matematica(logaritmo_redondeado+d)
    contenido_2         = Matematica(logaritmo_redondeado*d)
    contenido_3         = Matematica(logaritmo_redondeado-d)
    contenido_4         = Matematica(logaritmo_redondeado/d)
    contenido_5         = Matematica(logaritmo_redondeado**d.numerador)



elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c = Racional(randrange(2, 6)), Racional(randrange(2, 6)), Racional(randrange(2, 5))
    while a.numerador%b.numerador==0 or b.numerador%a.numerador==0:
        a, b, c = Racional(randrange(2, 6)), Racional(randrange(2, 6)), Racional(randrange(2, 5))
    logaritmo_redondeado = Racional(round(math.log(a.numerador,b.numerador),1))
    #================================Aquí va el enunciado================================================================
    enunciado = "Si "+Matematica(logaritmo(a, b)+r"\approx"+logaritmo_redondeado)+" entonces, de las siguientes alternativas, la mejor aproximación de "+Matematica(logaritmo(a, b**c.numerador))+" es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto  = Matematica(logaritmo_redondeado/c)
    contenido_2         = Matematica(logaritmo_redondeado+c)
    contenido_3         = Matematica(logaritmo_redondeado-c)
    contenido_4         = Matematica(c-logaritmo_redondeado)
    contenido_5         = Matematica(logaritmo_redondeado**c.numerador)



elif opcion==3:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c = Racional(randrange(2, 6)), Racional(randrange(2, 6)), Racional(randrange(2, 5))
    while a.numerador%b.numerador==0 or b.numerador%a.numerador==0:
        a, b, c = Racional(randrange(2, 6)), Racional(randrange(2, 6)), Racional(randrange(2, 5))
    logaritmo_redondeado = Racional(round(math.log(a.numerador,b.numerador),1))
    #================================Aquí va el enunciado================================================================
    enunciado = "Si "+Matematica(logaritmo(a, b)+r"\approx"+logaritmo_redondeado)+" entonces, de las siguientes alternativas, la mejor aproximación de "+Matematica(logaritmo(a**c.numerador, b))+" es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto  = Matematica(c*logaritmo_redondeado)
    contenido_2         = Matematica(logaritmo_redondeado+c)
    contenido_3         = Matematica(logaritmo_redondeado-c)
    contenido_4         = Matematica(logaritmo_redondeado/c)
    contenido_5         = Matematica(logaritmo_redondeado**c.numerador)


elif opcion==4:
    opcion_b = choice([1, 2])
    if opcion_b==1:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        a, b, d = Racional(randrange(2, 6)), Racional(randrange(2, 6)), Racional(randrange(2, 5))
        while a.numerador%b.numerador==0 or b.numerador%a.numerador==0:
            a, b, d = Racional(randrange(2, 6)), Racional(randrange(2, 6)), Racional(randrange(2, 5))
        logaritmo_redondeado = Racional(round(math.log(a.numerador,b.numerador),1))
        #================================Aquí va el enunciado================================================================
        enunciado = "Si "+Matematica(logaritmo(a, b)+r"\approx"+logaritmo_redondeado)+" entonces, de las siguientes alternativas, la mejor aproximación de "+Matematica(logaritmo((a/(b**d.numerador)), b))+" es"
        #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
        contenido_correcto  = Matematica(logaritmo_redondeado-d)
        contenido_2         = Matematica(logaritmo_redondeado*d)
        contenido_3         = Matematica(logaritmo_redondeado+d)
        contenido_4         = Matematica(logaritmo_redondeado/d)
        contenido_5         = Matematica(logaritmo_redondeado**d.numerador)

    elif opcion_b==2:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        a, b, d = Racional(randrange(2, 6)), Racional(randrange(2, 6)), Racional(randrange(2, 5))
        while a.numerador%b.numerador==0 or b.numerador%a.numerador==0:
            a, b, d = Racional(randrange(2, 6)), Racional(randrange(2, 6)), Racional(randrange(2, 5))
        logaritmo_redondeado = Racional(round(math.log(a.numerador,b.numerador),1))
        #================================Aquí va el enunciado================================================================
        enunciado = "Si "+Matematica(logaritmo(a, b)+r"\approx"+logaritmo_redondeado)+" entonces, de las siguientes alternativas, la mejor aproximación de "+Matematica(logaritmo(b**d.numerador/a, b))+" es"
        #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
        contenido_correcto  = Matematica(d-logaritmo_redondeado)
        contenido_2         = Matematica(logaritmo_redondeado*(-d))
        contenido_3         = Matematica(logaritmo_redondeado+d)
        contenido_4         = Matematica(logaritmo_redondeado/(-d))
        contenido_5         = Matematica(logaritmo_redondeado**d.numerador)



enunciado_oculto = enunciado











