{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b, c = Racional(randrange(2, 13)), Racional(randrange(3, 13)), Racional(randrange(3, 13))
while not a!=b!=c!=a:
    a, b, c = Racional(randrange(2, 13)), Racional(randrange(3, 13)), Racional(randrange(3, 13))

#================================Aquí va el enunciado================================================================
enunciado = Matematica(fraccion(logaritmo(a, c), logaritmo(b, c))+"=")

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(logaritmo(a, b))
contenido_2 = Matematica(logaritmo(a/b, c))
contenido_3 = Matematica(logaritmo(a,c))
contenido_4 = Matematica(logaritmo(a/b, 1))
contenido_5 = Matematica(logaritmo(b,a))

enunciado_oculto = [a, b, c]










