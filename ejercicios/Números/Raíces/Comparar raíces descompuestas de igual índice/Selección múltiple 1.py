{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b, c, d = Root(elegir(2,10,4,9), 2, elegir(1, 5)), Root(elegir(2,10,4,9), 2, elegir(1, 5)), Root(elegir(2,10,4,9), 2, elegir(1, 5)), Root(elegir(2,10,4,9), 2, elegir(1, 5))
lista_de_raices = [a, b, c, d]
while not lista_de_raices.count(a)==1 or not lista_de_raices.count(b)==1 or not lista_de_raices.count(c)==1 or not lista_de_raices.count(d)==1 or 3<=[a.parte_descompuesta, b.parte_descompuesta, c.parte_descompuesta, d.parte_descompuesta].count(1):
    a, b, c, d = Root(elegir(2,10,4,9), 2, elegir(1, 5)), Root(elegir(2,10,4,9), 2, elegir(1, 5)), Root(elegir(2,10,4,9), 2, elegir(1, 5)), Root(elegir(2,10,4,9), 2, elegir(1, 5))
    lista_de_raices = [a, b, c, d]
primero = {0:"a", 1:"b", 2:"c",3:"d"}[lista_de_raices.index(sorted(lista_de_raices)[0])]
segundo = {0:"a", 1:"b", 2:"c",3:"d"}[lista_de_raices.index(sorted(lista_de_raices)[1])]
tercero = {0:"a", 1:"b", 2:"c",3:"d"}[lista_de_raices.index(sorted(lista_de_raices)[2])]
cuarto = {0:"a", 1:"b", 2:"c",3:"d"}[lista_de_raices.index(sorted(lista_de_raices)[3])]
lista_de_letras = ["a","b","c","d"]
#================================Aquí va el enunciado================================================================
enunciado = "Sean las raíces "+Matematica("a = "+a)+", "+Matematica("b = "+b)+", "+Matematica("c = "+c)+" y "+Matematica("d = "+d)+". ¿Qué alternativa muestra las raíces ordenadas de menor a mayor?"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(primero+"<"+segundo+"<"+tercero+"<"+cuarto)
shuffle(lista_de_letras)
contenido_2 = Matematica(lista_de_letras[0]+"<"+lista_de_letras[1]+"<"+lista_de_letras[2]+"<"+lista_de_letras[3])
shuffle(lista_de_letras)
contenido_3 = Matematica(lista_de_letras[0]+"<"+lista_de_letras[1]+"<"+lista_de_letras[2]+"<"+lista_de_letras[3])
shuffle(lista_de_letras)
contenido_4 = Matematica(lista_de_letras[0]+"<"+lista_de_letras[1]+"<"+lista_de_letras[2]+"<"+lista_de_letras[3])
shuffle(lista_de_letras)
contenido_5 = Matematica(lista_de_letras[0]+"<"+lista_de_letras[1]+"<"+lista_de_letras[2]+"<"+lista_de_letras[3])



enunciado_oculto = [a, b, c, d]










