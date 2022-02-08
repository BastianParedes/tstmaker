{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
diccionario_coloquial_simbolico = {
r"El doble de un número puede representarse como" :                 [r"2x", r"2x"],
r"El triple de un número puede representarse como" :                [r"3x"],
r"El cuádruple de un número puede representarse como" :             [r"4x"],

r"Un número par puede representarse como" :                         [r"2x", r"2x"],
r"Un número impar puede representarse como" :                       [r"2x+1"],

r"Un múltiplo de $9$ puede representarse como" :                    [r"9x"],
r"Un múltiplo de $10$ puede representarse como" :                   [r"10x"],
r"Un múltiplo de $11$ puede representarse como" :                   [r"11x"],
r"Un múltiplo de $12$ puede representarse como" :                   [r"12x"],

r"La mitad de un número puede representarse como" :                 [r"\dfrac{x}{2}", r"\dfrac{50x}{100}"],
r"Un tercio de un número puede representarse como" :                [r"\dfrac{x}{3}"],
r"Un cuarto de un número puede representarse como" :                [r"\dfrac{x}{4}"],
r"Un quinto de un número puede representarse como" :                [r"\dfrac{x}{5}"],

r"El $10\%$ de un número puede representarse como" :                [r"\dfrac{10x}{100}"],
r"El $50\%$ de un número puede representarse como" :                [r"\dfrac{50x}{100}", r"\dfrac{x}{2}"],
r"El $75\%$ de un número puede representarse como" :                [r"\dfrac{75x}{100}"],

r"El sucesor de un número puede representarse como" :               [r"x+1"],
r"El sucesor del sucesor de un número puede representarse como" :   [r"x+2"],
r"El antecesor de un número puede representarse como" :             [r"x-1"],
r"El antecesor del antecesor de un número puede representarse como":[r"x-2"],

r"La suma de dos números puede representarse como" :                [r"x+y"],
r"La resta de dos números puede representarse como" :               [r"x-y"],
r"El producto de dos números puede representarse como" :            [r"xy"],
r"El cociente entre dos números puede representarse como" :         [r"\dfrac{x}{y}"],

r"Un número aumentado en $5$ puede representarse como" :            [r"x+5"],
r"Un número aumentado en $6$ puede representarse como" :            [r"x+6"],
r"Un número aumentado en $7$ puede representarse como" :            [r"x+7"],
r"Un número aumentado en $8$ puede representarse como" :            [r"x+8"],
r"Un número disminuido en $5$ puede representarse como" :           [r"x-5"],
r"Un número disminuido en $6$ puede representarse como" :           [r"x-6"],
r"Un número disminuido en $7$ puede representarse como" :           [r"x-7"],
r"Un número disminuido en $8$ puede representarse como" :           [r"x-8"],
r"Un número multiplicado por $5$ puede representarse como" :        [r"5x"],
r"Un número multiplicado por $6$ puede representarse como" :        [r"6x"],
r"Un número multiplicado por $7$ puede representarse como" :        [r"7x"],
r"Un número multiplicado por $8$ puede representarse como" :        [r"8x"],
r"Un número dividido entre $5$ puede representarse como" :          [r"\dfrac{x}{5}"],
r"Un número dividido entre $6$ puede representarse como" :          [r"\dfrac{x}{6}"],
r"Un número dividido entre $7$ puede representarse como" :          [r"\dfrac{x}{7}"],
r"Un número dividido entre $8$ puede representarse como" :          [r"\dfrac{x}{8}"],

r"Un número multiplicado por su sucesor puede representarse como" : [r"x\cdot (x+1)"],

r"La suma de dos números es igual a 1 puede representarse como" :                           [r"x+y=1"],
r"Un número disminuido en 2 es igual a otro número puede representarse como" :              [r"x-2=y"],
r"El producto de dos números es igual al antecesor del primero puede representarse como" :  [r"x\cdot y=x-1"],
r"El producto de dos números es igual al sucesor del primero puede representarse como" :    [r"x\cdot y=x+1"],
r"La resta entre dos números es igual a 4 puede representarse como" :                       [r"x-y=4"],
r"El cociente entre dos números es igual 6 puede representarse como" :                      [r"\dfrac{x}{y}=6"],
r"La suma de dos números es igual al producto de dichos números puede representarse como" : [r"x+y=x\cdot y"],
r"Un número disminuido en 3 es igual a 7 puede representarse como" :                        [r"x-3=7"],
r"La mitad de un número es igual a otro puede representarse como" :                         [r"\dfrac{x}{2}=y"]}

lista_de_simbolos = []
for coloquial in list(diccionario_coloquial_simbolico):
    lista_de_simbolos.append(diccionario_coloquial_simbolico[coloquial][0])

#================================Aquí va el enunciado================================================================
enunciado = choice(list(diccionario_coloquial_simbolico))

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(diccionario_coloquial_simbolico[enunciado][0], arreglar_espacios=False)

for simbolo in diccionario_coloquial_simbolico[enunciado]:
    while simbolo in lista_de_simbolos:
        lista_de_simbolos.remove(simbolo)
    
contenido_2 = choice(lista_de_simbolos)
lista_de_simbolos.remove(contenido_2)
contenido_3 = choice(lista_de_simbolos)
lista_de_simbolos.remove(contenido_3)
contenido_4 = choice(lista_de_simbolos)
lista_de_simbolos.remove(contenido_4)
contenido_5 = choice(lista_de_simbolos)
lista_de_simbolos.remove(contenido_5)

contenido_2, contenido_3, contenido_4, contenido_5 = Matematica(contenido_2, arreglar_espacios=False), Matematica(contenido_3, arreglar_espacios=False), Matematica(contenido_4, arreglar_espacios=False), Matematica(contenido_5, arreglar_espacios=False)





enunciado_oculto = enunciado











