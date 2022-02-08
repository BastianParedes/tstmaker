{"cantidad_opciones":5, "cantidad_disponible":50}


if opcion==1:
    p = Racional(randrange(1,100))
    n = Racional(randrange(100,1000))
    while (p*n/100).denominador!=1:
        p = Racional(randrange(1,100))
        n = Racional(randrange(100,1000))
    lista_provisional = ["directo","invertido"]
    shuffle(lista_provisional)
    directo_invertido_1 = lista_provisional[0]
    directo_invertido_2 = lista_provisional[1]
    diccionario_directoInvertido_enunciado = {"directo":"La cantidad de dinero que se ahorra el comprador es","invertido":"El nuevo precio del producto es"}
    diccionario_directoInvertido_respuesta = {"directo":Racional(p*n/100,cargar_decimal=choice([True,False])), "invertido":Racional(n-p*n/100,cargar_decimal=choice([True,False]))}
    #===============================================Aquí va el número del ejercicio y el enunciado.
    enunciado = f"Un{choice([' televisor', 'a bicicleta', 'a nintendo wii', ' computador'])} cuesta {Matematica(n)} dólares, pero al día siguiente tiene una rebaja del {Matematica(p)}\\%. "+diccionario_directoInvertido_enunciado[directo_invertido_1]
    #===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
    contenido_correcto = Matematica(diccionario_directoInvertido_respuesta[directo_invertido_1]) + " dólares"
    contenido_2 = Matematica(diccionario_directoInvertido_respuesta[directo_invertido_2]) + " dólares"
    contenido_3 = Matematica(Racional(n*p)) + " dólares"
    contenido_4 = Matematica(Racional(n+p,100,True)) + " dólares"
    contenido_5 = Matematica(n*(100-p)) + " dólares"




elif opcion==2:
    p = Racional(randrange(1,100))
    n = Racional(randrange(100,1000))
    while (p*n/100).denominador!=1:
        p = Racional(randrange(1,100))
        n = Racional(randrange(100,1000))
    lista_provisional = ["directo","invertido"]
    shuffle(lista_provisional)
    directo_invertido_1 = lista_provisional[0]
    directo_invertido_2 = lista_provisional[1]
    diccionario_directoInvertido_enunciado = {"directo":"La cantidad de motoos presentes en el estacionamiento es","invertido":"La cantidad de automóviles presentes en el estacionamiento es"}
    diccionario_directoInvertido_respuesta = {"directo":Racional(p*n/100,cargar_decimal=choice([True,False])), "invertido":Racional(n-p*n/100,cargar_decimal=choice([True,False]))}
    #===============================================Aquí va el número del ejercicio y el enunciado.
    enunciado = f"En un estacionamiento hay {n} vehículos, de los cuales el {p}\\% son motos y el resto son automóviles. "+diccionario_directoInvertido_enunciado[directo_invertido_1]
    #===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
    contenido_correcto = Matematica(diccionario_directoInvertido_respuesta[directo_invertido_1])
    contenido_2 = Matematica(diccionario_directoInvertido_respuesta[directo_invertido_2])
    contenido_3 = Matematica(Racional(n*p))
    contenido_4 = Matematica(Racional(n+p,100,True))
    contenido_5 = Matematica(n*(100-p))




