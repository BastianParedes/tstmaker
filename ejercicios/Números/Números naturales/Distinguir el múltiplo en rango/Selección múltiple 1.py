{"cantidad_opciones":1, "cantidad_disponible":50}

#===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
a=randrange(4, 11)
d=randrange(2, 11)

#===============================================Aquí va el número del ejercicio y el enunciado.
enunciado = f"El número que es mútliplo de {d}, mayor que {a*d-d+3} y menor que {a*d+d-1} es"

#===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
contenido_correcto = Matematica(a*d)
contenido_2 = Matematica(a*d+1)
contenido_3 = Matematica(a*d-1)
contenido_4 = Matematica(1)
contenido_5 = Matematica(a*d+2)

enunciado_oculto = [a, d]










