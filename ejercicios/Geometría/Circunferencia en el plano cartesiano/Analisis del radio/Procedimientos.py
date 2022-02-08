salto_automatico = False

procedimiento = fr"""Si la ecuación de la circunferencia es de la forma general, se debe transformar a su forma principal para obtener el radio. Luego se tienen tres opciones:
\hfill \break
\begin{{itemize}}
\item
Si el cuadrado del radio es positivo (mayor a cero), entonces la circunferencia es graficable.
\item
Si el cuadrado del radio es igual a cero, entonces la circunferencia es graficable, pero es un punto el cual es el centro.
\item
Si el cuadrado del radio es negativo (menor que cero), entonces la circunferencia no es graficable.
\end{{itemize}}
Ejemplo:
Sea una circunferencia cuya ecuación general es
\begin{{center}}
{Matematica(pol(potencia("x",2), potencia("y",2), -racional(14)*"x", racional(6)*"y", -63) + "=0")}
\end{{center}}
Se determina su ecuación principal
\begin{{center}}
{Matematica(pol(potencia("x-7",2) , potencia("y+3",2))+"=-5")}
\end{{center}}
El cuadrado del radio es igual a $-5$, es decir negativo, por lo que la circunferencia no es graficable."""
