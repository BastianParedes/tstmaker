{"cantidad_opciones":3, "cantidad_disponible":50}


class Evento:
    def __init__(self, frase, probabilidad):
        self.frase = frase
        self.probabilidad = Racional(probabilidad)
    
    def __str__(self):
        return self.frase


if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    evento_1 = choice([
        Evento('se obtenga un número par', Racional(3,6)),
        Evento('se obtenga un número impar', Racional(3,6)),
        Evento('se obtenga un número primo', Racional(3,6)),
        Evento('se obtenga un número menor que 3', Racional(2,6)),
        Evento('se obtenga un número mayor que 4', Racional(2,6)),
        Evento(f'se obtenga un número distinto de {randrange(1,7)}', Racional(5,6))
    ])
    evento_1.frase += ' al lanzar un dado'
    evento_2 = choice([
        Evento('se obtenga cara', Racional(1,2)),
        Evento('se obtenga sello', Racional(1,2))
    ])
    evento_2.frase += ' al lanzar una moneda'
    #================================Aquí va el enunciado================================================================
    enunciado = f'La probabilidad de que {evento_1} y {evento_2} es '
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(evento_1.probabilidad * evento_2.probabilidad)
    contenido_2 =        Matematica(evento_1.probabilidad + evento_2.probabilidad)
    contenido_3 =        Matematica(evento_1.probabilidad + evento_2.probabilidad - evento_1.probabilidad * evento_2.probabilidad)
    contenido_4 =        Matematica(choice([evento_1.probabilidad , evento_2.probabilidad]))
    contenido_5 =        Matematica(evento_1.probabilidad + evento_2.probabilidad + evento_1.probabilidad * evento_2.probabilidad)
    enunciado_oculto = enunciado





elif opcion==2:
    opcion_b = choice([1,2])
    if opcion_b == 1:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        lado_1, lado_2 = choice(['cara', 'sello']), choice(['cara', 'sello'])
        #================================Aquí va el enunciado================================================================
        enunciado = f'Se lanzan 2 monedas, la probabilidad de que se obtenga {lado_1} en la primera y {lado_2} en la segunda es'
        #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
        contenido_correcto = Matematica(Racional(1,4))
        contenido_2 =        Matematica(Racional(1,2))
        contenido_3 =        Matematica(Racional(3,4))
        contenido_4 =        Matematica(Racional(1))
        contenido_5 =        Matematica(Racional(0))
    
    elif opcion_b==2:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        lado_1, lado_2, lado_3 = choice(['cara', 'sello']), choice(['cara', 'sello']), choice(['cara', 'sello'])
        #================================Aquí va el enunciado================================================================
        enunciado = f'Se lanzan 3 monedas, la probabilidad de que se obtenga {lado_1} en la primera, {lado_2}, en la segunda y {lado_3} en la tercera es'
        #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
        contenido_correcto = Matematica(Racional(1,8))
        contenido_2 =        Matematica(Racional(1,4))
        contenido_3 =        Matematica(Racional(1,2))
        contenido_4 =        Matematica(Racional(1))
        contenido_5 =        Matematica(Racional(0))

    enunciado_oculto = [opcion, opcion_b]



elif opcion==3:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    eventos = [
        Evento('se obtenga un número par', Racional(3,6)),
        Evento('se obtenga un número impar', Racional(3,6)),
        Evento('se obtenga un número primo', Racional(3,6)),
        Evento('se obtenga un número menor que 3', Racional(2,6)),
        Evento('se obtenga un número mayor que 4', Racional(2,6)),
        Evento(f'se obtenga un número distinto de {randrange(1,7)}', Racional(5,6))
    ]
    shuffle(eventos)
    evento_1 , evento_2 = eventos[0], eventos[1]
    #================================Aquí va el enunciado================================================================
    enunciado = f'Se lanza un dado dos veces. La probabilidad de que la primera vez {evento_1} y la segunda {evento_2} es'
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(evento_1.probabilidad * evento_2.probabilidad)
    contenido_2 =        Matematica(evento_1.probabilidad + evento_2.probabilidad)
    contenido_3 =        Matematica(evento_1.probabilidad + evento_2.probabilidad - evento_1.probabilidad * evento_2.probabilidad)
    contenido_4 =        Matematica(abs(evento_1.probabilidad - evento_2.probabilidad))
    contenido_5 =        Matematica(evento_1.probabilidad + evento_2.probabilidad + evento_1.probabilidad * evento_2.probabilidad)







