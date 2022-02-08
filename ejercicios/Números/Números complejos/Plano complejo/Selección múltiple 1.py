{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
z = Complex(choice(list(range(-5, 0))+list(range(1, 6))), choice(list(range(-5, 0))+list(range(1, 6))))
while z.re==z.im==0:
    z = Complex(choice(list(range(-5, 0))+list(range(1, 6))), choice(list(range(-5, 0))+list(range(1, 6))))

#================================Aquí va el enunciado================================================================
enunciado = r"""Considera i como la unidad imaginaria. A continuación se presenta un plano complejo, en el cual está representado un número complejo mediante un punto.
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
"""
enunciado += fr"\tkzDefPoint({z.re},{z.im})"+r"""{Z}
\tkzDrawPoints[color=black,shape=circle,fill=black,size=10](Z)
\end{tikzpicture}
\end{center}
El número complejo representado es"""

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.=
contenido_correcto = Matematica(Complex(z.re, z.im))
contenido_2 = Matematica(Complex(z.im, z.re))
contenido_3 = Matematica(Complex(-z.re, -z.im))
contenido_4 = Matematica(Complex(-z.im, -z.re))
contenido_5 = Matematica(Complex(z.re+z.im, 0))

enunciado_oculto = z










