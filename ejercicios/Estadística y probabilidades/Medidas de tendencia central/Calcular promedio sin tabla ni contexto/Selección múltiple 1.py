{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
lista_de_elementos = []
for dato in range(0, randrange(3, 8)):
    lista_de_elementos.append(Racional(randrange(0, 20)))
suma_de_todos_los_elementos = Racional(0)
for dato in lista_de_elementos:
    suma_de_todos_los_elementos = suma_de_todos_los_elementos+dato
promedio = Racional(suma_de_todos_los_elementos, len(lista_de_elementos), True)
while promedio.denominador!=1:
    lista_de_elementos = []
    for dato in range(0, randrange(2, 7)):
        lista_de_elementos.append(Racional(randrange(0, 20)))
    suma_de_todos_los_elementos = Racional(0)
    for dato in lista_de_elementos:
        suma_de_todos_los_elementos = suma_de_todos_los_elementos+dato
    promedio = Racional(suma_de_todos_los_elementos, len(lista_de_elementos), True)

varianza = 0
desviacion_media = 0
for dato in lista_de_elementos:
    varianza += (dato-promedio)**2/len(lista_de_elementos)
    desviacion_media += abs(dato-promedio)/len(lista_de_elementos)
desviacion_estandar = Root(varianza)

#================================Aquí va el enunciado================================================================
enunciado = fr"""Observa el siguiente conjunto de datos
\begin{{center}}
"""
numeros = str(lista_de_elementos[0])
for dato in lista_de_elementos[1:]:
    numeros = numeros +r";  " + str(dato)
enunciado += Matematica(numeros, arreglar_espacios=True)+fr"""
\end{{center}}
{choice(["El promedio de este conjunto es", "La media aritmética de este conjunto es"])}"""
#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(promedio)
contenido_2 = Matematica(suma_de_todos_los_elementos) #Suma todos los datos, pero no los divide
contenido_3 = Matematica(desviacion_estandar) #Calcula la desviación estandar
contenido_4 = Matematica(varianza) #Calcula la varianza
contenido_5 = Matematica(desviacion_media) #Calcula la desviación media



enunciado_oculto = sorted(lista_de_elementos)











