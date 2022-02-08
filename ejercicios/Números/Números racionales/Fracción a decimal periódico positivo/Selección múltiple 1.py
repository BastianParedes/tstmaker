{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b = Racional(randrange(2, 201)), Racional(choice([9, 99]))
numero = Racional(a, b, True)
while numero.parte_entera=="0" or numero.parte_decimal_no_periodica!="" or not 1<=len(numero.parte_decimal_periodica)<=2:
    a, b = Racional(randrange(2, 10000)), Racional(choice([9, 99]))
    numero = Racional(a, b, True)

#================================Aquí va el número del ejercicio y el enunciado======================================
enunciado = Matematica(Racional((a/b).numerador)+":"+Racional((a/b).denominador)+"=")

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.=
contenido_correcto = Matematica(numero)
contenido_2 = Matematica(numero.parte_entera + "," + numero.parte_decimal_periodica)
contenido_3 = Matematica(numero.parte_decimal_periodica)
contenido_4 = Matematica(numero.parte_decimal_periodica + "," + numero.parte_entera)
contenido_5 = Matematica("0," + linea(numero.parte_decimal_periodica, azar=False))

enunciado_oculto = [a, b]










