{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b, c, indice = Racional(elegir(2,5)), Racional(elegir(-4,5,0)), Racional(elegir(-4,5,0)), Racional(elegir(2,5))
while c-b<=0 or (c-b)/a<=1:
    a, b, c, indice = Racional(elegir(-4,5,0)), Racional(elegir(-4,5,0)), Racional(elegir(-4,5,0)), Racional(elegir(2,5))
#================================Aquí va el enunciado================================================================
enunciado = "El valor de x que satisface la ecuación "+Matematica(choice([
    Pol(a*raiz("x",indice),b,azar=True)+"="+c,
    c +"="+ Pol(a*raiz("x",indice),b,azar=True)
    ]))+" es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(((c-b)/a)**indice)
contenido_2 = Matematica(Root((c-b)/a, indice))
contenido_3 = Matematica((c-b)/a)
contenido_4 = Matematica((c-b)**indice)
contenido_5 = Matematica(Root(c-b, indice))



enunciado_oculto = [a,b,c,indice]










