{"cantidad_opciones":2, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b, c, s = Racional(elegir(-10,11,0)), Racional(elegir(-10,11,0)), Racional(elegir(-10,11,0)), Racional(elegir(-10,10,0), randrange(1, 10))

if opcion==1:
    #================================Aquí va el enunciado================================================================
    enunciado = "La suma de las soluciones de la ecuación "+Matematica(ecuacion_azar(a*{"k":1, "x":2}, b*"x",c))+" es "+Matematica(s)+". El valor de k es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(-b/(a*s))
    contenido_2 = Matematica(b/(a*s))
    contenido_3 = Matematica(-c/(a*s))
    contenido_4 = Matematica(c/(a*s))
    contenido_5 = Matematica(-b/a)

elif opcion==2:
    #================================Aquí va el enunciado================================================================
    enunciado = "La suma de las soluciones de la ecuación "+Matematica(ecuacion_azar(a*{"x":2}, b*{"k":1,"x":1},c))+" es "+Matematica(s)+". El valor de k es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(-a*s/b)
    contenido_2 = Matematica(a*s/b)
    contenido_3 = Matematica(-a*s/c)
    contenido_4 = Matematica(a*s/c)
    contenido_5 = Matematica(-b/a)




enunciado_oculto = [a, b, c, s, opcion]










