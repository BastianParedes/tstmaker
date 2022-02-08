{"cantidad_opciones":2, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b, c, d = Racional(elegir(1,11)), Racional(elegir(1,11)), Racional(elegir(1,11)), Racional(elegir(1,11))
x, y = a/b, c/d
while x.denominador==1 or y.denominador==1:
    a, b, c, d = Racional(elegir(1,11)), Racional(elegir(1,11)), Racional(elegir(1,11)), Racional(elegir(1,11))
    x, y = a/b, c/d

if opcion==1:
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(x+":"+y+"=")


elif opcion==2:
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(fraccion(x, y)+"=")

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(x/y)
contenido_2 = Matematica(y/x)
contenido_3 = Matematica(x*y)
contenido_4 = Matematica(x+y)
contenido_5 = Matematica(abs(x-y))

enunciado_oculto = [x,y]










