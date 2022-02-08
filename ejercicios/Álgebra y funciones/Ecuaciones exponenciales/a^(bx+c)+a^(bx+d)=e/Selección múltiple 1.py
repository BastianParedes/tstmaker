{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b, c, d, x = Racional(randrange(2,6)),  Racional(elegir(1,6, 2)), Racional(randrange(0,6)), Racional(randrange(0,6)), Racional(randrange(0,4))
e = a**(b*x+c)+a**(b*x+d)
while not e<=1000:
    a, b, c, d, x = Racional(randrange(2,6)),  Racional(elegir(1,6, 2)), Racional(randrange(0,6)), Racional(randrange(0,6)), Racional(randrange(0,4))
    e = a**(b*x+c)+a**(b*x+d)
#================================Aquí va el enunciado================================================================
enunciado = "El valor de x que satisface la ecuación "+Matematica(choice([
    Pol(potencia(a,Pol(b*"x",c)), potencia(a,Pol(b*"x",d)),azar=True)+"="+e,
    e+"="+Pol(potencia(a,Pol(b*"x",c)), potencia(a,Pol(b*"x",d)),azar=True)
        ]))+" es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(x)
contenido_2 =        Matematica((e-c-d)/b)
contenido_3 =        Matematica((e-c-d)/(2*b))
contenido_4 =        Matematica((e-c-d)/(b**2))
contenido_5 =        Matematica(Root(e-c-d,b))



enunciado_oculto = [b, c, d, x]










