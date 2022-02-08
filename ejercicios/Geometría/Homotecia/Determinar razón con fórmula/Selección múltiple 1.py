{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
A, O, k = Par(Racional(randrange(-10, 10)),Racional(randrange(-10, 10))), Par(Racional(randrange(-10, 10)),Racional(randrange(-10, 10))), Racional(elegir(-10,10, 0,1))
while A.x==O.x or A.y==O.y:
    A, O, k = Par(Racional(randrange(-10, 10)),Racional(randrange(-10, 10))), Par(Racional(randrange(-10, 10)),Racional(randrange(-10, 10))), Racional(elegir(-10,10, 0,1))
B = k*(A-O)+O
#================================Aquí va el enunciado================================================================
enunciado = "Al punto "+Matematica(A, arreglar_espacios=True)+" se le aplica una homotecia con centro "+Matematica(O, arreglar_espacios=True)+" obteniendo el punto "+Matematica(B,arreglar_espacios=True)+". La razón de homotecia es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(k)
contenido_2 = Matematica(-k)
contenido_3 = Matematica(k**(-1))
contenido_4 = Matematica(-k**(-1))
contenido_5 = Matematica(abs(B-A))


enunciado_oculto = [A,B,k]











