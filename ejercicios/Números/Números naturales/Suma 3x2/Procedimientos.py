salto_automatico = False

procedimiento = r"""Cómo sumar números de dos o más dígitos (por ejemplo $4229+733$)\\
Ubica un número arriba del otro de tal manera que las unidades estén alineadas. Traza una línea debajo del número inferior.
\begin{align*}
4229\\
\underline{+\hspace{7pt}733}
\end{align*}
\hfill \break
Suma primero los dígitos correspondientes a las unidades ($9+3=12$). Este número es más grande que 10, entonces escribe un 1 arriba de la columna correspondiente a las decenas y escribe el 2 debajo de la línea en la columna correspondiente a las unidades.
\begin{align*}
1\hspace{4.9pt}\\
4229\\
\underline{+\hspace{7pt}733}\\
2
\end{align*}
\hfill \break
Suma los dígitos correspondientes a las decenas ($1+2+3=6$) y ubica el resultado debajo de la línea en la columna correspondiente a las decenas.
\begin{align*}
1\hspace{4.9pt}\\
4229\\
\underline{+\hspace{7pt}733}\\
62
\end{align*}
\hfill \break
Suma los números correspondientes a la columna de las centenas ($2+7=9$) y ubica el resultado debajo de la línea en la columna correspondiente a las centenas.
\begin{align*}
1\hspace{4.9pt}\\
4229\\
\underline{+\hspace{7pt}733}\\
962
\end{align*}
\hfill \break
Suma los números correspondientes a la columna de las unidades de mil, en este caso solo hay un número ($4$).
\begin{align*}
1\hspace{4.9pt}\\
4229\\
\underline{+\hspace{7pt}733}\\
4962
\end{align*}
\hfill \break
Respuesta: $4229+733=4962$"""
