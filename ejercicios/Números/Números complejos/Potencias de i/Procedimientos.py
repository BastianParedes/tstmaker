salto_automatico = False

procedimiento = r"""Para resolver potencias la unidad imaginaria $i$ es necesario conocer los cuatro siguientes resultados
\begin{itemize}
	\item $i^0=1$
	\item $i^1=i$
	\item $i^2=-1$
	\item $i^3=-i$
\end{itemize}
También es necesario comprender la siguiente propiedad:\\
Sea la potencia $i^n$, y sea r el resto al realizar la división $n:4$. Se cumple que $i^n=i^r$.\\
\hfill \break
Ejemplo 1: Calcula $i^{93}$\\
Desarrollo: Se calcula el resto de la división $93:4$, el cual es $1$, por lo que
\begin{center}
$i^{93}=i^1=i$
\end{center}
\hfill \break
Ejemplo 2: Calcula $i^{127}$\\
Desarrollo: Se calcula el resto de la división $127:4$, el cual es $3$, por lo que
\begin{center}
$i^{127}=i^3=-i$
\end{center}
\hfill \break
Este propiedad solo funciona cuando el exponente es positivo."""
