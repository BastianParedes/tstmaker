{"cantidad_opciones":1, "cantidad_disponible":50}

def plano_con_punto(x,y):
    return fr"""\begin{{tabular}}{{l}} \begin{{tikzpicture}} [scale=0.3]
\draw [step=1, thin, gray!50] (-4,-4) grid (4,4);
\draw [<->] (-5,0) -- (5,0) node[right] {{X}};
\draw [<->] (0,-5) -- (0,5) node[right] {{Y}};
\foreach \i in {{1,...,4}}
    \draw
        (\i , 0) node [anchor=north, font=\scriptsize] {{$\i$}}
        (0 , \i) node [anchor=east, font=\scriptsize] {{$\i$}}
        (-\i , 0) node [anchor=north, font=\scriptsize] {{$-\i$}}
        (0 , -\i) node [anchor=east, font=\scriptsize] {{$-\i$}};
\tkzDefPoint({x},{y}){{P}} \tkzDrawPoints(P) \end{{tikzpicture}} \end{{tabular}}"""

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
x, y = Racional(randrange(-4,5)), Racional(randrange(-4,5))
while x==y==0:
    x, y = Racional(randrange(-4,5)), Racional(randrange(-4,5))

#================================Aquí va el enunciado================================================================
enunciado = fr"""De los siguientes planos cartesianos, ¿Cuál es el que mejor representa al punto {Par(x,y)}?"""

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = plano_con_punto(x,y)

if abs(x)==abs(y):
    contenido_2 = plano_con_punto(-x,-y)
    contenido_3 = plano_con_punto(-x,y)
    contenido_4 = plano_con_punto(x,-y)
    contenido_5 = choice([plano_con_punto(x,0), plano_con_punto(0,y)])

elif x==0 or y==0:
    contenido_2 = plano_con_punto(-x,-y)
    contenido_3 = plano_con_punto(y,x)
    contenido_4 = plano_con_punto(-y,-x)
    contenido_5 = plano_con_punto(x+y,x+y)

else:
    lista_de_contenidos = [plano_con_punto(-x,-y), plano_con_punto(-x,y), plano_con_punto(x,-y), plano_con_punto(y,x), plano_con_punto(-y,-x), plano_con_punto(-y,x), plano_con_punto(y,-x)]
    contenido_2 = choice(lista_de_contenidos)
    lista_de_contenidos.remove(contenido_2)
    contenido_3 = choice(lista_de_contenidos)
    lista_de_contenidos.remove(contenido_3)
    contenido_4 = choice(lista_de_contenidos)
    lista_de_contenidos.remove(contenido_4)
    contenido_5 = choice(lista_de_contenidos)
    lista_de_contenidos.remove(contenido_5)


enunciado_oculto = Par(x,y)










