{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
lista_de_notas = []
for i in range(0, elegir(3,9, 7)):
    lista_de_notas.append(Racional(randrange(10,71)))
suma_de_notas = 0
for nota in lista_de_notas:
    suma_de_notas = suma_de_notas+nota
promedio = suma_de_notas/len(lista_de_notas)
while promedio.denominador!=1:
    lista_de_notas = []
    for i in range(0, elegir(3,9, 7)):
        lista_de_notas.append(Racional(randrange(10,71)))
    suma_de_notas = 0
    for nota in lista_de_notas:
        suma_de_notas = suma_de_notas+nota
    promedio = suma_de_notas/len(lista_de_notas)

nota_faltante = lista_de_notas[-1]
suma_incompleta = suma_de_notas-nota_faltante

lista_de_nombres = ["Aarón", "Ander", "Joaquín", "Abel", "Andrés", "Joel", "Abelardo", "Ángel", "Jon", "Abraham", "Aníbal", "Jordi", "Adalberto", "Antonio", "Jorge", "Adam", "Arnau", "José", "Adán", "Arturo", "Jose", "Antonio", "Adiran", "Asier", "Jose", "Luis", "Adolfo", "Augusto", "Jose", "Manuel", "Adrià", "Aurelio", "Jose", "Maria", "Adrián", "Baltasar", "Juan", "Agustín", "Bartolomé", "Blas", "Aimar", "Basilio", "Juan", "Antonio", "Aitor", "Benito", "Boris", "Alano", "Benjamín", "Juan", "Carlos", "Alberto", "Bernardo", "Borja", "Aldo", "Brahim", "Aleix", "Blas", "Brais", "Alejandro", "Boris", "Bruno", "Alejo", "Borja", "Calisto", "Alex", "Brahim", "Juan", "José", "Alfonso", "Brais", "Camilo", "Alfredo", "Bruno", "Juan", "Manuel", "Alonso", "Calisto", "Carlos", "Álvaro", "Camilo", "Julio", "Amadeo", "Carlos", "Cayetano", "Amado", "Cayetano", "César","Amando", "César", "Christian", "Ambrosio", "Christian", "Claudio", "Amin", "Claudio", "Clemente", "Anastasio", "Clemente", "Conrado", "Ander", "Conrado", "Constantino"]
nombre_1 = choice(lista_de_nombres)

lista_de_asignaturas = ["Matemática", "Lenguaje", "Psicología", "Educación física", "Religión"]
asignatura_1 = choice(lista_de_asignaturas)



#================================Aquí va el enunciado================================================================
enunciado = fr"""{nombre_1} obtuvo las siguientes notas en la asignatura {asignatura_1}
\begin{{center}}
"""
numeros = lista_de_notas[0]
for i in lista_de_notas[1:-1]:
    numeros = numeros +r";  " + i
enunciado += Matematica(numeros, arreglar_espacios=True)+fr"""
\end{{center}} 
Si quiere que su promedio sea {promedio} entonces su siguiente nota debe ser"""

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(nota_faltante)
contenido_2 =        Matematica(Racional(abs(len(lista_de_notas)-1)*promedio-(suma_incompleta),cargar_decimal=True))
contenido_3 =        Matematica(Racional(abs(len(lista_de_notas)+1)*promedio-(suma_incompleta),cargar_decimal=True))
contenido_4 =        Matematica(Racional(suma_incompleta/len(lista_de_notas)-1,cargar_decimal=True))
contenido_5 =        Matematica(Racional(suma_incompleta/len(lista_de_notas),cargar_decimal=True))



enunciado_oculto = sorted(lista_de_notas)











