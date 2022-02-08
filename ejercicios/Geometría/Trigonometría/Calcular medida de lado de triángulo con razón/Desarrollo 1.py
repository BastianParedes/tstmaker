{"cantidad_opciones":12, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
lado = randrange(1, 100)
angulo = elegir(10, 81, 15,30,45,60,75)
unidad_de_medida = choice(["mm", "cm", "m", "km"])
angulo_de_giro = randrange(0, 360)

#================================Aquí va el enunciado================================================================
enunciado = fr"""
\begin{{center}}
\begin{{tikzpicture}}

\tkzDefPoint({180+angulo_de_giro}:1){{C}}
\tkzDefPoint({0+angulo_de_giro}:3){{B}}
\tkzDefTriangle[two angles= 30 and 90](C,B) \tkzGetPoint{{A}}

\tkzDrawPoints(A,B,C)

\node [label={-300+angulo_de_giro}:A] at (A) {{}};
\node [label={-45+angulo_de_giro}:B] at (B) {{}};
\node [label={-165+angulo_de_giro}:C] at (C) {{}};

\tkzDefMidPoint(A,B) \tkzGetPoint{{AB}}
\tkzDefMidPoint(A,C) \tkzGetPoint{{AC}}
\tkzDefMidPoint(B,C) \tkzGetPoint{{BC}}

\tkzDrawPolygon(A,B,C)
\tkzMarkRightAngle(A,B,C)
"""

if opcion==1:
    razon = Racional(round(tan(angulo),2))
    segundo_lado = lado/razon
    enunciado = "Observa el siguiente triángulo" + enunciado + fr"""\node [label={0+angulo_de_giro}:{Matematica(lado)+" "+unidad_de_medida}] at (AB) {{}};
    \draw pic["{Matematica(potencia(angulo,'°'))}",draw,angle radius=1.4cm] {{angle=B--C--A}};
    \end{{tikzpicture}} \end{{center}}
    ¿Cuánto mide el lado BC? Considera """ + Matematica(r"tan "+Racional(angulo)+"°="+razon, arreglar_espacios=True)
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(segundo_lado)+" "+unidad_de_medida



elif opcion==2:
    razon = Racional(round(sin(angulo),2))
    segundo_lado = lado/razon
    enunciado = "Observa el siguiente triángulo" + enunciado + fr"""\node  [label={0+angulo_de_giro}:{Matematica(lado)+" "+unidad_de_medida}] at (AB) {{}};
    \draw pic["{Matematica(potencia(angulo,'°'))}",draw,angle radius=1.4cm] {{angle=B--C--A}};
    \end{{tikzpicture}} \end{{center}}
    ¿Cuánto mide el lado AC? Considera """ + Matematica(r"sin "+Racional(angulo)+"°="+razon, arreglar_espacios=True)
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(segundo_lado)+" "+unidad_de_medida



elif opcion==3:
    razon = Racional(round(tan(angulo),2))
    segundo_lado = lado*razon
    enunciado = "Observa el siguiente triángulo" + enunciado + fr"""\node [label={270+angulo_de_giro}:{Matematica(lado)+" "+unidad_de_medida}] at (BC) {{}};
    \draw pic["{Matematica(potencia(angulo,'°'))}",draw,angle radius=1.4cm] {{angle=B--C--A}};
    \end{{tikzpicture}} \end{{center}}
    ¿Cuánto mide el lado AB? Considera """ + Matematica(r"tan "+Racional(angulo)+"°="+razon, arreglar_espacios=True)
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(segundo_lado)+" "+unidad_de_medida



elif opcion==4:
    razon = Racional(round(cos(angulo),2))
    segundo_lado = lado/razon
    enunciado = "Observa el siguiente triángulo" + enunciado + fr"""\node [label={270+angulo_de_giro}:{Matematica(lado)+" "+unidad_de_medida}] at (BC) {{}};
    \draw pic["{Matematica(potencia(angulo,'°'))}",draw,angle radius=1.4cm] {{angle=B--C--A}};
    \end{{tikzpicture}} \end{{center}}
    ¿Cuánto mide el lado AC? Considera """ + Matematica(r"cos "+Racional(angulo)+"°="+razon, arreglar_espacios=True)
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(segundo_lado)+" "+unidad_de_medida



elif opcion==5:
    razon = Racional(round(sin(angulo),2))
    segundo_lado = lado*razon
    enunciado = "Observa el siguiente triángulo" + enunciado + fr"""\node [label={135+angulo_de_giro}:{Matematica(lado)+" "+unidad_de_medida}] at (AC) {{}};
    \draw pic["{Matematica(potencia(angulo,'°'))}",draw,angle radius=1.4cm] {{angle=B--C--A}};
    \end{{tikzpicture}} \end{{center}}
    ¿Cuánto mide el lado AB? Considera """ + Matematica(r"sin "+Racional(angulo)+"°="+razon, arreglar_espacios=True)
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(segundo_lado)+" "+unidad_de_medida



elif opcion==6:
    razon = Racional(round(cos(angulo),2))
    segundo_lado = lado*razon
    enunciado = "Observa el siguiente triángulo" + enunciado + fr"""\node [label={135+angulo_de_giro}:{Matematica(lado)+" "+unidad_de_medida}] at (AC) {{}};
    \draw pic["{Matematica(potencia(angulo,'°'))}",draw,angle radius=1.4cm] {{angle=B--C--A}};
    \end{{tikzpicture}} \end{{center}}
    ¿Cuánto mide el lado BC? Considera """ + Matematica(r"cos "+Racional(angulo)+"°="+razon, arreglar_espacios=True)
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(segundo_lado)+" "+unidad_de_medida



elif opcion==7:
    razon = Racional(round(tan(angulo),2))
    segundo_lado = lado*razon
    enunciado = "Observa el siguiente triángulo" + enunciado + fr"""\node  [label={0+angulo_de_giro}:{Matematica(lado)+" "+unidad_de_medida}] at (AB) {{}};
    \draw pic["{Matematica(potencia(angulo,'°'))}",draw,angle radius=1.4cm] {{angle=C--A--B}};
    \end{{tikzpicture}} \end{{center}}
    ¿Cuánto mide el lado BC? Considera """ + Matematica(r"tan "+Racional(angulo)+"°="+razon, arreglar_espacios=True)
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(segundo_lado)+" "+unidad_de_medida



elif opcion==8:
    razon = Racional(round(cos(angulo),2))
    segundo_lado = lado/razon
    enunciado = "Observa el siguiente triángulo" + enunciado + fr"""\node  [label={0+angulo_de_giro}:{Matematica(lado)+" "+unidad_de_medida}] at (AB) {{}};
    \draw pic["{Matematica(potencia(angulo,'°'))}",draw,angle radius=1.4cm] {{angle=C--A--B}};
    \end{{tikzpicture}} \end{{center}}
    ¿Cuánto mide el lado AC? Considera """ + Matematica(r"cos "+Racional(angulo)+"°="+razon, arreglar_espacios=True)
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(segundo_lado)+" "+unidad_de_medida



elif opcion==9:
    razon = Racional(round(tan(angulo),2))
    segundo_lado = lado/razon
    enunciado = "Observa el siguiente triángulo" + enunciado + fr"""\node [label={270+angulo_de_giro}:{Matematica(lado)+" "+unidad_de_medida}] at (BC) {{}};
    \draw pic["{Matematica(potencia(angulo,'°'))}",draw,angle radius=1.4cm] {{angle=C--A--B}};
    \end{{tikzpicture}} \end{{center}}
    ¿Cuánto mide el lado AB? Considera """ + Matematica(r"tan "+Racional(angulo)+"°="+razon, arreglar_espacios=True)
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(segundo_lado)+" "+unidad_de_medida



elif opcion==10:
    razon = Racional(round(sin(angulo),2))
    segundo_lado = lado/razon
    enunciado = "Observa el siguiente triángulo" + enunciado + fr"""\node [label={270+angulo_de_giro}:{Matematica(lado)+" "+unidad_de_medida}] at (BC) {{}};
    \draw pic["{Matematica(potencia(angulo,'°'))}",draw,angle radius=1.4cm] {{angle=C--A--B}};
    \end{{tikzpicture}} \end{{center}}
    ¿Cuánto mide el lado AC? Considera """ + Matematica(r"sin "+Racional(angulo)+"°="+razon, arreglar_espacios=True)
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(segundo_lado)+" "+unidad_de_medida



elif opcion==11:
    razon = Racional(round(cos(angulo),2))
    segundo_lado = lado*razon
    enunciado = "Observa el siguiente triángulo" + enunciado + fr"""\node [label={135+angulo_de_giro}:{Matematica(lado)+" "+unidad_de_medida}] at (AC) {{}};
    \draw pic["{Matematica(potencia(angulo,'°'))}",draw,angle radius=1.4cm] {{angle=C--A--B}};
    \end{{tikzpicture}} \end{{center}}
    ¿Cuánto mide el lado AB? Considera """ + Matematica(r"cos "+Racional(angulo)+"°="+razon, arreglar_espacios=True)
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(segundo_lado)+" "+unidad_de_medida



elif opcion==12:
    razon = Racional(round(sin(angulo),2))
    segundo_lado = lado*razon
    enunciado = "Observa el siguiente triángulo" + enunciado + fr"""\node [label={135+angulo_de_giro}:{Matematica(lado)+" "+unidad_de_medida}] at (AC) {{}};
    \draw pic["{Matematica(potencia(angulo,'°'))}",draw,angle radius=1.4cm] {{angle=C--A--B}};
    \end{{tikzpicture}} \end{{center}}
    ¿Cuánto mide el lado BC? Considera """ + Matematica(r"sin "+Racional(angulo)+"°="+razon, arreglar_espacios=True)
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(segundo_lado)+" "+unidad_de_medida




enunciado_oculto = [lado, angulo, opcion]
espacio_para_el_desarrollo = 6











