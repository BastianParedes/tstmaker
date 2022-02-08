{"cantidad_opciones":3, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
while True:
    base = Racional(randrange(1,16), randrange(2,16))
    if base.denominador != 1:
        break
exponente = randrange(0,5)

if opcion==1:#base positiva sin multiplicar por -1
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(potencia(base, exponente)+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    if exponente == 0:
        contenido_correcto = Matematica(Racional(1))
        contenido_2 =        Matematica(Racional(-1))
        contenido_3 =        Matematica(Racional(0))
        contenido_4 =        Matematica(base)
        contenido_5 =        Matematica(-base)
    elif exponente == 1:
        contenido_correcto = Matematica(base)
        contenido_2 =        Matematica(Racional(0))
        contenido_3 =        Matematica(Racional(1))
        contenido_4 =        Matematica(Racional(-1))
        contenido_5 =        Matematica(-base)
    else:
        contenido_correcto = Matematica(base**exponente)
        contenido_2 =        Matematica(base*exponente)
        contenido_3 =        Matematica(Racional(base.numerador**exponente, base.denominador))
        contenido_4 =        Matematica(Racional(base.numerador, base.denominador**exponente))
        contenido_5 =        Matematica(Racional(base.numerador, base.denominador*exponente))


if opcion==2:#base negativa
    base = -base
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(potencia(base, exponente)+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    if exponente == 0:
        contenido_correcto = Matematica(Racional(1))
        contenido_2 =        Matematica(Racional(-1))
        contenido_3 =        Matematica(Racional(0))
        contenido_4 =        Matematica(base)
        contenido_5 =        Matematica(-base)
    elif exponente == 1:
        contenido_correcto = Matematica(base)
        contenido_2 =        Matematica(Racional(0))
        contenido_3 =        Matematica(Racional(1))
        contenido_4 =        Matematica(Racional(-1))
        contenido_5 =        Matematica(-base)
    else:
        contenido_correcto = Matematica(base**exponente)
        contenido_2 =        Matematica(base*exponente)
        contenido_3 =        Matematica(Racional(base.numerador**exponente, base.denominador))
        contenido_4 =        Matematica(Racional(base.numerador, base.denominador**exponente))
        contenido_5 =        Matematica(Racional(base.numerador, base.denominador*exponente))


if opcion==3:#potencia multiplicada por -1
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica("-"+potencia(base, exponente)+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    if exponente == 0:
        contenido_correcto = Matematica(-1)
        contenido_2 =        Matematica(1)
        contenido_3 =        Matematica(0)
        contenido_4 =        Matematica(base)
        contenido_5 =        Matematica(-base)
    elif exponente == 1:
        contenido_correcto = Matematica(-base)
        contenido_2 =        Matematica(base)
        contenido_3 =        Matematica(0)
        contenido_4 =        Matematica(1)
        contenido_5 =        Matematica(-1)
    else:
        contenido_correcto = Matematica(-base**exponente)
        contenido_2 =        Matematica(base*exponente)
        contenido_3 =        Matematica(Racional(base.numerador**exponente, base.denominador))
        contenido_4 =        Matematica(-Racional(base.numerador**exponente, base.denominador))
        contenido_5 =        Matematica(-Racional(base.numerador, base.denominador*exponente))



if exponente==0:
    enunciado_oculto = "Exponente 0"
elif exponente==1:
    enunciado_oculto = "Exponente 1"
else:
    enunciado_oculto = [base, exponente, opcion]













