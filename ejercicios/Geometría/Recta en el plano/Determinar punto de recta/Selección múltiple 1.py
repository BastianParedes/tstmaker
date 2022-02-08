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
lista.remove(b)
c = choice(lista)
lista.remove(c)
d = choice(lista)
lista.remove(d)
e = choice(lista)
lista.remove(e)

#================================Aquí va el enunciado================================================================
enunciado = f"De los siguientes pares ordenados, el que representa un punto de la recta representada por la ecuación {Matematica(L.show_ecuacion_principal)} es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(Par(a, L.f(a)))
contenido_2 = Matematica(Par(b, L.f(b)+choice(list(range(-10, 0))+list(range(1, 10)))))
contenido_3 = Matematica(Par(c, L.f(c)+choice(list(range(-10, 0))+list(range(1, 10)))))
contenido_4 = Matematica(Par(d, L.f(d)+choice(list(range(-10, 0))+list(range(1, 10)))))
contenido_5 = Matematica(Par(e, L.f(e)+choice(list(range(-10, 0))+list(range(1, 10)))))

enunciado_oculto = [p1, p2]










