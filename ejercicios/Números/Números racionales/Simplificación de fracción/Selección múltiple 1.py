{"cantidad_opciones":1, "cantidad_disponible":50}

#===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
a = choice([2, 3, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20])
b = choice([2, 3, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20])
while b<=a:
    a = choice([2, 3, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20])
    b = choice([2, 3, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20])
c = choice([2, 3, 5, 6, 8, 9, 10])
a = a*c
b = b*c

#===============================================Aquí va el número del ejercicio y el enunciado.
enunciado = "Al simplificar la fracción " + Matematica(fraccion(a, b)) + " se obtiene"

#===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
contenido_correcto = Matematica(Racional(a, b))
contenido_2 = Matematica(fraccion(a, b))
contenido_3 = Matematica(Racional(b, a))
contenido_4 = Matematica(a)
contenido_5 = Matematica(fraccion(a*c, b*c))

enunciado_oculto = [a, b]










