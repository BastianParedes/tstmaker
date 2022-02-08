opcion = choice([1,2])

if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    distancia_maxima = racional(randrange(3,10))
    distancia_minima = racional(randrange(1,10))
    while not distancia_minima<distancia_maxima or distancia_maxima==2*distancia_minima:
        distancia_maxima = racional(randrange(3,10))
        distancia_minima = racional(randrange(1,10))
    #================================Aquí va el enunciado================================================================
    enunciado = f"Un péndulo en reposo está a {distancia_minima} cm del suelo, pero cuando se mueve alcanza una altura máxima de {distancia_maxima} cm. De los siguientes gráficos, el que mejor modela la distancia entre el suelo y el péndulo respecto del tiempo es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = fr"""\begin{{tabular}}{{l}}
    \begin{{tikzpicture}} [scale=0.3]
    \draw [<->] (-1,0) -- (7,0) node[right] {{tiempo}};
    \draw [<->] (0,-1) -- (0,4) node[above] {{distancia}};
    \draw [domain=0:6.2] plot (\x , {{sin(deg(\x))+2}});
    \draw (0,3) node [anchor=east, font=\footnotesize] {{${distancia_maxima}$}};
    \draw (0,1) node [anchor=east, font=\footnotesize] {{${distancia_minima}$}};
    \tkzDefPoint(0,3){{A}}
    \tkzDefPoint(1.5,3){{B}}
    \tkzDefPoint(0,1){{C}}
    \tkzDefPoint(4.7,1){{D}}
    \tkzDrawSegment[dashed, very thin](A,B)
    \tkzDrawSegment[dashed, very thin](C,D)
    \end{{tikzpicture}} \end{{tabular}}"""
    contenido_2 = fr"""\begin{{tabular}}{{l}}
    \begin{{tikzpicture}} [scale=0.3]
    \draw [<->] (-1,0) -- (7,0) node[right] {{tiempo}};
    \draw [<->] (0,-1) -- (0,4) node[above] {{distancia}};
    \draw [domain=0:6.2] plot (\x , {{sin(deg(\x))+2}});
    \draw (0,3) node [anchor=east, font=\footnotesize] {{${distancia_maxima}$}};
    \draw (0,1) node [anchor=east, font=\footnotesize] {{${distancia_maxima-distancia_minima}$}};
    \tkzDefPoint(0,3){{A}}
    \tkzDefPoint(1.5,3){{B}}
    \tkzDefPoint(0,1){{C}}
    \tkzDefPoint(4.7,1){{D}}
    \tkzDrawSegment[dashed, very thin](A,B)
    \tkzDrawSegment[dashed, very thin](C,D)
    \end{{tikzpicture}} \end{{tabular}}"""
    contenido_3 = fr"""\begin{{tabular}}{{l}}
    \begin{{tikzpicture}} [scale=0.3]
    \draw [<->] (-1,0) -- (7,0) node[right] {{tiempo}};
    \draw [<->] (0,-1) -- (0,4) node[above] {{distancia}};
    \draw [domain=0:6.2] plot (\x , {{sin(deg(\x))+2}});
    \draw (0,3) node [anchor=east, font=\footnotesize] {{${max(distancia_maxima-distancia_minima,distancia_minima)}$}};
    \draw (0,1) node [anchor=east, font=\footnotesize] {{${min(distancia_maxima-distancia_minima,distancia_minima)}$}};
    \tkzDefPoint(0,3){{A}}
    \tkzDefPoint(1.5,3){{B}}
    \tkzDefPoint(0,1){{C}}
    \tkzDefPoint(4.7,1){{D}}
    \tkzDrawSegment[dashed, very thin](A,B)
    \tkzDrawSegment[dashed, very thin](C,D)
    \end{{tikzpicture}} \end{{tabular}}"""
    contenido_4 = fr"""\begin{{tabular}}{{l}}
    \begin{{tikzpicture}} [scale=0.3]
    \draw [<->] (-1,0) -- (7,0) node[right] {{tiempo}};
    \draw [<->] (0,-4) -- (0,1) node[above] {{distancia}};
    \draw [domain=0:6.2] plot (\x , {{sin(deg(\x))-2}});
    \draw (0,-1) node [anchor=east, font=\footnotesize] {{${-distancia_maxima}$}};
    \draw (0,-3) node [anchor=east, font=\footnotesize] {{${-distancia_minima}$}};
    \tkzDefPoint(0,-1){{A}}
    \tkzDefPoint(1.5,-1){{B}}
    \tkzDefPoint(0,-3){{C}}
    \tkzDefPoint(4.7,-3){{D}}
    \tkzDrawSegment[dashed, very thin](A,B)
    \tkzDrawSegment[dashed, very thin](C,D)
    \end{{tikzpicture}} \end{{tabular}}"""
    contenido_5 = fr"""\begin{{tabular}}{{l}}
    \begin{{tikzpicture}} [scale=0.3]
    \draw [<->] (-1,0) -- (7,0) node[right] {{tiempo}};
    \draw [<->] (0,-4) -- (0,1) node[above] {{distancia}};
    \draw [domain=0:6.2] plot (\x , {{sin(deg(\x))-2}});
    \draw (0,-1) node [anchor=east, font=\footnotesize] {{${-distancia_minima}$}};
    \draw (0,-3) node [anchor=east, font=\footnotesize] {{${-distancia_maxima}$}};
    \tkzDefPoint(0,-1){{A}}
    \tkzDefPoint(1.5,-1){{B}}
    \tkzDefPoint(0,-3){{C}}
    \tkzDefPoint(4.7,-3){{D}}
    \tkzDrawSegment[dashed, very thin](A,B)
    \tkzDrawSegment[dashed, very thin](C,D)
    \end{{tikzpicture}} \end{{tabular}}"""


elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    distancia_maxima = 2*racional(randrange(1,20))
    #================================Aquí va el enunciado================================================================
    enunciado = f"La altura de la marea de cierta ciudad se puede modelar con una función sin(x). Las altura de las olas se miden con boyas oceánicas y se considera que la altura promedio en el día es 0 metros. Si la altura máxima que alcanzan las olas es de {distancia_maxima} metros, entonces de los siguientes gráficos el que mejor modela la altura de las olas respecto de la hora es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = fr"""\begin{{tabular}}{{l}}
    \begin{{tikzpicture}} [scale=0.3]
    \draw [<->] (-1,0) -- (7,0) node[right] {{hora}};
    \draw [<->] (0,-3) -- (0,3) node[above] {{altura [m]}};
    \draw [domain=0:6.2] plot (\x , {{sin(deg(\x))}});
    \draw (0,1) node [anchor=east, font=\footnotesize] {{${distancia_maxima}$}};
    \draw (0,-1) node [anchor=east, font=\footnotesize] {{${-distancia_maxima}$}};
    \tkzDefPoint(0,1){{A}}
    \tkzDefPoint(1.5,1){{B}}
    \tkzDefPoint(0,-1){{C}}
    \tkzDefPoint(4.7,-1){{D}}
    \tkzDrawSegment[dashed, very thin](A,B)
    \tkzDrawSegment[dashed, very thin](C,D)
    \end{{tikzpicture}} \end{{tabular}}"""
    contenido_2 = fr"""\begin{{tabular}}{{l}}
    \begin{{tikzpicture}} [scale=0.3]
    \draw [<->] (-1,0) -- (7,0) node[right] {{hora}};
    \draw [<->] (0,-3) -- (0,3) node[above] {{altura [m]}};
    \draw [domain=0:6.2] plot (\x , {{sin(deg(\x))}});
    \draw (0,1) node [anchor=east, font=\footnotesize] {{${distancia_maxima/2}$}};
    \draw (0,-1) node [anchor=east, font=\footnotesize] {{${-distancia_maxima/2}$}};
    \tkzDefPoint(0,1){{A}}
    \tkzDefPoint(1.5,1){{B}}
    \tkzDefPoint(0,-1){{C}}
    \tkzDefPoint(4.7,-1){{D}}
    \tkzDrawSegment[dashed, very thin](A,B)
    \tkzDrawSegment[dashed, very thin](C,D)
    \end{{tikzpicture}} \end{{tabular}}"""
    contenido_3 = fr"""\begin{{tabular}}{{l}}
    \begin{{tikzpicture}} [scale=0.3]
    \draw [<->] (-1,0) -- (7,0) node[right] {{hora}};
    \draw [<->] (0,-2) -- (0,4) node[above] {{altura [m]}};
    \draw [domain=0:6.2] plot (\x , {{sin(deg(\x))+1}});
    \draw (0,2) node [anchor=east, font=\footnotesize] {{${distancia_maxima}$}};
    \tkzDefPoint(0,2){{A}}
    \tkzDefPoint(1.5,2){{B}}
    \tkzDrawSegment[dashed, very thin](A,B)
    \end{{tikzpicture}} \end{{tabular}}"""
    contenido_4 = fr"""\begin{{tabular}}{{l}}
    \begin{{tikzpicture}} [scale=0.3]
    \draw [<->] (-1,0) -- (7,0) node[right] {{hora}};
    \draw [<->] (0,-2) -- (0,4) node[above] {{altura [m]}};
    \draw [domain=0:6.2] plot (\x , {{sin(deg(\x))+1}});
    \draw (0,2) node [anchor=east, font=\footnotesize] {{${distancia_maxima/2}$}};
    \tkzDefPoint(0,2){{A}}
    \tkzDefPoint(1.5,2){{B}}
    \tkzDrawSegment[dashed, very thin](A,B)
    \end{{tikzpicture}} \end{{tabular}}"""
    contenido_5 = fr"""\begin{{tabular}}{{l}}
    \begin{{tikzpicture}} [scale=0.3]
    \draw [<->] (-1,0) -- (7,0) node[right] {{hora}};
    \draw [<->] (0,-4) -- (0,2) node[above] {{altura [m]}};
    \draw [domain=0:6.2] plot (\x , {{sin(deg(\x))-1}});
    \draw (0,-2) node [anchor=east, font=\footnotesize] {{${-distancia_maxima/choice([1,2])}$}};
    \tkzDefPoint(0,-1){{A}}
    \tkzDefPoint(4.7,-1){{B}}
    \tkzDrawSegment[dashed, very thin](A,B)
    \end{{tikzpicture}} \end{{tabular}}"""



enunciado_oculto = enunciado
