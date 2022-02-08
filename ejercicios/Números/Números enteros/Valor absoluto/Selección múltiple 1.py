{"cantidad_opciones":3, "cantidad_disponible":50}

if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    n = Racional(0)
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica("|"+n+"|=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(0)
    contenido_2 = Matematica(elegir(-20, 20, 0))
    contenido_3 = Matematica(elegir(-20, 20, 0))
    contenido_4 = Matematica(elegir(-20, 20, 0))
    contenido_5 = Matematica(elegir(-20, 20, 0))

elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    n = Racional(randrange(-100, -1))
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica("|"+n+"|=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(abs(n))
    contenido_2 = Matematica(-abs(n))
    contenido_3 = Matematica(1)
    contenido_4 = Matematica(-1)
    contenido_5 = Matematica(Racional(n,2,True))

elif opcion==3:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    n = Racional(randrange(2, 100))
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica("|"+n+"|=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(abs(n))
    contenido_2 = Matematica(-abs(n))
    contenido_3 = Matematica(1)
    contenido_4 = Matematica(-1)
    contenido_5 = Matematica(Racional(n,2,True))



enunciado_oculto = n










