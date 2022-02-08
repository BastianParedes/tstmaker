{"cantidad_opciones":15, "cantidad_disponible":50}


fraccion_decimal = choice([False,True])

if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    casos_favorables = Racional(choice([5, 7]))
    casos_posibles = Racional(100)
    n = Racional(choice([8, 16]))
    k = n/4

    #================================Aquí va el enunciado================================================================
    enunciado = f"En una fábrica de bombillas, el {Matematica(Racional(casos_favorables*100, casos_posibles,True))}\% de ellas sale con defectos. La probabilidad de que en una muestra de {Matematica(n)} se encuentren {Matematica(k)} bombillas defectuosas es"



elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    casos_favorables = Racional(choice([8, 10]))
    casos_posibles = Racional(100)
    n = Racional(choice([10, 11]))
    k = n-5

    #================================Aquí va el enunciado================================================================
    enunciado = f"En las pruebas realizadas a los automóviles de cierta empresa se descubrió que el {Matematica(Racional(casos_favorables*100, casos_posibles,True))}\% presenta fuga de aceite. Si se revisan {Matematica(n)} automóviles ¿Cuál es la probabilidad de que {Matematica(k)} de ellos pierdan aceite?"



elif opcion==3:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    casos_favorables = Racional(choice([3, 4]))
    casos_posibles = casos_favorables +1
    n = Racional(choice([24, 41]))
    k = n-23

    #================================Aquí va el enunciado================================================================
    enunciado = f"Un examen consta de {Matematica(n)} preguntas de alternativas de {Matematica(casos_posibles)} preguntas cada una. Si todos los ejercicios son contestados al azar ¿cuál es la probabilidad de que {Matematica(k)} respuestas sean erradas?"



elif opcion==4:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    casos_favorables = Racional(1)
    casos_posibles = Racional(2)
    n = Racional(choice([10, 13, 14]))
    k = n-9
    lado = choice(["cara", "sello"])

    #================================Aquí va el enunciado================================================================
    enunciado = f"Se lanza una moneda {Matematica(n)} veces. ¿Cuál es la probabilidad de que en {Matematica(k)} "
    enunciado_extra = f"ocasiones se obtenga {Matematica(lado)}?"



elif opcion==5:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    casos_favorables = Racional(choice([18, 25]))
    casos_posibles = Racional(100)
    n = Racional(choice([28, 32]))
    k = n/4

    #================================Aquí va el enunciado================================================================
    enunciado = f"Un jugador profesional de básquetbol tiene una probabilidad de encestar de {Matematica(Racional((casos_posibles-casos_favorables)*100, casos_posibles,True))}\% cada vez que lanza. ¿Cuál es la probabilidad de que falle {Matematica(k)} lanzamientos si tiene {Matematica(n)} intentos?"



elif opcion==6:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    casos_favorables = Racional(choice([45, 95]))
    casos_posibles = Racional(100)
    n = Racional(choice([51, 60]))
    k = n-19

    #================================Aquí va el enunciado================================================================
    enunciado = f"Se tiene un dado cargado en el cual la probabilidad de que salga un número par es {Matematica(Racional((casos_posibles-casos_favorables)*100, casos_posibles,True))}\%. La probabilidad de que salgan {Matematica(k)} números impares al realizar {Matematica(n)} lanzamientos es"



elif opcion==7:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    casos_favorables = Racional(choice([30, 50]))
    casos_posibles = casos_favorables +10
    n = Racional(choice([22, 31]))
    k = n-21

    #================================Aquí va el enunciado================================================================
    enunciado = f"La probabilidad de que cierto arquero le de al centro de la diana es de {Matematica(Racional(casos_favorables,casos_posibles,True))}. Si lanza {Matematica(n)} flechas, la probabilidad de que {Matematica(k)} de ellas hayan dado al centro es"



elif opcion==8:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    casos_favorables = Racional(choice([96, 60]))
    casos_posibles = Racional(100)
    n = Racional(choice([33, 60]))
    k = n/3
    
    #================================Aquí va el enunciado================================================================
    enunciado = f"La última novela de un autor ha tenido un gran éxito, hasta el punto de que el {Matematica(Racional(casos_favorables*100, casos_posibles,True))}\% de los lectores ya la han leído. Un grupo de {Matematica(n)} amigos son aficionados a la lectura. ¿Cuál es la probabilidad de que en el grupo hayan leído la novela {Matematica(k)} personas?"



