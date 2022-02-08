{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
numerador, denominador = Racional(randrange(1, 6)), Racional(randrange(1, 6))
while numerador==denominador:
    numerador, denominador = Racional(randrange(1, 6)), Racional(randrange(1, 6))
exponente = Racional(randrange(-5, 0))

#================================Aquí va el enunciado================================================================
enunciado = Matematica(potencia(numerador/denominador,exponente)+"=")

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica((numerador/denominador)**exponente)
contenido_2 = Matematica((numerador/denominador)**(-exponente))
contenido_3 = Matematica(-(numerador/denominador)**exponente)
contenido_4 = Matematica(-(numerador/denominador)**(-exponente))
contenido_5 = Matematica((numerador/denominador)**(1/exponente))

enunciado_oculto = [numerador, denominador, exponente]










