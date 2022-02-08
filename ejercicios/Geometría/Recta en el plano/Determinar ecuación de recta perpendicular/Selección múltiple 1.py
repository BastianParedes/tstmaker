{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
x1, y1, x2, y2, x3, y3 = Racional(randrange(1, 10)), Racional(randrange(1, 10)), Racional(randrange(1, 10)), Racional(randrange(1, 10)), Racional(randrange(1, 10)), Racional(randrange(1, 10))
while (y2-y1)*(x3-x2)==(y3-y2)*(x2-x1) or x1==x2 or y1==y2 :
    x1, y1, x2, y2, x3, y3 = Racional(randrange(1, 10)), Racional(randrange(1, 10)), Racional(randrange(1, 10)), Racional(randrange(1, 10)), Racional(randrange(1, 10)), Racional(randrange(1, 10))
L = Recta(Par(x1,y1), Par(x2,y2))

#================================Aquí va el enunciado================================================================
enunciado = "Sea la recta L cuya ecuación es "+Matematica(L.show_ecuacion_principal)+". La ecuación de la recta que es perpendicular a L y pasa por el punto "+Matematica(Par(x3,y3))+" es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(Recta(Par(x3,y3),pendiente=-1/L.m).show_ecuacion_principal)
contenido_2 = Matematica(Recta(Par(x3,y3),pendiente=L.m).show_ecuacion_principal)
contenido_3 = Matematica(L.show_ecuacion_principal)
contenido_4 = Matematica(Recta(Par(x3,y3),pendiente=-L.m).show_ecuacion_principal)
contenido_5 = Matematica(Recta(Par(x3,y3),pendiente=1/L.m).show_ecuacion_principal)

enunciado_oculto = [x1,x2,x3,y1,y2,y3]










