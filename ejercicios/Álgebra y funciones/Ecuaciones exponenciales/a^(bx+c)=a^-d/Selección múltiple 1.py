{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b, c, d = Racional(randrange(1,6),randrange(2,6)),  Racional(elegir(-4,5, 0)), Racional(randrange(-4,5)), Racional(randrange(1,5))
while a.denominador==1:
    a = Racional(randrange(1,6),randrange(2,6))
#================================Aquí va el enunciado================================================================
enunciado = "El valor de x que satisface la ecuación "+Matematica(choice([
    potencia(a,Pol(b*"x",c))+"="+a**(-d),
    a**(-d)+"="+potencia(a,Pol(b*"x",c))
        ]))+" es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica((-c-d)/b)
contenido_2 =        Matematica((-c+d)/b)
contenido_3 =        Matematica(-c/b)
contenido_4 =        Matematica(c/b)
contenido_5 =        Matematica((a**d-c)/b)



enunciado_oculto = [a, b, c, d]










