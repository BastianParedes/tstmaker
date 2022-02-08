{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
p1 = Par(randrange(-5, 5),randrange(-5, 5))
p2 = Par(randrange(-5, 5),randrange(-5, 5))
p3 = Par(randrange(-5, 5),randrange(-5, 5))
p4 = Par(randrange(-5, 5),randrange(-5, 5))
while p1.x==p2.x or p3.x==p4.x or (p2.y-p1.y)/(p2.x-p1.x)==(p4.y-p3.y)/(p4.x-p3.x) or -(p2.y-p1.y)/(p2.x-p1.x)==(p4.y-p3.y)/(p4.x-p3.x):
    p1 = Par(randrange(-5, 5),randrange(-5, 5))
    p2 = Par(randrange(-5, 5),randrange(-5, 5))
    p3 = Par(randrange(-5, 5),randrange(-5, 5))
    p4 = Par(randrange(-5, 5),randrange(-5, 5))
L1 = Recta(p1, p2)
L2 = Recta(p3, p4)
#================================Aquí va el enunciado================================================================
enunciado = fr"""Sean las rectas ${sub("L",1)}$ y ${sub("L",2)}$ tales que
${sub("L",1)}:\ """+"\\"+fr"""{{{choice([L1.show_ecuacion_principal, L1.show_ecuacion_general])}$
${sub("L",2)}:\ """+"\\"+fr"""{{{choice([L2.show_ecuacion_principal, L2.show_ecuacion_general])}$
Calcula el punto de intersección entre ${sub("L",1)}$ y ${sub("L",2)}$."""

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(Par((L2.n-L1.n)/(L1.m-L2.m), L1.m*(L2.n-L1.n)/(L1.m-L2.m)+L1.n))




enunciado_oculto = [p1, p2, p3, p4]
espacio_para_el_desarrollo = 8











