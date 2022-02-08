{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
while True:
    P, O, k = Par(Racional(randrange(-10, 10)),Racional(randrange(-10, 10))), Par(Racional(randrange(-10, 10)),Racional(randrange(-10, 10))), Racional(elegir(-10,10, 0,1))
    if P.x!=O.x and P.y!=O.y:
        break


#================================Aquí va el enunciado================================================================
enunciado = f"Sean los puntos O{Matematica(P)} y P{Matematica(O)}. Sea el punto Q obtenido al hacer una homotecia sobre O respecto de P con razón {Matematica(k)}. Las coordenadas de Q son"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(k*(P-O)+O, arreglar_espacios=True)
contenido_2 = Matematica(k*(O-P)+O, arreglar_espacios=True)
contenido_3 = Matematica((P-O)+O, arreglar_espacios=True)
contenido_4 = Matematica((O-P)+O, arreglar_espacios=True)
contenido_5 = Matematica(k*(P+O)+O, arreglar_espacios=True)



enunciado_oculto = [P,O,k]

