salto_automatico = False

procedimiento = r"""El área de rectángulos puede obtenerse contando los cuadrados que tienen dentro.\\
Ejemplo: ¿Cuánto mide la superficie combreada?
\begin{center} \begin{tikzpicture} [scale=0.5]
\draw [step=1, thin, gray!50] (0,0) grid (9,9);
\filldraw[draw=black,fill=gray!100] plot coordinates{({3},{3})({3},{8})({6},{8})({6},{3})({3},{3})};
\end{tikzpicture} \end{center}
Mide 15 unidades cuadradas ya que hay 15 cuadrados sombreados"""