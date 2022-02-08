{"cantidad_opciones":2, "cantidad_disponible":50}


if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, d = elegir(1, 20), elegir(1, 20), elegir(2, 20)
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(fraccion(a,d)+"+"+fraccion(b,d)+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(fraccion(a+b,d))
    contenido_2 = Matematica(fraccion(abs(a-b), d))
    contenido_3 = Matematica(fraccion(a+b,d+d))
    contenido_4 = Matematica(fraccion(choice([a,b]),d+d))
    contenido_5 = Matematica(fraccion(a*b, d*d))

elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, d = elegir(1, 20), elegir(1, 20), elegir(2, 20)
    while a-b<0:
        a, b = elegir(1, 20), elegir(1, 20)
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(fraccion(a,d)+"-"+fraccion(b,d)+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(fraccion(a-b,d))
    contenido_2 = Matematica(fraccion(a+b, d))
    contenido_3 = Matematica(fraccion(a-b,d-d))
    contenido_4 = Matematica(fraccion(choice([a,b]),d-d))
    contenido_5 = Matematica(fraccion(a*b, d*d))






enunciado_oculto = [a, b, d, opcion]










