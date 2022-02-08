{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b = Natural(randrange(1000, 10000)), Natural(randrange(10, 100))

#================================Aquí va el enunciado================================================================
enunciado = Matematica(a+por()+b+"=")

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = a*b



#Sin dejar espacio
contenido_2 = 0
for digito in str(b):
    contenido_2 += a.numero*int(digito)



#Sin reserva y sin dejar espacio
contenido_3 = 0
for posicion_del_digito_de_b in range(b.cantidad_de_digitos-1, -1, -1):
    resultado_provisional = ""
    for posicion_del_digito_de_a in range(a.cantidad_de_digitos-1, -1, -1):
        resultado_provisional = str(int(str(a)[posicion_del_digito_de_a])*int(str(b)[posicion_del_digito_de_b]))[-1] + resultado_provisional
    contenido_3 += int(resultado_provisional)



#Sin reserva
contenido_4 = 0
posicion = 0
for posicion_del_digito_de_b in range(b.cantidad_de_digitos-1, -1, -1):
    resultado_provisional = ""
    for posicion_del_digito_de_a in range(a.cantidad_de_digitos-1, -1, -1):
        resultado_provisional = str(int(str(a)[posicion_del_digito_de_a])*int(str(b)[posicion_del_digito_de_b]))[-1] + resultado_provisional
    contenido_4 += int(resultado_provisional)*10**posicion
    posicion += 1



#Se suman
contenido_5 = a+b




enunciado_oculto = [a,b]










