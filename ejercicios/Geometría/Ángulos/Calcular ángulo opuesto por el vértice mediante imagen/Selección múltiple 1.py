{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
letra = choice([r"\alpha", r"\beta", r"\gamma"])
angulo_conocido = elegir(45,135,90)
angulo_de_giro = elegir(0,360)

#================================Aquí va el enunciado================================================================
enunciado = fr"""¿Cuál es el valor de ${letra}$?

\begin{{center}}
\begin{{tikzpicture}} [scale=1]

\tkzDefPoint(0,0){{O}}
\tkzDefPoint({0+angulo_de_giro}:1.5){{A}}
\tkzDefPoint({angulo_conocido+angulo_de_giro}:1.5){{B}}
\tkzDefPoint({180+angulo_de_giro}:1.5){{C}}
\tkzDefPoint({angulo_conocido+180+angulo_de_giro}:1.5){{D}}

\tkzDrawPoints(A,B,C,D)

\node [label={270+angulo_de_giro}:A] at (A){{}};
\node [label={90+angulo_conocido+angulo_de_giro}:B] at (B){{}};
\node [label={90+angulo_de_giro}:C] at (C){{}};
\node [label={270+angulo_conocido+angulo_de_giro}:B] at (D){{}};

\tkzDrawSegment[<->,add=0.1 and 0.1](A,C)
\tkzDrawSegment[<->,add=0.1 and 0.1](B,D)

\draw pic["{Matematica(str(angulo_conocido)+'°')}",draw,angle radius=0.8cm] {{angle=A--O--B}};
\draw pic["${letra}$",draw,angle radius=0.7cm] {{angle=C--O--D}};

\end{{tikzpicture}}
\end{{center}}"""

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(str(angulo_conocido)+"°")
contenido_2 = Matematica(str(abs(90-angulo_conocido))+"°")
contenido_3 = Matematica(str(360-angulo_conocido)+"°")
contenido_4 = Matematica(str(180-angulo_conocido)+"°")
contenido_5 = Matematica(str(2*angulo_conocido)+"°")


enunciado_oculto = angulo_conocido










