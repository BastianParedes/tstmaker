salto_automatico = False

procedimiento = r"""El perímetro de los rectángulos se calcula con la siguiente fórmula
\begin{center}
$\mathrm{A=2b+2h}$
\end{center}
Donde b es la medida de la base y h es la medida de la altura.\\
Otra forma de calcular el perímetro de los rectángulos consiste de sumar las medidas de los cuatro lados.\\
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
Calcula el perímetro de ABCD.\\
Desarrollo:
\begin{center}
$\mathrm{P=2b+2h=2\cdot 8+2\cdot 4=24}$
\end{center}
Respuesta: El perímetro de ABCD es $24 \mathrm{m}$"""
