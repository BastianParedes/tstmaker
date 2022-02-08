{"cantidad_opciones":3, "cantidad_disponible":50}

a, b = Racional(randrange(3, 100)), Racional(randrange(3, 100))

if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    while b<a:
        a, b = Racional(randrange(3, 100)), Racional(randrange(3, 100))

    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(f"{a}-{b}=")

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(a-b)
    contenido_2 = Matematica(-a+b)
    contenido_3 = Matematica(-a-b)
    contenido_4 = Matematica(a+b)
    contenido_5 = Matematica(a*b)


elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    while a==b:
        a, b = Racional(randrange(3, 100)), Racional(randrange(3, 100))

    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(f"-{a}+{b}=")

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(-a+b)
    contenido_2 = Matematica(a-b)
    contenido_3 = Matematica(a+b)
    contenido_4 = Matematica(-a-b)
    contenido_5 = Matematica(a*b)


elif opcion==3:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    while a==b:
        a, b = Racional(randrange(3, 100)), Racional(randrange(3, 100))

    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(f"-{a}-{b}=")

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(-a-b)
    contenido_2 = Matematica(a-b)
    contenido_3 = Matematica(-a+b)
    contenido_4 = Matematica(a+b)
    contenido_5 = Matematica(a*b)




enunciado_oculto = [a, b]










