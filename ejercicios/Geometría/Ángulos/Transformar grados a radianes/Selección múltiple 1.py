{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a = Racional(elegir(1, 360))

#================================Aquí va el enunciado================================================================
enunciado = "El ángulo "+ Matematica(a+"°")+" transformado a radianes es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(a/180*PI()+" rad", arreglar_espacios=True)
contenido_2 = Matematica(a/180/PI()+" rad", arreglar_espacios=True)
contenido_3 = Matematica(180/a*PI()+" rad", arreglar_espacios=True)
contenido_4 = Matematica(180/a/PI()+" rad", arreglar_espacios=True)
contenido_5 = Matematica(a/360*PI()+" rad", arreglar_espacios=True)



enunciado_oculto = a










