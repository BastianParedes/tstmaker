{"cantidad_opciones":7, "cantidad_disponible":50}

#Dado
if opcion==1:
    opcion_b = choice([1,2,3,4,5,6])

    if opcion_b==1:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        numero = Natural(randrange(1, 7))
        casos_posibles = len(numero.lista_de_divisores)
        total_de_casos = 6
        #================================Aquí va el enunciado================================================================
        enunciado = f"Se lanza un dado normal de 6 caras numeradas de 1 a 6. La probabilidad de que el número obtenido sea divisor de {numero} es"


    elif opcion_b==2:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        casos_posibles = 3
        total_de_casos = 6
        #================================Aquí va el enunciado================================================================
        enunciado = "Se lanza un dado normal de 6 caras numeradas de 1 a 6. La probabilidad de que el número obtenido sea primo es"


    elif opcion_b==3:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        numero = randrange(0, 8)
        total_de_casos = 6
        casos_posibles = 0
        for i in range(1, 7):
            if i<numero:
                casos_posibles += 1
        #================================Aquí va el enunciado================================================================
        enunciado = f"Se lanza un dado normal de 6 caras numeradas de 1 a 6. La probabilidad de que el número ontenido sea menor que {numero} es"


    elif opcion_b==4:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        total_de_casos = 6
        casos_posibles = 3
        #================================Aquí va el enunciado================================================================
        enunciado = f"Se lanza un dado normal de 6 caras numeradas de 1 a 6. La probabilidad de obtener un número {choice(['par', 'impar'])} es"


    elif opcion_b==5:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        numero = randrange(1, 7)
        total_de_casos = 6
        casos_posibles = 0
        for i in range(1, 7):
            if i%numero==0:
                casos_posibles += 1
        #================================Aquí va el enunciado================================================================
        enunciado = f"Se lanza un dado normal de 6 caras numeradas de 1 a 6. La probabilidad de obtener un múltiplo de {numero} es"


    elif opcion_b==6:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        total_de_casos = 6
        casos_posibles = 2
        #================================Aquí va el enunciado================================================================
        enunciado = f"Se lanza un dado normal de 6 caras numeradas de 1 a 6. La probabilidad de obtener un número con raiz cuadrada exacta es"










# Mazo de cartas inglesas
elif opcion==2:
    opcion_b = choice([1,2,3,4,5,6,7])

    if opcion_b==1:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        casos_posibles = 4
        total_de_casos = 52
        #================================Aquí va el enunciado================================================================
        enunciado = f"Se saca una carta de un mazo de cartas inglesas (52 cartas). La probabilidad de obtener {choice(['un as', 'un rey', 'una reina'])} es"


    elif opcion_b==2:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        numero = Natural(randrange(2, 11))
        casos_posibles = len(numero.lista_de_divisores)*4
        total_de_casos = 52
        #================================Aquí va el enunciado================================================================
        enunciado = f"Se saca una carta de un mazo de cartas inglesas (52 cartas). La probabilidad de obtener una carta con un número divisor de {numero} es"


    elif opcion_b==3:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        casos_posibles = 4*4
        total_de_casos = 52
        #================================Aquí va el enunciado================================================================
        enunciado = "Se saca una carta de un mazo de cartas inglesas (52 cartas). La probabilidad de obtener una carta con un número primo es"


    elif opcion_b==4:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        casos_posibles = 5*4
        total_de_casos = 52
        #================================Aquí va el enunciado================================================================
        enunciado = "Se saca una carta de un mazo de cartas inglesas (52 cartas). La probabilidad de obtener una carta con un número compuesto es"


    elif opcion_b==5:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        casos_posibles = 4*4
        total_de_casos = 52
        #================================Aquí va el enunciado================================================================
        enunciado = "Se saca una carta de un mazo de cartas inglesas (52 cartas). La probabilidad de obtener una carta sin número es"


    elif opcion_b==6:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        casos_posibles = 5*4
        total_de_casos = 52
        #================================Aquí va el enunciado================================================================
        enunciado = "Se saca una carta de un mazo de cartas inglesas (52 cartas). La probabilidad de obtener una carta con un número par es"


    elif opcion_b==7:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        casos_posibles = 4*4
        total_de_casos = 52
        #================================Aquí va el enunciado================================================================
        enunciado = "Se saca una carta de un mazo de cartas inglesas (52 cartas). La probabilidad de obtener una carta con un número impar es"










#Caja con pelotas de colores
elif opcion==3:
    opcion_b = choice([1,2])

    if opcion_b==1:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        blancas = randrange(2, 5)
        negras= randrange(2, 4)
        rojas = randrange(2, 5)
        casos_posibles = rojas
        total_de_casos = blancas+negras+rojas
        #================================Aquí va el enunciado================================================================
        enunciado = f"En una caja hay {blancas} pelotas solo blancas, {negras} solo negras y {rojas} solo rojas. La probabilidad de sacar una roja es"
        

    elif opcion_b==2:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        verdes = randrange(2, 5)
        amarillas = randrange(2, 4)
        rosadas = randrange(2, 5)
        casos_posibles = rosadas
        total_de_casos = verdes+amarillas+rosadas
        #================================Aquí va el enunciado================================================================
        enunciado = f"En una caja hay {verdes+amarillas+rosadas} pelotas, de las cuales {verdes} son solo verdes, {amarillas} son solo amarillas y el resto son solo rosadas. La probabilidad de sacar una rosada es"










