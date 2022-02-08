{"cantidad_opciones":2, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b, c, x, y = Racional(elegir(-5,6,0)), Racional(elegir(-5,6)), Racional(elegir(-5,6)), Racional(elegir(-3,4)), Racional(elegir(-5,6,0))
while a*x**2+b*x+c==0:
    a, b, c, x, y = Racional(elegir(-5,6,0)), Racional(elegir(-5,6)), Racional(elegir(-5,6)), Racional(elegir(-3,4)), Racional(elegir(-5,6,0))

letra_funcion = choice(["f", "g", "h"])

if opcion==1:
    #================================Aquí va el enunciado================================================================
    enunciado = "Sea la función "+Matematica(letra_funcion+"(x)="+Pol(a*{"x":2}, b*"x", c))+". ¿Cuál valor de k si "+Matematica("("+x+", "+Pol(a*x**2+b*x+c+y, "k", azar=True)+")", arreglar_espacios=True)+" pertenece a la gráfica de "+letra_funcion+"?"

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(-y)
    contenido_2 = Matematica(y)
    contenido_3 = Matematica(a*x**2+b*x+c)
    contenido_4 = Matematica(-(a*x**2+b*x+c))
    contenido_5 = Matematica(-a*x**2+b*x+c)


elif opcion==2:
    #================================Aquí va el enunciado================================================================
    enunciado = "Sea la función "+Matematica(letra_funcion+"(x)="+Pol(a*{"x":2}, b*"x", c))+". ¿Cuál valor de k si "+Matematica("("+x+", "+(a*x**2+b*x+c)*y*"k"+")", arreglar_espacios=True)+" pertenece a la gráfica de "+letra_funcion+"?"

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(1/y)
    contenido_2 = Matematica(y)
    contenido_3 = Matematica((a*x**2+b*x+c)/y)
    contenido_4 = Matematica(y/(a*x**2+b*x+c))
    contenido_5 = Matematica(-a*x**2+b*x+c)




enunciado_oculto = [a,b,c,x,y,opcion]










