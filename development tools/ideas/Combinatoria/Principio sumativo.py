opcion = choice([1,2,3])


def completar_enunciado(cantidades, atributos, cantidad):
    shuffle(atributos)
    resultado = f"{cantidades[0]} {atributos[0]}"
    for i in range(1, cantidad):
        if i!=cantidad-1:
            resultado += f", {cantidades[i]} {atributos[i]}"
        else:
            resultado += f" y {cantidades[i]} {atributos[i]}"
    return resultado




if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    lista_de_atributos = ["motos", "bicicletas", "buses", "automóviles"]
    lista_de_atributos = lista_de_atributos[:randrange(2,len(lista_de_atributos))]
    cantidad = len(lista_de_atributos)
    cantidades = []
    for _ in range(cantidad):
        cantidades.append(randrange(2,10))    
    #================================Aquí va el enunciado================================================================
    enunciado = f"Una persona tiene que ir a otra diudad, para ello cuenta con {completar_enunciado(cantidades,lista_de_atributos,cantidad)}. La cantidad de formas en las que puede viajar es"



elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    lista_de_atributos = ["gallinas", "vacas", "cerdos", "tamaños", "resoluciones"]
    lista_de_atributos = lista_de_atributos[:randrange(2,len(lista_de_atributos))]
    cantidad = len(lista_de_atributos)
    cantidades = []
    for _ in range(cantidad):
        cantidades.append(randrange(2,10))
    #================================Aquí va el enunciado================================================================
    enunciado = f"Una persona quiere comer carne en el almuerzo, pero debe decidir qué animal matar de sus {completar_enunciado(cantidades,lista_de_atributos,cantidad)}. La cantidad de animales entre los que tiene para elegir es"



elif opcion==3:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    lista_de_atributos = ["tonalidades de rojo", "tonalidades de azul", "tonalidades de amarillo", "tonalidades de verde", "tonalidades de café"]
    lista_de_atributos = lista_de_atributos[:randrange(2,len(lista_de_atributos))]
    cantidad = len(lista_de_atributos)
    cantidades = []
    for _ in range(cantidad):
        cantidades.append(randrange(2,10))
    #================================Aquí va el enunciado================================================================
    enunciado = f"Una persona sabe qué auto quiere comprar, pero no se decide por el color. La tienda tiene {completar_enunciado(cantidades,lista_de_atributos,cantidad)}. La cantidad de autos que puede elegir la persona es"








#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = 0
contenido_2 =        1
contenido_3 =        choice([0,1])
contenido_4 =        choice([0,1])
contenido_5 =        choice([0,1])

for numero in cantidades:
    contenido_correcto += numero
    contenido_2 *=        numero
    contenido_3 =         abs(choice([contenido_3+numero, contenido_3*numero, contenido_3-numero]))
    contenido_4 =         abs(choice([contenido_4+numero, contenido_4*numero, contenido_4-numero]))
    contenido_5 =         abs(choice([contenido_5+numero, contenido_5*numero, contenido_5-numero]))

contenido_correcto = Matematica(contenido_correcto)
contenido_2 =        Matematica(contenido_2)
contenido_3 =        Matematica(contenido_3)
contenido_4 =        Matematica(contenido_4)
contenido_5 =        Matematica(contenido_5)


enunciado_oculto = sorted(cantidades)
