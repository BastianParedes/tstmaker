from Definiciones import *

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
casos_de_perpendicularidad = [
    "Las dos tablas que forman la cruz de Jesus",
    "La vía de un auto y su paso peatonal",
    "Esquinas de las ventanas",
    "Esquinas de la calle",
    "La letra L",
    "La letra T",
    "Ejes del plano cartesiano"
]

casos_de_no_perpendicularidad = [
    "Las dos vías del tren",
    "Las tablas que unen las vías del tren",
    "Los postes de luz",
    "Las vías de los autos en las autopistas",
    "Los peldaños de las escaleras",
    "Veredas en lados contrarios",
    "Dos filas de personas que están una al lado de la otra",
    "Símbolo de pausa de un video",
    "Piernas de una persona parada y estirada",
    "Dos faros, uno al lado del otro",
    "Dedos estirados de una persona",
    "Patas de una mesa de cuatro patas",
    "Patas de una silla de cuatro patas",
    "Las dos filas de asientos a los costados de las micros",

    "Las dos ruedas de una bicicleta",
    "Collar de mascota",
    "Muñequera",
    "Colgante"
]

#================================Aquí va el enunciado================================================================
enunciado = "¿En cuál de las siguientes situaciones, lugares u objetos se identifican dos lineas perpendiculares?"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = choice(casos_de_perpendicularidad)
contenido_2 = choice(casos_de_no_perpendicularidad)
casos_de_no_perpendicularidad.remove(contenido_2)
contenido_3 = choice(casos_de_no_perpendicularidad)
casos_de_no_perpendicularidad.remove(contenido_3)
contenido_4 = choice(casos_de_no_perpendicularidad)
casos_de_no_perpendicularidad.remove(contenido_4)
contenido_5 = choice(casos_de_no_perpendicularidad)
casos_de_no_perpendicularidad.remove(contenido_5)


enunciado_oculto = contenido_correcto
