{"cantidad_opciones":1, "cantidad_disponible":50}

#===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
b = Racional(elegir(-12,13,0))
c = Racional(elegir(-12,13,0))
while abs(b)==abs(c):
    b = Racional(elegir(-12,13,0))
    c = Racional(elegir(-12,13,0))

#===============================================Aquí va el número del ejercicio y el enunciado.
enunciado = "La factorización de " + Matematica(Pol({"x":2}, (b+c)*"x", b*c)) + " es"

#===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
contenido_correcto = Matematica("("+ Pol("x", b) + ")(" + Pol("x", c) + ")")
contenido_2 = Matematica("("+ Pol("x", -b) + ")(" + Pol("x", c) + ")")
contenido_3 = Matematica(potencia(Pol("x", b), 2))
contenido_4 = Matematica("("+ Pol("x", -b) + ")(" + Pol("x",-c) + ")")
contenido_5 = Matematica("("+ Pol({"x": 2},b) + ")(" + Pol({"x":2},c) + ")")

enunciado_oculto = [b, c]










