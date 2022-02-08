{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b, c, indice, d, e = Racional(elegir(2,5)), Racional(elegir(-4,5,0)), Racional(elegir(-4,5,0)), Racional(elegir(2,5)), Racional(elegir(-5,5,0)), Racional(elegir(-5,5,0))
while c-b<=0 or (c-b)/a<=1:
    a, b, c, indice, d, e = Racional(elegir(2,5)), Racional(elegir(-4,5,0)), Racional(elegir(-4,5,0)), Racional(elegir(2,5)), Racional(elegir(-5,5,0)), Racional(elegir(-5,5,0))
#================================Aquí va el enunciado================================================================
enunciado = "El valor de x que satisface la ecuación "+Matematica(choice([
    Pol(a*raiz(Pol(d*"x",e),indice),b,azar=True)+"="+c,
    c +"="+ Pol(a*raiz(Pol(d*"x",e),indice),b,azar=True)
    ]))+" es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica((((c-b)/a)**indice-e)/d)
contenido_2 = Matematica(((c-b)/a-e)/d)
contenido_3 = Matematica(((c-b)/a)**indice)
contenido_4 = Matematica(((c-b)/a)**indice-e)
contenido_5 = Matematica(Root(c-b, indice))



enunciado_oculto = [a,b,c,indice]










