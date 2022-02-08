salto_automatico = False

procedimiento = r"""Los números complejos pueden ubicarse en un plano complejo (equivalente al plano cartesiano). Para ello se debe transformar el número complejo en un par ordenado, donde le la coordenada X es la parte real y la coordenada Y es la parte imaginaria.\\
Ejemplo: Ubica en un plano complejo en número complejo $-4-3i$.\\
Desarrollo: Primero se transforma el número complejo a par ordenado\\
\begin{center}
$-4-3i\Longrightarrow \left(-4,\ -3\right)$
\end{center}
Luego se ubica el par ordenado en un plano complejo.\\\\
Respuesta:
\begin{center}
\begin{tikzpicture}[scale=0.5]
\draw [step=1, thin, gray!50]  (-5,-5) grid (5,5);
\draw 
(1,0) node [anchor=north, font=\small] {$1$}
(-1,0) node [anchor=north, font=\small] {$-1$}
(0,1) node [anchor=east, font=\small] {$\mathrm{i}$}
(0,-1) node [anchor=east, font=\small] {$-\mathrm{i}$};
\foreach \i in {2,...,5}
\draw
(\i,0) node [anchor=north, font=\small] {$\i$}
(-\i,0) node [anchor=north, font=\small] {$-\i$}
(0,\i) node [anchor=east, font=\small] {$\i \mathrm{i}$}
(0,-\i) node [anchor=east, font=\small] {$-\i \mathrm{i}$};
\draw [<->] (-6,0) -- (6,0) node[right] {$\mathrm{Re}$};
\draw [<->] (0,-6) -- (0,6) node[above] {$\mathrm{Im}$};
\tkzDefPoint(-4,-3){Z}
\tkzDrawPoints[color=black,shape=circle,fill=black,size=10](Z)
\end{tikzpicture}
\end{center}"""
