{"cantidad_opciones":2, "cantidad_disponible":50}

def transformar_unidad(distancia_en_metros, unidad_de_medida):
    distancia_en_metros = Racional(distancia_en_metros)
    if unidad_de_medida=="mm":
        return Matematica(Racional(distancia_en_metros*1000,cargar_decimal=True)+" mm")
    elif unidad_de_medida=="cm":
        return Matematica(Racional(distancia_en_metros*100,cargar_decimal=True)+" cm")
    elif unidad_de_medida=="m":
        return Matematica(Racional(distancia_en_metros,cargar_decimal=True)+" m")
    elif unidad_de_medida=="km":
        return Matematica(Racional(distancia_en_metros,1000,cargar_decimal=True)+" km")

#===================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras============
lista_de_distancias = list(range(500,1000))
distancia_1 = choice(lista_de_distancias)
lista_de_distancias.remove(distancia_1)
distancia_2 = choice(lista_de_distancias)
lista_de_distancias.remove(distancia_2)
distancia_3 = choice(lista_de_distancias)
lista_de_distancias.remove(distancia_3)
distancia_4 = choice(lista_de_distancias)
lista_de_distancias.remove(distancia_4)
distancia_5 = choice(lista_de_distancias)

lista_de_nombres = ["María", "Carmen", "Josefa", "Ana", "Isabel", "Pilar", "Dolores", "Laura", "Teresa", "Antonio", "José", "Manuel", "Francisco", "David", "Juan", "Javier", "Luis", "Daniel"]
nombre_1 = choice(lista_de_nombres)
lista_de_nombres.remove(nombre_1)
nombre_2 = choice(lista_de_nombres)
lista_de_nombres.remove(nombre_2)
nombre_3 = choice(lista_de_nombres)
lista_de_nombres.remove(nombre_3)
nombre_4 = choice(lista_de_nombres)
lista_de_nombres.remove(nombre_4)
nombre_5 = choice(lista_de_nombres)

unidades_de_medida = ["mm", "cm", "m", "km"]
unidad_1, unidad_2, unidad_3, unidad_4, unidad_5 =  choice(unidades_de_medida), choice(unidades_de_medida), choice(unidades_de_medida), choice(unidades_de_medida), choice(unidades_de_medida)
lista_de_unidades_de_medida = [unidad_1, unidad_2, unidad_3, unidad_4, unidad_5]
while not 1<=lista_de_unidades_de_medida.count("mm")<=2 or not 1<=lista_de_unidades_de_medida.count("cm")<=2 or not 1<=lista_de_unidades_de_medida.count("m")<=2 or not lista_de_unidades_de_medida.count("km")<=2:
    unidad_1, unidad_2, unidad_3, unidad_4, unidad_5 =  choice(unidades_de_medida), choice(unidades_de_medida), choice(unidades_de_medida), choice(unidades_de_medida), choice(unidades_de_medida)
    lista_de_unidades_de_medida = [unidad_1, unidad_2, unidad_3, unidad_4, unidad_5]

lista_de_distancias = [distancia_1, distancia_2, distancia_3, distancia_4, distancia_5]
lista_de_nombres = [nombre_1, nombre_2, nombre_3, nombre_4, nombre_5]
diccionario_distancia_nombre = {}
for i in range(0, 5):
    diccionario_distancia_nombre[lista_de_distancias[i]] = lista_de_nombres[i]
lista_de_distancias = sorted(lista_de_distancias)


if opcion==1:
    #===================================Aquí va el número del ejercicio y el enunciado.=========================================
    enunciado = f"5 amigos hacen una competencia corriendo toda la distancia que puedan sin detenerse. {nombre_1} corrió {transformar_unidad(distancia_1,unidad_1)}, {nombre_2} corrió {transformar_unidad(distancia_2,unidad_2)}, {nombre_3} corrió {transformar_unidad(distancia_3,unidad_3)}, {nombre_4} corrió {transformar_unidad(distancia_4,unidad_4)} y {nombre_5} corrió {transformar_unidad(distancia_5,unidad_5)}. ¿Quién corrió más?"
    #===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.=====
    contenido_correcto = diccionario_distancia_nombre[lista_de_distancias[4]]
    contenido_2 = diccionario_distancia_nombre[lista_de_distancias[3]]
    contenido_3 = diccionario_distancia_nombre[lista_de_distancias[2]]
    contenido_4 = diccionario_distancia_nombre[lista_de_distancias[1]]
    contenido_5 = diccionario_distancia_nombre[lista_de_distancias[0]]

elif opcion==2:
    #===================================Aquí va el número del ejercicio y el enunciado.=========================================
    enunciado = f"5 amigos hacen una competencia corriendo toda la distancia que puedan sin detenerse. {nombre_1} corrió {transformar_unidad(distancia_1,unidad_1)}, {nombre_2} corrió {transformar_unidad(distancia_2,unidad_2)}, {nombre_3} corrió {transformar_unidad(distancia_3,unidad_3)}, {nombre_4} corrió {transformar_unidad(distancia_4,unidad_4)} y {nombre_5} corrió {transformar_unidad(distancia_5,unidad_5)}. ¿Quién corrió menos?"
    #===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.=====
    contenido_correcto = diccionario_distancia_nombre[lista_de_distancias[0]]
    contenido_2 = diccionario_distancia_nombre[lista_de_distancias[1]]
    contenido_3 = diccionario_distancia_nombre[lista_de_distancias[2]]
    contenido_4 = diccionario_distancia_nombre[lista_de_distancias[3]]
    contenido_5 = diccionario_distancia_nombre[lista_de_distancias[4]]
    


enunciado_oculto = [lista_de_distancias, sorted(unidades_de_medida)]











