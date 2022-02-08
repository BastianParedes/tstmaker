{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
z = Complex(randrange(-10, 10),randrange(-12, 0))
while z.re==0 or z.im==0 or z.re+z.im==0:
    z = Complex(randrange(-10, 10),randrange(-12, 0))

#================================Aquí va el enunciado================================================================
enunciado = "Considera i la unidad imaginaria. El (los) valor(es) que puede tomar x en la ecuación "+Matematica(potencia(Pol("x",-z.re),2)+"+"+z.im**2+"=0")+ " es (son)"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto  = r"\begin{tabular}{p{1.1 cm} p{0.1 cm} p{1 cm}}"+Matematica(z)+"&;&"+Matematica(z.conjugate())+r"\\ \end{tabular}"
contenido_2         = r"\begin{tabular}{p{1.1 cm} p{0.1 cm} p{1 cm}}"+Matematica(Complex(z.re,z.im**2))+"&;&"+Matematica(Complex(z.re,-z.im**2))+r"\\ \end{tabular}"
contenido_3         = r"\begin{tabular}{p{1.1 cm} p{0.1 cm} p{1 cm}}"+Matematica(Complex(z.re**2,z.im))+"&;&"+Matematica(Complex(z.re**2,-z.im))+r"\\ \end{tabular}"
contenido_4         = r"\begin{tabular}{p{1.1 cm} p{0.1 cm} p{1 cm}}"+Matematica(Complex(0,-z.im**2))+"&&"+r"\\ \end{tabular}"
contenido_5         = r"\begin{tabular}{p{1.1 cm} p{0.1 cm} p{1 cm}}"+Matematica(Complex(0,z.re+z.im))+"&&"+r"\\ \end{tabular}"

enunciado_oculto = z