elif opcion==9:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    casos_favorables = Racional(choice([30, 35]))
    casos_posibles = casos_favorables +15
    n = Racional(choice([20, 48]))
    k = n/4

    #================================Aquí va el enunciado================================================================
    enunciado = f"Un agente de seguros vende pólizas a {Matematica(n)} personas de la misma edad y que disfrutan de buena salud. Según las tablas actuales, la probabilidad de que cada persona en estas condiciones viva 30 años o más es {Matematica(Racional(casos_favorables, casos_posibles,True))}. La probabilidad de que, transcurridos 30 años, vivan {Matematica(k)} personas es"



elif opcion==10:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    casos_favorables = Racional(choice([2, 12]))
    casos_posibles = casos_favorables*18
    n = Racional(choice([5, 35]))
    k = n/5

    #================================Aquí va el enunciado================================================================
    enunciado = f"En unas pruebas de alcoholemia se ha observado que el {Matematica(Racional(casos_favorables*100, casos_posibles,True))}\% de los conductores controlados dan positivo y que el 51\% de los conductores controlados no llevan puesto el cinturón de seguridad. También se ha observado que las dos infracciones son independientes. Un guardia de tráfico para {Matematica(n)} conductores al azar. Si tenemos en cuenta que el número de conductores es suficientemente importante como para estimar que la proporción de infractores no varía al hacer la selección, ¿cuál es la probabilidad de que {Matematica(k)} de ellos hayan bebido alcohol?"



elif opcion==10:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    casos_favorables = Racional(choice([10,40]))
    casos_posibles = casos_favorables*15
    n = Racional(choice([12, 27]))
    k = n/3

    #================================Aquí va el enunciado================================================================
    enunciado = f"En cierta empresa de juguetes, {Matematica(casos_posibles-casos_favorables)} de cada {Matematica(casos_posibles)} productos sí son aptos para ser usados por niños. Si se inspeccionan {Matematica(n)} juguetes, ¿cuál es la probabilidad de que {Matematica(k)} de ellos no puedan ser usados por niños?"



elif opcion==11:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    casos_favorables = Racional(choice([36,42]))
    casos_posibles = casos_favorables*3
    n = Racional(choice([37, 41]))
    k = n-11

    #================================Aquí va el enunciado================================================================
    enunciado = f"Pedro tiene una hurna en la cual hay {Matematica(Racional(3*casos_favorables,2,True))} bolas, {Matematica(casos_favorables)} de ellas son azules, {Matematica(Racional(casos_favorables,2,True))} son rojas y el resto son verdes. Pedro quiere realizar un experimento el cual consiste en sacar una bola al azar, observar su color y devolvera. ¿Cuál es la probabilidad de obtener {Matematica(k)} bolas verdes si realiza su experimento {Matematica(n)} veces?"



elif opcion==11:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    casos_favorables = Racional(1)
    casos_posibles = Racional(2)
    n = Racional(choice([25, 30, 50]))
    k = n-9

    #================================Aquí va el enunciado================================================================
    enunciado = f"Una prueba de matemática consta solo de {Matematica(n)} preguntas de verdadero y falso en las que no es necesario justificar las respuestas. Si la prueba es respondida al azar en su totalidad, ¿cuál es la probabilidad de que {Matematica(k)} respuestas sean correctas?"



elif opcion==12:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    casos_favorables = Racional(choice([3, 4]))
    casos_posibles = casos_favorables +5
    n = Racional(choice([25, 30]))
    k = n-8

    #================================Aquí va el enunciado================================================================
    enunciado = f"En cierta habitación hay {Matematica(casos_favorables)} mujeres por cada {Matematica(casos_posibles-casos_favorables)} hombres. Si se escogen {Matematica(n)} personas al azar, ¿cuál es la probabilidad de que {Matematica(k)} de ellas sean mujeres?"



