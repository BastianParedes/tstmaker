{"cantidad_opciones":1, "cantidad_disponible":1}

if opcion==1:
    #================================Aquí va el enunciado================================================================
    enunciado = r"""Se pueden determinar las coordenadas del extremo de un vector dado $\overrightarrow{\mathrm{u}}$, que tiene la misma dirección y origen que $\overrightarrow{\mathrm{v}}$ de la figura adjunta, si se sabe que:
\begin{center} \begin{tikzpicture} [scale=0.5]
\draw [-angle 45] (-2,0) -- (7,0) node[below] {x};
\draw [-angle 45] (0,-2) -- (0,5) node[left] {y};

\draw [dashed] (0,3) -- (5,3) -- (5,0);

\draw [-angle 45, line width=1pt] (0,0) -- (5,3);

\node at ($(0,3)+(180:0.3)$) {3};
\node at ($(5,0)+(-90:0.32)$) {5};

\node at ($(2.5,1.5)+(135:0.5)$) {$\overrightarrow{\mathrm{v}}$};
\end{tikzpicture} \end{center}"""
    #================================Aquí están los contenidos de las informaciones. También la alternativa correcta=====
    informacion_1 = r"$\overrightarrow{\mathrm{u}}$ y $\overrightarrow{\mathrm{v}}$ tienen el mismo sentido."
    informacion_2 = r"El módulo de $\overrightarrow{\mathrm{u}}$ es igual al doble del módulo de $\overrightarrow{\mathrm{v}}$."
    alternativa_correcta = "C"













