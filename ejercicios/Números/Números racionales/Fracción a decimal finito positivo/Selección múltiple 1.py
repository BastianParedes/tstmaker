{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b = Racional(randrange(2, 100)), Racional(randrange(2, 100))
numero = Racional(a, b, True)
while numero.parte_entera=="0" or numero.parte_decimal_no_periodica=="" or numero.parte_decimal_periodica!="" or numero.parte_entera==numero.parte_decimal_no_periodica:
    a, b = Racional(randrange(2, 100)), Racional(randrange(2, 100))
    numero = Racional(a, b, True)

#================================Aquí va el número del ejercicio y el enunciado======================================
enunciado = Matematica(Racional((a/b).numerador)+":"+Racional((a/b).denominador)+"=")

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.=
contenido_correcto = Matematica(numero)
contenido_2 = Matematica(numero.parte_entera)
contenido_3 = Matematica(numero.parte_entera + "," + linea(numero.parte_decimal_no_periodica, azar=False))
contenido_4 = Matematica(numero.parte_decimal_no_periodica + "," + numero.parte_entera)
contenido_5 = Matematica("0," + numero.parte_decimal_no_periodica)

enunciado_oculto = [a, b]










