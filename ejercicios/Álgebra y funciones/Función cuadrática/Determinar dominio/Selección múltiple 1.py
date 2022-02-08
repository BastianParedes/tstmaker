{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b, c = Racional(elegir(-10,10,0)), Racional(elegir(-10,10)), Racional(elegir(-10,10))
letra_de_funcion = choice(["f", "g", "h"])
#================================Aquí va el enunciado================================================================
enunciado = "El dominio de la función " +Matematica(letra_de_funcion+"(x)="+Pol(Term(a,{"x":2}), b*"x", c, azar=True))+ " es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(letra_conjunto("R"))
contenido_2 = Matematica(fr"\left[{-b/(2*a)}, +{INF()}\right[", arreglar_espacios=True)
contenido_3 = Matematica(fr"\left[{(4*a*c-b**2)/(4*a)}, +{INF()}\right[", arreglar_espacios=True)
contenido_4 = Matematica(fr"\left]-{INF()}, {-b/(2*a)}\right]", arreglar_espacios=True)
contenido_5 = Matematica(fr"\left]-{INF()}, {(4*a*c-b**2)/(4*a)}\right]", arreglar_espacios=True)


enunciado_oculto = [a, b, c]










