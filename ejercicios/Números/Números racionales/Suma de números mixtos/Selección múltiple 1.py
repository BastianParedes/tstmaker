{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
fraccion_1 = Racional(randrange(3, 100), randrange(2, 10))
while fraccion_1<1 or fraccion_1.denominador==1:
    fraccion_1 = Racional(randrange(10, 100), randrange(1, 100))
n_1 = fraccion_1.numerador
d_1 = fraccion_1.denominador
p_1 = int(fraccion_1.parte_entera)
r_1 = fraccion_1.resto
fraccion_2 = Racional(randrange(3, 100), randrange(2, 10))
while fraccion_2<1 or fraccion_2.denominador==1:
    fraccion_2 = Racional(randrange(10, 100), randrange(1, 100))
n_2 = fraccion_2.numerador
d_2 = fraccion_2.denominador
p_2 = int(fraccion_2.parte_entera)
r_2 = fraccion_2.resto
while fraccion_1 - fraccion_2<=1:
    fraccion_1 = Racional(randrange(3, 100), randrange(2, 10))
    while fraccion_1<1 or fraccion_1.denominador==1:
        fraccion_1 = Racional(randrange(10, 100), randrange(1, 100))
    n_1 = fraccion_1.numerador
    d_1 = fraccion_1.denominador
    p_1 = int(fraccion_1.parte_entera)
    r_1 = fraccion_1.resto
    fraccion_2 = Racional(randrange(3, 100), randrange(2, 10))
    while fraccion_2<1 or fraccion_2.denominador==1:
        fraccion_2 = Racional(randrange(10, 100), randrange(1, 100))
    n_2 = fraccion_2.numerador
    d_2 = fraccion_2.denominador
    p_2 = int(fraccion_2.parte_entera)
    r_2 = fraccion_2.resto

#================================Aquí va el enunciado================================================================
enunciado = Matematica(fraccion_1.show_mixto+"+"+fraccion_2.show_mixto+"=")

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica((fraccion_1+fraccion_2).show_mixto)
contenido_2 = Matematica((abs(fraccion_1-fraccion_2)).show_mixto)
contenido_3 = Matematica((int(p_1)+Racional(r_2,d_2)).show_mixto)
contenido_4 = Matematica((int(p_2)+Racional(r_1,d_1)).show_mixto)
contenido_5 = Matematica((fraccion_1*fraccion_2).show_mixto)




enunciado_oculto = [fraccion_1, fraccion_2]











