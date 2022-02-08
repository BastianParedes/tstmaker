{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b = randrange(1, 10), randrange(1, 10)

#================================Aquí va el enunciado================================================================
enunciado = "El cociente y el resto al hacer la división "+Matematica(str(a)+":"+str(b))+" son, respectivamente,"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = r"\begin{tabular}{p{0.5 cm} p{0.5 cm} p{0.5 cm}}"+ Matematica(int(a/b))+"&y&"+Matematica(a%b)+r"\\ \end{tabular}"
contenido_2 = r"\begin{tabular}{p{0.5 cm} p{0.5 cm} p{0.5 cm}}"+ Matematica(int(a/b)+choice([0,1]))+"&y&"+Matematica(abs(a%b-1))+r"\\ \end{tabular}"
contenido_3 = r"\begin{tabular}{p{0.5 cm} p{0.5 cm} p{0.5 cm}}"+ Matematica(int(a/b)+choice([0,2]))+"&y&"+Matematica(a%b+choice([1,2]))+r"\\ \end{tabular}"
contenido_4 = r"\begin{tabular}{p{0.5 cm} p{0.5 cm} p{0.5 cm}}"+ Matematica(abs(int(a/b)-choice([0,1])))+"&y&"+Matematica(a%b+choice([1,2]))+r"\\ \end{tabular}"
contenido_5 = r"\begin{tabular}{p{0.5 cm} p{0.5 cm} p{0.5 cm}}"+ Matematica(abs(int(a/b)-choice([0,1])))+"&y&"+Matematica(abs(a%b-choice([1,2])))+r"\\ \end{tabular}"


enunciado_oculto = [a,b]










