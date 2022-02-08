{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b, x = Racional(randrange(2,10)), Racional(randrange(-20, 21)), Racional(randrange(0, 20))
while a*x+b<0:
    a, b, x = Racional(randrange(2,10)), Racional(randrange(-20, 21)), Racional(randrange(0, 20))

#================================Aquí va el enunciado================================================================
enunciado = "El valor de x que satisface la ecuación "+Matematica(choice([
    Pol(a*"x",b) +"="+ (a*x+b),
    (a*x+b) +"="+ Pol(a*"x",b)
    ]))+" es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(x)
contenido_2 = Matematica(a*x+b)
contenido_3 = Matematica(abs(a+b))
contenido_4 = Matematica(abs(a-b))
contenido_5 = Matematica(abs(a*b))

enunciado_oculto = [a, b, x]










