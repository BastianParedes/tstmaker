{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a = Racional(randrange(1, 101), choice([9, 99]), True)
while a.parte_decimal_no_periodica!="" and a.parte_decimal_periodica=="":
    a = Racional(randrange(1, 101), choice([9, 99]), True)
#================================Aquí va el enunciado================================================================
enunciado = Matematica(a+"=")

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(Racional(a))
contenido_2 = Matematica(Racional(a.parte_entera+"."+a.parte_decimal_periodica))
contenido_3 = Matematica(a**(-1))
contenido_4 = Matematica(Racional(a.parte_entera+"."+a.parte_decimal_periodica)**(-1))
contenido_5 = Matematica(a/10)



enunciado_oculto = enunciado










