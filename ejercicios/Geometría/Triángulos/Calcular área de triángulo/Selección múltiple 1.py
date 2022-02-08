{"cantidad_opciones":3, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
b, h = Racional(randrange(5,20)), Racional(randrange(1,20))

unidad_de_medida = choice(["mm", "cm", "m", "km"])
angulo_de_giro = randrange(0,360)

lista_de_letras = ["A","B","C","D"]
shuffle(lista_de_letras)
letra_A, letra_B, letra_C, letra_D = lista_de_letras[0], lista_de_letras[1], lista_de_letras[2], lista_de_letras[3]

extension_base = Racional(randrange(1, 20))

#================================Aquí va el enunciado================================================================

if opcion==1:
    b1 = Racional(b-randrange(1,int(b)))
    b2 = b-b1
    enunciado = fr"""En el siguiente triángulo {Matematica(letra_C+letra_D+"="+h+" "+unidad_de_medida,arreglar_espacios=True)}, {Matematica(letra_A+letra_D+"="+b1+" "+unidad_de_medida,arreglar_espacios=True)} y {Matematica(letra_D+letra_B+"="+b2+" "+unidad_de_medida,arreglar_espacios=True)}
\begin{{center}} \begin{{tikzpicture}} [scale={uniform(1,1.5)}, rotate={angulo_de_giro}]
\coordinate [label={225+angulo_de_giro}:{letra_A}] (A) at ({-uniform(0.8,2.5)},0);
\coordinate [label={-45+angulo_de_giro}:{letra_B}] (B) at ({uniform(0.8,2.5)},0);
\coordinate [label={90+angulo_de_giro}:{letra_C}] (C) at (0,{uniform(0.8,2.5)});
\coordinate [label={-90+angulo_de_giro}:{letra_D}] (D) at (0,0);

\tkzDrawPolygon(A,B,C)

\draw [dashed] (C) -- (D);

\tkzMarkRightAngle[size=0.15]({choice(["B,D,C", "C,D,A"])})

\end{{tikzpicture}} \end{{center}}
El área del triángulo es"""



elif opcion==2:
    enunciado = fr"""En el siguiente triángulo {Matematica(letra_C+letra_A+"="+h+" "+unidad_de_medida,arreglar_espacios=True)} y {Matematica(letra_A+letra_B+"="+b+" "+unidad_de_medida,arreglar_espacios=True)}
\begin{{center}} \begin{{tikzpicture}} [scale={uniform(1,1.5)}, rotate={angulo_de_giro}]
\coordinate [label={225+angulo_de_giro}:{letra_A}] (A) at (0,0);
\coordinate [label={-45+angulo_de_giro}:{letra_B}] (B) at ({uniform(0.8,2.5)},0);
\coordinate [label={90+angulo_de_giro}:{letra_C}] (C) at (0,{uniform(0.8,2.5)});

\tkzDrawPolygon(A,B,C)

\tkzMarkRightAngle[size=0.15](B,A,C)

\end{{tikzpicture}} \end{{center}}
El área del triángulo es"""



elif opcion==3:
    medida_dibujo = -uniform(0.8,3)
    enunciado = fr"""En el siguiente triángulo {Matematica(choice([letra_C+letra_D,letra_D+letra_C])+"="+h+" "+unidad_de_medida,arreglar_espacios=True)}, {Matematica(choice([letra_A+letra_B,letra_B+letra_A])+"="+b+" "+unidad_de_medida,arreglar_espacios=True)} y {Matematica(choice([letra_A+letra_D,letra_D+letra_A])+"="+extension_base+" "+unidad_de_medida,arreglar_espacios=True)}
\begin{{center}} \begin{{tikzpicture}} [scale={uniform(1,1.5)}, rotate={angulo_de_giro}]
\coordinate [label={-90+angulo_de_giro}:{letra_A}] (A) at (0,0);
\coordinate [label={-45+angulo_de_giro}:{letra_B}] (B) at ({uniform(0.8,2.5)},0);
\coordinate [label={135+angulo_de_giro}:{letra_C}] (C) at ({medida_dibujo},{uniform(0.8,2.5)});
\coordinate [label={-90+angulo_de_giro}:{letra_D}] (D) at ({medida_dibujo},0);

\tkzDrawPolygon(A,B,C)

\draw [dashed] (C) -- (D) -- (A);

\tkzMarkRightAngle[size=0.15](A,D,C)

\end{{tikzpicture}} \end{{center}}
El área del triángulo es"""



#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(Racional(b*h/2,cargar_decimal=choice([True,False]))+" "+potencia(unidad_de_medida,2,parentesis_automatico=False))
contenido_2 = Matematica(Racional(b*h,cargar_decimal=choice([True,False]))+" "+potencia(unidad_de_medida,2,parentesis_automatico=False))
contenido_3 = Matematica(Racional(b+h,cargar_decimal=choice([True,False]))+" "+potencia(unidad_de_medida,2,parentesis_automatico=False))
contenido_4 = Matematica(Racional(b+h/2,cargar_decimal=choice([True,False]))+" "+potencia(unidad_de_medida,2,parentesis_automatico=False))
contenido_5 = Matematica(Racional((b+extension_base)*h/2,cargar_decimal=choice([True,False]))+" "+potencia(unidad_de_medida,2,parentesis_automatico=False))




enunciado_oculto = [b,h]











