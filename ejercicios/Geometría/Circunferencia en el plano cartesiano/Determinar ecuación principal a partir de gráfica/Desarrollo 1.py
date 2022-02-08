{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
r = Racional(randrange(1, 7))
h, k, = choice([-1,1])*Racional(randrange(0, (7-r).numerador)), choice([-1,1])*Racional(randrange(0, (7-r).numerador))



#================================Aquí va el enunciado================================================================
enunciado = fr"""Observa la siguiente circunferencia
\begin{{center}}
\begin{{tikzpicture}} [scale=0.5]

\draw [step=1, thin, gray!50] (-6,-6) grid (6,6);

\draw [<->] (-7,0) -- (7,0) node[above] {{X}};
\draw [<->] (0,-7) -- (0,7) node[right] {{Y}};

\foreach \i in {{1,...,6}}
    \draw
        (\i , 0) node [anchor=north, font=\footnotesize] {{$\i$}}
        (-\i , 0) node [anchor=north, font=\footnotesize] {{$-\i$}}
        (0 , \i) node [anchor=east, font=\footnotesize] {{$\i$}}
        (0 , -\i) node [anchor=east, font=\footnotesize] {{$-\i$}};

\draw ({h},{k}) circle({r});
\end{{tikzpicture}}
\end{{center}}

Calcula la ecuación principal de la circunferencia mostrada."""

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(potencia(Pol("x",-h),2)+"+"+potencia(Pol("y",-k),2)+"="+r**2)



enunciado_oculto = [h, k, r]
espacio_para_el_desarrollo = 3











