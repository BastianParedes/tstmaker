{"cantidad_opciones":1, "cantidad_disponible":50}

unidad_de_medida = choice(["mm", "cm", "m", "km"])
letra = choice(["x", "y", "z"])

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
x1, x2, x3 = Racional(randrange(0,3)), Racional(randrange(6,9)), Racional(randrange(3,6))
y1, y2, y3 = Racional(randrange(0,3)), Racional(randrange(0,4)), Racional(randrange(5,9))
l1, l2, l3 = Racional(randrange(1,30)), Racional(randrange(1,30)), Racional(randrange(1,30))
#================================Aquí va el enunciado================================================================
enunciado = fr"""A continuación se representan las medidas de los lados de un triángulo
\begin{{center}} \begin{{tikzpicture}} [scale=0.5]
\tkzDefPoint({x1},{y1}){{A}}
\tkzDefPoint({x2},{y2}){{B}}
\tkzDefPoint({x3},{y3}){{C}}
\tkzDrawPolygon(A,B,C)
\tkzLabelSegment[below](A,B){{{Matematica(l1+" "+unidad_de_medida)}}}
\tkzLabelSegment[right](B,C){{{Matematica(l2+" "+unidad_de_medida)}}}
\tkzLabelSegment[left](C,A){{{Matematica(l3+" "+unidad_de_medida)}}}
\end{{tikzpicture}} \end{{center}}
¿Cuánto mide el perímetro del triángulo?"""
#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(l1+l2+l3+" "+unidad_de_medida)
contenido_2 = Matematica(l1*l2*l3+" "+unidad_de_medida)
contenido_3 = Matematica(3*(l1+l2+l3)+" "+unidad_de_medida)
contenido_4 = Matematica(3*l1*l2*l3+" "+unidad_de_medida)
contenido_5 = Matematica(Racional(l1+l2+l3,2,cargar_decimal=choice([True,False]))+" "+unidad_de_medida)



enunciado_oculto = [l1, l2, l3]











