{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b, c, d, e, f = Racional(randrange(2,4)), Racional(elegir(-5,6, 0)), Racional(elegir(-5,6)), Racional(elegir(-5,6, 0)), Racional(elegir(-5,6, 0)), Racional(randrange(0,4))
while b/d==c/e or b-d==0 or b-d*f==0 or b+d==0 or b*d==0:
    a, b, c, d, e, f = Racional(randrange(2,4)), Racional(elegir(-5,6, 0)), Racional(elegir(-5,6)), Racional(elegir(-5,6, 0)), Racional(elegir(-5,6, 0)), Racional(randrange(0,4))

#================================Aquí va el enunciado================================================================
enunciado = "El valor de x que satisface la ecuación "+Matematica(choice([
    fraccion(potencia(a,Pol(b*"x",c,azar=True)),potencia(a,Pol(d*"x",e,azar=True)))+"="+choice([a**f, potencia(a,f,quitar_1=True)]),
    choice([a**f, potencia(a,f,quitar_1=True)])+"="+fraccion(potencia(a,Pol(b*"x",c,azar=True)),potencia(a,Pol(d*"x",e,azar=True)))
        ]))+" es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica((f+e-c)/(b-d))
contenido_2 =        Matematica((f-c/e)/(b/d))
contenido_3 =        Matematica((e*f-c)/(b-d*f))
contenido_4 =        Matematica((f+e+c)/(b+d))
contenido_5 =        Matematica((f-c*e)/(b*d))



enunciado_oculto = [b, c, d, e, f]











