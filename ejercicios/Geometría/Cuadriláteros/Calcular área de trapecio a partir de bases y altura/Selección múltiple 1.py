{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
base_menor = Racional(randrange(1,50))
base_mayor = Racional(randrange(1,50))
while (base_menor+base_mayor)%2==1 or not base_menor<base_mayor:
    base_menor = Racional(randrange(1,50))
    base_mayor = Racional(randrange(1,50))
altura = Racional(randrange(1,50))

unidad_de_medida = choice(["mm", "cm", "m", "km"])

angulo_de_giro = randrange(0,360)
angulo_de_giro = 0
distancia_dibujo_1 = randrange(5,15)/10
distancia_dibujo_2 = distancia_dibujo_1 + randrange(5,15)/10
distancia_dibujo_3 = distancia_dibujo_2 + randrange(5,15)/10
altura_dibujo = randrange(8,20)/10

lista_de_letras = ["A","B","C","D","E"]
shuffle(lista_de_letras)
#lista_de_letras = ["A","B","C","D","E"]
letra_A, letra_B, letra_C, letra_D, letra_E = lista_de_letras[0], lista_de_letras[1], lista_de_letras[2], lista_de_letras[3], lista_de_letras[4]

#================================Aquí va el enunciado================================================================
enunciado = fr"""En el siguiente trapecio se cumple que {Matematica(linea(letra_A+letra_B))} mide {Matematica(base_mayor+" "+unidad_de_medida,arreglar_espacios=True)} y {Matematica(linea(letra_C+letra_D))} mide {Matematica(base_menor+" "+unidad_de_medida,arreglar_espacios=True)}
\begin{{center}} \begin{{tikzpicture}} [scale=1, rotate={angulo_de_giro}]

\coordinate [label={-135+angulo_de_giro}:{letra_A}] (A) at (0, 0);
\coordinate [label={-45+angulo_de_giro}:{letra_B}] (B) at ({distancia_dibujo_3}, 0);
\coordinate [label={45+angulo_de_giro}:{letra_C}] (C) at ({distancia_dibujo_2}, {altura_dibujo});
\coordinate [label={135+angulo_de_giro}:{letra_D}] (D) at ({distancia_dibujo_1}, {altura_dibujo});

\tkzDrawPolygon(A,B,C,D)

"""
if choice([True,False]):
    enunciado += fr"""\coordinate [label={-90+angulo_de_giro}:{letra_E}] (H) at ({distancia_dibujo_1}, 0);
\draw [dashed] (D) -- (H);
\tkzMarkRightAngle[size=0.15]({choice(["B,H,D", "D,H,A"])})
\end{{tikzpicture}} \end{{center}}
Si {Matematica(linea(letra_E+letra_D))} mide {Matematica(altura+" "+unidad_de_medida,arreglar_espacios=True)}, entonces el área del paralelepípedo mide
"""
else:
    enunciado += fr"""\coordinate [label={-90+angulo_de_giro}:{letra_E}] (H) at ({distancia_dibujo_2}, 0);
\draw [dashed] (C) -- (H);
\tkzMarkRightAngle[size=0.15]({choice(["B,H,C", "C,H,A"])})
\end{{tikzpicture}} \end{{center}}
Si {Matematica(linea(letra_E+letra_C))} mide {Matematica(altura+" "+unidad_de_medida,arreglar_espacios=True)}, entonces el área del paralelepípedo mide
"""

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica((base_menor+base_mayor)/2*altura +" "+potencia(unidad_de_medida,2,parentesis_automatico=False), arreglar_espacios=True)
contenido_2 =        Matematica((base_menor+base_mayor)*2*altura +" "+potencia(unidad_de_medida,2,parentesis_automatico=False), arreglar_espacios=True)
contenido_3 =        Matematica((base_menor+base_mayor)*altura +" "+potencia(unidad_de_medida,2,parentesis_automatico=False), arreglar_espacios=True)
contenido_4 =        Matematica(base_menor*altura +" "+potencia(unidad_de_medida,2,parentesis_automatico=False), arreglar_espacios=True)
contenido_5 =        Matematica(base_mayor*altura +" "+potencia(unidad_de_medida,2,parentesis_automatico=False), arreglar_espacios=True)



enunciado_oculto = [base_menor, base_mayor, altura]