#Ejercicio de verdadero y falso
elif opcion==4:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    casos_posibles = 1
    total_de_casos = 2
    #================================Aquí va el enunciado================================================================
    enunciado = f'Una pregunta de tipo "verdadero y falso", que no requiere justificación, es respondida al azar. La probabilidad de la respuesta sea {choice(["correcta", "incorrecta"])} es'










#Ejercicio de monedas
elif opcion==5:
    opcion_b = choice([1,2,3,4])
    if opcion_b==1:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        casos_posibles = 1
        total_de_casos = 2
        #================================Aquí va el enunciado================================================================
        enunciado = f"La probabilidad de obtener {choice(['sello', 'cara'])}, al lanzar una moneda, es"

    elif opcion_b==2:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        casos_posibles = 1
        total_de_casos = 4
        #================================Aquí va el enunciado================================================================
        enunciado = f"La probabilidad de obtener dos {choice(['sellos', 'caras'])}, al lanzar dos monedas, es"

    elif opcion_b==3:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        casos_posibles = 2
        total_de_casos = 4
        #================================Aquí va el enunciado================================================================
        enunciado = f"Se lanzan dos monedas iguales. La probabilidad de que ambas caigan sobre el mismo lado es"

    elif opcion_b==4:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        casos_posibles = 2
        total_de_casos = 4
        #================================Aquí va el enunciado================================================================
        enunciado = f"Se lanzan dos monedas iguales. La probabilidad de que caigan sobre lados distintos es"










#Ejercicio de selección múltiple
elif opcion==6:
    opcion_b = choice([1,2])

    if opcion_b==1:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        cantidad_de_alternativas = choice([4, 5])
        casos_posibles = 1
        total_de_casos = cantidad_de_alternativas
        #================================Aquí va el enunciado================================================================
        enunciado = f"Se responde, al azar, una pregunta de selección múltipe de {cantidad_de_alternativas} alternativas. La probabilidad de que la respuesta sea correcta es"

    elif opcion_b==2:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        cantidad_de_alternativas = choice([4, 5])
        casos_posibles = cantidad_de_alternativas-1
        total_de_casos = cantidad_de_alternativas
        #================================Aquí va el enunciado================================================================
        enunciado = f"Se responde, al azar, una pregunta de selección múltipe de {cantidad_de_alternativas} alternativas. La probabilidad de que la respuesta sea incorrecta es"










#Bolsa de fichas con números
elif opcion==7:
    opcion_b = choice([1,2,3])

    if opcion_b==1:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        cantidad_de_fichas = randrange(5, 13)
        total_de_casos = cantidad_de_fichas
        casos_posibles = 0
        for i in range(0, cantidad_de_fichas):
            if i%2==0:
                casos_posibles +=1
        #================================Aquí va el enunciado================================================================
        enunciado = f"En una bolsa hay {cantidad_de_fichas} fichas numeradas desde 0 hasta {cantidad_de_fichas-1}. Si se saca una ficha al azar, ¿cuál es la probabilidad de que el número sea par?"


    elif opcion_b==2:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        cantidad_de_fichas = randrange(5, 13)
        numero = choice([3, 4, 5, 6, 7])
        total_de_casos = cantidad_de_fichas
        casos_posibles = 0
        for i in range(0, cantidad_de_fichas):
            if i>=numero:
                casos_posibles +=1
        #================================Aquí va el enunciado================================================================
        enunciado = f"En una bolsa hay {cantidad_de_fichas} fichas numeradas desde 0 hasta {cantidad_de_fichas-1}. Si se saca una ficha al azar, ¿cuál es la probabilidad de que el número sea mayor o igual a {numero}?"

    elif opcion_b==3:
        enunciado = f"En una bolsa hay 100 fichas numeradas desde 1 hasta 100. Si se saca una ficha al azar, ¿cuál es la probabilidad de que la decena y la unidad del número sean iguales?"
        total_de_casos = 100
        casos_posibles = 10










casos_posibles = Racional(casos_posibles)
total_de_casos = Racional(total_de_casos)
#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
if casos_posibles==0:
    contenido_correcto = Matematica(Racional(0))
    contenido_2 = Matematica(Racional(1,4))
    contenido_3 = Matematica(Racional(1,2))
    contenido_4 = Matematica(Racional(3,4))
    contenido_5 = Matematica(Racional(1))

elif total_de_casos==casos_posibles*2:
    contenido_correcto = Matematica(Racional(1,2))
    contenido_2 = Matematica(Racional(1,4))
    contenido_3 = Matematica(Racional(1,3))
    contenido_4 = Matematica(Racional(2,3))
    contenido_5 = Matematica(Racional(1))

elif total_de_casos==casos_posibles:
    contenido_correcto = Matematica(Racional(1))
    contenido_2 = Matematica(Racional(0))
    contenido_3 = Matematica(Racional(1,4))
    contenido_4 = Matematica(Racional(1,2))
    contenido_5 = Matematica(Racional(3,4))

else:
    contenido_correcto = Matematica(casos_posibles/total_de_casos)
    contenido_2 = Matematica(total_de_casos/total_de_casos)
    contenido_3 = Matematica(Racional(1,2))
    contenido_4 = Matematica(Racional(1, randrange(3, 7)))
    contenido_5 = Matematica(1-casos_posibles/total_de_casos)





enunciado_oculto = enunciado











