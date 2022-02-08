{"cantidad_opciones":2, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b, c, d = Racional(elegir(-11,12,0)), Racional(elegir(-11,12,0)), Racional(elegir(-11,12,0)), Racional(elegir(-11,12,0))
x, y = a/b, c/d
while x.denominador==1 or y.denominador==1 or (0<a and 0<b and 0<c and 0<d):
    a, b, c, d = Racional(elegir(-11,12,0)), Racional(elegir(-11,12,0)), Racional(elegir(-11,12,0)), Racional(elegir(-11,12,0))
    x, y = a/b, c/d

if opcion==1:
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(fraccion(a,b)+":"+fraccion(c,d)+"=")


elif opcion==2:
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(fraccion(fraccion(a,b), fraccion(c,d))+"=")

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(x/y)
contenido_2 = Matematica(y/x)
contenido_3 = Matematica(x*y)
contenido_4 = Matematica(x+y)
contenido_5 = Matematica(abs(x-y))

enunciado_oculto = [a,b,c,d]










