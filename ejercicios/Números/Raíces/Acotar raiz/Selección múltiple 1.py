{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
lista = list(range(1, 12))
numero_1 = Racional(choice(lista))
lista.remove(numero_1)
numero_2 = Racional(choice(lista))
lista.remove(numero_2)
numero_3 = Racional(choice(lista))
lista.remove(numero_3)
numero_4 = Racional(choice(lista))
lista.remove(numero_4)
numero_5 = Racional(choice(lista))
lista.remove(numero_5)
numero_en_medio = Racional(randrange(numero_1.numerador**2+1, (numero_1.numerador+1)**2))

#================================Aquí va el enunciado================================================================
enunciado = r"Es verdadero respecto al numero\ \ "+Matematica(raiz(numero_en_medio))+r"\ \ que"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(numero_1+"<"+raiz(numero_en_medio)+"<"+(numero_1+1))
contenido_2 = Matematica(numero_2+"<"+raiz(numero_en_medio)+"<"+(numero_2+1))
contenido_3 = Matematica(numero_3+"<"+raiz(numero_en_medio)+"<"+(numero_3+1))
contenido_4 = Matematica(numero_4+"<"+raiz(numero_en_medio)+"<"+(numero_4+1))
contenido_5 = Matematica(numero_5+"<"+raiz(numero_en_medio)+"<"+(numero_5+1))

enunciado_oculto = numero_en_medio










