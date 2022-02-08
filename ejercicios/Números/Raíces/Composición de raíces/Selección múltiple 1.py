{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, x = Racional(randrange(3, 13)), Racional(elegir(2, 12, 4, 9))

#================================Aquí va el enunciado================================================================
enunciado = Matematica(a*Root(x)+"=")

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(raiz(a**2*x))
contenido_2 = Matematica(raiz(a*x))
contenido_3 = Matematica(raiz(a*x**2))
contenido_4 = Matematica(raiz(a**2*x**2))
contenido_5 = Matematica(a*x)



enunciado_oculto = [a, x]










