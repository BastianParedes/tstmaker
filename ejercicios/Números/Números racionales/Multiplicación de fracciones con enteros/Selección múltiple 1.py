{"cantidad_opciones":1, "cantidad_disponible":50}

#===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
a, b, c, d = Racional(choice(list(range(-15,0))+list(range(2, 16)))), Racional(choice(list(range(-15,0))+list(range(2, 16)))), Racional(choice(list(range(-15,0))+list(range(2, 16)))), Racional(choice(list(range(-15,0))+list(range(2, 16))))
while 0<a and 0<b and 0<c and 0<d or b+d==0:
    a, b, c, d = Racional(choice(list(range(-15,0))+list(range(2, 16)))), Racional(choice(list(range(-15,0))+list(range(2, 16)))), Racional(choice(list(range(-15,0))+list(range(2, 16)))), Racional(choice(list(range(-15,0))+list(range(2, 16))))
f1 = a/b
f2 = c/d
#===============================================Aquí va el número del ejercicio y el enunciado.
enunciado = Matematica(fraccion(a,b) + por() + fraccion(c,d) + "=")

#===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
contenido_correcto = Matematica(f1*f2)
contenido_2 = Matematica(f1+f2)
contenido_3 = Matematica(f1-f2)
contenido_4 = Matematica(f1/f2)
contenido_5 = Matematica((a+c)/(b+d))

enunciado_oculto = [a, b, c, d]










