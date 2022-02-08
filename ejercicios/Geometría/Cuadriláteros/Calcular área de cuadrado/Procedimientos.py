salto_automatico = False

procedimiento = r"""El área de los cuadrados se calcula con cualquiera de las siguientes dos fórmulas
\begin{center}
$\mathrm{A={L}^{2}}$\\
$\mathrm{A=L\cdot L}$
\end{center}
Donde L es la medida de cualquiera de los cuatro lados del cuadrado.\\
Es importante recordar que los cuatro lados de los cuadrados miden lo mismo.\\
Ejemplo:\\
Sea el cuadrado ABCD que se muestra a continuación
\begin{center}
\begin{tikzpicture}
\tkzDefPoint(0,0){A}
\tkzDefPoint(2,0){B}
\tkzDefPoint(2,2){C}
\tkzDefPoint(0,2){D}
\tkzDrawPolygon(A,B,C,D)
\node [label=225:A] at (A) {};
\node [label=315:B] at (B) {};
\node [label=45:C] at (C) {};
\node [label=135:D] at (D) {};
\tkzLabelSegment[below](A,B){$5 \mathrm{m}$}
\end{tikzpicture}
\end{center}
Calcula el área de ABCD.\\
Desarrollo:
\begin{center}
$\mathrm{A}={\mathrm{L}}^{2}={5}^{2}=5\cdot 5=25$
\end{center}
Respuesta: El área de ABCD es $25 {\mathrm{m}}^{2}$"""
