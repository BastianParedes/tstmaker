{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
while True:
    # ax+by=c
    # dx+ey=f
    x, y = Racional(randrange(-10, 10)), Racional(randrange(-10, 10))
    a, b, d, e = Racional(randrange(-10,10)), Racional(randrange(-10, 10)), Racional(randrange(-10, 10)), Racional(randrange(-10, 10))
    c, f = a*x+b*y , d*x+e*y
    if not (a==0 or b==0 or c==0 or d==0 or e==0 or f==0 or a*e-b*d==0 or b*d-a*e==0 or a+b==0 or d+e==0 or a+d==0 or b+e==0):
        break
    
pares_de_letras = choice([["a","b","y"], ["m","n","y"], ["p","q","y"], ["r","s","y"], ["u","v","y"], ["x","y","e"]])
primera_letra = pares_de_letras[0]
segunda_letra = pares_de_letras[1]
conector = pares_de_letras[2]
primera_ecuacion = Matematica(ecuacion_azar(a*primera_letra,b*segunda_letra,c))
segunda_ecuacion = Matematica(ecuacion_azar(d*primera_letra,e*segunda_letra,f))

#================================Aquí va el enunciado================================================================
enunciado = fr"""Los valores de {primera_letra} {conector} {segunda_letra} que satisfacen al sistema de ecuaciones
\begin{{center}} \begin{{tabular}}{{r|}}{primera_ecuacion}\\{segunda_ecuacion}\\\hline \end{{tabular}} \end{{center}}
son"""

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto =    r"\begin{tabular}{p{1.1 cm} p{0.1 cm} p{1.1 cm}}"+        Matematica(f"{primera_letra}="+(b*f-c*e)/(a*e-b*d))+"&;&"+    Matematica(f"{segunda_letra}="+(a*f-c*d)/(b*d-a*e))+r"\\ \end{tabular}"
contenido_2 =           r"\begin{tabular}{p{1.1 cm} p{0.1 cm} p{1.1 cm}}"+        Matematica(f"{primera_letra}="+(-c)/(a+b))+"&;&"+             Matematica(f"{segunda_letra}="+(-f)/(d+e))+r"\\ \end{tabular}"
contenido_3 =           r"\begin{tabular}{p{1.1 cm} p{0.1 cm} p{1.1 cm}}"+        Matematica(f"{primera_letra}="+(-f)/(d+e))+"&;&"+             Matematica(f"{segunda_letra}="+(-c)/(a+b))+r"\\ \end{tabular}"
contenido_4 =           r"\begin{tabular}{p{1.1 cm} p{0.1 cm} p{1.1 cm}}"+        Matematica(f"{primera_letra}="+(-b-c)/(a))+"&;&"+             Matematica(f"{segunda_letra}="+(-e-f)/(d))+r"\\ \end{tabular}"
contenido_5 =           r"\begin{tabular}{p{1.1 cm} p{0.1 cm} p{1.1 cm}}"+        Matematica(f"{primera_letra}="+(-c-f)/(a+d))+"&;&"+           Matematica(f"{segunda_letra}="+(-c-f)/(b+e))+r"\\ \end{tabular}"

enunciado_oculto = [a, b, c, d, e, f]










