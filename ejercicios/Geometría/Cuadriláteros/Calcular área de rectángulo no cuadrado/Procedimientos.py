salto_automatico = False

procedimiento = r"""El área de los rectángulos se calcula con la siguiente fórmula
\begin{center}
$\mathrm{A=bh}$
\end{center}
Donde b es la medida de la base y h es la medida de la altura.\\
Es importante recordar que los lados opuestos de los rectángulos miden lo mismo.\\
Ejemplo:\\
Sea el rectángulo ABCD que se muestra a continuación
\begin{center}
\begin{tikzpicture}
\tkzDefPoint(0,0){A}
\tkzDefPoint(3,0){B}
\tkzDefPoint(3,2){C}
\tkzDefPoint(0,2){D}
\tkzDrawPolygon(A,B,C,D)
\node [label=225:A] at (A) {};
\node [label=315:B] at (B) {};
\node [label=45:C] at (C) {};
\node [label=135:D] at (D) {};
\tkzLabelSegment[below](A,B){$8 \mathrm{m}$}
\tkzLabelSegment[left](D,A){$4 \mathrm{m}$}
\end{tikzpicture}
\end{center}
Calcula el área de ABCD.\\
Desarrollo:
\begin{center}
$\mathrm{A=bh=8\cdot 4=32}$
\end{center}
Respuesta: El área de ABCD es $32 \mathrm{m}$"""
