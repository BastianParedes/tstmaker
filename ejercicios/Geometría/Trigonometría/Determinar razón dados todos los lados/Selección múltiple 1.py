{"cantidad_opciones":6, "cantidad_disponible":50}

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
a = trio[0]
b = trio[1]
c = trio[2]

unidad_de_medida = choice(["mm", "cm", "m", "km"])
letra = choice([r"\alpha", r"\beta", r"\gamma"])
angulo_de_giro = randrange(0, 360)

#================================Aquí va el enunciado================================================================
enunciado = fr"""El triángulo ABC es rectángulo en B. AB mide {Matematica(a)} {unidad_de_medida}, BC mide {Matematica(b)} {unidad_de_medida} y AC mide {Matematica(c)} {unidad_de_medida}.
\begin{{center}}
\begin{{tikzpicture}}

\tkzDefPoint({-180+angulo_de_giro}:1){{C}}
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
\node [label={0+angulo_de_giro}:{Matematica(a)+f" {unidad_de_medida}"}] at (AB) {{}};
\node [label={-90+angulo_de_giro}:{Matematica(b)+f" {unidad_de_medida}"}] at (BC) {{}};
\node [label={-225+angulo_de_giro}:{Matematica(c)+f" {unidad_de_medida}"}] at (AC) {{}};
"""

if opcion==1:
    enunciado += fr"""\draw pic["${letra}$",draw,angle radius=1cm] {{angle=B--C--A}};
    \end{{tikzpicture}} \end{{center}}""" + Matematica(r"\sin"+letra+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(a/c)
    contenido_2 = Matematica(b/c)
    contenido_3 = Matematica(a/b)
    contenido_4 = Matematica(c/a)
    contenido_5 = Matematica(c/b)


elif opcion==2:
    enunciado += fr"""\draw pic["${letra}$",draw,angle radius=1cm] {{angle=B--C--A}};
    \end{{tikzpicture}} \end{{center}}""" + Matematica(r"\cos"+letra+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(b/c)
    contenido_2 = Matematica(a/c)
    contenido_3 = Matematica(a/b)
    contenido_4 = Matematica(c/a)
    contenido_5 = Matematica(c/a)


elif opcion==3:
    enunciado += fr"""\draw pic["${letra}$",draw,angle radius=1cm] {{angle=B--C--A}};
    \end{{tikzpicture}} \end{{center}}""" + Matematica(r"\tan"+letra+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(a/b)
    contenido_2 = Matematica(a/c)
    contenido_3 = Matematica(b/c)
    contenido_4 = Matematica(b/a)
    contenido_5 = Matematica(c/a)


elif opcion==4:
    enunciado += fr"""\draw pic["${letra}$",draw,angle radius=1cm] {{angle=C--A--B}};
    \end{{tikzpicture}} \end{{center}}""" + Matematica(r"\sin"+letra+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(b/c)
    contenido_2 = Matematica(a/c)
    contenido_3 = Matematica(b/a)
    contenido_4 = Matematica(c/b)
    contenido_5 = Matematica(c/a)


elif opcion==5:
    enunciado += fr"""\draw pic["${letra}$",draw,angle radius=1cm] {{angle=C--A--B}};
    \end{{tikzpicture}} \end{{center}}""" + Matematica(r"\cos"+letra+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(a/c)
    contenido_2 = Matematica(b/c)
    contenido_3 = Matematica(b/a)
    contenido_4 = Matematica(c/a)
    contenido_5 = Matematica(c/b)


elif opcion==6:
    enunciado += fr"""\draw pic["${letra}$",draw,angle radius=1cm] {{angle=C--A--B}};
    \end{{tikzpicture}} \end{{center}}""" + Matematica(r"\tan"+letra+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(b/a)
    contenido_2 = Matematica(a/c)
    contenido_3 = Matematica(b/c)
    contenido_4 = Matematica(c/a)
    contenido_5 = Matematica(c/b)




enunciado_oculto = [a, b, c, opcion]










