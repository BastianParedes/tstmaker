{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
lista_de_datos = []
for _ in range(0, randrange(3, 8)):
    lista_de_datos.append(Racional(randrange(0, 20)))
suma_de_todos_los_datos = Racional(0)
for dato in lista_de_datos:
    suma_de_todos_los_datos = suma_de_todos_los_datos+dato
promedio = Racional(suma_de_todos_los_datos, len(lista_de_datos), True)
while promedio.denominador!=1:
    lista_de_datos = []
    for _ in range(0, randrange(3, 8)):
        lista_de_datos.append(Racional(randrange(0, 20)))
    suma_de_todos_los_datos = Racional(0)
    for dato in lista_de_datos:
        suma_de_todos_los_datos = suma_de_todos_los_datos+dato
    promedio = Racional(suma_de_todos_los_datos, len(lista_de_datos), True)

varianza = 0
desviacion_media = 0
for dato in lista_de_datos:
    varianza += (dato-promedio)**2/len(lista_de_datos)
    desviacion_media += abs(dato-promedio)/len(lista_de_datos)
desviacion_estandar = Root(varianza)

#================================Aquí va el enunciado================================================================
enunciado = fr"""Observa el siguiente conjunto de datos
\begin{{center}}
"""
numeros = lista_de_datos[0]
for dato in lista_de_datos[1:]:
    numeros = numeros +r";  " + dato
enunciado += Matematica(numeros, arreglar_espacios=True)+fr"""
\end{{center}}
El rango de este conjunto es"""
#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(max(lista_de_datos)-min(lista_de_datos))
contenido_2 = Matematica(desviacion_estandar) #Calcula la desviacion estándar
contenido_3 = Matematica(promedio) #Calcula el promedio
contenido_4 = Matematica(varianza) #Calcula la varianza
contenido_5 = Matematica(desviacion_media) #Calcula la desviación media



enunciado_oculto = sorted(lista_de_datos)











