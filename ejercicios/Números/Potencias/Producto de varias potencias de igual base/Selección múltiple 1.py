{"cantidad_opciones":1, "cantidad_disponible":50}

#===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
a, b, c, d, e= randrange(2, 10), randrange(2, 10), randrange(2, 10), randrange(2, 10), randrange(3, 10)
while b==c==d==e:
    a, b, c, d, e= randrange(2, 10), randrange(2, 10), randrange(2, 10), randrange(2, 10), randrange(3, 10)

#===============================================Aquí va el número del ejercicio y el enunciado.
enunciado = Matematica(potencia(a, b) +por()+potencia(a, c) +por()+potencia(a, d) +por()+ potencia(a, e) + "=")

#===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
contenido_correcto = Matematica(potencia(a, b+c+d+e, quitar_1=True))
contenido_2 = Matematica(potencia(a, b*c*d*e, quitar_1=True))
contenido_3 = Matematica(potencia(4*a, b*c*d*e, quitar_1=True))
contenido_4 = Matematica(potencia(2*a, b+c+d+e, quitar_1=True))
contenido_5 = Matematica(potencia(a**4, b*c*d*e, quitar_1=True))

enunciado_oculto = [a, b, c, d, e]










