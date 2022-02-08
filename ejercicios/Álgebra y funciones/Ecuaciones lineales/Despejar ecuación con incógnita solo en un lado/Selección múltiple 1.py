{"cantidad_opciones":2, "cantidad_disponible":50}

if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, x = Racional(elegir(-20,21,0)), Racional(randrange(1, 20)), Racional(randrange(1, 20))
    while  a+b==0 or a-b==0:
        a, b, x = Racional(elegir(-20,21,0)), Racional(randrange(1, 20)), Racional(randrange(1, 20))
    #================================Aquí va el enunciado================================================================
    enunciado = "El valor de x que satisface la ecuación "+Matematica(ecuacion_azar(a,b*"x", -(a+b*x)))+" es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(x)
    contenido_2 = Matematica(x/(a+b))
    contenido_3 = Matematica(x/(a-b))
    contenido_4 = Matematica((x-a)/b)
    contenido_5 = Matematica((x+a)/b)


elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c = Racional(elegir(-20,21,0)), Racional(randrange(1, 20)), Racional(elegir(-20,21,0))
    while (c-a)/b<0 or c-a<0 or a+b==0 or a-b==0:
            a, b, c = Racional(elegir(-20,21,0)), Racional(randrange(1, 20)), Racional(elegir(-20,21,0))
    x = (c-a)/b
    #================================Aquí va el enunciado================================================================
    enunciado = "El valor de x que satisface la ecuación "+Matematica(ecuacion_azar(a,b*"x", -c))+" es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica((c-a)/b)
    contenido_2 = Matematica((c+a)/b)
    contenido_3 = Matematica(c/(b+a))
    contenido_4 = Matematica(c/(b-a))
    contenido_5 = Matematica(choice([c+a+b, c-a-b]))



enunciado_oculto = [a, b, x]










