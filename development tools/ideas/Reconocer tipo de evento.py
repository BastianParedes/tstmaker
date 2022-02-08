#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
lista_eventos_imposibles = [
    "Obtener un 0 al lanzar un dado de 6 caras numeradas de 1 a 6.",
    "Obtener un 7 al lanzar un dado de 6 caras numeradas de 1 a 6.",
    "Que nazca un perro con alas capaz de volar.",
    "Sacar una pelota verde de una urna que tiene solo pelotas rojas.",
    "Sacar 4 pelotas de una urna que tiene 3 pelotas."
]

lista_eventos_posibles = [
    "Obtener un 1 al lanzar un dado de 6 caras numeradas de 1 a 6.",
    "Obtener un 2 al lanzar un dado de 6 caras numeradas de 1 a 6.",
    "Obtener un 3 al lanzar un dado de 6 caras numeradas de 1 a 6.",
    "Obtener un 4 al lanzar un dado de 6 caras numeradas de 1 a 6.",
    "Obtener un 5 al lanzar un dado de 6 caras numeradas de 1 a 6.",
    "Obtener un 6 al lanzar un dado de 6 caras numeradas de 1 a 6.",
    "Contagiarse el resfriado al estar cerca de alguien.",
    "Morir al sufrir un accidente de tránsito.",
    "Ganar la lotería jugando solo una vez en la vida.",
    "Sentir dolor al golpear una pared.",
    "Que alguien te crea una mentira.",
    "Decir un número y que resulte ser la edad de la persona que tienes en frente.",
    "Que el volcán más cercano erupcione en la próxima hora.",
    "Obtener la nota más alta de tu clase al responder un examen.",
    "Encontrar a un perro en una tienda de gatos"
]

lista_eventos_seguros = [
    "Obtener un número menor que 7 al lanzar un dado de 6 caras numeradas de 1 a 6.",
    "Obtener un número mayor que 0 al lanzar un dado de 6 caras numeradas de 1 a 6.",
    "Repetir de curso si todas las notas son menores a 40.",
    "Sacar una pelota verde de una urna que tiene solo pelotas verdes.",
    "Obtener la mejor nota posible en un examen al responder todo correctamente.",
    "Quemarse al nadar en agua a 100 °C.",
    "Que se genere llama cuando una chispa toca un líquido inflamable.",
]


opcion = choice([1,2,3])

if opcion==1:
    #================================Aquí va el enunciado================================================================
    enunciado = f"¿Cuál de los siguientes {choice(['sucesos','eventos'])} es imposible?"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = choice(lista_eventos_imposibles)
    contenido_2 =        choice(lista_eventos_posibles+lista_eventos_seguros)
    contenido_3 =        choice(lista_eventos_posibles+lista_eventos_seguros)
    contenido_4 =        choice(lista_eventos_posibles+lista_eventos_seguros)
    contenido_5 =        choice(lista_eventos_posibles+lista_eventos_seguros)


elif opcion==2:
    #================================Aquí va el enunciado================================================================
    enunciado = f"¿Cuál de los siguientes {choice(['sucesos','eventos'])} es posible?"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = choice(lista_eventos_posibles)
    contenido_2 =        choice(lista_eventos_imposibles+lista_eventos_seguros)
    contenido_3 =        choice(lista_eventos_imposibles+lista_eventos_seguros)
    contenido_4 =        choice(lista_eventos_imposibles+lista_eventos_seguros)
    contenido_5 =        choice(lista_eventos_imposibles+lista_eventos_seguros)


elif opcion==3:
    #================================Aquí va el enunciado================================================================
    enunciado = f"¿Cuál de los siguientes {choice(['sucesos','eventos'])} es seguro?"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = choice(lista_eventos_seguros)
    contenido_2 =        choice(lista_eventos_imposibles+lista_eventos_posibles)
    contenido_3 =        choice(lista_eventos_imposibles+lista_eventos_posibles)
    contenido_4 =        choice(lista_eventos_imposibles+lista_eventos_posibles)
    contenido_5 =        choice(lista_eventos_imposibles+lista_eventos_posibles)



enunciado_oculto = contenido_correcto
