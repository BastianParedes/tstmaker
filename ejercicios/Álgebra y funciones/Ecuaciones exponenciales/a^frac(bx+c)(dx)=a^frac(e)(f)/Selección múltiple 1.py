{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b, c, d, e, f = Racional(randrange(2,6)),  Racional(elegir(-5,6, 0)), Racional(elegir(-4,5, 0)), Racional(elegir(-5,6, 0)), Racional(randrange(0,4)), Racional(randrange(1,5))
while b*f-d*e==0 or b+d==0:
    a, b, c, d, e, f = Racional(randrange(2,6)),  Racional(elegir(-5,6, 0)), Racional(elegir(-4,5, 0)), Racional(elegir(-5,6, 0)), Racional(randrange(0,4)), Racional(randrange(1,5))

#================================Aquí va el enunciado================================================================
enunciado = "El valor de x que satisface la ecuación "+Matematica(choice([
    raiz(potencia(a,Pol(b*"x",c)),d*"x")+"="+Root(a**e,f,descomponer=choice([True,False])),
    Root(a**e,f,descomponer=choice([True,False]))+"="+raiz(potencia(a,Pol(b*"x",c)),d*"x")
        ]))+" es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(-c*f/(b*f-d*e))
contenido_2 =        Matematica((b+c)/d)
contenido_3 =        Matematica(e/f)
contenido_4 =        Matematica((d*e/f-c)/b)
contenido_5 =        Matematica((e+f-c)/(b+d))



enunciado_oculto = [b,c,d,e,f]











