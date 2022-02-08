{"cantidad_opciones":3, "cantidad_disponible":50}

unidad_de_medida = choice(["mm", "cm", "m", "km"])
angulo_de_giro = randrange(0,360)
# letra_A, letra_B, letra_C, letra_D = "A", "B", "C", "D"

#Cuadrado dentro de circunferencia
if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    r, h = Racional(randrange(1, 11)), Racional(randrange(1, 11))
    #================================Aquí va el enunciado================================================================
    enunciado = fr"""A continuación se muestra una circunferencia cuyo {choice(["radio mide "+Matematica(r+" "+unidad_de_medida,arreglar_espacios=True), "diámetro mide "+Matematica(2*r+" "+unidad_de_medida,arreglar_espacios=True)])} circunscrita a un cuadrado
    \begin{{center}} \begin{{tikzpicture}} [scale={randrange(10,20)/10}, rotate={angulo_de_giro}]
    \draw (0,0) circle(1);
    \coordinate (A) at (45:1);
    \coordinate (B) at (135:1);
    \coordinate (C) at (225:1);
    \coordinate (D) at (315:1);
    \tkzDrawPolygon(A,B,C,D);
    \end{{tikzpicture}} \end{{center}}
    Ambas figuras se trasladan {Matematica(h+" "+unidad_de_medida,arreglar_espacios=True)} con un vector de traslación perpendicular al plano que las contiene. La cantidad de espacio que hay entre medio de los cuerpos generados es"""
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(Pol(r**2*h*PI(),-2*r**2*h)+" "+potencia(unidad_de_medida,3,parentesis_automatico=False),arreglar_espacios=True)
    contenido_2 =        Matematica(Pol(r**2*h*PI(),-4*r**2*h)+" "+potencia(unidad_de_medida,3,parentesis_automatico=False),arreglar_espacios=True)
    contenido_3 =        Matematica(Pol(r**2*h*PI(),2*r**2*h)+" "+potencia(unidad_de_medida,3,parentesis_automatico=False),arreglar_espacios=True)
    contenido_4 =        Matematica((r**2*h-2*r**2*h)*choice([1,PI()])+" "+potencia(unidad_de_medida,3,parentesis_automatico=False),arreglar_espacios=True)
    contenido_5 =        Matematica(choice([r**2*h*PI(),2*r**2*h])+" "+potencia(unidad_de_medida,3,parentesis_automatico=False),arreglar_espacios=True)
    enunciado_oculto = [r,h]


#Triángulo dentro de cuadrado
elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    l, h = Racional(randrange(1, 11)), Racional(randrange(1, 11))
    diccionario_colores = {"rojo":"red", "azul":"blue", "amarillo":"yellow", "violeta":"violet", "verde":"green", "café":"brown"}
    color_triangulo = choice(list(diccionario_colores))
    #================================Aquí va el enunciado================================================================
    enunciado = fr"""A continuación se muestra un triángulo {color_triangulo} inscrito en un cuadrado cuyos lados miden {Matematica(l+" "+unidad_de_medida,arreglar_espacios=True)}
    \begin{{center}} \begin{{tikzpicture}} [scale={randrange(10,30)/10}, rotate={angulo_de_giro}]
    \coordinate (A) at (0,0);
    \coordinate (B) at (1,0);
    \coordinate (C) at (1,1);
    \coordinate (D) at (0,1);
    \coordinate (E) at ({randrange(1,10)/10},1);
    \draw (A)--(D)--(C)--(B);
    \tkzDrawPolygon[{diccionario_colores[color_triangulo]}](A,B,E);
    \end{{tikzpicture}} \end{{center}}
    Ambas figuras se trasladan {Matematica(h+" "+unidad_de_medida,arreglar_espacios=True)} con un vector de traslación perpendicular al plano que las contiene. La cantidad de espacio que hay entre medio de los cuerpos generados es"""
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(l**2*h/2+" "+potencia(unidad_de_medida,3,parentesis_automatico=False),arreglar_espacios=True)
    contenido_2 =        Matematica(l**2*h+" "+potencia(unidad_de_medida,3,parentesis_automatico=False),arreglar_espacios=True)
    contenido_3 =        Matematica(l**2+" "+potencia(unidad_de_medida,3,parentesis_automatico=False),arreglar_espacios=True)
    contenido_4 =        Matematica(l**2/2+" "+potencia(unidad_de_medida,3,parentesis_automatico=False),arreglar_espacios=True)
    contenido_5 =        Matematica(l*Root(2)*h/2+" "+potencia(unidad_de_medida,3,parentesis_automatico=False),arreglar_espacios=True)
    enunciado_oculto = [l,h]



#Circunferencia dentro de cuadrado
elif opcion==3:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    r, h = Racional(randrange(1, 11)), Racional(randrange(1, 11))
    #================================Aquí va el enunciado================================================================
    enunciado = fr"""A continuación se muestra una circunferencia cuyo {choice(["radio mide "+Matematica(r+" "+unidad_de_medida,arreglar_espacios=True), "diámetro mide "+Matematica(2*r+" "+unidad_de_medida,arreglar_espacios=True)])} inscrita a un cuadrado
    \begin{{center}} \begin{{tikzpicture}} [scale={randrange(10,20)/10}, rotate={angulo_de_giro}]
    \draw (0,0) circle(1);
    \coordinate (A) at (-1,-1);
    \coordinate (B) at (1,-1);
    \coordinate (C) at (1,1);
    \coordinate (D) at (-1,1);
    \tkzDrawPolygon(A,B,C,D);
    \end{{tikzpicture}} \end{{center}}
    Ambas figuras se trasladan {Matematica(h+" "+unidad_de_medida,arreglar_espacios=True)} con un vector de traslación perpendicular al plano que las contiene. La cantidad de espacio que hay entre medio de los cuerpos generados es"""
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(Pol((2*r)**2*h, -r**2*h*PI())+" "+potencia(unidad_de_medida,3,parentesis_automatico=False),arreglar_espacios=True)
    contenido_2 =        Matematica(Pol(r**2*h, -r**2*h*PI())+" "+potencia(unidad_de_medida,3,parentesis_automatico=False),arreglar_espacios=True)
    contenido_3 =        Matematica(Pol(2*r**2*h, r**2*h*PI())+" "+potencia(unidad_de_medida,3,parentesis_automatico=False),arreglar_espacios=True)
    contenido_4 =        Matematica(Pol((2*r)**2*h, r**2*h*PI())+" "+potencia(unidad_de_medida,3,parentesis_automatico=False),arreglar_espacios=True)
    contenido_5 =        Matematica(choice([r**2*h*PI(),(2*r)**2*h])+" "+potencia(unidad_de_medida,3,parentesis_automatico=False),arreglar_espacios=True)
    enunciado_oculto = [r,h]















