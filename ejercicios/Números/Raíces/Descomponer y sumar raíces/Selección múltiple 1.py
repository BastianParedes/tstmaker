{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b, c, d, e, f = Racional(elegir(1,6)), Racional(elegir(1,6)), Racional(elegir(1,6)), Racional(elegir(1,6)), Racional(elegir(1,6)), Racional(elegir(1,6))
g, h = Racional(elegir(2,11,4,9)), Racional(elegir(2,11,4,9))

while 4<=[a,b,c,d,e,f].count(1):
    a, b, c, d, e, f = Racional(elegir(1,6)), Racional(elegir(1,6)), Racional(elegir(1,6)), Racional(elegir(1,6)), Racional(elegir(1,6)), Racional(elegir(1,6))
while g==h:
    g, h = Racional(elegir(2,11,4,9)), Racional(elegir(2,11,4,9))
cantidad_a_quitar = choice([0,1,2,3])
lista_de_partes_descompuestas = [Racional(elegir(-5,6,0)), Racional(elegir(-5,6,0)), Racional(elegir(-5,6,0)), Racional(elegir(-5,6,0)), Racional(elegir(-5,6,0)), Racional(elegir(-5,6,0))]
while not lista_de_partes_descompuestas.count(0)==cantidad_a_quitar:
    lista_de_partes_descompuestas[lista_de_partes_descompuestas.index(choice(lista_de_partes_descompuestas))] = Racional(0)
a2, b2, c2, d2, e2, f2 = lista_de_partes_descompuestas[0], lista_de_partes_descompuestas[1], lista_de_partes_descompuestas[2], lista_de_partes_descompuestas[3], lista_de_partes_descompuestas[4], lista_de_partes_descompuestas[5]

#================================Aquí va el enunciado================================================================
enunciado = Matematica(Pol(a2*raiz(a**2*g), b2*raiz(b**2*g), c2*raiz(c**2*g), d2*raiz(d**2*h), e2*raiz(e**2*h), f2*raiz(f**2*h), azar=True)+"=")

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(Pol((a2*a+b2*b+c2*c)*raiz(g), (d2*d+e2*e+f2*f)*raiz(h), azar=True))
contenido_2 = Matematica(Pol((a2*a**2+b2*b**2+c2*c**2)*raiz(g), (d2*d**2+e2*e**2+f2*f**2)*raiz(h), azar=True))
contenido_3 = Matematica(Pol((a+b+c)*raiz(g), (d+e+f)*raiz(h), azar=True))
contenido_4 = Matematica(Pol((a2+b2+c2)*raiz(g), (d2+e2+f2)*raiz(h), azar=True))
contenido_5 = Matematica(Pol(raiz(g), raiz(h), azar=True))



enunciado_oculto = [a, b, c, d, e, f, g, h, a2, b2, c2, d2, e2, f2]










