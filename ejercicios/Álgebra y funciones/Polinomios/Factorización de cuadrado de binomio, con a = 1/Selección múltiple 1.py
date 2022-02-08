{"cantidad_opciones":1, "cantidad_disponible":50}

#===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
b = Racional(elegir(-15, 16, 0))

#===============================================Aquí va el número del ejercicio b el enunciado.
enunciado = "La factorización de " + Matematica(Pol({"x":2}, 2*b*"x", b**2, azar=True)) + " es"

#===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
contenido_correcto = Matematica(potencia(Pol("x", b), 2))
contenido_2 = Matematica(potencia(Pol({"x":2}, b**2), 2))
contenido_3 = Matematica("("+ Pol({"x":2}, b**2) +")")
contenido_4 = Matematica("("+ Pol({"x":2}, 2*b) + ")(" + Pol({"x":2}, b**2) + ")")
contenido_5 = Matematica("("+ Pol({"x":2}, b) + ")(" + Pol({"x":2}, -b) + ")")

enunciado_oculto = enunciado










