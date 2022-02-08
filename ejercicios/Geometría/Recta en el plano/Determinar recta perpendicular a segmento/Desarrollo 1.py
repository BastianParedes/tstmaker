{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
p1 = Par(randrange(-10, 10), randrange(-10, 10))
p2 = Par(randrange(-10, 10), randrange(-10, 10))
while p1.x.show==p2.x.show or p1.y.show==p2.y.show:
    p1 = Par(randrange(-10, 10), randrange(-10, 10))
    p2 = Par(randrange(-10, 10), randrange(-10, 10))
pm = (p1+p2)/2
L_segmento = Recta(p1, p2)
L = Recta(pm, pendiente=(Racional(1,-L_segmento.m)))

#================================Aquí va el enunciado================================================================
enunciado = f"Considera los puntos A{Matematica(p1)} y B{Matematica(p2)}. Calcula la función de la recta que es perpendicular al segmento AB y pasa por su punto medio."

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(L.show_funcion)




enunciado_oculto = [p1, p2]
espacio_para_el_desarrollo = 8











