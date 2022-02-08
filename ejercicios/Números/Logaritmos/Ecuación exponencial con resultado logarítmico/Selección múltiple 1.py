{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
b1,b2 = Racional(randrange(2,7)), Racional(randrange(2,7))
e1, e2 = Racional(randrange(1,7)), Racional(randrange(1,7))
while isinstance(Log(b1,b2).valor, Racional):
    b1,b2 = Racional(randrange(2,7)), Racional(randrange(2,7))
    e1, e2 = Racional(randrange(1,7)), Racional(randrange(1,7))
letra = choice(["x", "y", "z"])

#================================Aquí va el enunciado================================================================
enunciado = f"Considera la ecuación {Matematica(ecuacion_azar(potencia(b1,e1,quitar_1=True), Racional(-1)*potencia(b2,Pol(letra,e2,azar=True))))}. De las siguientes alternativas, la que no contiene el valor de {letra} que satisface a la ecuación dada es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(Pol(Log(e1,b1),-Log(e2,b2)))
contenido_2 =        Matematica(Fraction(Pol(Log(b1,10,e1),-Log(b2,10,e2)), Log(b2)))
contenido_3 =        Matematica(Pol(Fraction(Log(b1,10,e1),Log(b2)), -e2))
contenido_4 =        Matematica(Pol(Log(b1,b2,e1), -e2))
contenido_5 =        Matematica(Log(b1**e1/b2**e2, b2))



enunciado_oculto = [b1,b2,e1,e2]











