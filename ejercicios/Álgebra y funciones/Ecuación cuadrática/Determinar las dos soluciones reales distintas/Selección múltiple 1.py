{"cantidad_opciones":4, "cantidad_disponible":50}

# Resultados enteros
if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, x1, x2 = Racional(elegir(-10,11,0)), Racional(elegir(-10,11)), Racional(elegir(-10,11))
    while abs(x1)==abs(x2):
        a, x1, x2 = Racional(1), Racional(elegir(-10,11)), Racional(elegir(-10,11))
    b, c = a*(-x1-x2), a*x1*x2
    #================================Aquí va el enunciado================================================================
    enunciado = f"Las {choice(['raíces','soluciones'])} de la ecuación "+ Matematica(ecuacion_azar(a*{"x":2}, b*"x", c)) +" son"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = r"\begin{tabular}{p{2 cm} p{0.1 cm} p{2 cm}}"+ Matematica(x1)                                  +"&;&"+ Matematica(x2)                                  +r"\\ \end{tabular}"
    contenido_2 = r"\begin{tabular}{p{2 cm} p{0.1 cm} p{2 cm}}"+        Matematica(-b/(2*a))                            +"&;&"+ Matematica((4*a*c-b**2)/(4*a))                  +r"\\ \end{tabular}"
    contenido_3 = r"\begin{tabular}{p{2 cm} p{0.1 cm} p{2 cm}}"+        Matematica(Pol(-b,-Root(abs(b-4*a*c)))/(2*a))   +"&;&"+ Matematica(Pol(-b,Root(abs(b**2-4*a*c)))/(2*a)) +r"\\ \end{tabular}"
    contenido_4 = r"\begin{tabular}{p{2 cm} p{0.1 cm} p{2 cm}}"+        Matematica(Pol(-b,-Root(abs(b-4*a*c)))/a)       +"&;&"+ Matematica(Pol(-b,Root(abs(b**2-4*a*c)))/a)     +r"\\ \end{tabular}"
    contenido_5 = r"\begin{tabular}{p{2 cm} p{0.1 cm} p{2 cm}}"+        Matematica((-b-(b**2-4*a*c))/(2*a))             +"&;&"+ Matematica((-b+(b**2-4*a*c))/(2*a))             +r"\\ \end{tabular}"


# Resultados no necesariamente enteros
elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c  = Racional(elegir(-3,4,0)), Racional(elegir(-10,11)), Racional(elegir(-10,11))
    while not 0<b**2-4*a*c:
        a, b, c  = Racional(elegir(-3,4,0)), Racional(elegir(-10,11)), Racional(elegir(-10,11))
    #================================Aquí va el enunciado================================================================
    enunciado = f"Las {choice(['raíces','soluciones'])} de la ecuación "+ Matematica(ecuacion_azar(a*{"x":2}, b*"x", c)) +" son"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = r"\begin{tabular}{p{2 cm} p{0.1 cm} p{2 cm}}"+ Matematica(Pol(-b,-Root(b**2-4*a*c))/(2*a))   +"&;&"+ Matematica(Pol(-b,Root(b**2-4*a*c))/(2*a))    +r"\\ \end{tabular}"
    contenido_2 = r"\begin{tabular}{p{2 cm} p{0.1 cm} p{2 cm}}"+        Matematica(b**2-4*a*c)                        +"&;&"+ Matematica((4*a*c-b**2))                      +r"\\ \end{tabular}"
    contenido_3 = r"\begin{tabular}{p{2 cm} p{0.1 cm} p{2 cm}}"+        Matematica(Pol(b,-Root(b**2-4*a*c))/(-2*a))   +"&;&"+ Matematica(Pol(b,-Root(b**2-4*a*c))/(-2*a))   +r"\\ \end{tabular}"
    contenido_4 = r"\begin{tabular}{p{2 cm} p{0.1 cm} p{2 cm}}"+        Matematica((-b)/(2*a))                        +"&;&"+ Matematica((4*a*c-b**2)/(4*a))                +r"\\ \end{tabular}"
    contenido_5 = r"\begin{tabular}{p{2 cm} p{0.1 cm} p{2 cm}}"+        Matematica((-b)/a)                            +"&;&"+ Matematica((b**2-4*a*c)/(4*a))                +r"\\ \end{tabular}"



enunciado_oculto = [a,b,c]










