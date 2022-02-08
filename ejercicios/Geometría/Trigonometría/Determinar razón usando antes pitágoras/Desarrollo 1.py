{"cantidad_opciones":12, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
lista_trios = [
[Racional(3), Racional(4), Racional(5)]
, [Racional(6), Racional(8), Racional(10)]
, [Racional(9), Racional(12), Racional(15)]
, [Racional(5), Racional(12), Racional(13)]
, [Racional(10), Racional(24), Racional(26)]
, [Racional(8), Racional(15), Racional(17)]
, [Racional(7), Racional(24), Racional(25)]
, [Racional(1), Root(2), Root(3)]
, [Racional(1), Root(3), Racional(2)]
, [Racional(1), Racional(2), Root(5)]
, [Racional(1), Root(5), Root(6)]
, [Racional(1), Root(6), Root(7)]
, [Racional(1), Root(7), Root(8)]
, [Racional(1), Root(8), Racional(3)]
, [Racional(2), Root(2), Root(6)]
, [Racional(2), Root(3), Root(7)]
, [Racional(2), Root(5), Racional(3)]
, [Racional(2), Root(6), Root(10)]
, [Racional(2), Racional(3), Root(13)]
, [Racional(2), Racional(4), Root(20)]
, [Racional(2), Racional(5), Root(29)]
, [Racional(3), Racional(5), Root(34)]
, [Racional(4), Racional(5), Root(41)]
]
trio = choice(lista_trios)
a, b, c = trio[0], trio[1], trio[2]

unidad_de_medida = choice(["mm", "cm", "m", "km"])
letra = choice([r"\alpha", r"\beta", r"\gamma"])
angulo_de_giro = randrange(0, 360)

#================================Aquí va el enunciado================================================================
enunciado = fr"""Observa el siguiente triángulo ABC rectángulo en B.
\begin{{center}}
\begin{{tikzpicture}}

\tkzDefPoint({-180+angulo_de_giro}:1){{C}}
\tkzDefPoint({0+angulo_de_giro}:3){{B}}
\tkzDefTriangle[two angles= 30 and 90](C,B) \tkzGetPoint{{A}}

\tkzDrawPoints(A,B,C)

\node [label={60+angulo_de_giro}:A] at (A) {{}};
\node [label={315+angulo_de_giro}:B] at (B) {{}};
\node [label={195+angulo_de_giro}:C] at (C) {{}};

\tkzDefMidPoint(A,B) \tkzGetPoint{{AB}}
\tkzDefMidPoint(A,C) \tkzGetPoint{{AC}}
\tkzDefMidPoint(B,C) \tkzGetPoint{{BC}}

\tkzDrawPolygon(A,B,C)
\tkzMarkRightAngle(A,B,C)
"""

if opcion==1:
    enunciado += fr"""\draw pic["${letra}$",draw,angle radius=1cm] {{angle=B--C--A}};
    \node [label={0+angulo_de_giro}:{Matematica(a)+f" {unidad_de_medida}"}] at (AB) {{}};
    \node [label={-90+angulo_de_giro}:{Matematica(b)+f" {unidad_de_medida}"}] at (BC) {{}};
    \end{{tikzpicture}} \end{{center}} Calcula """ + Matematica(r"\sin"+letra)
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(a/c)



elif opcion==2:
    enunciado += fr"""\draw pic["${letra}$",draw,angle radius=1cm] {{angle=B--C--A}};
    \node [label={0+angulo_de_giro}:{Matematica(a)+f" {unidad_de_medida}"}] at (AB) {{}};
    \node [label={-90+angulo_de_giro}:{Matematica(b)+f" {unidad_de_medida}"}] at (BC) {{}};
    \end{{tikzpicture}} \end{{center}} Calcula """ + Matematica(r"\cos"+letra)
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(b/c)



elif opcion==3:
    enunciado += fr"""\draw pic["${letra}$",draw,angle radius=1cm] {{angle=B--C--A}};
    \node [label={0+angulo_de_giro}:{Matematica(a)+f" {unidad_de_medida}"}] at (AB) {{}};
    \node [label={-225+angulo_de_giro}:{Matematica(c)+f" {unidad_de_medida}"}] at (AC) {{}};
    \end{{tikzpicture}} \end{{center}} Calcula """ + Matematica(r"\cos"+letra)
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(b/c)



elif opcion==4:
    enunciado += fr"""\draw pic["${letra}$",draw,angle radius=1cm] {{angle=B--C--A}};
    \node [label={0+angulo_de_giro}:{Matematica(a)+f" {unidad_de_medida}"}] at (AB) {{}};
    \node [label={-225+angulo_de_giro}:{Matematica(c)+f" {unidad_de_medida}"}] at (AC) {{}};
    \end{{tikzpicture}} \end{{center}} Calcula """ + Matematica(r"\tan"+letra)
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(a/b)



elif opcion==5:
    enunciado += fr"""\draw pic["${letra}$",draw,angle radius=1cm] {{angle=B--C--A}};
    \node [label={-90+angulo_de_giro}:{Matematica(b)+f" {unidad_de_medida}"}] at (BC) {{}};
    \node [label={-225+angulo_de_giro}:{Matematica(c)+f" {unidad_de_medida}"}] at (AC) {{}};
    \end{{tikzpicture}} \end{{center}} Calcula """ + Matematica(r"\sin"+letra)
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(a/c)



elif opcion==6:
    enunciado += fr"""\draw pic["${letra}$",draw,angle radius=1cm] {{angle=B--C--A}};
    \node [label={-90+angulo_de_giro}:{Matematica(b)+f" {unidad_de_medida}"}] at (BC) {{}};
    \node [label={-225+angulo_de_giro}:{Matematica(c)+f" {unidad_de_medida}"}] at (AC) {{}};
    \end{{tikzpicture}} \end{{center}} Calcula """ + Matematica(r"\tan"+letra)
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(a/b)



elif opcion==7:
    enunciado += fr"""\draw pic["${letra}$",draw,angle radius=1cm] {{angle=C--A--B}};
    \node [label={0+angulo_de_giro}:{Matematica(a)+f" {unidad_de_medida}"}] at (AB) {{}};
    \node [label={-90+angulo_de_giro}:{Matematica(b)+f" {unidad_de_medida}"}] at (BC) {{}};
    \end{{tikzpicture}} \end{{center}} Calcula """ + Matematica(r"\sin"+letra)
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(b/c)



elif opcion==8:
    enunciado += fr"""\draw pic["${letra}$",draw,angle radius=1cm] {{angle=C--A--B}};
    \node [label={0+angulo_de_giro}:{Matematica(a)+f" {unidad_de_medida}"}] at (AB) {{}};
    \node [label={-90+angulo_de_giro}:{Matematica(b)+f" {unidad_de_medida}"}] at (BC) {{}};
    \end{{tikzpicture}} \end{{center}} Calcula """ + Matematica(r"\cos"+letra)
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(a/c)



elif opcion==9:
    enunciado += fr"""\draw pic["${letra}$",draw,angle radius=1cm] {{angle=C--A--B}};
    \node [label={0+angulo_de_giro}:{Matematica(a)+f" {unidad_de_medida}"}] at (AB) {{}};
    \node [label={-225+angulo_de_giro}:{Matematica(c)+f" {unidad_de_medida}"}] at (AC) {{}};
    \end{{tikzpicture}} \end{{center}} Calcula """ + Matematica(r"\sin"+letra)
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(b/c)



elif opcion==10:
    enunciado += fr"""\draw pic["${letra}$",draw,angle radius=1cm] {{angle=C--A--B}};
    \node [label={0+angulo_de_giro}:{Matematica(a)+f" {unidad_de_medida}"}] at (AB) {{}};
    \node [label={-225+angulo_de_giro}:{Matematica(c)+f" {unidad_de_medida}"}] at (AC) {{}};
    \end{{tikzpicture}} \end{{center}} Calcula """ + Matematica(r"\tan"+letra)
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(b/a)



elif opcion==11:
    enunciado += fr"""\draw pic["${letra}$",draw,angle radius=1cm] {{angle=C--A--B}};
    \node [label={-90+angulo_de_giro}:{Matematica(b)+f" {unidad_de_medida}"}] at (BC) {{}};
    \node [label={-225+angulo_de_giro}:{Matematica(c)+f" {unidad_de_medida}"}] at (AC) {{}};
    \end{{tikzpicture}} \end{{center}} Calcula """ + Matematica(r"\cos"+letra)
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(a/c)



elif opcion==12:
    enunciado += fr"""\draw pic["${letra}$",draw,angle radius=1cm] {{angle=C--A--B}};
    \node [label={-90+angulo_de_giro}:{Matematica(b)+f" {unidad_de_medida}"}] at (BC) {{}};
    \node [label={-225+angulo_de_giro}:{Matematica(c)+f" {unidad_de_medida}"}] at (AC) {{}};
    \end{{tikzpicture}} \end{{center}} Calcula """ + Matematica(r"\tan"+letra)
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(b/a)




enunciado_oculto = [a, b, c, opcion]
espacio_para_el_desarrollo = 8











