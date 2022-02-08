{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b, c, d, e = Racional(randrange(2,6)), Racional(elegir(-5,6, 0)), Racional(randrange(-5,6)), Racional(elegir(-5,6, 0)), Racional(randrange(-5,6))
while b-d==0 or b+d==0 or b*d==0 or b**d==0:
    a, b, c, d, e = Racional(randrange(2,6)), Racional(elegir(-5,6, 0)), Racional(randrange(-5,6)), Racional(elegir(-5,6, 0)), Racional(randrange(-5,6))
#================================Aquí va el enunciado================================================================
enunciado = "El valor de x que satisface la ecuación "+Matematica(choice([
    potencia(a,Pol(b*"x",c,azar=True))+"="+potencia(a,Pol(d*"x",e,azar=True)),
    potencia(a,Pol(d*"x",e,azar=True))+"="+potencia(a,Pol(b*"x",c,azar=True))
        ]))+" es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica((e-c)/(b-d))
contenido_2 =        Matematica((e+c)/(b+d))
contenido_3 =        Matematica((e*c)/(b*d))
contenido_4 =        Matematica((e-c)/(b+d))
contenido_5 =        Matematica((e+c)/(b**d))



enunciado_oculto = [b,c,d,e]











