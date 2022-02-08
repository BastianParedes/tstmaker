{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
p1, p2 = Par(randrange(-10, 10), randrange(-10, 10)), Par(randrange(-10, 10), randrange(-10, 10))
while p1.x==p2.x:
    p1, p2 = Par(randrange(-10, 10), randrange(-10, 10)), Par(randrange(-10, 10), randrange(-10, 10))
L = Recta(p1, p2)
lista = list(range(-10, 10))
a = choice(lista)
lista.remove(a)
b = choice(lista)

#================================Aquí va el enunciado================================================================
enunciado_verdadero = f"Un punto por contenido por la gráfica de la recta representada por la ecuación {Matematica(L.show_ecuacion_principal)} es "+Matematica(Par(a, L.f(a)))+"."

enunciado_falso = f"Un punto por contenido por la gráfica de la recta representada por la ecuación {Matematica(L.show_ecuacion_principal)} es "+Matematica(Par(b, L.f(b)+choice(list(range(-10, 0))+list(range(1, 10)))))+"."




enunciado_oculto = [p1, p2]











