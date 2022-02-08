{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
h, k, r = choice([-1,1])*Racional(randrange(1, 7)), choice([-1,1])*Racional(randrange(1, 7)), Racional(randrange(2, 8))
#================================Aquí va el enunciado================================================================
enunciado = "Sea la circunferencia C cuya ecuación general es "+Matematica(Pol({"x":2}, {"y":2}, -2*h*"x", -2*k*"y", h**2+k**2-r**2)+"=0")+". El centro de C es"
#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(Par(h,k))

lista_de_contenidos = [Matematica(Par(-h,-k)), Matematica(Par(-h,k)), Matematica(Par(h,-k)), Matematica(Par(k,h)), Matematica(Par(-k,-h)), Matematica(Par(-k,h)), Matematica(Par(k,-h)), Matematica(Par(-k,-h))]

contenido_2 = choice(lista_de_contenidos)
lista_de_contenidos.remove(contenido_2)
contenido_3 = choice(lista_de_contenidos)
lista_de_contenidos.remove(contenido_3)
contenido_4 = choice(lista_de_contenidos)
lista_de_contenidos.remove(contenido_4)
contenido_5 = choice(lista_de_contenidos)
lista_de_contenidos.remove(contenido_5)



enunciado_oculto = [h,k,r]










