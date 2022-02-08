{"cantidad_opciones":3, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b, c = Racional(randrange(1, 21)), Racional(randrange(1, 21)), Racional(randrange(1, 21))
while 180*a/(a+b+c)<40 or 180*b/(a+b+c)<40 or 180*c/(a+b+c)<40 or 180%(a+b+c).numerador!=0:
    a, b, c = Racional(randrange(1, 11)), Racional(randrange(1, 11)), Racional(randrange(1, 11))
angulo_de_giro = randrange(0, 360)

#================================Aquí va el enunciado================================================================
enunciado = fr"""En el siguiente triángulo el ángulo BAC mide {Matematica(a*"x")} grados, el ángulo CBA mide {Matematica(b*"x")} grados y el ángulo ACB mide {Matematica(c*"x")} grados.
\begin{{center}}
\begin{{tikzpicture}}[scale=2]
\tkzDefPoint({(180+angulo_de_giro)%360}:1){{A}}
\tkzDefPoint({angulo_de_giro}:1){{B}}
\tkzDefTriangle[two angles= {180*a/(a+b+c)} and {180*b/(a+b+c)}](A,B) \tkzGetPoint{{C}}
\tkzDrawPolygon(A,B,C)

\node [label={(200+angulo_de_giro)%360}:A] at (A){{}};
\node [label={(-30+angulo_de_giro)%360}:B] at (B){{}};
\node [label={(90+angulo_de_giro)%360}:C] at (C){{}};

\draw pic["{Matematica(a*"x")}",draw,angle radius=0.8cm] {{angle=B--A--C}};
\draw pic["{Matematica(b*"x")}",draw,angle radius=0.8cm] {{angle=C--B--A}};
\draw pic["{Matematica(c*"x")}",draw,angle radius=0.8cm] {{angle=A--C--B}};

\end{{tikzpicture}} \end{{center}} 
En valor de x, en grados, es"""

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
if a==b==c:
    contenido_correcto = Matematica(180/(a+b+c))
    contenido_2 = Matematica(60)
    contenido_3 = Matematica(a)
    contenido_4 = Matematica(2*a)
    contenido_5 = Matematica(3*a)

elif a==b:
    contenido_correcto = Matematica(180/(a+b+c))
    contenido_2 = Matematica(180/a)
    contenido_3 = Matematica(180*a/(a+b+c))
    contenido_4 = Matematica(180/c)
    contenido_5 = Matematica(180*c/(a+b+c))

elif b==c:
    contenido_correcto = Matematica(180/(a+b+c))
    contenido_2 = Matematica(180/a)
    contenido_3 = Matematica(180*b)
    contenido_4 = Matematica(180*b/(a+b+c))
    contenido_5 = Matematica(180*a/(a+b+c))

elif a==c:
    contenido_correcto = Matematica(180/(a+b+c))
    contenido_2 = Matematica(180*c/(a+b+c))
    contenido_3 = Matematica(180*b)
    contenido_4 = Matematica(180/c)
    contenido_5 = Matematica(180*b/(a+b+c))

else:
    contenido_correcto = Matematica(180/(a+b+c))
    contenido_2 = Matematica(180/a)
    contenido_3 = Matematica(180/b)
    contenido_4 = Matematica(180/c)
    contenido_5 = Matematica(180*choice([a, b, c])/(a+b+c))

enunciado_oculto = [a, b, c]










