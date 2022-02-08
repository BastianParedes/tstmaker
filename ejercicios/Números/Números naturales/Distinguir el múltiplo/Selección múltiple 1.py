{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
x = Racional(elegir(2, 13))

#================================Aquí va el enunciado================================================================
enunciado = f"Un múltiplo de {Matematica(x)} es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(x*randrange(1, 15))
contenido_2 = Matematica(x*randrange(1, 16)+choice([-1,1]))
contenido_3 = Matematica(x*randrange(1, 16)+choice([-1,1]))
contenido_4 = Matematica(x*randrange(1, 16)+choice([-1,1]))
contenido_5 = Matematica(x*randrange(1, 16)+choice([-1,1]))

enunciado_oculto = [x, contenido_correcto]










