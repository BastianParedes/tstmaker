{"cantidad_opciones":2, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b, c = Racional(randrange(2, 10)), Racional(randrange(1, 10)), Racional(randrange(1, 10))
while (type(Root(b))==Racional and type(Root(c))==Racional) or b==c:
    a, b, c = Racional(randrange(2, 10)), Racional(randrange(1, 10)), Racional(randrange(1, 10))

if opcion==1:
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(a/(Pol(Root(b), Root(c)))+"=")

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(a*Pol(Root(b), Racional(-1)*Root(c)) / (b-c))
    contenido_2 = Matematica(a*Pol(Root(b), Root(c)) / (b+c))
    contenido_3 = Matematica(a*Pol(Root(b), Root(c)) / (b-c))
    contenido_4 = Matematica(a*Pol(Root(b), Racional(-1)*Root(c)) / (b+c))
    contenido_5 = Matematica(a*Root(abs(b-c)) / (b+c))

elif opcion==2:
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(a/(Pol(Root(b), Racional(-1)*Root(c)))+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(a*Pol(Root(b), Root(c)) / (b-c))
    contenido_2 = Matematica(a*Pol(Root(b), Racional(-1)*Root(c)) / (b+c))
    contenido_3 = Matematica(a*Pol(Root(b), Racional(-1)*Root(c)) / (b-c))
    contenido_4 = Matematica(a*Pol(Root(b), Root(c)) / (b+c))
    contenido_5 = Matematica(a*Root(b+c) / (b-c))


enunciado_oculto=[b,c,opcion]










