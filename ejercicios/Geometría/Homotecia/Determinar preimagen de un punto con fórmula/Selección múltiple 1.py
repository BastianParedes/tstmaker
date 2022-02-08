{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
A, O, k = Par(Racional(randrange(-10, 10)),Racional(randrange(-10, 10))), Par(Racional(randrange(-10, 10)),Racional(randrange(-10, 10))), Racional(elegir(-10,10, 0,1))
while A.x==O.x or A.y==O.y:
    A, O, k = Par(Racional(randrange(-10, 10)),Racional(randrange(-10, 10))), Par(Racional(randrange(-10, 10)),Racional(randrange(-10, 10))), Racional(elegir(-10,10, 0,1))
B = k*(A-O)+O

#================================Aquí va el enunciado================================================================
enunciado = "A un punto P se le aplica una homotecia con centro "+Matematica(O, arreglar_espacios=True)+f" y razón de homotecia {Matematica(k)} obteniendo el punto homotético {Matematica(B, arreglar_espacios=True)}. Las coordenadas de P son"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(A, arreglar_espacios=True)
contenido_2 = Matematica(k*(B-O)+O, arreglar_espacios=True)
contenido_3 = Matematica(k*(O-B)+B, arreglar_espacios=True)
contenido_4 = Matematica(k*(B+O)-O, arreglar_espacios=True)
contenido_5 = Matematica(k*(O+B)-B, arreglar_espacios=True)



enunciado_oculto = [A,O,k]











