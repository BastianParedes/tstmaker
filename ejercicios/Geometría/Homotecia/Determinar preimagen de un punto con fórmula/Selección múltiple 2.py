{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
while True:
    O, P, k = Par(Racional(randrange(-10, 10)),Racional(randrange(-10, 10))), Par(Racional(randrange(-10, 10)),Racional(randrange(-10, 10))), Racional(elegir(-10,10, 0,1))
    if P.x!=O.x and P.y!=O.y:
        break

P2 = k*(P-O)+O
P3 = k*(P+O)+O
P4 = k*(O+P)+P

#================================Aquí va el enunciado================================================================
enunciado = f"A un punto P se le aplica una homotecia respecto de {Matematica(O)} y razón {Matematica(k)}. Si las coordenadas del punto homotético de P son {Matematica(P2)}, ¿cuál es la distancia entre P y su homotético?"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(P.distancia(P2), arreglar_espacios=True) + ' unidades'
contenido_2 = Matematica(P.distancia(P3), arreglar_espacios=True) + ' unidades'
contenido_3 = Matematica(P.distancia(P4), arreglar_espacios=True) + ' unidades'
contenido_4 = Matematica(abs(k*P2), arreglar_espacios=True) + ' unidades'
contenido_5 = Matematica(O.distancia(P2), arreglar_espacios=True) + ' unidades'



enunciado_oculto = [O,P,k]

