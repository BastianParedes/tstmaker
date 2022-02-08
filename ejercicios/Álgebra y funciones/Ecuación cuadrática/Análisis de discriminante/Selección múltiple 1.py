{"cantidad_opciones":3, "cantidad_disponible":50}

if opcion == 1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c, d = Racional(randrange(-3, 4)), Racional(randrange(-5, 6)), Racional(randrange(-5, 6)), Racional(randrange(-2, 3))
    while a==0 or c==0:
        a, b, c, d = Racional(randrange(-3, 4)), Racional(randrange(-5, 6)), Racional(randrange(-5, 6)), Racional(randrange(-2, 3))
    #================================Aquí va el enunciado================================================================
    enunciado = "Sea la ecuación "+Matematica(ecuacion_azar(Term(a,{"x":2}),2*a*b*"x",a*b**2+a*c**2))+". Es verdadero que dicha ecuación"

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = "Tiene dos soluciones reales distintas"
    contenido_2 = "Tiene dos soluciones reales iguales"
    contenido_3 = "Tiene dos soluciones no reales distintas"



elif opcion == 2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b = Racional(randrange(-5, 6)), Racional(randrange(-5, 6))
    while a==0:
        a, b = Racional(randrange(-5, 6)), Racional(randrange(-5, 6))
    #================================Aquí va el enunciado================================================================
    enunciado = "Sea la ecuación "+Matematica(ecuacion_azar(Term(a**2,{"x":2}),2*a*b*"x",b**2))+". Es verdadero que dicha ecuación"

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = "Tiene dos soluciones reales iguales"
    contenido_2 = "Tiene dos soluciones no reales distintas"
    contenido_3 = "Tiene dos soluciones reales distintas"



elif opcion == 3:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c, d = Racional(randrange(-3, 4)), Racional(randrange(-5, 6)), Racional(randrange(-5, 6)), Racional(randrange(-2, 3))
    while a==0 or c==0:
        a, b, c, d = Racional(randrange(-3, 4)), Racional(randrange(-5, 6)), Racional(randrange(-5, 6)), Racional(randrange(-2, 3))
    #================================Aquí va el enunciado================================================================
    enunciado = "Sea la ecuación "+Matematica(ecuacion_azar(Term(a*c,{"x":2}),a*b*c*d*"x",b*d))+". Es verdadero que dicha ecuación"

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = "Tiene dos soluciones reales distintas"
    contenido_2 = "Tiene dos soluciones reales iguales"
    contenido_3 = "Tiene dos soluciones no reales distintas"



contenidos_extras=["No tiene soluciones", "Tiene dos soluciones distintas, una real y otra no real", "Tiene tres soluciones reales distintas"]
contenido_4 = choice(contenidos_extras)
contenidos_extras.remove(contenido_4)
contenido_5 = choice(contenidos_extras)

enunciado_oculto = enunciado










