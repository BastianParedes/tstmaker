{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b, c = Racional(randrange(2, 13)), Racional(randrange(3, 13)), Racional(randrange(3, 13))

#================================Aquí va el enunciado================================================================
enunciado = Matematica(logaritmo(a,c)+"+"+logaritmo(b, c)+"=")

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(logaritmo(a*b,c))
contenido_2 = Matematica(logaritmo(a+b,c))
contenido_3 = Matematica(logaritmo(a/b,c))
contenido_4 = Matematica(logaritmo(a*b,c**2))
contenido_5 = Matematica(logaritmo(a+b,2*c))

enunciado_oculto = [a, b, c]










