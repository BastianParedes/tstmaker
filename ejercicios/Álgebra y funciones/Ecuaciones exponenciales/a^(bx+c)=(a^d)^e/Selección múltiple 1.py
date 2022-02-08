{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b, c, d, e = Racional(elegir(2,5)), Racional(elegir(-4,5, 0,2)), Racional(elegir(-4,5)), Racional(elegir(2,5)), Racional(elegir(2,5))

#================================Aquí va el enunciado================================================================
enunciado = enunciado = "El valor de x que satisface la ecuación "+Matematica(choice([
    potencia(a,Pol(b*"x",c,azar=True))+"="+potencia(a**d,e,quitar_1=True),
    potencia(a**d,e,quitar_1=True)+"="+potencia(a,Pol(b*"x",c,azar=True))
        ]))+" es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica((d*e-c)/b)
contenido_2 =        Matematica((d**e-c)/b)
contenido_3 =        Matematica((d+e-c)/b)
contenido_4 =        Matematica((e-c)/b)
contenido_5 =        Matematica((d*e+c)/b)



enunciado_oculto = [a,b,c,d,e]










