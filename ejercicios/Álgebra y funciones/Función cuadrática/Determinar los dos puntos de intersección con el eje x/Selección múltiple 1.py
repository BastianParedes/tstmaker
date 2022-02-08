{"cantidad_opciones":2, "cantidad_disponible":50}

# Resultados enteros
if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, x1, x2 = Racional(elegir(-10,11,0)), Racional(elegir(-10,11)), Racional(elegir(-10,11))
    while abs(x1)==abs(x2):
        a, x1, x2 = Racional(1), Racional(elegir(-10,11)), Racional(elegir(-10,11))
    b, c = a*(-x1-x2), a*x1*x2
    letra = choice(["f", "g", "h"])
    #================================Aquí va el enunciado================================================================
    enunciado = "Sea la función "+ Matematica(letra+"(x)="+choice([-1,1])*Pol(a*{"x":2}, b*"x", c, azar=True)) +f". Los puntos de intersección entre la gráfica de {letra} y el eje x son"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = r"\begin{tabular}{p{2 cm} p{0.1 cm} p{2 cm}}"+ Matematica(r"("+x1+", 0)", arreglar_espacios=True)                               +"&;&"+ Matematica(r"("+x2+", 0)", arreglar_espacios=True)+r"\\ \end{tabular}"
    contenido_2 = r"\begin{tabular}{p{2 cm} p{0.1 cm} p{2 cm}}"+        Matematica(r"("+(-b)/(2*a)+", 0)", arreglar_espacios=True)                       +"&;&"+ Matematica(r"("+(4*a*c-b**2)/(4*a)+", 0)", arreglar_espacios=True)+r"\\ \end{tabular}"
    contenido_3 = r"\begin{tabular}{p{2 cm} p{0.1 cm} p{2 cm}}"+        Matematica(r"("+Pol(-b,-Root(abs(b-4*a*c)))/(2*a)+", 0)", arreglar_espacios=True)+"&;&"+ Matematica(r"("+Pol(-b,Root(abs(b**2-4*a*c)))/(2*a)+", 0)", arreglar_espacios=True)+r"\\ \end{tabular}"
    contenido_4 = r"\begin{tabular}{p{2 cm} p{0.1 cm} p{2 cm}}"+        Matematica(r"("+Pol(-b,-Root(abs(b-4*a*c)))/(a)+", 0)", arreglar_espacios=True)  +"&;&"+ Matematica(r"("+Pol(-b,Root(abs(b**2-4*a*c)))/(a)+", 0)", arreglar_espacios=True)+r"\\ \end{tabular}"
    contenido_5 = r"\begin{tabular}{p{2 cm} p{0.1 cm} p{2 cm}}"+        Matematica(r"("+(-b-(b**2-4*a*c))/(2*a)+", 0)", arreglar_espacios=True)          +"&;&"+ Matematica(r"("+(-b+(b**2-4*a*c))/(2*a)+", 0)", arreglar_espacios=True)+r"\\ \end{tabular}"


# Resultados no necesariamente enteros
elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c  = Racional(elegir(-3,4,0)), Racional(elegir(-10,11)), Racional(elegir(-10,11))
    while not 0<b**2-4*a*c:
        a, b, c  = Racional(elegir(-3,4,0)), Racional(elegir(-10,11)), Racional(elegir(-10,11))
    letra = choice(["f", "g", "h"])
    #================================Aquí va el enunciado================================================================
    enunciado = "Sea la función "+ Matematica(letra+"(x)="+choice([-1,1])*Pol(a*{"x":2}, b*"x", c, azar=True)) +f". Los puntos de intersección entre la gráfica de {letra} y el eje x son"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = r"\begin{tabular}{p{2 cm} p{0.1 cm} p{2 cm}}"+ Matematica(r"("+Pol(-b,-Root(b**2-4*a*c))/(2*a)+", 0)", arreglar_espacios=True)   +"&;&"+ Matematica(r"("+Pol(-b,Root(b**2-4*a*c))/(2*a)+", 0)", arreglar_espacios=True)+r"\\ \end{tabular}"
    contenido_2 = r"\begin{tabular}{p{2 cm} p{0.1 cm} p{2 cm}}"+        Matematica(r"("+(b**2-4*a*c)+", 0)", arreglar_espacios=True)                      +"&;&"+ Matematica(r"("+(4*a*c-b**2)+", 0)", arreglar_espacios=True)+r"\\ \end{tabular}"
    contenido_3 = r"\begin{tabular}{p{2 cm} p{0.1 cm} p{2 cm}}"+        Matematica(r"("+Pol(b,-Root(b**2-4*a*c))/(-2*a)+", 0)", arreglar_espacios=True)   +"&;&"+ Matematica(r"("+Pol(b,-Root(b**2-4*a*c))/(-2*a)+", 0)", arreglar_espacios=True)+r"\\ \end{tabular}"
    contenido_4 = r"\begin{tabular}{p{2 cm} p{0.1 cm} p{2 cm}}"+        Matematica(r"("+(-b)/(2*a)+", 0)", arreglar_espacios=True)                        +"&;&"+ Matematica(r"("+(4*a*c-b**2)/(4*a)+", 0)", arreglar_espacios=True)+r"\\ \end{tabular}"
    contenido_5 = r"\begin{tabular}{p{2 cm} p{0.1 cm} p{2 cm}}"+        Matematica(r"("+(-b)/a+", 0)", arreglar_espacios=True)                            +"&;&"+ Matematica(r"("+(b**2-4*a*c)/(4*a)+", 0)", arreglar_espacios=True)+r"\\ \end{tabular}"



enunciado_oculto = [a,b,c]










