salto_automatico = False

procedimiento = r"""Para ubicar un punto en un plano cartesiano mediante sus coordenadas se debe considerar que el primer número es la coordenada X y el segundo es la coordenada Y. Desde el origen, es decir, el punto (0,0), se avanza a la derecha la cantidad de veces que indique la coordenada X, luego se sube la cantidad de veces que indique la coordenada Y.\\
Ejemplo: Ubica en un plano cartesiano el punto (5,3).\\
Desarrollo: Para lograrlo se debe ubicar el lapiz en el punto origen, luego se avanzan 5 espacios a la derecha y se suben 3.
\begin{center} \begin{tikzpicture}
\draw [step=1, thin, gray!50] (0,0) grid (9,9);
\draw [->] (0,0) -- (10,0) node[right] {X};
\draw [->] (0,0) -- (0,10) node[above] {Y};
\foreach \i in {1,...,9} \draw
(\i , 0) node [anchor=north, font=\scriptsize] {$\i$}
(0 , \i) node [anchor=east, font=\scriptsize] {$\i$};
\tkzDefPoint(5,3){P}
\tkzDrawPoints(P)
\end{tikzpicture} \end{center}"""
