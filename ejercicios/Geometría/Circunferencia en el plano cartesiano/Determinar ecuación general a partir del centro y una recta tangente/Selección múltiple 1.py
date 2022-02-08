{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
p = Par(randrange(-10, 10), randrange(-10, 10))
L = Recta(Par(0, randrange(-10, 10)), pendiente=randrange(-10, 10))
A = Racional(-L.m.numerador)
B = Racional(L.m.denominador)
C = -L.n*L.m.denominador
r = abs(A*p.x+B*p.y+C)/Root(A**2+B**2)

#================================Aquí va el enunciado================================================================
enunciado =  "Determina la ecuación general de la circunferencia cuyo centro es el punto O"+Matematica(p)+" y es tangente a la recta L definida por la ecuación "+Matematica(choice([L.show_ecuacion_principal, L.show_ecuacion_general]))

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(Circunferencia(p.x, p.y, r).show_ecuacion_general)
contenido_2 = Matematica(Circunferencia(p.x, p.y, 2*r).show_ecuacion_general)
contenido_3 = Matematica(Circunferencia(p.x, p.y, r/2).show_ecuacion_general)
contenido_4 = Matematica(Circunferencia(p.x, p.y, (2*r)**2).show_ecuacion_general)
contenido_5 = Matematica(Circunferencia(p.x, p.y, (r/2)**2).show_ecuacion_general)

enunciado_oculto = [p, L]










