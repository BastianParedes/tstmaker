{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, h = Racional(elegir(-5,6,0)), Racional(elegir(-10,11))
b, c = -2*a*h, a*h**2

#================================Aquí va el enunciado================================================================
enunciado = "Sea la ecuación "+ Matematica(ecuacion_azar(a*{"x":2}, b*"x", c)) +f". El valor de x es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(h)
contenido_2 = Matematica(2*h)
contenido_3 = Matematica(h/2)
contenido_4 = Matematica(-h)
contenido_5 = Matematica(-2*h)




enunciado_oculto = [a,b,c]










