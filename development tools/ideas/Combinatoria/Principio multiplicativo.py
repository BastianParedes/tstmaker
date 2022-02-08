opcion = choice([1,2,3,4,5])


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
    lista_de_atributos = ["guantes", "poleras", "polerones", "sombreros", "bufandas", "pantalones", "zapatos"]
    lista_de_atributos = lista_de_atributos[:randrange(2,len(lista_de_atributos))]
    cantidad = len(lista_de_atributos)
    cantidades = []
    for _ in range(cantidad):
        cantidades.append(randrange(2,10))    
    #================================Aquí va el enunciado================================================================
    enunciado = f"Una persona tiene que completar su vestimenta, para ello cuenta con {completar_enunciado(cantidades,lista_de_atributos,cantidad)}. La cantidad de formas en las que puede completar su vestimenta es"



elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    lista_de_atributos = ["marcas", "modelos", "colores", "tamaños", "resoluciones"]
    lista_de_atributos = lista_de_atributos[:randrange(2,len(lista_de_atributos))]
    cantidad = len(lista_de_atributos)
    cantidades = []
    for _ in range(cantidad):
        cantidades.append(randrange(2,10))
    #================================Aquí va el enunciado================================================================
    enunciado = f"Una persona quiere comprar un televisor, pero la tienda tiene {completar_enunciado(cantidades,lista_de_atributos,cantidad)}. La cantidad de opciones disponibles para el comprador es"



elif opcion==3:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    lista_de_atributos = ["tipos de queso", "grosores de masa", "ingredientes", "salsas"]
    lista_de_atributos = lista_de_atributos[:randrange(2,len(lista_de_atributos))]
    cantidad = len(lista_de_atributos)
    cantidades = []
    for _ in range(cantidad):
        cantidades.append(randrange(2,10))
    #================================Aquí va el enunciado================================================================
    enunciado = f"Una persona quiere comprar una pizza, pero la tienda tiene {completar_enunciado(cantidades,lista_de_atributos,cantidad)}. La cantidad pizzas que se pueden construir es"



elif opcion==4:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    lista_de_atributos = ["procesadores", "tarjetas gráficas", "tipos de tarjetas ram", "placas madre", "gabinetes", "sistemas de RGB"]
    lista_de_atributos = lista_de_atributos[:randrange(2,len(lista_de_atributos))]
    cantidad = len(lista_de_atributos)
    cantidades = []
    for _ in range(cantidad):
        cantidades.append(randrange(2,10))
    #================================Aquí va el enunciado================================================================
    enunciado = f"Una persona quiere construir su computador, para ello va a una tienda y le ofrecen {completar_enunciado(cantidades,lista_de_atributos,cantidad)}. La cantidad computadores que se pueden armar es"



elif opcion==5:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    lista_de_atributos = ["dado de 4 caras", "dado de 6 caras", "dado de 32 caras"]
    lista_de_atributos = lista_de_atributos[:randrange(2,len(lista_de_atributos))]
    cantidad = len(lista_de_atributos)
    cantidades = [1,1,1][:cantidad]
    #================================Aquí va el enunciado================================================================
    enunciado = f"Una persona quiere saber cuántos resultados puede obtener si lanza {completar_enunciado(cantidades,lista_de_atributos,cantidad)}. La respuesta que encontró dicha persona es"
    cantidades = [4,6,32][:cantidad]






#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = 1
contenido_2 =        0
contenido_3 =        choice([0,1])
contenido_4 =        choice([0,1])
contenido_5 =        choice([0,1])

for numero in cantidades:
    contenido_correcto *= numero
    contenido_2 +=        numero
    contenido_3 =         abs(choice([contenido_3+numero, contenido_3*numero, contenido_3-numero]))
    contenido_4 =         abs(choice([contenido_4+numero, contenido_4*numero, contenido_4-numero]))
    contenido_5 =         abs(choice([contenido_5+numero, contenido_5*numero, contenido_5-numero]))

contenido_correcto = Matematica(contenido_correcto)
contenido_2 =        Matematica(contenido_2)
contenido_3 =        Matematica(contenido_3)
contenido_4 =        Matematica(contenido_4)
contenido_5 =        Matematica(contenido_5)


enunciado_oculto = sorted(cantidades)
