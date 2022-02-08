{"cantidad_opciones":1, "cantidad_disponible":50}

def graficar_Circunferencia(h,k,r):
    return fr"""\begin{{tabular}}{{l}} 
\begin{{tikzpicture}} [scale=0.3]
\draw [step=1, thin, gray!50] (-5,-5) grid (5,5);
\draw [<->] (-6,0) -- (6,0) node[above] {{X}};
\draw [<->] (0,-6) -- (0,6) node[right] {{Y}};
\foreach \i in {{1,...,5}} \draw
    (\i , 0) node [anchor=north, font=\scriptsize] {{$\i$}}
    (-\i , 0) node [anchor=north, font=\scriptsize] {{$-\i$}}
    (0 , \i) node [anchor=east, font=\scriptsize] {{$\i$}}
    (0 , -\i) node [anchor=east, font=\scriptsize] {{$-\i$}};
\draw ({h},{k}) circle({r});
\end{{tikzpicture}}
\end{{tabular}}"""




#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
r = Racional(randrange(1, 5))
h, k, = choice([-1,1])*Racional(randrange(0, (5-r).numerador)), choice([-1,1])*Racional(randrange(0, (5-r).numerador))

#================================Aquí va el enunciado================================================================
enunciado = f"Dibuja un esbozo de la circunferencia C cuya ecuación general es {Matematica(Pol({'x':2}, {'y':2}, -2*h*'x', -2*k*'y', h**2+k**2-r**2)+'=0')}."

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = graficar_Circunferencia(h,k,r)


enunciado_oculto = [h, k, r]
espacio_para_el_desarrollo = 8











