salto_automatico = False

procedimiento = r"""Los triángulos rectángulos son aquellos que tienen un ángulo recto, es decir, un ángulo de 90°. Los dos lados que forman al ángulo recto se llaman "catetos" y el lado restante se llama "hipotenusa".\\
El teorema de Pitágoras solo puede aplicarse sobre triángulos rectángulos. Dicho teorema establece que
\begin{center}
$\mathrm{{\left(primer\ cateto\right)}^{2}+{\left(segundo\ cateto\right)}^{2}={\left(hipotenusa\right)}^{2}}$
\end{center}
Este teorema tiene múltiples usos, pero el más importante consiste en calcular la medida de un lado del triángulo si se conocen las medidas de los otros dos.\\\\
Ejemplo:\\
En el siguiente triángulo rectángulo se tiene que el lado BC mide $5\ km$ y el lado AC mide $\sqrt{34}\ km$
\begin{center}
\begin{tikzpicture}

\tkzDefPoint(95:1){C}
\tkzDefPoint(275:3){B}
\tkzDefTriangle[two angles= 30 and 90](C,B) \tkzGetPoint{A}

\tkzDrawPoints(A,B,C)

\node [label=-25:A] at (A) {};
\node [label=230:B] at (B) {};
\node [label=110:C] at (C) {};

\tkzDefMidPoint(A,B) \tkzGetPoint{AB}
\tkzDefMidPoint(A,C) \tkzGetPoint{AC}
\tkzDefMidPoint(B,C) \tkzGetPoint{BC}

\tkzDrawPolygon(A,B,C)
\tkzMarkRightAngle(A,B,C)

\node [label=185:$\mathrm{3}$ km] at (BC) {};
\node [label=50:$\mathrm{\sqrt{\mathrm{34}}}$ km] at (AC) {};
\end{tikzpicture} \end{center}
¿Cuánto mide el lado AB?\\\\
Desarrollo:
La hipotenusa del triángulo dibujado es el lado AC. Los lados AB y BC son los catetos. No se conoce la medida del lado AB, por lo que se le asigna una letra por mientras, en este ejemplo se le asignará la letra x. Utilizando el teorema de Pitágoras se puede obtener la ecuación
\begin{center}
$\mathrm{{primer\ cateto}^{2}+{segundo\ cateto}^{2}={hipotenusa}^{2}}$\\
$\mathrm{{x}^{2}+{3}^{2}={\sqrt{34}}^{2}}$\\
\end{center}
Al resolver las potencias, la ecuación queda
\begin{center}
$\mathrm{{x}^{2}+9=34}$
\end{center}
Luego se despeja x
\begin{center}
$\mathrm{{x}^{2}+9-9=34-9}$\\
$\mathrm{{x}^{2}+0=25}$\\
$\mathrm{{x}^{2}=25}$\\
$\mathrm{sqrt{{x}^{2}}=sqrt{25}}$\\
$\mathrm{x=5}$
\end{center}
\hfill \break
Respuesta: El lado AB mide $\mathrm{5\ km}$."""
