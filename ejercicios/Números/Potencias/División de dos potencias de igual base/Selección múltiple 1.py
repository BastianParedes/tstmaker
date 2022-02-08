{"cantidad_opciones":1, "cantidad_disponible":50}

#===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
lista = list(range(-10, -1))+list(range(2, 11))
a, b = Racional(choice(lista)), Racional(choice(lista))
while a==b:
    a, b = Racional(choice(lista)), Racional(choice(lista))

#===============================================Aquí va el número del ejercicio y el enunciado.
enunciado = Matematica(fraccion("x"**a, "x"**b)+"=")

#===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
contenido_correcto = Matematica("x"**(a-b))
contenido_2 = Matematica("x"**(a+b))
contenido_3 = Matematica("x"**(b-a))
contenido_4 = Matematica("x"**(a*b))
contenido_5 = Matematica("x"**(a/b))

enunciado_oculto = [a, b]










