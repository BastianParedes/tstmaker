{"cantidad_opciones":3, "cantidad_disponible":50}

extra = list(range(-4, 0))+list(range(1, 5))

if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    m, n = Racional(choice(list(range(-10, 0))+list(range(1, 11)))), Racional(randrange(-10, 11))
    x1, x2, x3, x4, x5 = Racional(choice(list(range(-5, 0))+list(range(1, 6)))), Racional(choice(list(range(-5, 0))+list(range(1, 6)))), Racional(choice(list(range(-5, 0))+list(range(1, 6)))), Racional(choice(list(range(-5, 0))+list(range(1, 6)))), Racional(choice(list(range(-5, 0))+list(range(1, 6))))

    #================================Aquí va el enunciado================================================================
    enunciado = "Considera la función "+Matematica("f(x)="+Pol(m*"x",n))+". El valor de "+Matematica(f"f({x1})")+" es"

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(m*x1+n)
    contenido_2 = Matematica(m*x2+n+Racional(choice(extra)))
    contenido_3 = Matematica(m*x3+n+Racional(choice(extra)))
    contenido_4 = Matematica(m*x4+n+Racional(choice(extra)))
    contenido_5 = Matematica(m*x5+n+Racional(choice(extra)))

elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c = Racional(choice(list(range(-10, 0))+list(range(1, 11)))), Racional(choice(list(range(-10, 0))+list(range(1, 11)))), Racional(choice(list(range(-10, 0))+list(range(1, 11))))
    x1, x2, x3, x4, x5 = Racional(choice(list(range(-5, 0))+list(range(1, 6)))), Racional(choice(list(range(-5, 0))+list(range(1, 6)))), Racional(choice(list(range(-5, 0))+list(range(1, 6)))), Racional(choice(list(range(-5, 0))+list(range(1, 6)))), Racional(choice(list(range(-5, 0))+list(range(1, 6))))

    #================================Aquí va el enunciado================================================================
    enunciado = "Considera la función "+Matematica("f(x)="+Pol(Term(a,{"x":2}),b*"x",c))+". El valor de "+Matematica(f"f({x1})")+" es"

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(a*x1**2+b*x1+c)
    contenido_2 = Matematica(a*x2**2+b*x2+c+Racional(choice(extra)))
    contenido_3 = Matematica(a*x3**2+b*x3+c+Racional(choice(extra)))
    contenido_4 = Matematica(a*x4**2+b*x4+c+Racional(choice(extra)))
    contenido_5 = Matematica(a*x5**2+b*x5+c+Racional(choice(extra)))

elif opcion==3:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a = Racional(choice(list(range(-5, 0))+list(range(1, 6))))
    x1, x2, x3, x4, x5 = Racional(randrange(0,4)), Racional(randrange(0,4)), Racional(randrange(0,4)), Racional(randrange(0,4)), Racional(randrange(0,4))

    #================================Aquí va el enunciado================================================================
    enunciado = "Considera la función "+Matematica("f(x)="+potencia(a,"x"))+". El valor de "+Matematica(f"f({x1})")+" es"

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(a**x1)
    contenido_2 = Matematica(a**x2+Racional(choice(extra)))
    contenido_3 = Matematica(a**x3+Racional(choice(extra)))
    contenido_4 = Matematica(a**x4+Racional(choice(extra)))
    contenido_5 = Matematica(a**x5+Racional(choice(extra)))



enunciado_oculto = enunciado










