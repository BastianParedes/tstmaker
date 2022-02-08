{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
r = Racional(elegir(1, 26))
unidad_de_medida = choice(["mm", "cm", "m", "km"])

#================================Aquí va el enunciado================================================================
enunciado = "El área de una esfera que tiene un " +choice(["radio de "+Matematica(r+" "+unidad_de_medida, arreglar_espacios=True), "diámetro de "+Matematica(2*r+" "+unidad_de_medida, arreglar_espacios=True)])+" es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(4*r**2*PI()+" "+potencia(unidad_de_medida,2, parentesis_automatico=False), arreglar_espacios=True)
contenido_2 = Matematica(2*r**2*PI()+" "+potencia(unidad_de_medida,2, parentesis_automatico=False), arreglar_espacios=True)
contenido_3 = Matematica(Racional(3,4)*r**3*PI()+" "+potencia(unidad_de_medida,2, parentesis_automatico=False), arreglar_espacios=True)
contenido_4 = Matematica(r/4*PI()+" "+potencia(unidad_de_medida,2, parentesis_automatico=False), arreglar_espacios=True)
contenido_5 = Matematica(r/2*PI()+" "+potencia(unidad_de_medida,2, parentesis_automatico=False), arreglar_espacios=True)




enunciado_oculto = enunciado










