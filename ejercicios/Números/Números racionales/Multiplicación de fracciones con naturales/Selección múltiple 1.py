{"cantidad_opciones":1, "cantidad_disponible":50}

#===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
f1, f2 = Racional(randrange(2, 21),randrange(2, 21)), Racional(randrange(2, 21),randrange(2, 21))
while f1.denominador==1 or f2.denominador==1:
    f1, f2 = Racional(randrange(2, 21),randrange(2, 21)), Racional(randrange(2, 21),randrange(2, 21))
#===============================================Aquí va el número del ejercicio y el enunciado.
enunciado = Matematica(f1 + por() + f2 + "=")

#===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
contenido_correcto = Matematica(f1*f2)
contenido_2 = Matematica(f1+f2)
contenido_3 = Matematica(abs(f1-f2))
contenido_4 = Matematica(f1/f2)
contenido_5 = Matematica(Racional(f1.numerador+f2.numerador)/Racional(f1.denominador+f2.denominador))

enunciado_oculto = [f1, f2]










