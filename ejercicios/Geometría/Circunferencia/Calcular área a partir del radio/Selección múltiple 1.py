{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
r = Racional(randrange(1, 100))
angulo = Racional(choice([randrange(-10, 11), randrange(80, 101), randrange(170, 191), randrange(260, 281)]))
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
    El área de dicha circunferencia es"""


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
    El área de dicha circunferencia es"""


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
    El área de dicha circunferencia es"""


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
    El área de dicha circunferencia es"""

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(r**2*PI()+" "+potencia(unidad_de_medida, 2, False), arreglar_espacios=True)
contenido_2 = Matematica(r*PI()+" "+potencia(unidad_de_medida, 2, False), arreglar_espacios=True)
contenido_3 = Matematica(2*r*PI()+" "+potencia(unidad_de_medida, 2, False), arreglar_espacios=True)
contenido_4 = Matematica(2*r/PI()+" "+potencia(unidad_de_medida, 2, False), arreglar_espacios=True)
contenido_5 = Matematica(r*PI()/2+" "+potencia(unidad_de_medida, 2, False), arreglar_espacios=True)

enunciado_oculto = r










