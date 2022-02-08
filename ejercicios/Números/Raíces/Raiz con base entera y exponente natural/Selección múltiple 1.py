{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
base = randrange(-7, 13)

if base in [-7, -6, -5, -4]:
    indice = choice([3, 5])

elif base==-3:
    indice = choice([3, 5])

elif base==-2:
    indice = choice([3, 5, 7, 9])

elif base==-1:
    indice = choice([13, 25])

elif base==0:
    indice = choice([4, 25])

elif base==1:
    indice = choice([4, 25])

elif base==2:
    indice = randrange(4, 10)

elif base==3:
    indice = randrange(2, 7)

elif base in [4, 5, 6, 7]:
    indice = randrange(2, 6)

elif base in [8, 9, 10, 11, 12]:
    indice = randrange(2, 4)

base, indice = Racional(base), Racional(indice)

#================================Aquí va el enunciado================================================================
enunciado = Matematica(raiz(base**indice, indice)+"=")

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
if base==0:
    contenido_correcto = Matematica(0)
    contenido_2 = Matematica(indice)
    contenido_3 = Matematica(-indice)
    contenido_4 = Matematica(fraccion(indice,0))
    contenido_5 = Matematica(1)

elif base==-1 or base==1:
    contenido_correcto = Matematica(base)
    contenido_2 = Matematica(-base)
    contenido_3 = Matematica(indice)
    contenido_4 = Matematica(-indice)
    contenido_5 = Matematica(base/indice)

else:
    contenido_correcto = Matematica(base)
    contenido_2 = Matematica(indice**base)
    contenido_3 = Matematica(base*indice)
    contenido_4 = Matematica(Racional(base,indice,True))
    contenido_5 = Matematica(choice([indice+base, -base]))

enunciado_oculto = [base, indice]










