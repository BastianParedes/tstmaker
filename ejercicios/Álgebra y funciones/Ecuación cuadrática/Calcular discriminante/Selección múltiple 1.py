{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b, c = Racional(randrange(-10, 11)), Racional(randrange(-10, 11)), Racional(randrange(-10, 11))
while a==0:
    a, b, c = Racional(randrange(-10, 11)), Racional(randrange(-10, 11)), Racional(randrange(-10, 11))

#================================Aquí va el enunciado================================================================
enunciado = "El discriminante de la ecuación "+ Matematica(ecuacion_azar(Term(a,{"x":2}), b*"x", c)) +" es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(b**2-4*a*c)
contenido_2 = Matematica(b-4*a*c)
contenido_3 = Matematica(b**2)
contenido_4 = Matematica(b**2+4*a*c)
contenido_5 = Matematica(-b**2-4*a*c)

enunciado_oculto = [a, b, c]










