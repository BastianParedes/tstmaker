salto_automatico = False

procedimiento = r"""Todos los triángulos tienen tres ángulos y siempre se cumple que al sumarlos el resultado es 180. Esto escrito en una ecuación queda
\begin{center}
$\alpha+\beta+\gamma=180$
\end{center}
Donde $\alpha$, $\beta$ y $\gamma$ son los tres ángulos del triángulo.\\\\
Ejemplo: En el siguiente triángulo el ángulo BAC mide $\alpha$, el ángulo CBA mide ${58}^{\degree}$ y el ángulo ACB mide ${68}^{\degree}$.
\begin{center}
\begin{tikzpicture}[scale=2]
\tkzDefPoint(61:1){A}
\tkzDefPoint(241:1){B}
\tkzDefTriangle[two angles= 54 and 58](A,B) \tkzGetPoint{C}
\tkzDrawPolygon(A,B,C)
\node [label=91:A] at (A){};
\node [label=241:B] at (B){};
\node [label=331:C] at (C){};
    \draw pic["$\alpha$",draw,angle radius=1cm] {angle=B--A--C};
    \draw pic["${58}^{\degree}$",draw,angle radius=1cm] {angle=C--B--A};
    \draw pic["${68}^{\degree}$",draw,angle radius=1cm] {angle=A--C--B};
\end{tikzpicture} \end{center}
¿Cuál es el valor de $\alpha$?\\\\
Desarrollo:\\
Se conocen dos de los tres ángulos del triángulo y se sabe que al sumarlos el resultado es 180, por lo que se puede escribir
\begin{center}
$\alpha+58+68=180$
\end{center}
Luego sumando 58 y 68 la ecuación queda
\begin{center}
$\alpha+126=180$
\end{center}
\hfill \break
Ahora solo hay que responder ¿Qué ángulo sumado a 126 resulta 180?\\
Hay varias formas de responder esta pregunta, pero una de ellas consiste en realizar la resta $180-122$ que es igual a $54$.\\\\
Respuesta: El valor de $\alpha$ es igual 54°."""
