{"cantidad_opciones":2, "cantidad_disponible":50}

if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========}
    while True:
        p1 = Par(elegir(-6,6, -1,0,1) , elegir(-6,6, -1,0,1))
        p2 = Par(elegir(-6,6, -1,0,1) , elegir(-6,6, -1,0,1))
        pr = p1 + p2

        if pr.x != 0 and pr.y != 0 and abs(pr) <= 6 and abs(p1-p2) <= 6 and abs(Racional(p1.x,p2.x)) != abs(Racional(p1.y,p2.y)) and abs(Racional(p1.x,pr.x)) != abs(Racional(p1.y,pr.y)) and abs(Racional(p2.x,pr.x)) != abs(Racional(p2.y,pr.y)):
            break
    #================================Aquí va el enunciado================================================================
    enunciado = f"Sean los vectores " + Matematica(vector('v')+'='+p1) + " y " + Matematica(vector('u')+'='+p2) + ". La alternativa que muestra correctamente la operación " + Matematica(vector('v') + "+" + vector('u')) + " es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = fr"""\begin{{tabular}}{{l}}
\begin{{tikzpicture}} [scale=0.28]
\draw [step=1, thin, gray!50] (-6,-6) grid (6,6);
\draw [<->] (-6,0) -- (6,0) node[right] {{X}};
\draw [<->] (0,-6) -- (0,6) node[above] {{Y}};

\draw [->, line width=0.7pt] (0,0) -- ({float(p1.x)} , {float(p1.y)});
\draw [->, line width=0.7pt] (0,0) -- ({float(p2.x)} , {float(p2.y)});
\draw [->, thin, gray!120] ({float(p1.x)} , {float(p1.y)}) -- ({float(pr.x)} , {float(pr.y)});
\draw [->, line width=1pt] (0,0) -- ({float(pr.x)} , {float(pr.y)});

\end{{tikzpicture}} \end{{tabular}}"""

    #el primero está negativo
    contenido_2 = fr"""\begin{{tabular}}{{l}}
\begin{{tikzpicture}} [scale=0.28]
\draw [step=1, thin, gray!50] (-6,-6) grid (6,6);
\draw [<->] (-6,0) -- (6,0) node[right] {{X}};
\draw [<->] (0,-6) -- (0,6) node[above] {{Y}};

\draw [->, line width=0.7pt] (0,0) -- ({float(p1.x)} , {float(p1.y)});
\draw [->, line width=0.7pt] (0,0) -- ({float(p2.x)} , {float(p2.y)});
\draw [->, thin, gray!120] (0,0) -- ({float((-p1).x)} , {float((-p1).y)});
\draw [->, thin, gray!120] ({float((-p1).x)} , {float((-p1).y)}) -- ({float((-p1+p2).x)} , {float((-p1+p2).y)});
\draw [->, line width=1pt] (0,0) -- ({float((-p1+p2).x)} , {float((-p1+p2).y)});

\end{{tikzpicture}} \end{{tabular}}"""

    #el primero está negativo, segunda posisicón
    contenido_3 = fr"""\begin{{tabular}}{{l}}
\begin{{tikzpicture}} [scale=0.28]
\draw [step=1, thin, gray!50] (-6,-6) grid (6,6);
\draw [<->] (-6,0) -- (6,0) node[right] {{X}};
\draw [<->] (0,-6) -- (0,6) node[above] {{Y}};

\draw [->, line width=0.7pt] (0,0) -- ({float(p1.x)} , {float(p1.y)});
\draw [->, line width=0.7pt] (0,0) -- ({float(p2.x)} , {float(p2.y)});
\draw [->, thin, gray!120] (0,0) -- ({float((-p1).x)} , {float((-p1).y)});
\draw [->, thin, gray!120] ({float((p2).x)} , {float((p2).y)}) -- ({float((-p1+p2).x)} , {float((-p1+p2).y)});
\draw [->, line width=1pt] (0,0) -- ({float((-p1+p2).x)} , {float((-p1+p2).y)});

\end{{tikzpicture}} \end{{tabular}}"""

    #el segundo está negativo
    contenido_4 = fr"""\begin{{tabular}}{{l}}
