{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
amplitud = Racional(randrange(3, 20))
cantidad_de_limites = randrange(3, 6)
limites_menores = [Racional(randrange(2, 20))]
for i in range(1, cantidad_de_limites):
    limites_menores.append(limites_menores[0]+amplitud*i)
limites_mayores = []
marcas_de_clase = []
for limite_menor in limites_menores:
    limites_mayores.append(limite_menor+amplitud)
    marcas_de_clase.append(limite_menor+amplitud/2)

lista_de_frecuencias = []
suma_de_frecuencias = 0
for _ in range(0, cantidad_de_limites):
    lista_de_frecuencias.append(randrange(1, 10))
    suma_de_frecuencias += lista_de_frecuencias[-1]

promedio = Racional(0)
for i in range(0, cantidad_de_limites):
    promedio += marcas_de_clase[i]*lista_de_frecuencias[i]/suma_de_frecuencias



while promedio.denominador!=1:
    amplitud = Racional(randrange(3, 20))
    cantidad_de_limites = randrange(3, 6)
    limites_menores = [Racional(randrange(2, 20))]
    for i in range(1, cantidad_de_limites):
        limites_menores.append(limites_menores[0]+amplitud*i)
    limites_mayores = []
    marcas_de_clase = []
    for limite_menor in limites_menores:
        limites_mayores.append(limite_menor+amplitud)
        marcas_de_clase.append(limite_menor+amplitud/2)

    lista_de_frecuencias = []
    suma_de_frecuencias = 0
    for _ in range(0, cantidad_de_limites):
        lista_de_frecuencias.append(randrange(1, 10))
        suma_de_frecuencias += lista_de_frecuencias[-1]

    promedio = Racional(0)
    for i in range(0, cantidad_de_limites):
        promedio += marcas_de_clase[i]*lista_de_frecuencias[i]/suma_de_frecuencias





#================================Aquí va el enunciado================================================================
enunciado = fr"""A continuación se muestra una tabla de datos agrupados y sus respectivas frecuencias aboslutas
\begin{{center}} \begin{{tabular}}{{|c|c|}} \hline
{Matematica(sub("I","i"))}&{Matematica(sub("f","i"))}\\ \hline
"""
if choice([1,2])==1:
    parentesis_izquierdo = r"\left["
    parentesis_derecho = r"\right["
else:
    parentesis_izquierdo = r"\left]"
    parentesis_derecho = r"\right]"

for fila in range(0,cantidad_de_limites):
    enunciado += fr"${parentesis_izquierdo}{limites_menores[fila]},\ {limites_mayores[fila]}{parentesis_derecho}$&${lista_de_frecuencias[fila]}$\\ \hline"+"\n"
enunciado += fr"""\end{{tabular}} \end{{center}}
{choice(["La media aritmética", "El promedio"])} de este conjunto es"""

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(promedio)
contenido_2 = Matematica((limites_menores[0]+limites_mayores[-1])/2)
contenido_3 = Matematica((limites_menores[0]+limites_menores[-1])/2)
contenido_4 = Matematica((limites_mayores[0]+limites_mayores[-1])/2)
contenido_5 = Matematica(promedio*suma_de_frecuencias)



enunciado_oculto = [amplitud, cantidad_de_limites, limites_menores[0]]











