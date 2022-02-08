{"cantidad_opciones":2, "cantidad_disponible":50}

if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c, d, e, f = Racional(elegir(-10, 10, 0)), Racional(elegir(-10, 10, 0)), Racional(elegir(-10, 10, 0)), Racional(elegir(-10, 10, 0)), Racional(elegir(-10, 10, 0)), Racional(elegir(-10, 10, 0))
    while d**2*e-b*a-b*f==0:
        a, b, c, d, e, f = Racional(elegir(-10, 10, 0)), Racional(elegir(-10, 10, 0)), Racional(elegir(-10, 10, 0)), Racional(elegir(-10, 10, 0)), Racional(elegir(-10, 10, 0)), Racional(elegir(-10, 10, 0))
    #================================Aquí va el enunciado================================================================
    enunciado = choice([
        "Considera i como la unidad imaginaria. Los valores de x e y que satisfacen la ecuación "+Matematica(Pol(a*"x", b*"i", c*"y")+ "=" +d*"("+Pol(e, "xi)", f*"x").show)+" son",
        "Considera i como la unidad imaginaria. Los valores de x e y que satisfacen la ecuación "+Matematica(d*"("+Pol(e, "xi)", f*"x").show+ "=" +Pol(a*"x", b*"i", c*"y"))+" son"
    ])
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.=
    contenido_correcto = r"\begin{tabular}{p{1.1 cm} p{0.1 cm} p{1.1 cm}}"+ Matematica("x="+(b/d))+"&;&"+           Matematica("y="+(d**2*e+b*f-a*b)/(c*d))+r"\\ \end{tabular}"
    contenido_2 = r"\begin{tabular}{p{1.1 cm} p{0.1 cm} p{1.1 cm}}"+ Matematica("x="+(d**2*e+b*f-a*b)/(c*d))+"&;&"+ Matematica("y="+(b/d))+r"\\ \end{tabular}"
    contenido_3 = r"\begin{tabular}{p{1.1 cm} p{0.1 cm} p{1.1 cm}}"+ Matematica("x="+(-b/d))+"&;&"+                 Matematica("y="+(d**2*e+b*f-a*b)/(-c*d))+r"\\ \end{tabular}"
    contenido_4 = r"\begin{tabular}{p{1.1 cm} p{0.1 cm} p{1.1 cm}}"+ Matematica("x="+(d**2*e+b*f-a*b)/(-c*d))+"&;&"+Matematica("y="+(-b/d))+r"\\ \end{tabular}"
    contenido_5 = r"\begin{tabular}{p{1.1 cm} p{0.1 cm} p{1.1 cm}}"+ Matematica("x="+(a/d))+"&;&"+                  Matematica("y="+(b**2)/(a*c*e))+r"\\ \end{tabular}"


elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c, d, e = Racional(elegir(-10, 10, 0)), Racional(elegir(-10, 10, 0)), Racional(elegir(-10, 10, 0)), Racional(elegir(-10, 10, 0)), Racional(elegir(-10, 10, 0))
    #================================Aquí va el enunciado================================================================
    enunciado = choice([
        "Considera i como la unidad imaginaria. Los valores de x e y que satisfacen la ecuación "+Matematica(Pol(a*"x",b*"(").show+Complex(c,d)+")=" +e*"yi")+" son",
        "Considera i como la unidad imaginaria. Los valores de x e y que satisfacen la ecuación "+Matematica(e*"yi="+Pol(a*"x",b*"(").show+Complex(c,d)+")")+" son"
    ])
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.=
    contenido_correcto = r"\begin{tabular}{p{1.1 cm} p{0.1 cm} p{1.1 cm}}"+ Matematica("x="+(-b)*c/a)+"&;&"+           Matematica("y="+b*d/e)+r"\\ \end{tabular}"
    contenido_2 = r"\begin{tabular}{p{1.1 cm} p{0.1 cm} p{1.1 cm}}"+ Matematica("x="+(b)*c/a)+"&;&"+           Matematica("y="+b*d/e)+r"\\ \end{tabular}"
    contenido_3 = r"\begin{tabular}{p{1.1 cm} p{0.1 cm} p{1.1 cm}}"+ Matematica("x="+(-b)*c/a)+"&;&"+           Matematica("y="+(-b)*d/e)+r"\\ \end{tabular}"
    contenido_4 = r"\begin{tabular}{p{1.1 cm} p{0.1 cm} p{1.1 cm}}"+ Matematica("x="+a/(-b*c))+"&;&"+           Matematica("y="+e/(b*d))+r"\\ \end{tabular}"
    contenido_5 = r"\begin{tabular}{p{1.1 cm} p{0.1 cm} p{1.1 cm}}"+ Matematica("x="+a/(b*c))+"&;&"+           Matematica("y="+(-e)/(b*d))+r"\\ \end{tabular}"


enunciado_oculto = enunciado










