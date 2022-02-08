{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
r = Racional(randrange(1, 100))
angulo = Racional(choice([randrange(-10, 11), randrange(80, 101), randrange(170, 191), randrange(260, 281)]))
pi = Racional(choice([3.1, 3.14]),1, True)
unidad_de_medida = choice(["mm", "cm", "m", "km"])

#================================Aquí va el enunciado================================================================
if -10<=angulo<=10:
    enunciado = fr"""A continuación se muestra una circunferencia donde OA es radio y mide {r} {unidad_de_medida}.
    \begin{{center}}
    \begin{{tikzpicture}}
    \tkzDefPoint(0,0){{O}}
    \tkzDrawPoints(O)
    \tkzLabelPoints[left](O)

    \tkzDefPoint({angulo}:1.7){{A}}
    \tkzDrawPoints(A)
    \tkzLabelPoints[right](A)

    \draw(O) -- (A);
    \tkzLabelSegment[above](O,A){{{Matematica(f"r={r}")} {unidad_de_medida}}}

    \draw (0,0) circle(1.7);

    \end{{tikzpicture}}
    \end{{center}}
    Calcula el área de dicha circunferencia considerando {Matematica(PI()+"="+pi)}."""


elif 80<=angulo<=100:
    enunciado = fr"""A continuación se muestra una circunferencia donde OA es radio y mide {r} {unidad_de_medida}.
    \begin{{center}}
    \begin{{tikzpicture}}
    \tkzDefPoint(0,0){{O}}
    \tkzDrawPoints(O)
    \tkzLabelPoints[below](O)

    \tkzDefPoint({angulo}:1.7){{A}}
    \tkzDrawPoints(A)
    \tkzLabelPoints[above](A)

    \draw(O) -- (A);
    \tkzLabelSegment[right](O,A){{{Matematica(f"r={r}")} {unidad_de_medida}}}

    \draw (0,0) circle(1.7);

    \end{{tikzpicture}}
    \end{{center}}
    Calcula el área de dicha circunferencia considerando {Matematica(PI()+"="+pi)}."""


elif 170<=angulo<=190:
    enunciado = fr"""A continuación se muestra una circunferencia donde OA es radio y mide {r} {unidad_de_medida}.
    \begin{{center}}
    \begin{{tikzpicture}}
    \tkzDefPoint(0,0){{O}}
    \tkzDrawPoints(O)
    \tkzLabelPoints[right](O)

    \tkzDefPoint({angulo}:1.7){{A}}
    \tkzDrawPoints(A)
    \tkzLabelPoints[left](A)

    \draw(O) -- (A);
    \tkzLabelSegment[above](O,A){{{Matematica(f"r={r}")} {unidad_de_medida}}}

    \draw (0,0) circle(1.7);

    \end{{tikzpicture}}
    \end{{center}}
    Calcula el área de dicha circunferencia considerando {Matematica(PI()+"="+pi)}."""


else:
    enunciado = fr"""A continuación se muestra una circunferencia donde OA es radio y mide {r} {unidad_de_medida}.
    \begin{{center}}
    \begin{{tikzpicture}}
    \tkzDefPoint(0,0){{O}}
    \tkzDrawPoints(O)
    \tkzLabelPoints[above](O)

    \tkzDefPoint({angulo}:1.7){{A}}
    \tkzDrawPoints(A)
    \tkzLabelPoints[below](A)

    \draw(O) -- (A);
    \tkzLabelSegment[right](O,A){{{Matematica(f"r={r}")} {unidad_de_medida}}}

    \draw (0,0) circle(1.7);

    \end{{tikzpicture}}
    \end{{center}}
    Calcula el área de dicha circunferencia considerando {Matematica(PI()+"="+pi)}."""

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(Racional(r**2*pi,cargar_decimal=True)+" "+potencia(unidad_de_medida, 2, False), arreglar_espacios=True)
contenido_2 = Matematica(Racional(r*pi,cargar_decimal=True)+" "+potencia(unidad_de_medida, 2, False), arreglar_espacios=True)
contenido_3 = Matematica(Racional(2*r*pi,cargar_decimal=True)+" "+potencia(unidad_de_medida, 2, False), arreglar_espacios=True)
contenido_4 = Matematica(Racional(round(2*r/pi,2),cargar_decimal=True)+" "+potencia(unidad_de_medida, 2, False), arreglar_espacios=True)
contenido_5 = Matematica(Racional(r*pi/2,cargar_decimal=True)+" "+potencia(unidad_de_medida, 2, False), arreglar_espacios=True)

enunciado_oculto = r