\begin{{tikzpicture}} [scale=0.28]
\draw [step=1, thin, gray!50] (-6,-6) grid (6,6);
\draw [<->] (-6,0) -- (6,0) node[right] {{X}};
\draw [<->] (0,-6) -- (0,6) node[above] {{Y}};

\draw [->, line width=0.7pt] (0,0) -- ({float(p1.x)} , {float(p1.y)});
\draw [->, line width=0.7pt] (0,0) -- ({float(p2.x)} , {float(p2.y)});
\draw [->, thin, gray!120] (0,0) -- ({float((-p2).x)} , {float((-p2).y)});
\draw [->, thin, gray!120] ({float((-p2).x)} , {float((-p2).y)}) -- ({float((p1-p2).x)} , {float((p1-p2).y)});
\draw [->, line width=1pt] (0,0) -- ({float((p1-p2).x)} , {float((p1-p2).y)});

\end{{tikzpicture}} \end{{tabular}}"""

    #ambos están negativos
    contenido_5 = fr"""\begin{{tabular}}{{l}}
\begin{{tikzpicture}} [scale=0.28]
\draw [step=1, thin, gray!50] (-6,-6) grid (6,6);
\draw [<->] (-6,0) -- (6,0) node[right] {{X}};
\draw [<->] (0,-6) -- (0,6) node[above] {{Y}};

\draw [->, line width=0.7pt] (0,0) -- ({float(p1.x)} , {float(p1.y)});
\draw [->, line width=0.7pt] (0,0) -- ({float(p2.x)} , {float(p2.y)});
\draw [->, thin, gray!120] (0,0) -- ({float(-p1.x)} , {float(-p1.y)});
\draw [->, thin, gray!120] (0,0) -- ({float(-p2.x)} , {float(-p2.y)});
\draw [->, thin, gray!120] ({float(-p1.x)} , {float(-p1.y)}) -- ({float((-p1-p2).x)} , {float((-p1-p2).y)});
\draw [->, line width=1pt] (0,0) -- ({float((-p1-p2).x)} , {float((-p1-p2).y)});

\end{{tikzpicture}} \end{{tabular}}"""

    enunciado_oculto = [opcion , p1 , p2]


elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    while True:
        p1 = Par(elegir(-6,6, -1,0,1) , elegir(-6,6, -1,0,1))
        p2 = Par(elegir(-6,6, -1,0,1) , elegir(-6,6, -1,0,1))
        pr = p1 - p2
        
        if pr.x != 0 and pr.y != 0 and abs(pr) <= 6 and abs(p1+p2) <= 6 and abs(Racional(p1.x,p2.x)) != abs(Racional(p1.y,p2.y)) and abs(Racional(p1.x,pr.x)) != abs(Racional(p1.y,pr.y)) and abs(Racional(p2.x,pr.x)) != abs(Racional(p2.y,pr.y)):
            break
    #================================Aquí va el enunciado================================================================
    enunciado = f"Sean los vectores " + Matematica(vector('v')+'='+p1) + " y " + Matematica(vector('u')+'='+p2) + ". La alternativa que muestra correctamente la operación " + Matematica(vector('v') + "-" + vector('u')) + " es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = fr"""\begin{{tabular}}{{l}}
\begin{{tikzpicture}} [scale=0.28]
\draw [step=1, thin, gray!50] (-6,-6) grid (6,6);
\draw [<->] (-6,0) -- (6,0) node[right] {{X}};
\draw [<->] (0,-6) -- (0,6) node[above] {{Y}};

\draw [->, line width=0.7pt] (0,0) -- ({float(p1.x)} , {float(p1.y)});
\draw [->, line width=0.7pt] (0,0) -- ({float(p2.x)} , {float(p2.y)});
\draw [->, thin, gray!120] (0,0) -- ({float((-p2).x)} , {float((-p2).y)});
\draw [->, thin, gray!120] ({float((-p2).x)} , {float((-p2).y)}) -- ({float((p1-p2).x)} , {float((p1-p2).y)});
\draw [->, line width=1pt] (0,0) -- ({float((p1-p2).x)} , {float((p1-p2).y)});

\end{{tikzpicture}} \end{{tabular}}"""

    #el primero está negativo
    contenido_2 = fr"""\begin{{tabular}}{{l}}
