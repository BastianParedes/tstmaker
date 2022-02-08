{"cantidad_opciones":3, "cantidad_disponible":50}



if opcion == 1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c, d = Racional(randrange(-3, 4)), Racional(randrange(-5, 6)), Racional(randrange(-5, 6)), Racional(randrange(-2, 3))
    while a==0 or c==0:
        a, b, c, d = Racional(randrange(-3, 4)), Racional(randrange(-5, 6)), Racional(randrange(-5, 6)), Racional(randrange(-2, 3))
    #================================Aquí va el enunciado================================================================
    enunciado = "Considera la función "+Matematica("f(x)="+Pol(Term(a,{"x":2}),2*a*b*"x",a*b**2+a*c**2))+". Es verdadero que la gráfica de dicha función"

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = "No intersecta al eje X"
    contenido_2 = "Intersecta al eje X en un único punto"
    contenido_3 = "Intersecta al eje X en dos puntos"



elif opcion == 2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b = Racional(randrange(-5, 6)), Racional(randrange(-5, 6))
    while a==0:
        a, b = Racional(randrange(-5, 6)), Racional(randrange(-5, 6))
    #================================Aquí va el enunciado================================================================
    enunciado = "Considera la función "+Matematica("f(x)="+Pol(Term(a**2,{"x":2}),2*a*b*"x",b**2))+". Es verdadero que la gráfica de dicha función"

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = "Intersecta al eje X en un único punto"
    contenido_2 = "No intersecta al eje X"
    contenido_3 = "Intersecta al eje X en dos puntos"



elif opcion == 3:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c, d = Racional(randrange(-3, 4)), Racional(randrange(-5, 6)), Racional(randrange(-5, 6)), Racional(randrange(-2, 3))
    while a==0 or c==0:
        a, b, c, d = Racional(randrange(-3, 4)), Racional(randrange(-5, 6)), Racional(randrange(-5, 6)), Racional(randrange(-2, 3))
    #================================Aquí va el enunciado================================================================
    enunciado = "Considera la función "+Matematica("f(x)="+Pol(Term(a*c,{"x":2}),a*b*c*d*"x",b*d))+". Es verdadero que la gráfica de dicha función"

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = "Intersecta al eje X en dos puntos"
    contenido_2 = "Intersecta al eje X en un único punto"
    contenido_3 = "No intersecta al eje X"



contenidos_extras=["No intersecta al eje Y", "Intersecta al eje Y en dos puntos", "Intersecta al eje X en 3 puntos"]
contenido_4 = choice(contenidos_extras)
contenidos_extras.remove(contenido_4)
contenido_5 = choice(contenidos_extras)

enunciado_oculto = enunciado










