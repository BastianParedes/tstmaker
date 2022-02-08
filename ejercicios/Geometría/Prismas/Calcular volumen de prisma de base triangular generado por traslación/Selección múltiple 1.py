{"cantidad_opciones":3, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
da, ab = Racional(randrange(1, 10)),Racional(randrange(1, 10))
b, ht, hp = da+ab, Racional(randrange(1, 10)), Racional(randrange(2, 10))

unidad_de_medida = choice(["mm", "cm", "m", "km"])

angulo_de_giro = randrange(0,360)

lista_de_letras = ["A","B","C","D"]
shuffle(lista_de_letras)
letra_A, letra_B, letra_C, letra_D= lista_de_letras[0], lista_de_letras[1], lista_de_letras[2], lista_de_letras[3]

# letra_A, letra_B, letra_C, letra_D = "A", "B", "C", "D"


if opcion==1:
    lista_de_partes = [Matematica(linea(letra_D+letra_A)+f" mide {da} "+unidad_de_medida,arreglar_espacios=True),
    Matematica(linea(letra_A+letra_B)+f" mide {ab} "+unidad_de_medida,arreglar_espacios=True)]
    shuffle(lista_de_partes)
    lista_de_lados = [Matematica(linea(letra_D+letra_B)+f" mide {b} "+unidad_de_medida,arreglar_espacios=True),
    lista_de_partes[0]+", "+lista_de_partes[1]]
    shuffle(lista_de_lados)
    #================================Aquí va el enunciado================================================================
    enunciado = fr"""En el siguiente triángulo se cumple que {lista_de_lados[0]} y {Matematica(linea(letra_A+letra_C)+f" mide {ht} "+unidad_de_medida,arreglar_espacios=True)}
    \begin{{center}} \begin{{tikzpicture}} [scale=0.5, rotate={angulo_de_giro}]
    \coordinate [label={270+angulo_de_giro}:{letra_A}] ({letra_A}) at (0,0);
    \coordinate [label={randrange(-45,45)+angulo_de_giro}:{letra_B}] ({letra_B}) at ({randrange(10,40)/10},0);
    \coordinate [label={randrange(45,135)+angulo_de_giro}:{letra_C}] ({letra_C}) at (0,{randrange(10,40)*1.7/10});
    \coordinate [label={180-randrange(-45,45)+angulo_de_giro}:{letra_D}] ({letra_D}) at ({-randrange(10,40)/10},0);
    \tkzDrawPolygon({letra_B},{letra_C},{letra_D});
    \tkzDrawSegment[dashed]({letra_A},{letra_C});
    """+choice([fr"\tkzMarkRightAngle[size=0.4]({letra_B},{letra_A},{letra_C})", fr"\tkzMarkRightAngle[size=0.4]({letra_C},{letra_A},{letra_D})"])+fr"""
    \end{{tikzpicture}} \end{{center}}
    Sea el cuerpo generado al trasladar el triángulo {Matematica(hp+" "+unidad_de_medida,arreglar_espacios=True)} con un vector de traslación perpendicular al plano que contiene a dicho triángulo. El volumen de dicho cuerpo es"""


elif opcion==2:
    bc = Root(ht**2+b**2)
    lista_de_lados = [
        Matematica(linea(letra_A+letra_B)+f" mide {b} "+unidad_de_medida,arreglar_espacios=True),
        Matematica(linea(letra_B+letra_C)+f" mide {bc} "+unidad_de_medida,arreglar_espacios=True),
        Matematica(linea(letra_C+letra_A)+f" mide {ht} "+unidad_de_medida,arreglar_espacios=True)
    ]
    shuffle(lista_de_lados)

    enunciado = fr"""En el siguiente triángulo rectángulo en {letra_A} se cumple que {lista_de_lados[0]} y {lista_de_lados[1]}
    \begin{{center}} \begin{{tikzpicture}} [scale=1, rotate={angulo_de_giro}]
    \coordinate [label={270+angulo_de_giro}:{letra_A}] ({letra_A}) at (0,0);
    \coordinate [label={randrange(-45,45)+angulo_de_giro}:{letra_B}] ({letra_B}) at ({randrange(10,30)/10},0);
    \coordinate [label={randrange(45,135)+angulo_de_giro}:{letra_C}] ({letra_C}) at (0,{randrange(10,30)/10});
    \tkzDrawPolygon({letra_A},{letra_B},{letra_C});
    \tkzMarkRightAngle[size=0.2]({letra_B},{letra_A},{letra_C})
    \end{{tikzpicture}} \end{{center}}
    Sea el cuerpo generado al trasladar el triángulo {Matematica(hp+" "+unidad_de_medida,arreglar_espacios=True)} con un vector de traslación perpendicular al plano que contiene a dicho triángulo. El volumen de dicho cuerpo es"""



elif opcion==3:
    bc = Root(ht**2+ab**2)
    lista_de_lados = [
        Matematica(linea(letra_A+letra_B)+f" mide {b} "+unidad_de_medida,arreglar_espacios=True),
        Matematica(linea(letra_C+letra_D)+f" mide {ht} "+unidad_de_medida,arreglar_espacios=True),
        Matematica(linea(letra_D+letra_A)+f" mide {randrange(1, 10)} "+unidad_de_medida,arreglar_espacios=True)
    ]
    shuffle(lista_de_lados)
    lado_DA_dibujo = randrange(10,30)/10

    enunciado = fr"""En la siguiente figura se cumple que {lista_de_lados[0]}, {lista_de_lados[1]} y {lista_de_lados[2]}
    \begin{{center}} \begin{{tikzpicture}} [scale=1, rotate={angulo_de_giro}]

    \coordinate [label={270+angulo_de_giro}:{letra_A}] ({letra_A}) at (0,0);
    \coordinate [label={randrange(-45,45)+angulo_de_giro}:{letra_B}] ({letra_B}) at ({randrange(10,30)/10},0);
    \coordinate [label={randrange(90,135)+angulo_de_giro}:{letra_C}] ({letra_C}) at (-{lado_DA_dibujo},{randrange(10,30)/10});
    \coordinate [label={randrange(180,270)+angulo_de_giro}:{letra_D}] ({letra_D}) at (-{lado_DA_dibujo},0);

    \draw [dashed] ({letra_C})--({letra_D})--({letra_A});

    \tkzDrawPolygon({letra_A},{letra_B},{letra_C});

    \tkzMarkRightAngle[size=0.2]({letra_A},{letra_D},{letra_C})

    \end{{tikzpicture}} \end{{center}}
    Sea el cuerpo generado al trasladar el triángulo {Matematica(letra_A+letra_B+letra_C)} {Matematica(hp+" "+unidad_de_medida,arreglar_espacios=True)} con un vector de traslación perpendicular al plano que contiene a dicho triángulo. El volumen de dicho cuerpo es"""



#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(b*ht/2*hp+" "+potencia(unidad_de_medida,3,parentesis_automatico=False),arreglar_espacios=True)
contenido_2 =        Matematica(b*ht/3*hp+" "+potencia(unidad_de_medida,3,parentesis_automatico=False),arreglar_espacios=True)#Al calcular el área del triángulo divide entre 3 en lugar de 2
contenido_3 =        Matematica(b*ht*hp+" "+potencia(unidad_de_medida,3,parentesis_automatico=False),arreglar_espacios=True)#Al calcular el área del triángulo no divide entre 2
contenido_4 =        Matematica(b*ht/2+" "+potencia(unidad_de_medida,3,parentesis_automatico=False),arreglar_espacios=True)#Calcula el área del triángulo, pero no el volumen
contenido_5 =        Matematica(b*ht+" "+potencia(unidad_de_medida,3,parentesis_automatico=False),arreglar_espacios=True)#Solo multiplica base por altura del triángulo


enunciado_oculto = [b, ht, hp]