\begin{{tikzpicture}} [scale=0.28]
\draw [step=1, thin, gray!50] (-6,-6) grid (6,6);
\draw [<->] (-6,0) -- (6,0) node[right] {{X}};
\draw [<->] (0,-6) -- (0,6) node[above] {{Y}};

\draw [->, line width=0.7pt] (0,0) -- ({float(p1.x)} , {float(p1.y)});
\draw [->, line width=0.7pt] (0,0) -- ({float(p2.x)} , {float(p2.y)});
\draw [->, thin, gray!120] (0,0) -- ({float((-p1).x)} , {float((-p1).y)});
\draw [->, thin, gray!120] ({float((-p1).x)} , {float((-p1).y)}) -- ({float((-p1+p2).x)} , {float((-p1+p2).y)});
\draw [->, line width=1pt] (0,0) -- ({float((-p1+p2).x)} , {float((-p1+p2).y)});

\end{{tikzpicture}} \end{{tabular}}"""

    #el primero está negativo, segunda posisicón
    contenido_3 = fr"""\begin{{tabular}}{{l}}
\begin{{tikzpicture}} [scale=0.28]
\draw [step=1, thin, gray!50] (-6,-6) grid (6,6);
\draw [<->] (-6,0) -- (6,0) node[right] {{X}};
\draw [<->] (0,-6) -- (0,6) node[above] {{Y}};

\draw [->, line width=0.7pt] (0,0) -- ({float(p1.x)} , {float(p1.y)});
\draw [->, line width=0.7pt] (0,0) -- ({float(p2.x)} , {float(p2.y)});
\draw [->, thin, gray!120] (0,0) -- ({float((-p1).x)} , {float((-p1).y)});
\draw [->, thin, gray!120] ({float((p2).x)} , {float((p2).y)}) -- ({float((-p1+p2).x)} , {float((-p1+p2).y)});
\draw [->, line width=1pt] (0,0) -- ({float((-p1+p2).x)} , {float((-p1+p2).y)});

\end{{tikzpicture}} \end{{tabular}}"""

    #ambos están positivos
    contenido_4 = fr"""\begin{{tabular}}{{l}}
\begin{{tikzpicture}} [scale=0.28]
\draw [step=1, thin, gray!50] (-6,-6) grid (6,6);
\draw [<->] (-6,0) -- (6,0) node[right] {{X}};
\draw [<->] (0,-6) -- (0,6) node[above] {{Y}};

\draw [->, line width=0.7pt] (0,0) -- ({float(p1.x)} , {float(p1.y)});
\draw [->, line width=0.7pt] (0,0) -- ({float(p2.x)} , {float(p2.y)});
\draw [->, thin, gray!120] ({float(p1.x)} , {float(p1.y)}) -- ({float((p1+p2).x)} , {float((p1+p2).y)});
\draw [->, line width=1pt] (0,0) -- ({float((p1+p2).x)} , {float((p1+p2).y)});

\end{{tikzpicture}} \end{{tabular}}"""

    #ambos están negativos
    contenido_5 = fr"""\begin{{tabular}}{{l}}
\begin{{tikzpicture}} [scale=0.28]
\draw [step=1, thin, gray!50] (-6,-6) grid (6,6);
\draw [<->] (-6,0) -- (6,0) node[right] {{X}};
\draw [<->] (0,-6) -- (0,6) node[above] {{Y}};

\draw [->, line width=0.7pt] (0,0) -- ({float(p1.x)} , {float(p1.y)});
\draw [->, line width=0.7pt] (0,0) -- ({float(p2.x)} , {float(p2.y)});
\draw [->, thin, gray!120] (0,0) -- ({float(-p1.x)} , {float(-p1.y)});
\draw [->, thin, gray!120] (0,0) -- ({float(-p2.x)} , {float(-p2.y)});
\draw [->, thin, gray!120] ({float(-p1.x)} , {float(-p1.y)}) -- ({float((-p1-p2).x)} , {float((-p1-p2).y)});
\draw [->, line width=1pt] (0,0) -- ({float((-p1-p2).x)} , {float((-p1-p2).y)});

\end{{tikzpicture}} \end{{tabular}}"""

    enunciado_oculto = [opcion , p1 , p2]

