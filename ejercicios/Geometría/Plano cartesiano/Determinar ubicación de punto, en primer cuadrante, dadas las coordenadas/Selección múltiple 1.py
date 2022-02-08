{"cantidad_opciones":1, "cantidad_disponible":50}

def plano_con_punto(x,y):
    return fr"""\begin{{tabular}}{{l}} \begin{{tikzpicture}} [scale=0.3]
\draw [step=1, thin, gray!50] (0,0) grid (9,9);
\draw [->] (0,0) -- (10,0) node[right] {{X}};
\draw [->] (0,0) -- (0,10) node[above] {{Y}};
\foreach \i in {{1,...,9}} \draw
(\i , 0) node [anchor=north, font=\scriptsize] {{$\i$}}
(0 , \i) node [anchor=east, font=\scriptsize] {{$\i$}};
\tkzDefPoint({x},{y}){{P}}
\tkzDrawPoints(P)
\end{{tikzpicture}} \end{{tabular}}"""

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
x, y = Racional(randrange(0,10)), Racional(randrange(0,10))
while x==y==0:
    x, y = Racional(randrange(0,10)), Racional(randrange(0,10))

#================================Aquí va el enunciado================================================================
enunciado = fr"""De los siguientes planos cartesianos, ¿Cuál es el que mejor representa al punto {Par(x,y)}?"""

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = plano_con_punto(x,y)

if x==y:
    contenido_2 = plano_con_punto(0,y)
    contenido_3 = plano_con_punto(x,0)
    contenido_4 = plano_con_punto(x-1,y-1)
    contenido_5 = choice([plano_con_punto(x-1,0),plano_con_punto(0,y-1)])

elif x==0 or y==0:
    contenido_2 = plano_con_punto(x+y,x+y)
    contenido_3 = plano_con_punto(y,x)
    contenido_4 = plano_con_punto(randrange(1, 9),randrange(1, 9))
    contenido_5 = plano_con_punto(randrange(1, 9),randrange(1, 9))

else:
    lista_de_contenidos = [plano_con_punto(y,x), plano_con_punto(0,y), plano_con_punto(x,0), plano_con_punto(y,0), plano_con_punto(0,x)]
    contenido_2 = choice(lista_de_contenidos)
    lista_de_contenidos.remove(contenido_2)
    contenido_3 = choice(lista_de_contenidos)
    lista_de_contenidos.remove(contenido_3)
    contenido_4 = choice(lista_de_contenidos)
    lista_de_contenidos.remove(contenido_4)
    contenido_5 = choice(lista_de_contenidos)
    lista_de_contenidos.remove(contenido_5)



enunciado_oculto = [x,y]










