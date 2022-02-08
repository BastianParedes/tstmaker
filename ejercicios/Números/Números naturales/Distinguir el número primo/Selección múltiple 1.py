{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
numeros_compuestos = list(range(0,40))
for primo in [2,3,5,7,11,13,17,19,23,29,31,37]:
    numeros_compuestos.remove(primo)

#================================Aquí va el enunciado================================================================
enunciado = "De los siguiente números, ¿cuál es un número primo?"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(choice([2,3,5,7,11,13,17,19,23,29,31,37]))

contenido_2 = choice(numeros_compuestos)
numeros_compuestos.remove(contenido_2)
contenido_3 = choice(numeros_compuestos)
numeros_compuestos.remove(contenido_3)
contenido_4 = choice(numeros_compuestos)
numeros_compuestos.remove(contenido_4)
contenido_5 = choice(numeros_compuestos)



enunciado_oculto = [contenido_correcto, contenido_2, contenido_3, contenido_4, contenido_5]










