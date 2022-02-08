{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
p1 = Par(elegir(-10, 10), elegir(-10, 10))
p2 = Par(elegir(-10, 10), elegir(-10, 10))

#================================Aquí va el enunciado================================================================
enunciado = "Las coordenadas del punto medio entre los puntos "+Matematica("A"+p1)+" y "+Matematica("B"+p2)+" son"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica((p1+p2)/2)
contenido_2 = Matematica(p1+p2)
contenido_3 = Matematica((p1-p2)/2)
contenido_4 = Matematica((p2-p1)/2)
contenido_5 = Matematica(p2-p1)



enunciado_oculto = [p1, p2]










