{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
r = randrange(1, 13)
C = Circunferencia(0, 0, r)
x1 = Racional(randrange(-r, r+1))
x2 = Racional(randrange(-r, r+1))
x3 = Racional(randrange(-r, r+1))
x4 = Racional(randrange(-r, r+1))
x5 = Racional(randrange(-r, r+1))
y1 = Racional(randrange(-r, r+1))
y2 = Racional(randrange(-r, r+1))
y3 = Racional(randrange(-r, r+1))
y4 = Racional(randrange(-r, r+1))
y5 = Racional(randrange(-r, r+1))

#================================Aquí va el enunciado================================================================
enunciado = "Considera la circunferencia C cuya ecuación es "+Matematica(choice([C.show_ecuacion_principal, C.show_ecuacion_general]))+". Un punto de C es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(choice([
    Par(x1, Root(r**2-x1**2)),
    Par(Root(r**2-y1**2), y1)
]))

contenido_2 = Matematica(choice([
    Par(x2, Root(r**2-x2**2+randrange(1, 10))),
    Par(Root(r**2-y2**2+randrange(1, 10)), y2)
]))

contenido_3 = Matematica(choice([
    Par(x3, Root(r**2-x3**2+randrange(1, 10))),
    Par(Root(r**2-y3**2+randrange(1, 10)), y3)
]))

contenido_4 = Matematica(choice([
    Par(x4, Root(r**2-x4**2+randrange(1, 10))),
    Par(Root(r**2-y4**2+randrange(1, 10)), y4)
]))

contenido_5 = Matematica(choice([
    Par(x5, Root(r**2-x5**2+randrange(1, 10))),
    Par(Root(r**2-y5**2+randrange(1, 10)), y5)
]))





enunciado_oculto = [C, x1, y1]










