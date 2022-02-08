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
enunciado = "La distancia entre el punto "+Matematica(Par(x,y))+" y la recta L de ecuación "+Matematica(choice([L.show_ecuacion_principal, L.show_ecuacion_general]))+" es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(abs(A*x+B*y+C)/Root(A**2+B**2))+" unidades"
contenido_2 =        Matematica(abs(A*x+B*y+C)/Root(L.m**2+L.n**2))+" unidades"
contenido_3 =        Matematica(abs(A*x+B*y+C)/Root(x**2+y**2))+" unidades"
contenido_4 =        Matematica(abs(L.m*x+L.n*y+C)/Root(A**2+B**2))+" unidades"
contenido_5 =        Matematica(abs(A*x+B*y+C)/(A**2+B**2))+" unidades"

enunciado_oculto=[x,y,L.show_funcion]










