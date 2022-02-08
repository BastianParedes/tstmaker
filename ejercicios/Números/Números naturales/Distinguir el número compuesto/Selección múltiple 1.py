{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
numeros_primos = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

numeros_compuestos = list(range(2,101))
for primo in numeros_primos:
    numeros_compuestos.remove(primo)

#================================Aquí va el enunciado================================================================
enunciado = "De los siguiente números, ¿cuál es un número compuesto?"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(choice(numeros_compuestos))

contenido_2 = choice(numeros_primos)
numeros_primos.remove(contenido_2)
contenido_3 = choice(numeros_primos)
numeros_primos.remove(contenido_3)
contenido_4 = choice(numeros_primos)
numeros_primos.remove(contenido_4)
contenido_5 = choice(numeros_primos)



enunciado_oculto = [contenido_correcto]










