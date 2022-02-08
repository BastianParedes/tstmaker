{"cantidad_opciones":3, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
parte_numerica = elegir(-30,31,0)
lista_letras = ["b", "c", "d", "f", "g", "h", "w", "x", "y", "z"]
letra_1, letra_2, letra_3, letra_4 = choice(lista_letras), choice(lista_letras), choice(lista_letras), choice(lista_letras)
while letra_1==letra_2 or letra_2==letra_3 or letra_1==letra_3:
    letra_1, letra_2, letra_3 = choice(lista_letras), choice(lista_letras), choice(lista_letras)
while letra_4 in [letra_1, letra_2, letra_3]:
    letra_4 = choice(lista_letras)
exponente_1, exponente_2, exponente_3, exponente_4 = randrange(1,6), randrange(1,6), randrange(1,6), randrange(1,6)


if opcion==1:
    #================================Aquí va el enunciado================================================================
    enunciado = "El término semejante a "+Matematica(Term(parte_numerica, {letra_1:exponente_1}))+" es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(Term(elegir(-30,31,0,parte_numerica), {letra_1:exponente_1}))
    contenido_2 =        Matematica(Term(parte_numerica, {letra_1:elegir(1,6,exponente_1)}))
    contenido_3 =        Matematica(Term(elegir(-30,31,0,parte_numerica), {letra_3:exponente_1}))
    contenido_4 =        Matematica(Term(parte_numerica, {letra_2:exponente_1}))
    contenido_5 =        Matematica(Term(elegir(-30,31,0), {letra_4:exponente_4}))

    enunciado_oculto = [letra_1, exponente_1]


elif opcion==2:
    #================================Aquí va el enunciado================================================================
    enunciado = "El término semejante a "+Matematica(Term(parte_numerica, {letra_1:exponente_1, letra_2:exponente_2}))+" es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(Term(elegir(-30,31,parte_numerica), {letra_1:exponente_1, letra_2:exponente_2}))
    contenido_2 =        Matematica(Term(parte_numerica, {letra_1:elegir(1,6,exponente_1), letra_2:elegir(1,6,exponente_2)}))
    contenido_3 =        Matematica(Term(elegir(-30,31,parte_numerica), {letra_2:exponente_1, letra_3:exponente_2}))
    contenido_4 =        Matematica(Term(elegir(-30,31,parte_numerica), {letra_3:exponente_1, letra_4:exponente_2}))
    contenido_5 =        Matematica(Term(elegir(-30,31,parte_numerica), {letra_1:elegir(1,6,exponente_1), letra_2:elegir(1,6,exponente_2)}))

    enunciado_oculto = [letra_1, exponente_1, letra_2, exponente_2]



elif opcion==3:
    #================================Aquí va el enunciado================================================================
    enunciado = "El término semejante a "+Matematica(Term(parte_numerica, {letra_1:exponente_1, letra_2:exponente_2, letra_3:exponente_3}))+" es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(Term(elegir(-30,31,parte_numerica), {letra_1:exponente_1, letra_2:exponente_2, letra_3:exponente_3}))
    contenido_2 =        Matematica(Term(parte_numerica, {letra_1:elegir(1,6,exponente_1), letra_2:elegir(1,6,exponente_2), letra_3:elegir(1,6,exponente_3)}))
    contenido_3 =        Matematica(Term(elegir(-30,31,parte_numerica), {letra_4:exponente_1, letra_2:exponente_2, letra_3:exponente_3}))
    contenido_4 =        Matematica(Term(elegir(-30,31,parte_numerica), {letra_1:exponente_1, letra_4:exponente_2, letra_3:exponente_3}))
    contenido_5 =        Matematica(Term(elegir(-30,31,parte_numerica), {letra_1:exponente_1, letra_2:exponente_2, letra_4:exponente_3}))

    enunciado_oculto = [letra_1, exponente_1, letra_2, exponente_2, letra_3, exponente_3]











