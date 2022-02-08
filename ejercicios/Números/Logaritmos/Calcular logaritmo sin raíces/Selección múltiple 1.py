{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a = Racional(randrange(2, 11))
b = Racional(choice([-1, 1])*randrange(1, 4))
c = Racional(choice([-1, 1])*randrange(1, 4))
while a==1 or b==c or b.signo==c.signo=="+":
    a = Racional(randrange(2, 11))
    b = Racional(choice([-1, 1])*randrange(1, 4))
    c = Racional(choice([-1, 1])*randrange(1, 4))

#================================Aquí va el enunciado================================================================
enunciado = Matematica(logaritmo(a**b, a**c,False)+"=")

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(b/c)
contenido_2 =        Matematica(-b/c)
contenido_3 =        Matematica(c/b)
contenido_4 =        Matematica(-c/b)
contenido_5 =        Matematica(choice([a,b,c]))



enunciado_oculto = [a, b, c]











