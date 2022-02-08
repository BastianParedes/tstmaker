{"cantidad_opciones":1, "cantidad_disponible":50}

#===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
a, b, c, d = choice([3, 7, 11, 13, 20]), choice([3, 7, 11, 13, 20]), choice([3, 7, 11, 13, 20]), choice([3, 7, 11, 13, 20])

#===============================================Aquí va el número del ejercicio y el enunciado.
enunciado = Matematica(potencia(a, b) +por()+ potencia(a, c) + "=")

#===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
contenido_correcto = Matematica(potencia(a, b+c, quitar_1=True))
contenido_2 = Matematica(potencia(a, b*c, quitar_1=True))
contenido_3 = Matematica(potencia(2*a, b*c, quitar_1=True))
contenido_4 = Matematica(potencia(2*a, b+c, quitar_1=True))
contenido_5 = Matematica(potencia(a**2, b*c, quitar_1=True))

enunciado_oculto = [a, b, c, d]










