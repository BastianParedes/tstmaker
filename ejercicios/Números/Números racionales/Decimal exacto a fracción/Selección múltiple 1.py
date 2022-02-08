{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b = elegir(1, 1000), choice([10, 100, 1000])
n = Racional(a, b, True)
while n.parte_decimal_no_periodica=="" or n.parte_decimal_periodica!="" or a%10==0:
    a, b = elegir(1, 1000), choice([10, 100, 1000])
    n = Racional(a, b, True)

#================================Aquí va el enunciado================================================================
enunciado = "La forma fraccionaria de "+Matematica(n)+" es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(Racional(a,b))
contenido_2 = Matematica(fraccion(int(n.show.replace(",","")), n))
contenido_3 = Matematica(Racional(a, int(str(b).replace("0","9").replace("1","9"))))
contenido_4 = Matematica(Racional(a, int(str(b).replace("1","9"))))
contenido_5 = Matematica(fraccion(n.parte_entera, n.parte_decimal_no_periodica))



enunciado_oculto = n










