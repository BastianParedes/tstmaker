{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b = Racional(elegir(1, 21)), Racional(elegir(1, 21))
while type(Root(a/b))==Racional and (a/b).denominador!=1:
    a, b = Racional(elegir(1, 21)), Racional(elegir(1, 21))
print(a,b)
#================================Aquí va el enunciado================================================================
enunciado = Matematica(fraccion(raiz(a), raiz(b))+"=")

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(Root(a/b))
contenido_2 = Matematica(Root(a*b))
contenido_3 = Matematica(Root(a+b))
contenido_4 = Matematica(Root(abs(a-b)))
contenido_5 = Matematica(Racional(round(b/a,2),True))



enunciado_oculto = [a,b]










