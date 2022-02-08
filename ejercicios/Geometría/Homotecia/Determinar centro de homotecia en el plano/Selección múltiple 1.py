{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
A, B, C = Par(randrange(-5,5),randrange(-5,5)), Par(randrange(-5,5),randrange(-5,5)), Par(randrange(-5,5),randrange(-5,5))
O = Par(randrange(-5,5),randrange(-5,5))
k = elegir(-2,3, 0,1)
AO, BO, CO = k*(A-O)+O, k*(B-O)+O, k*(C-O)+O
while not -5<=AO.x<=5 or not -5<=AO.y<=5 or not -5<=BO.x<=5 or not -5<=BO.y<=5 or not -5<=CO.x<=5 or not -5<=CO.y<=5 or O in [A,B,C,AO,BO,CO] or A.x==B.x==C.x or A.y==B.y==C.y or (A.y-B.y)*(B.x-C.x)==(B.y-C.y)*(A.x-B.x):
    A, B, C = Par(randrange(-5,5),randrange(-5,5)), Par(randrange(-5,5),randrange(-5,5)), Par(randrange(-5,5),randrange(-5,5))
    O = Par(randrange(-5,5),randrange(-5,5))
    k = elegir(-2,3, 0,1)
    AO, BO, CO = k*(A-O)+O, k*(B-O)+O, k*(C-O)+O

#================================Aquí va el enunciado================================================================
enunciado = fr"""A continuación se muestra el triángulo ABC sobre el cual se realizó una homotecia obteniéndo el triángulo A'B'C'
\begin{{center}} \begin{{tikzpicture}} [scale=0.5]
\draw [step=1, thin, gray!50, dashed] (-5,-5) grid (5,5);
\draw [<->] (-6,0) -- (6,0) node[right] {{X}};
\draw [<->] (0,-6) -- (0,6) node[above] {{Y}};
\foreach \i in {{1,...,5}}
    \draw
        (\i , 0) node [anchor=north, font=\footnotesize] {{$\i$}}
        (-\i , 0) node [anchor=north, font=\footnotesize] {{$-\i$}}
        (0 , \i) node [anchor=east, font=\footnotesize] {{$\i$}}
        (0 , -\i) node [anchor=east, font=\footnotesize] {{$-\i$}};

\tkzDefPoint({A.x},{A.y}){{A}}
\tkzDefPoint({B.x},{B.y}){{B}}
\tkzDefPoint({C.x},{C.y}){{C}}
\tkzDefPoint({AO.x},{AO.y}){{A'}}
\tkzDefPoint({BO.x},{BO.y}){{B'}}
\tkzDefPoint({CO.x},{CO.y}){{C'}}

\tkzDrawPoints[fill=black](A,B,C, A',B',C')

\tkzDrawPolygon(A,B,C)
\tkzDrawPolygon(A',B',C')

\tkzLabelPoints[above](A)
\tkzLabelPoints[above](B)
\tkzLabelPoints[above](C)

\tkzLabelPoints[above](A')
\tkzLabelPoints[above](B')
\tkzLabelPoints[above](C')

\end{{tikzpicture}} \end{{center}}
Las coordenadas del centro de homotecia son"""

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(O, arreglar_espacios=True)
contenido_2 =        Matematica((A+BO)/2, arreglar_espacios=True)
contenido_3 =        Matematica((A+CO)/2, arreglar_espacios=True)
contenido_4 =        Matematica((B+CO)/2, arreglar_espacios=True)
contenido_5 =        Matematica((C+AO)/2, arreglar_espacios=True)



enunciado_oculto = [A, B, C, O, k]










