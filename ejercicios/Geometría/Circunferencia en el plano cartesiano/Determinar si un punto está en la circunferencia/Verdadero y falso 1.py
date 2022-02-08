{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
r = randrange(1, 13)
C = Circunferencia(0, 0, r)
x1 = Racional(randrange(-r, r+1))
x2 = Racional(randrange(-r, r+1))
y1 = Racional(randrange(-r, r+1))
y2 = Racional(randrange(-r, r+1))

#================================Aquí va el enunciado================================================================
enunciado_verdadero = "Considera la circunferencia C cuya ecuación es "+Matematica(choice([C.show_ecuacion_principal, C.show_ecuacion_general]))+". Un punto de C es "+Matematica(choice([    Par(x1, Root(r**2-x1**2)),    Par(Root(r**2-y1**2), y1) ]))+"."

enunciado_falso = "Considera la circunferencia C cuya ecuación es "+Matematica(choice([C.show_ecuacion_principal, C.show_ecuacion_general]))+". Un punto de C es "+Matematica(choice([    Par(x2, Root(r**2-x2**2+randrange(1, 10))),    Par(Root(r**2-y2**2+randrange(1, 10)), y2) ]))+"."





enunciado_oculto = [C, x1, y1]











