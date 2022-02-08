{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, x = Racional(randrange(2, 13)), Racional(choice([2, 3, 5, 6, 7, 8, 10, 11]))

#================================Aquí va el enunciado================================================================
enunciado = Matematica(raiz(a**2*x)+"=")

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(a*raiz(x))
contenido_2 = Matematica(a**2*x)
contenido_3 = Matematica(raiz(a*x))
contenido_4 = Matematica(a*x)
contenido_5 = Matematica(x*raiz(a))


enunciado_oculto = enunciado










