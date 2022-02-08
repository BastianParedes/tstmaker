{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b, c, exponente = Racional(elegir(2,5)), Racional(elegir(-4,5,0)), Racional(elegir(-4,5,0)), Racional(elegir(2,5))
while c-b<=0 or (c-b)/a<=1:
    a, b, c, exponente = Racional(elegir(2,5)), Racional(elegir(-4,5,0)), Racional(elegir(-4,5,0)), Racional(elegir(2,5))
#================================Aquí va el enunciado================================================================
enunciado = "El valor de x que satisface la ecuación "+Matematica(Pol(a*"x"**exponente,b,azar=True)+"="+c)+" es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(Root((c-b)/a, exponente))
contenido_2 = Matematica((c-b)/a)
contenido_3 = Matematica(((c-b)/a)**exponente)
contenido_4 = Matematica((c-b)**exponente)
contenido_5 = Matematica(Root(c-b, exponente))



enunciado_oculto = [a,b,c,exponente]










