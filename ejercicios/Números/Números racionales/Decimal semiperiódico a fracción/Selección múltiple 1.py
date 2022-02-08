{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
p_entera, p_d_n_periodica, p_d_periodica = str(randrange(1, 10)), str(randrange(0, 20)), str(randrange(1, 20))
b = ""
for digito in p_d_periodica:
    b += "9"
for digito in p_d_n_periodica:
    b += "0"
numero = Racional(int(p_entera+p_d_n_periodica+p_d_periodica)-int(p_entera+p_d_n_periodica),int(b),True)
while numero.parte_decimal_no_periodica!=p_d_n_periodica or numero.parte_decimal_periodica!=p_d_periodica:
    p_entera, p_d_n_periodica, p_d_periodica = str(randrange(1, 10)), str(randrange(0, 20)), str(randrange(1, 20))
    b = ""
    for digito in p_d_periodica:
        b += "9"
    for digito in p_d_n_periodica:
        b += "0"
    numero = Racional(int(p_entera+p_d_n_periodica+p_d_periodica)-int(p_entera+p_d_n_periodica),int(b),True)

b2 = "9"
for digito in p_d_n_periodica:
    b2 += "0"
for digito in p_d_periodica:
    b2 += "0"

b3 = "1"
for digito in p_d_periodica:
    b3 += "0"
for digito in p_d_n_periodica:
    b3 += "0"

#================================Aquí va el enunciado================================================================
enunciado = f"La forma fraccionaria de " + Matematica(numero) + " es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(Racional(int(p_entera+p_d_n_periodica+p_d_periodica)-int(p_entera+p_d_n_periodica), b))
contenido_2        = Matematica(fraccion(int(p_entera+p_d_n_periodica+p_d_periodica)-int(p_entera+p_d_n_periodica), b2))
contenido_3        = Matematica(fraccion(int(p_entera+p_d_n_periodica+p_d_periodica)-int(p_entera+p_d_n_periodica), b3))
contenido_4        = Matematica(fraccion(int(p_entera+p_d_n_periodica+p_d_periodica)-int(p_entera), b))
contenido_5        = Matematica(fraccion(int(p_entera+p_d_n_periodica+p_d_periodica)-int(p_entera), b3))

enunciado_oculto = numero










