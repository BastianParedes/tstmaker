{"cantidad_opciones":3, "cantidad_disponible":50}

if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    h, k, r = choice([-1,1])*Racional(randrange(1, 7)), choice([-1,1])*Racional(randrange(1, 7)), Racional(randrange(1, 7))
    #================================Aquí va el enunciado================================================================
    enunciado = "Sea la circunferencia C cuya ecuación general es "+Matematica(Pol({"x":2}, {"y":2}, -2*h*"x", -2*k*"y", h**2+k**2-r**2)+"=0")+". Es verdadero que"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = "C no puede ser graficada."
    contenido_2 = "La gráfica de C es solo un punto."
    contenido_3 = "El radio es positivo."
    contenido_4 = f"El centro de C  es {Matematica(Par(h,-k))}"
    contenido_5 = f"El centro de C  es {Matematica(Par(-h, choice([-k,k])))}"


elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    h, k, r = choice([-1,1])*Racional(randrange(1, 7)), choice([-1,1])*Racional(randrange(1, 7)), Racional(0)
    #================================Aquí va el enunciado================================================================
    enunciado = "Sea la circunferencia C cuya ecuación general es "+Matematica(Pol({"x":2}, {"y":2}, -2*h*"x", -2*k*"y", h**2+k**2-r**2)+"=0")+". Es verdadero que"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = "La gráfica de C es solo un punto."
    contenido_2 = "C no puede ser graficada."
    contenido_3 = "El radio es positivo."
    contenido_4 = f"El centro de C  es {Matematica(Par(h,-k))}"
    contenido_5 = f"El centro de C  es {Matematica(Par(-h, choice([-k,k])))}"


elif opcion==3:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    h, k, r = choice([-1,1])*Racional(randrange(1, 7)), choice([-1,1])*Racional(randrange(1, 7)), -Racional(randrange(1, 7))
    #================================Aquí va el enunciado================================================================
    enunciado = "Sea la circunferencia C cuya ecuación general es "+Matematica(Pol({"x":2}, {"y":2}, -2*h*"x", -2*k*"y", h**2+k**2-r**2)+"=0")+". Es verdadero que"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = "El radio es positivo."
    contenido_2 = "La gráfica de C es solo un punto."
    contenido_3 = "C no puede ser graficada."
    contenido_4 = f"El centro de C  es {Matematica(Par(h,-k))}"
    contenido_5 = f"El centro de C  es {Matematica(Par(-h, choice([-k,k])))}"


enunciado_oculto = [opcion,h,k,r]










