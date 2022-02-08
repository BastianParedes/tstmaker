{"cantidad_opciones":3, "cantidad_disponible":15}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
lista_racionales = [
    "Suma de dos números racionales",
    "Resta de dos números racionales",
    "Producto de dos números racionales",
    "Cociente de dos números racionales",
    "Potencia de base racional y exponente racional",
]

lista_irracionales = [
    "Suma de un racional con un irracional",
    "Resta de un racional con un irracional",
    "Producto de un racional distinto de 0 con un irracional",
    "Cociente entre un dividendo irracional y un  divisor racional",
]

lista_indeterminados = [
    "i-ésima raiz de un número racional, con i racional",
    "Suma de irracionales",
    "Resta de irracionales",
    "Potencia de exponente racional y base irracional",
    "Producto de un racional con un irracional",
    "Cociente entre un dividendo irracional y un  divisor irracional",
]





if opcion==1:
    shuffle(lista_racionales)
    lista_combinada = lista_irracionales + lista_indeterminados
    shuffle(lista_combinada)
    #================================Aquí va el enunciado================================================================
    enunciado = "¿En cuál de las siguientes operaciones se obtiene SIEMPRE un número racional?"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = lista_racionales[0]
    contenido_2 =        lista_combinada[0]
    contenido_3 =        lista_combinada[1]
    contenido_4 =        lista_combinada[2]
    contenido_5 =        lista_combinada[3]



elif opcion==2:
    lista_combinada = lista_racionales + lista_indeterminados
    shuffle(lista_combinada)
    shuffle(lista_irracionales)
    #================================Aquí va el enunciado================================================================
    enunciado = "¿En cuál de las siguientes operaciones se obtiene SIEMPRE un número irracional?"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = lista_irracionales[0]
    contenido_2 =        lista_combinada[0]
    contenido_3 =        lista_combinada[1]
    contenido_4 =        lista_combinada[2]
    contenido_5 =        lista_combinada[3]



elif opcion==3:
    lista_combinada = lista_racionales + lista_irracionales
    shuffle(lista_combinada)
    shuffle(lista_indeterminados)
    #================================Aquí va el enunciado================================================================
    enunciado = "¿En cuál de las siguientes operaciones no es posible afirmar que el resultado será SIEMPRE racional, o bien SIEMPRE irracional?"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = lista_indeterminados[0]
    contenido_2 =        lista_combinada[0]
    contenido_3 =        lista_combinada[1]
    contenido_4 =        lista_combinada[2]
    contenido_5 =        lista_combinada[3]



enunciado_oculto = contenido_correcto











