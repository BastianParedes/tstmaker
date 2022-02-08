{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
while True:
    p_1 = []
    p_2 = []
    for _ in range(choice([2,3])):
        if choice([True,False]):#agregar un número
            p_1.append(elegir(-10,10,0,-1,1))
        else:#agregar una letra
            letra = choice(["x","y"])
            p_1.append(Term(elegir(-3,4,0), {letra:1}))
            
    for _ in range(choice([2,3])):
        if choice([True,False]):#agregar un número
            p_2.append(elegir(-10,10,0,-1,1))
        else:#agregar una letra
            letra = choice(["x","y"])
            p_2.append(Term(elegir(-3,4,0), {letra:1}))

    p_1 = Pol(lista_de_terminos=p_1, reducir=True)
    p_2 = Pol(lista_de_terminos=p_2, reducir=True)

    if len(p_1.lista_de_terminos)==1 or len(p_2.lista_de_terminos)==1:
        continue

    elif p_1==Pol(0) or p_2==Pol(0):
        continue

    elif 4 <= len(p_1.lista_de_terminos)+len(p_2.lista_de_terminos) <=5:
        break

if isinstance(p_2,(Racional,Term)):#el mas corto siempre será el p_1
    p_1,p_2 = p_2,p_1

p_2.show = "("+p_2.show+")"
if not isinstance(p_1, (Racional,Term)):
    p_1.show = "("+p_1.show+")"

#================================Aquí va el enunciado================================================================
enunciado = Matematica(p_1.show+p_2.show+"=")

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(p_1*p_2)

#solo multiplica los que están en medio
contenido_2 =        Matematica(Pol(lista_de_terminos=  p_1.lista_de_terminos[:-1] + [p_1.lista_de_terminos[-1]*p_2.lista_de_terminos[0]] + p_2.lista_de_terminos[1:]  , reducir=True))

#suma los polinomios
contenido_3 =        Matematica(p_1 + p_2)

#suma muchas veces en lugar de multiplicar muchas veces.
lista_provisional_1 = []
for t_1 in p_1.lista_de_terminos:
    for t_2 in p_2.lista_de_terminos:
        lista_provisional_1.append(Pol(t_1,t_2,reducir=True))
lista_provisional_2 = []
for polinomio in lista_provisional_1:
    for termino in polinomio.lista_de_terminos:
        lista_provisional_2.append(termino)
contenido_4 =        Matematica(Pol(lista_de_terminos=lista_provisional_2,reducir=True))

#suma las partes numericas a las t_2
lista_provisional = []
for t_1 in p_1.lista_de_terminos:
    for t_2 in p_2.lista_de_terminos:
        lista_provisional.append(Term(t_1.factor_numerico+t_2.factor_numerico , t_2.diccionario_de_letras_y_exponentes))
contenido_5 =        Matematica(Pol(lista_de_terminos=lista_provisional,reducir=True))
    



enunciado_oculto = [p_1, p_2]










