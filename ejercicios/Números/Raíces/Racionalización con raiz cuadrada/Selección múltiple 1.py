{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b = Racional(randrange(1, 10)), Racional(randrange(2, 60))
while type(Root(b))==Racional:
    a, b = Racional(randrange(1, 10)), Racional(randrange(2, 60))

#================================Aquí va el enunciado================================================================
enunciado = Matematica(fraccion(a,Root(b))+"=")

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(a*Root(b)/b)
contenido_2 = Matematica(a/b)
contenido_3 = Matematica(a*Root(b))
contenido_4 = Matematica(Root(b)/a)
contenido_5 = Matematica(Root(a*b)/(a*b))

enunciado_oculto = b










