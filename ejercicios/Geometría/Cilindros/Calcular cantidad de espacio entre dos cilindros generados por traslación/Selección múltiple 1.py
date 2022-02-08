{"cantidad_opciones":1, "cantidad_disponible":50}

radio_menor, h = Racional(randrange(2,10)), Racional(randrange(2,10))
radio_mayor = radio_menor+Racional(randrange(1,10))
unidad_de_medida = choice(["mm", "cm", "m", "km"])
radio_menor_dibujo = randrange(5,15)/10
radio_mayor_dibujo = radio_menor_dibujo+randrange(5,15)/10

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
r, h = Racional(randrange(1, 11)), Racional(randrange(1, 11))
#================================Aquí va el enunciado================================================================
enunciado = fr"""A continuación se muestra una circunferencia cuyo {choice(["radio mide "+Matematica(radio_menor+" "+unidad_de_medida,arreglar_espacios=True), "diámetro mide "+Matematica(2*radio_menor+" "+unidad_de_medida,arreglar_espacios=True)])} dentro de otra circunferencia cuyo {choice(["radio mide "+Matematica(radio_mayor+" "+unidad_de_medida,arreglar_espacios=True), "diámetro mide "+Matematica(2*radio_mayor+" "+unidad_de_medida,arreglar_espacios=True)])}
\begin{{center}} \begin{{tikzpicture}} [scale=1, rotate={randrange(0,360)}]
\draw ({randrange(0,int((radio_mayor_dibujo-radio_menor_dibujo)*10)+1)/10}, 0) circle({radio_menor_dibujo});
\draw (0,0) circle({radio_mayor_dibujo});
\end{{tikzpicture}} \end{{center}}
Ambas circunferencias se trasladan {Matematica(h+" "+unidad_de_medida,arreglar_espacios=True)} con un vector de traslación perpendicular al plano que las contiene. La cantidad de espacio que hay entre medio de los cuerpos generados es"""
#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica((radio_mayor**2-radio_menor**2)*h*PI()+" "+potencia(unidad_de_medida,3,parentesis_automatico=False),arreglar_espacios=True)
contenido_2 =        Matematica((radio_mayor-radio_menor)**2*h*PI()+" "+potencia(unidad_de_medida,3,parentesis_automatico=False),arreglar_espacios=True)#calcula el volumen entre medio restando los radios antes de elevar a dos
contenido_3 =        Matematica(radio_mayor**2*h*PI()+" "+potencia(unidad_de_medida,3,parentesis_automatico=False),arreglar_espacios=True)#calcula solo el volumen del cilindro mayor
contenido_4 =        Matematica(radio_menor**2*h*PI()+" "+potencia(unidad_de_medida,3,parentesis_automatico=False),arreglar_espacios=True)#calcula solo el volumen del cilindro menor
contenido_5 =        Matematica((radio_mayor**2+radio_menor**2)*h*PI()+" "+potencia(unidad_de_medida,3,parentesis_automatico=False),arreglar_espacios=True)#suma los volumenes



enunciado_oculto = [r,h]











