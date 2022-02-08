{"cantidad_opciones":5, "cantidad_disponible":50}

a, b = Racional(randrange(3, 100)), Racional(randrange(3, 100))
while b==a:
    a, b = Racional(randrange(3, 100)), Racional(randrange(3, 100))


if opcion==1:
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(f"{-a}{por()}{b}=")

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(-a*b)
    contenido_2 = Matematica(a*b)
    contenido_3 = Matematica(a+b)
    contenido_4 = Matematica(-a+b)
    contenido_5 = Matematica(-a-b)



elif opcion==2:
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(f"{a}{por()}({-b})=")

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(a*(-b))
    contenido_2 = Matematica(a*b)
    contenido_3 = Matematica(a-b)
    contenido_4 = Matematica(-a+b)
    contenido_5 = Matematica(-a-b)



elif opcion==3:
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(f"-{a}{por()}({-b})=")

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(-a*(-b))
    contenido_2 = Matematica(-a*b)
    contenido_3 = Matematica(-a-b)
    contenido_4 = Matematica(-a+b)
    contenido_5 = Matematica(a-b)



elif opcion==4:
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(f"(-{a}){por()}({-b})=")

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(-a*(-b))
    contenido_2 = Matematica(-a*b)
    contenido_3 = Matematica(-a-b)
    contenido_4 = Matematica(a+b)
    contenido_5 = Matematica(-a+b)



elif opcion==5:
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(f"-(-{a}){por()}({-b})=")

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(a*(-b))
    contenido_2 = Matematica(a*b)
    contenido_3 = Matematica(-a+b)
    contenido_4 = Matematica(a-b)
    contenido_5 = Matematica(-a-b)



enunciado_oculto = [a, b]










