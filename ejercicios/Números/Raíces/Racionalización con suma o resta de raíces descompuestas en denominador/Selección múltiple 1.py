{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b, c, d, e = Racional(randrange(2, 10)), Racional(randrange(1, 10)), Racional(randrange(1, 10)), Racional(elegir(-10,10,0)), Racional(elegir(-10,10,0))
while (type(Root(b))==Racional and type(Root(c))==Racional) or d**2*b-e**2*c==0 or d**2*b**2-e**2*c**2==0 or d**2*b+e**2*c==0 or (a%d==0 and a%e==0):
    a, b, c, d, e = Racional(randrange(2, 10)), Racional(randrange(1, 10)), Racional(randrange(1, 10)), Racional(elegir(-10,10,0)), Racional(elegir(-10,10,0))

#================================Aquí va el enunciado================================================================
enunciado = Matematica(a/(Pol(d*Root(b), e*Root(c),azar=True))+"=")

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(Pol(a*d*Root(b),-a*e*Root(c)) / (d**2*b-e**2*c))
contenido_2 =        Matematica(Pol(a*d*Root(b),-a*e*Root(c)) / (d**2*b**2-e**2*c**2))
contenido_3 =        Matematica(Pol(a*d*Root(b), a*e*Root(c)) / (d**2*b-e**2*c))
contenido_4 =        Matematica(Pol(a*d*Root(b), a*e*Root(c)) / (d**2*b**2-e**2*c**2))
contenido_5 =        Matematica(Pol(a*d*Root(b) ,a*e*Root(c)) / (d**2*b+e**2*c))


enunciado_oculto=[b,c,d,e]










