{"cantidad_opciones":3, "cantidad_disponible":50}

if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    h, k, r = choice([-1,1])*Racional(randrange(1, 7)), choice([-1,1])*Racional(randrange(1, 7)), Racional(randrange(1, 7))
    #================================Aquí va el enunciado================================================================
    enunciado_verdadero = "Sea la circunferencia C cuya ecuación general es "+Matematica(Pol({"x":2}, {"y":2}, -2*h*"x", -2*k*"y", h**2+k**2-r**2)+"=0")+". C no puede ser graficada."
    
    enunciado_falso = "Sea la circunferencia C cuya ecuación general es "+Matematica(Pol({"x":2}, {"y":2}, -2*h*"x", -2*k*"y", h**2+k**2-r**2)+"=0")+". "+choice([
    "La gráfica de C es solo un punto.",
    "El radio es positivo.",
    f"El centro de C  es {Matematica(Par(h,-k))}.",
    f"El centro de C  es {Matematica(Par(-h, choice([-k,k])))}."
    ])

elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    h, k, r = choice([-1,1])*Racional(randrange(1, 7)), choice([-1,1])*Racional(randrange(1, 7)), Racional(0)
    #================================Aquí va el enunciado================================================================
    enunciado_verdadero = "Sea la circunferencia C cuya ecuación general es "+Matematica(Pol({"x":2}, {"y":2}, -2*h*"x", -2*k*"y", h**2+k**2-r**2)+"=0")+". La gráfica de C es solo un punto."

    enunciado_falso = "Sea la circunferencia C cuya ecuación general es "+Matematica(Pol({"x":2}, {"y":2}, -2*h*"x", -2*k*"y", h**2+k**2-r**2)+"=0")+". "+choice([
    "C no puede ser graficada.",
    "El radio es positivo.",
    f"El centro de C  es {Matematica(Par(h,-k))}.",
    f"El centro de C  es {Matematica(Par(-h, choice([-k,k])))}."
    ])

elif opcion==3:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    h, k, r = choice([-1,1])*Racional(randrange(1, 7)), choice([-1,1])*Racional(randrange(1, 7)), -Racional(randrange(1, 7))
    #================================Aquí va el enunciado================================================================
    enunciado_verdadero = "Sea la circunferencia C cuya ecuación general es "+Matematica(Pol({"x":2}, {"y":2}, -2*h*"x", -2*k*"y", h**2+k**2-r**2)+"=0")+". El radio es positivo."

    enunciado_falso = "Sea la circunferencia C cuya ecuación general es "+Matematica(Pol({"x":2}, {"y":2}, -2*h*"x", -2*k*"y", h**2+k**2-r**2)+"=0")+". "+choice([
    "La gráfica de C es solo un punto.",
    "C no puede ser graficada.",
    f"El centro de C  es {Matematica(Par(h,-k))}.",
    f"El centro de C  es {Matematica(Par(-h, choice([-k,k])))}."
    ])




enunciado_oculto = [opcion,h,k,r]










