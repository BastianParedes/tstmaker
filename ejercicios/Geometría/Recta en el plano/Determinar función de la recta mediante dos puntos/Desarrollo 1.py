{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b, c, d = Racional(randrange(-10, 10)), Racional(randrange(-10, 10)), Racional(randrange(-10, 10)), Racional(randrange(-10, 10))
while c-a==0 or d-b==0 or c-d==0 or d-b==0 or b-a==0:
    a, b, c, d = Racional(randrange(-10, 10)), Racional(randrange(-10, 10)), Racional(randrange(-10, 10)), Racional(randrange(-10, 10))

#================================Aquí va el enunciado================================================================
enunciado = "Determina la función de la recta que pasa por los puntos "+Matematica(Par(a,b))+" y "+Matematica(Par(c,d))+"."

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto =    Matematica(Recta(Par(a,b), Par(c,d)).show_funcion)




enunciado_oculto = [a, b, c, d]
espacio_para_el_desarrollo = 8











