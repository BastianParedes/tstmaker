{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
z = Complex(randrange(-15, 16), choice(list(range(-15, 0))+list(range(1, 15))))

#================================Aquí va el enunciado================================================================
enunciado = "Considera i como la unida imaginaria. "+Matematica("|"+z+"|=")

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(abs(z))
contenido_2 = Matematica((z.re**2+z.im**2))
contenido_3 = Matematica((z.re+z.im))

if Racional(z.re**2-z.im**2).numerador<0:
    contenido_4 = Matematica(raiz(Racional(z.re**2-z.im**2)))
else:
    contenido_4 = Matematica(Root(z.re**2-z.im**2))


if Racional(z.re-z.im).numerador<0:
    contenido_5 = Matematica(raiz(z.re-z.im))
else:
    contenido_5 = Matematica(z.re-z.im)

enunciado_oculto = z










