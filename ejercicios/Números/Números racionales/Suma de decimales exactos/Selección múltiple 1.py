{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b = Racional(randrange(1, 10000), choice([10, 100, 1000]),True), Racional(randrange(1, 10000), choice([10, 100, 1000]), True)
while a.parte_decimal_no_periodica=="" or b.parte_decimal_no_periodica=="":
    a, b = Racional(randrange(1, 10000), choice([10, 100, 1000]),True), Racional(randrange(1, 10000), choice([10, 100, 1000]), True)

#================================Aquí va el enunciado================================================================
enunciado = Matematica(a+"+"+b+"=")

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(Racional(a+b, cargar_decimal=True))
contenido_2 = Matematica(int(a.show.replace(",",""))+int(b.show.replace(",","")))
contenido_3 = Matematica(Racional(abs(a-b), cargar_decimal=True))
contenido_4 = Matematica(Racional(int(a)+b, cargar_decimal=True))
contenido_5 = Matematica(Racional(a+int(b), cargar_decimal=True))

enunciado_oculto = [a,b]