elif opcion==13:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    casos_favorables = Racional(choice([10, 15]))
    casos_posibles = casos_favorables*2
    n = Racional(choice([20, 30]))
    k = n-5

    #================================Aquí va el enunciado================================================================
    enunciado = f"La probabilidad de que cada estudiante, por separado, de IV medio se licencie es de {Matematica(Racional(casos_favorables,casos_posibles,True))}. La probabilidad de que {Matematica(k)} estudiantes, de {Matematica(n)}, se licencien es"



elif opcion==14:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    casos_favorables = Racional(1)
    casos_posibles = Racional(2)
    n = Racional(choice([3, 4, 5]))
    k = n-2

    #================================Aquí va el enunciado================================================================
    enunciado = f"La probabilidad de que, en una familia de {Matematica(n)} hijos, {Matematica(k)} de ellos sean mujeres es"



elif opcion==15:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    casos_favorables = Racional(1)
    casos_posibles = Racional(2)
    n = Racional(choice([3, 4, 5]))
    k = n-2

    #================================Aquí va el enunciado================================================================
    enunciado = f"Los estudios muestran que el {Matematica(Racional((casos_posibles-casos_favorables)*100, casos_posibles,True))}\% de la población chilena es alérgica a cierto fármaco. Si a un grupo de {Matematica(n)} personas se les da el fármaco, ¿cuál es la probabilidad de que {Matematica(k)} de ellas se mantengan sanas?"





# ================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero======
if casos_favorables/casos_posibles==0.5:
    contenido_correcto = Matematica(coeficiente_binomial(n, k)     +por()+ potencia(Racional(casos_favorables,casos_posibles), n, quitar_1=True))
    contenido_2        = Matematica(coeficiente_binomial(n, k)     +por()+ potencia(Racional(casos_favorables,casos_posibles,fraccion_decimal), k, quitar_1=True))
    contenido_3        = Matematica(coeficiente_binomial(k, n)     +por()+ potencia(Racional(casos_favorables,casos_posibles,fraccion_decimal), n, quitar_1=True))
    contenido_4        = Matematica(coeficiente_binomial(k, n)     +por()+ potencia(Racional(casos_favorables,casos_posibles,fraccion_decimal), k, quitar_1=True))
    contenido_5        = Matematica(coeficiente_binomial(k, n-k)   +por()+ potencia(Racional(casos_favorables,casos_posibles,fraccion_decimal), n, quitar_1=True))

else:
    contenido_correcto = Matematica(coeficiente_binomial(n, k)     +por()+ potencia(Racional(casos_favorables,casos_posibles,fraccion_decimal), k, quitar_1=True)                 +por()+ potencia(Racional(casos_posibles-casos_favorables,casos_posibles,fraccion_decimal), n-k, quitar_1=True))
    contenido_2        = Matematica(coeficiente_binomial(n, k)     +por()+ potencia(Racional(casos_posibles-casos_favorables,casos_posibles,fraccion_decimal), k, quitar_1=True)  +por()+ potencia(Racional(casos_favorables,casos_posibles,fraccion_decimal), n-k, quitar_1=True))
    contenido_3        = Matematica(coeficiente_binomial(n, k)     +por()+ potencia(Racional(casos_favorables,casos_posibles,fraccion_decimal), n, quitar_1=True)                 +por()+ potencia(Racional(casos_posibles-casos_favorables,casos_posibles,fraccion_decimal), n-k, quitar_1=True))
    contenido_4        = Matematica(coeficiente_binomial(k, n)     +por()+ potencia(Racional(casos_favorables,casos_posibles,fraccion_decimal), n)                 +por()+ potencia(Racional(casos_posibles-casos_favorables,casos_posibles,fraccion_decimal), n, quitar_1=True))
    contenido_5        = Matematica(coeficiente_binomial(k, n)     +por()+ potencia(Racional(casos_posibles-casos_favorables,casos_posibles,fraccion_decimal), n, quitar_1=True)  +por()+ potencia(Racional(casos_favorables,casos_posibles,fraccion_decimal), k, quitar_1=True))

enunciado_oculto = enunciado