elif opcion==3:
    p = Racional(randrange(1,100))
    n = Racional(randrange(100,1000))
    while (p*n/100).denominador!=1:
        p = Racional(randrange(1,100))
        n = Racional(randrange(100,1000))
    lista_provisional = ["directo","invertido"]
    shuffle(lista_provisional)
    directo_invertido_1 = lista_provisional[0]
    directo_invertido_2 = lista_provisional[1]
    diccionario_directoInvertido_enunciado = {"directo":"acertará","invertido":"fallará"}
    diccionario_directoInvertido_respuesta = {"directo":Racional(p*n/100,cargar_decimal=choice([True,False])), "invertido":Racional(n-p*n/100,cargar_decimal=choice([True,False]))}
    #===============================================Aquí va el número del ejercicio y el enunciado.
    enunciado = f"{choice(['Michael Jordan', 'Lebron James', 'Kevin Durant', 'Derrick Rose'])} acierta el {p}\\% de sus tiros. Si este jugador lanza {n} pelotas, entonces "+diccionario_directoInvertido_enunciado[directo_invertido_1]
    #===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
    contenido_correcto = Matematica(diccionario_directoInvertido_respuesta[directo_invertido_1]) + " lanzamientos"
    contenido_2 = Matematica(diccionario_directoInvertido_respuesta[directo_invertido_2]) + " lanzamientos"
    contenido_3 = Matematica(Racional(n*p)) + " lanzamientos"
    contenido_4 = Matematica(Racional(n+p,100,True)) + " lanzamientos"
    contenido_5 = Matematica(n*(100-p)) + " lanzamientos"





elif opcion==4:
    p = Racional(randrange(1,100))
    n = Racional(randrange(100,1000))
    while (p*n/100).denominador!=1:
        p = Racional(randrange(1,100))
        n = Racional(randrange(100,1000))
    lista_provisional = ["directo","invertido"]
    shuffle(lista_provisional)
    directo_invertido_1 = lista_provisional[0]
    directo_invertido_2 = lista_provisional[1]
    diccionario_directoInvertido_enunciado = {"directo":"correctas","invertido":"erradas"}
    diccionario_directoInvertido_respuesta = {"directo":Racional(p*n/100,cargar_decimal=choice([True,False])), "invertido":Racional(n-p*n/100,cargar_decimal=choice([True,False]))}
    #===============================================Aquí va el número del ejercicio y el enunciado.
    enunciado = f"{choice(['Byron', 'Michael', 'Jonathan', 'Brayatan'])} respondió bien al {p}\\% de las preguntas de una prueba de {n} preguntas. La cantidad de respuestas "+diccionario_directoInvertido_enunciado[directo_invertido_1]+" que tuvo es"
    #===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
    contenido_correcto = Matematica(diccionario_directoInvertido_respuesta[directo_invertido_1])
    contenido_2 = Matematica(diccionario_directoInvertido_respuesta[directo_invertido_2])
    contenido_3 = Matematica(Racional(n*p))
    contenido_4 = Matematica(Racional(n+p,100,True))
    contenido_5 = Matematica(n*(100-p))






elif opcion==5:
    p = Racional(randrange(1,100))
    n = Racional(randrange(100,1000))
    while (p*n/100).denominador!=1:
        p = Racional(randrange(1,100))
        n = Racional(randrange(100,1000))
    lista_provisional = ["directo","invertido"]
    shuffle(lista_provisional)
    directo_invertido_1 = lista_provisional[0]
    directo_invertido_2 = lista_provisional[1]
    diccionario_directoInvertido_enunciado = {"directo":"El valor total del pan es","invertido":"El vuelto que el vendedor le tiene que dar a la señora es"}
    diccionario_directoInvertido_respuesta = {"directo":Racional(p*n/100,cargar_decimal=choice([True,False])), "invertido":Racional(n-p*n/100,cargar_decimal=choice([True,False]))}
    #===============================================Aquí va el número del ejercicio y el enunciado.
    enunciado = f"Una señora le entregó {n} dólares al vendedor de pan. Mientras esperaba su vuelto el vendedor le dice \""+choice([f"El precio total del pan corresponde al {p}",f"El vuelto que tengo que entregarle corresponde al {100-p}"])+"\\% de lo que me entregó\". "+diccionario_directoInvertido_enunciado[directo_invertido_1]
    #===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
    contenido_correcto = Matematica(diccionario_directoInvertido_respuesta[directo_invertido_1])+" dólares"
    contenido_2 = Matematica(diccionario_directoInvertido_respuesta[directo_invertido_2])+" dólares"
    contenido_3 = Matematica(Racional(n*p))+" dólares"
    contenido_4 = Matematica(Racional(n+p,100,True))+" dólares"
    contenido_5 = Matematica(n*(100-p))+" dólares"






enunciado_oculto = [opcion,n,p]











