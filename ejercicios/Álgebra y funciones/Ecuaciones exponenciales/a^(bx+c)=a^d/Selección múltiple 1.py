{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b, c, d = Racional(randrange(2,6)), Racional(elegir(-5,6, 0,)), Racional(randrange(-5,6)), Racional(randrange(1, 3))

#================================Aquí va el enunciado================================================================
enunciado = "El valor de x que satisface la ecuación "+Matematica(choice([
    potencia(a,Pol(b*"x",c,azar=True))+"="+choice([a**d,potencia(a,d,quitar_1=True)]),
    choice([a**d,potencia(a,d,quitar_1=True)])+"="+potencia(a,Pol(b*"x",c,azar=True))
        ]))+" es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica((d-c)/b)
contenido_2 =        Matematica((a**d-c)/b)
contenido_3 =        Matematica((1-c)/b)
contenido_4 =        Matematica(-c/b)
contenido_5 =        Matematica((d+c)/b)



enunciado_oculto = [b,c,d]










