{"cantidad_opciones":1, "cantidad_disponible":40}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
cantidad_radicandos = choice([2,3])
while True:
    lista_primos = [2,3,5,7,11,13]
    shuffle(lista_primos)
    lista_primos = sorted(lista_primos[:cantidad_radicandos])
    resultado = 1
    for primo in lista_primos:
        resultado *= primo
    if resultado**2 < 1000:
        break



lista_divisores = lista_primos + lista_primos
shuffle(lista_divisores)

while True:
    lista_radicandos = []
    for _ in range(cantidad_radicandos):
        lista_radicandos.append(1)
    for primo in lista_divisores:
        index = randrange(0, len(lista_radicandos))
        lista_radicandos[index] *= primo

    condicion_1, condicion_2 = False, True
    if 1 not in lista_radicandos:
        condicion_1 = True

    for radicando in lista_radicandos:
        if lista_radicandos.count(radicando) != 1 and type(Root(radicando)) != Racional:
            condicion_2 = False
            break

    if condicion_1 and condicion_2:
        break


#================================Aquí va el enunciado================================================================
enunciado = str(raiz(lista_radicandos[0]))
for radicando in lista_radicandos[1:]:
    enunciado += r"\cdot "+str(raiz(radicando))
enunciado += "="
enunciado = Matematica(enunciado)

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(resultado)
contenido_2 =        Matematica(resultado**2) #solo borró la raiz, pero no la calculó
contenido_3 =        Matematica(raiz(resultado))#calculó la raiz, pero no borró el símbolo

contenido_4 =        0
contenido_5 =        0
for radicando in lista_radicandos:
    contenido_4 += radicando
    contenido_5 += radicando
contenido_4 =        Matematica(raiz(contenido_4))#sumó los radicandos y no borró el símbolo
contenido_5 =        Matematica(contenido_5)#sumó los radicandos y borró el símbolo de raiz



print(cantidad_radicandos)
enunciado_oculto = sorted(lista_radicandos)










