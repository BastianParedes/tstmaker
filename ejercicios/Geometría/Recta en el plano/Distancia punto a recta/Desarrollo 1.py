{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
x1, y1, x2, y2, x, y = Racional(randrange(1, 10)), Racional(randrange(1, 10)), Racional(randrange(1, 10)), Racional(randrange(1, 10)), Racional(randrange(1, 10)), Racional(randrange(1, 10))
while (y2-y1)*(x-x2)==(y-y2)*(x2-x1) or x1==x2 or y1==y2 :
    x1, y1, x2, y2, x, y = Racional(randrange(1, 10)), Racional(randrange(1, 10)), Racional(randrange(1, 10)), Racional(randrange(1, 10)), Racional(randrange(1, 10)), Racional(randrange(1, 10))
L = Recta(Par(x1,x2), Par(x2,y2))
A = Racional(-L.m.numerador)
B = Racional(L.m.denominador)
C = -L.n*L.m.denominador

#================================Aquí va el enunciado================================================================
enunciado = "Calcula la distancia entre el punto "+Matematica(Par(x,y))+" y la recta L de ecuación "+Matematica(choice([L.show_ecuacion_principal, L.show_ecuacion_general]))+"."

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(abs(A*x+B*y+C)/Root(A**2+B**2))+" unidades"




enunciado_oculto=[x,y,L.show_funcion]
espacio_para_el_desarrollo = 8











