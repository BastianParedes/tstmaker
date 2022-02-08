{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
x, y = Racional(randrange(-5,5)), Racional(randrange(-5,5))
while x==y==0:
    x, y = Racional(randrange(-5,5)), Racional(randrange(-5,5))

#================================Aquí va el enunciado================================================================
enunciado = fr"""¿Cuales son las coordenadas del punto P representado en el siguiente plano cartesiano?
\begin{{center}}
\begin{{tikzpicture}} [scale=0.4]
\draw [step=1, thin, gray!50] (-5,-5) grid (5,5);
\draw [<->] (-6,0) -- (6,0) node[right] {{X}};
\draw [<->] (0,-6) -- (0,6) node[right] {{Y}};
\foreach \i in {{1,...,5}}
    \draw
        (\i , 0) node [anchor=north, font=\footnotesize] {{$\i$}}
        (0 , \i) node [anchor=east, font=\footnotesize] {{$\i$}}
        (-\i , 0) node [anchor=north, font=\footnotesize] {{$-\i$}}
        (0 , -\i) node [anchor=east, font=\footnotesize] {{$-\i$}};
\tkzDefPoint({x},{y}){{P}}
\tkzDrawPoints(P)
\tkzLabelPoints[above](P)
\end{{tikzpicture}}
\end{{center}}
"""
#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(Par(x,y))

if abs(x)==abs(y):
    contenido_2 = Matematica(Par(-x,-y))
    contenido_3 = Matematica(Par(-x,y))
    contenido_4 = Matematica(Par(x,-y))
    contenido_5 = Matematica(Par(x+y,0))

elif x==0 or y==0:
    contenido_2 = Matematica(Par(-x,-y))
    contenido_3 = Matematica(Par(y,x))
    contenido_4 = Matematica(Par(-y,-x))
    contenido_5 = Matematica(Par(x+y,x+y))

else:
    lista_de_contenidos = [Matematica(Par(-x,-y)), Matematica(Par(-x,y)), Matematica(Par(x,-y)), Matematica(Par(y,x)), Matematica(Par(-y,-x)), Matematica(Par(-y,x)), Matematica(Par(y,-x))]
    contenido_2 = choice(lista_de_contenidos)
    lista_de_contenidos.remove(contenido_2)
    contenido_3 = choice(lista_de_contenidos)
    lista_de_contenidos.remove(contenido_3)
    contenido_4 = choice(lista_de_contenidos)
    lista_de_contenidos.remove(contenido_4)
    contenido_5 = choice(lista_de_contenidos)
    lista_de_contenidos.remove(contenido_5)



enunciado_oculto = Par(x,y)










