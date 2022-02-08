{"cantidad_opciones":1, "cantidad_disponible":30}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
base = randrange(0, 13)

if base==0:
    exponente = randrange(50,100)
elif base==1:
    exponente = randrange(50,100)
elif base==2:
    exponente = elegir(0, 11)
elif base==3:
    exponente = randrange(0, 6)
elif base==4:
    exponente = randrange(0, 5)
elif base==5:
    exponente = randrange(0, 5)
elif base in [6,7]:
    exponente = randrange(0, 5)
elif base in [8,9,11,12]:
    exponente = randrange(0, 3)
elif base==10:
    exponente = randrange(0, 5)


base, exponente = Racional(base), Racional(exponente)

#================================Aquí va el enunciado================================================================
enunciado = Matematica(potencia(base, exponente)+"=")

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
if base==0:
    contenido_correcto = Matematica(base**exponente)
    contenido_2 = Matematica(exponente)
    contenido_3 = Matematica(-exponente)
    contenido_4 = Matematica(1)
    contenido_5 = Matematica(-1)
elif base==1:
    contenido_correcto = Matematica(base**exponente)
    contenido_2 = Matematica(exponente)
    contenido_3 = Matematica(-exponente)
    contenido_4 = Matematica(base+exponente)
    contenido_5 = Matematica(exponente-base)
else:
    if exponente==0:
        contenido_correcto = Matematica(1)
        contenido_2 = Matematica(0)
        contenido_3 = Matematica(base)
        contenido_4 = Matematica(-base)
        contenido_5 = Matematica(-1)
    elif exponente==1:
        contenido_correcto = Matematica(base)
        contenido_2 = Matematica(1)
        contenido_3 = Matematica(-1)
        contenido_4 = Matematica(-base)
        contenido_5 = Matematica(base+exponente)
    else:
        contenido_correcto = Matematica(base**exponente)
        contenido_2 = Matematica(exponente**base)
        contenido_3 = Matematica(base*exponente)
        contenido_4 = Matematica(base+exponente)
        contenido_5 = Matematica(Racional(exponente, base))


if exponente==0:
    enunciado_oculto = "exponente 0"
elif exponente==1:
    enunciado_oculto = "exponente 1"
elif base==0:
    enunciado_oculto = "base 0"
elif base==1:
    enunciado_oculto = "base 1"
else:
    enunciado_oculto = [base, exponente]












