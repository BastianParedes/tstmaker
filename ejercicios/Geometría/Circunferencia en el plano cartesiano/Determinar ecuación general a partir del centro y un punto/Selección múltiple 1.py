{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
p1, p2 = Par(randrange(-10, 10), randrange(-10, 10)), Par(randrange(-10, 10), randrange(-10, 10))
while p1==p2:
    p1, p2 = Par(randrange(-10, 10), randrange(-10, 10)), Par(randrange(-10, 10), randrange(-10, 10))
r = abs(p1-p2)

#================================Aquí va el enunciado================================================================
enunciado =  "Determina la ecuación general de la circunferencia cuyo centro es el punto O"+Matematica(p1)+" y pasa por el punto P"+Matematica(p2)

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(Circunferencia(p1.x, p1.y, r).show_ecuacion_general)
contenido_2 = Matematica(Circunferencia(p2.x, p2.y, r).show_ecuacion_general)
contenido_3 = Matematica(Circunferencia(p1.x, p1.y, r**2).show_ecuacion_general)
contenido_4 = Matematica(Circunferencia(p2.x, p2.y, r**2).show_ecuacion_general)
contenido_5 = Matematica(Circunferencia(p1.x, p1.y, 2*r**2).show_ecuacion_general)

enunciado_oculto = [p1, p2]










