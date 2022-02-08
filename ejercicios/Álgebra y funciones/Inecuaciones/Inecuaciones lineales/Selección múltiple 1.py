{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
diccionario_simbolos_invertidos = {r"\leq ":r"\geq ", r"\geq ":r"\leq ", "<":">", ">":"<"}
simbolo = choice(list(diccionario_simbolos_invertidos))
letra = choice(["x", "y", "z"])

suma_de_numeros_sin_letra = 0
polinomio_de_terminos_sin_letra = []
for i in range(0, randrange(1,6)):
    numero = elegir(-9,9, 0)
    suma_de_numeros_sin_letra += Racional(numero)
    polinomio_de_terminos_sin_letra.append(numero)

suma_de_numeros_con_letra = 0
polinomio_de_terminos_con_letra = []
for i in range(0, randrange(1,6)):
    numero = elegir(-9,9, 0)
    suma_de_numeros_con_letra += numero
    polinomio_de_terminos_con_letra.append(Term(numero, letra))
while suma_de_numeros_con_letra==0:
    suma_de_numeros_con_letra = 0
    polinomio_de_terminos_con_letra = []
    for i in range(0, randrange(1,6)):
        numero = elegir(-9,9, 0)
        suma_de_numeros_con_letra += numero
        polinomio_de_terminos_con_letra.append(Term(numero, letra))

#================================Aquí va el enunciado================================================================
enunciado = fr"""¿Cuál es la inecuación que se obtiene al despejar {letra} en la siguiente inecuación?
\begin{{center}}
{Matematica(ecuacion_azar(lista_de_terminos=polinomio_de_terminos_con_letra+polinomio_de_terminos_sin_letra, simbolo=simbolo), arreglar_espacios=False)}
\end{{center}}"""

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
if suma_de_numeros_con_letra<0:
    simbolo = diccionario_simbolos_invertidos[simbolo]
contenido_correcto = Matematica(letra+simbolo+(-suma_de_numeros_sin_letra/suma_de_numeros_con_letra), arreglar_espacios=False)
contenido_2 = Matematica(letra+diccionario_simbolos_invertidos[simbolo]+(-suma_de_numeros_sin_letra/suma_de_numeros_con_letra), arreglar_espacios=False)
contenido_3 = Matematica(letra+simbolo+(suma_de_numeros_sin_letra/suma_de_numeros_con_letra), arreglar_espacios=False)
contenido_4 = Matematica(letra+diccionario_simbolos_invertidos[simbolo]+(suma_de_numeros_sin_letra/suma_de_numeros_con_letra), arreglar_espacios=False)
contenido_5 = Matematica(letra+choice([simbolo,diccionario_simbolos_invertidos[simbolo]])+(choice([-1,1])*suma_de_numeros_sin_letra*suma_de_numeros_con_letra), arreglar_espacios=False)


enunciado_oculto = [polinomio_de_terminos_sin_letra, polinomio_de_terminos_con_letra]












