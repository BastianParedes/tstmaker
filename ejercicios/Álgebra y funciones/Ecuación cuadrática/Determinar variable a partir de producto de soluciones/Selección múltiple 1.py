{"cantidad_opciones":2, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b, c, p = Racional(elegir(-10,11,0)), Racional(elegir(-10,11,0)), Racional(elegir(-10,11,0)), Racional(elegir(-10,10,0), randrange(1, 10))

if opcion==1:
    #================================Aquí va el enunciado================================================================
    enunciado = "El producto de las soluciones de la ecuación "+Matematica(ecuacion_azar(a*{"k":1, "x":2}, b*"x",c))+" es "+Matematica(p)+". El valor de k es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(c/(a*p))
    contenido_2 = Matematica(-c/(a*p))
    contenido_3 = Matematica(b/(a*p))
    contenido_4 = Matematica(-b/(a*p))
    contenido_5 = Matematica(c/a)

elif opcion==2:
    #================================Aquí va el enunciado================================================================
    enunciado = "El producto de las soluciones de la ecuación "+Matematica(ecuacion_azar(a*{"x":2}, b*{"x":1},c*"k"))+" es "+Matematica(p)+". El valor de k es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(a*p/c)
    contenido_2 = Matematica(-a*p/c)
    contenido_3 = Matematica(a*p/b)
    contenido_4 = Matematica(-a*p/b)
    contenido_5 = Matematica(c/a)




enunciado_oculto = [a, b, c, p, opcion]










