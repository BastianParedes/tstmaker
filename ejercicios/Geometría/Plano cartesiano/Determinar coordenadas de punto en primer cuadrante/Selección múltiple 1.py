{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
x, y = Racional(randrange(0,10)), Racional(randrange(0,10))
while x==y==0:
    x, y = Racional(randrange(0,10)), Racional(randrange(0,10))

#================================Aquí va el enunciado================================================================
enunciado = fr"""¿Cuales son las coordenadas del punto representado en el siguiente plano cartesiano?
\begin{{center}}
\begin{{tikzpicture}} [scale=0.4]
\draw [step=1, thin, gray!50] (0,0) grid (9,9);
\draw [->] (0,0) -- (10,0) node[right] {{X}};
\draw [->] (0,0) -- (0,10) node[above] {{Y}};
\foreach \i in {{1,...,9}}
    \draw
        (\i , 0) node [anchor=north, font=\footnotesize] {{$\i$}}
        (0 , \i) node [anchor=east, font=\footnotesize] {{$\i$}};
\tkzDefPoint({x},{y}){{P}}
\tkzDrawPoints(P)
\end{{tikzpicture}}
\end{{center}}
"""
#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(Par(x,y))

if x==y:
    contenido_2 = Matematica(Par(0,y))
    contenido_3 = Matematica(Par(x,0))
    contenido_4 = Matematica(Par(x-1,y-1))
    contenido_5 = Matematica(choice([Par(x-1,0),Par(0,y-1)]))

elif x==0 or y==0:
    contenido_2 = Matematica(Par(x+y,x+y))
    contenido_3 = Matematica(Par(y,x))
    contenido_4 = Matematica(Par(randrange(1, 9),randrange(1, 9)))
    contenido_5 = Matematica(Par(randrange(1, 9),randrange(1, 9)))

else:
    lista_de_contenidos = [Matematica(Par(y,x)), Matematica(Par(0,y)), Matematica(Par(x,0)), Matematica(Par(y,0)), Matematica(Par(0,x))]
    contenido_2 = choice(lista_de_contenidos)
    lista_de_contenidos.remove(contenido_2)
    contenido_3 = choice(lista_de_contenidos)
    lista_de_contenidos.remove(contenido_3)
    contenido_4 = choice(lista_de_contenidos)
    lista_de_contenidos.remove(contenido_4)
    contenido_5 = choice(lista_de_contenidos)
    lista_de_contenidos.remove(contenido_5)



enunciado_oculto = [x,y]










