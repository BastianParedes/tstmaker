{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
b = Racional(randrange(2, 52))

#================================Aquí va el enunciado================================================================
enunciado = "El valor de "+Matematica(raiz(-b**2))+" es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(Complex(0,b))+", con i la unidad imaginaria"
contenido_2 = Matematica(b)
contenido_3 = Matematica(-b)
contenido_4 = Matematica(Complex(0,b**2))+", con i la unidad imaginaria"
contenido_5 = Matematica(Complex(0,-b**2))+", con i la unidad imaginaria"

enunciado_oculto = b










