{"cantidad_opciones":1, "cantidad_disponible":50}
#Arreglar para poder escribir mejor las respuestas debido a la ausencia de puntos de multiplicación, por esto no puedo poner dos bases numéricas
#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
while True:
    cantidad_numeros = choice([0,1])
    cantidad_letras = choice([1,2,3])
    if cantidad_letras+cantidad_numeros in [2,3]:
        break

lista_bases_numericas = ["2","3","5","6","7","8"]
lista_bases_literales = ["a","b","c","x","y","z"]
shuffle(lista_bases_numericas)
shuffle(lista_bases_literales)
lista_bases_numericas = lista_bases_numericas[:cantidad_numeros]
lista_bases_literales = lista_bases_literales[:cantidad_letras]

while True:
    lista_exponentes_numerador = []
    lista_exponentes_denominador = []
    lista_terminos_numerador = []
    lista_terminos_denominador = []

    for base in lista_bases_numericas+lista_bases_literales:
        repeticiones_numerador = choice([1,2,3])
        repeticiones_denominador = choice([1,2,3])
        for _ in range(0,repeticiones_numerador):
            lista_terminos_numerador.append(Term(1,{str(base):elegir(-9,10,0)}))
        for _ in range(0,repeticiones_denominador):
            lista_terminos_denominador.append(Term(1,{str(base):elegir(-9,10,0)}))
    
    if len(lista_terminos_numerador)<=6 and len(lista_terminos_denominador)<=6:
        break

shuffle(lista_terminos_numerador)
shuffle(lista_terminos_denominador)




#================================Aquí va el enunciado================================================================
enunciado_numerador = str(lista_terminos_numerador[0])
for termino_numerador in lista_terminos_numerador[1:]:
    enunciado_numerador += r"\cdot " + str(termino_numerador)

enunciado_denominador = str(lista_terminos_denominador[0])
for termino_denominador in lista_terminos_denominador[1:]:
    enunciado_denominador += r"\cdot " + str(termino_denominador)

enunciado = Matematica(fraccion(enunciado_numerador,enunciado_denominador)    +"=")



#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
termino_final = lista_terminos_numerador[0]
for termino in lista_terminos_numerador[0:]:
    termino_final = termino_final*termino
for termino in lista_terminos_denominador:
    termino_final = termino_final/termino
contenido_correcto = Matematica(termino_final)


termino_final = lista_terminos_numerador[0]
for termino in lista_terminos_numerador[0:]:
    termino_final = termino_final*termino
for termino in lista_terminos_denominador:
    termino_final = termino_final*termino
contenido_2 = Matematica(termino_final) #Sumó los exponentes de abajo


termino_final = lista_terminos_numerador[0]
for termino in lista_terminos_numerador[0:]:
    termino_final = termino_final/termino
for termino in lista_terminos_denominador:
    termino_final = termino_final*termino
contenido_3 = Matematica(termino_final) #Restó los de arriba y sumó los de abajo

termino_final = lista_terminos_numerador[0]
for termino in lista_terminos_numerador[0:]:
    termino_final = termino_final/termino
for termino in lista_terminos_denominador:
    termino_final = termino_final/termino
contenido_4 = Matematica(termino_final) #Restó los de arriba y los de abajo


termino_final = lista_terminos_numerador[0]
for termino in lista_terminos_numerador[0:]+lista_terminos_denominador:
    termino_final = choice([termino_final*termino, termino_final/termino])
contenido_5 = Matematica(termino_final) #Sumó o restó ignorando las propiedades (calculado al azar)




enunciado_oculto = [lista_terminos_numerador,lista_terminos_denominador]












