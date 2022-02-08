{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a = Racional(elegir(1, 360), elegir(1, 360))
while not 0<=a<=2:
    a = Racional(elegir(1, 360), elegir(1, 360))

#================================Aquí va el enunciado================================================================
enunciado = "El ángulo "+ Matematica(a*PI()+" rad") +" transformado a grados es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(potencia(a/180,"°"))
contenido_2 = Matematica(potencia(180/a,"°"))
contenido_3 = Matematica(potencia(a/180*PI(),"°"))
contenido_4 = Matematica(potencia(a/180/PI(),"°"))
contenido_5 = Matematica(potencia(a/360,"°"))



enunciado_oculto = a










