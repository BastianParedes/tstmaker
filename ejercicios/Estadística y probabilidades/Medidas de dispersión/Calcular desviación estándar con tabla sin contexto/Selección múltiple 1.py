{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
lista_de_datos = [randrange(1,10)]
diccionario_dato_frecuencia = {lista_de_datos[0]:randrange(1,6)}
suma_de_frecuencias = diccionario_dato_frecuencia[lista_de_datos[0]]
for i in range(1, randrange(2,5)+1):
    lista_de_datos.append(lista_de_datos[0]+i)
    diccionario_dato_frecuencia[lista_de_datos[-1]] = randrange(1,6)
    suma_de_frecuencias = suma_de_frecuencias + diccionario_dato_frecuencia[lista_de_datos[-1]]
promedio = Racional(0)
for dato in lista_de_datos:
    promedio += dato*diccionario_dato_frecuencia[dato]
promedio = promedio / suma_de_frecuencias
while promedio.denominador!=1:
    lista_de_datos = [randrange(1,10)]
    diccionario_dato_frecuencia = {lista_de_datos[0]:randrange(1,6)}
    suma_de_frecuencias = diccionario_dato_frecuencia[lista_de_datos[0]]
    for i in range(1, randrange(2,5)+1):
        lista_de_datos.append(lista_de_datos[0]+i)
        diccionario_dato_frecuencia[lista_de_datos[-1]] = randrange(1,6)
        suma_de_frecuencias = suma_de_frecuencias + diccionario_dato_frecuencia[lista_de_datos[-1]]
    promedio = Racional(0)
    for dato in lista_de_datos:
        promedio += dato*diccionario_dato_frecuencia[dato]
    promedio = promedio / suma_de_frecuencias



varianza = 0
desviacion_media = 0
for dato in lista_de_datos:
    varianza += (dato-promedio)**2    *diccionario_dato_frecuencia[dato]
    desviacion_media = desviacion_media + abs(dato-promedio)    *diccionario_dato_frecuencia[dato]
varianza = varianza /suma_de_frecuencias
desviacion_media = desviacion_media /suma_de_frecuencias
desviacion_estandar = Root(varianza)

#================================Aquí va el enunciado================================================================
enunciado = fr"""A continuación se muestra una tabla con un conjunto de datos y sus respectivas frecuencias aboslutas
\begin{{center}} \begin{{tabular}}{{|c|c|}} \hline
{Matematica(sub("x","i"))}&{Matematica(sub("f","i"))}\\ \hline
"""
for dato in lista_de_datos:
    enunciado += fr"{Matematica(dato)}&{Matematica(diccionario_dato_frecuencia[dato])}\\ \hline"
enunciado += r"""\end{tabular} \end{center}
La desviación estándar de este conjunto es"""

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(desviacion_estandar)
contenido_2 = Matematica(max(lista_de_datos)-min(lista_de_datos)) #Calcula el rango
contenido_3 = Matematica(promedio) #Calcula el promedio
contenido_4 = Matematica(varianza) #Calcula la varianza
contenido_5 = Matematica(desviacion_media) #Calcula la desviación media



enunciado_oculto = diccionario_dato_frecuencia











