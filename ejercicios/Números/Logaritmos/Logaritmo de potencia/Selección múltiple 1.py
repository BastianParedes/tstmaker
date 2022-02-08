{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b, c = Racional(randrange(2, 13)), Racional(randrange(3, 13)), Racional(randrange(3, 13))
while a==b or b==-1 or b==0 or b==1:
    a, b, c = Racional(randrange(2, 13)), Racional(randrange(3, 13)), Racional(randrange(3, 13))

#================================Aquí va el enunciado================================================================
enunciado = Matematica(logaritmo(potencia(a,b),c,False)+"=")

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(b+por()+logaritmo(a,c))
contenido_2 = Matematica(logaritmo(a, potencia(c,b)))
contenido_3 = Matematica(potencia(logaritmo(a,c),b))
contenido_4 = Matematica(fraccion(logaritmo(a,c),b))
contenido_5 = Matematica((logaritmo(potencia(b,a),c,False)))

enunciado_oculto = [a, b, c]










