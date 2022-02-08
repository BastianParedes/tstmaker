{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b = randrange(1, 13), choice(list(range(2, 7))+list(range(8, 13)))
while a%b==0:
    a, b = randrange(1, 13), choice(list(range(2, 7))+list(range(8, 13)))
exponente = Racional(-a, b, True)

#================================Aquí va el enunciado================================================================
enunciado = Matematica(potencia("x",exponente)+"=")

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(choice([fraccion(1,"x")**(-exponente), "x"**exponente]))
contenido_2 = Matematica(fraccion(1,"x")**exponente)
contenido_3 = Matematica("x"**(exponente**(-1)))
contenido_4 = Matematica("-x"**(-exponente))
contenido_5 = Matematica("-"+"x"**(-exponente))

enunciado_oculto = [a, b]










