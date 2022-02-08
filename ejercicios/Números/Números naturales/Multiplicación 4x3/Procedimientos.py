salto_automatico = False

procedimiento = r"""La multiplicación de números de dos o más dígitos se hace multiplicando sus dígitos. Es importante considerar las reservas y los espacios a dejar durante el proceso. El procedimiento se explicará con un ejemplo.\\
Ejemplo: Calcula $472\cdot 1930$.\\\\
Desarrollo: Primero es útil hacer que el número con menos dígitos esté a la derecha, por lo que el ejercicio queda\\
\begin{center}
$1930\cdot 472$
\end{center}
Se inicia multiplicando los dígitos del número de la izquierda con la unidad del número de la derecha. Se debe tener cuidado de escribir y sumar las reservas cuando corresponda.
\begin{align*}
193\fbox{0}&\cdot 47\fbox{2}\\
0&
\end{align*}

\begin{align*}
19\fbox{3}0&\cdot 47\fbox{2}\\
60&
\end{align*}

\begin{align*}
1\hspace{13pt}&\\
1\fbox{9}30&\cdot 47\fbox{2}\\
860&
\end{align*}

\begin{align*}
1\hspace{10pt}&\\
\fbox{1}930&\cdot 47\fbox{2}\\
3860&
\end{align*}
\hfill \break
Luego se debe dejar un espacio vacío (en este caso se puso una x) y se borran las reservas.
\begin{align*}
1930&\cdot 472\\
3860&\\
x
\end{align*}
\hfill \break
Luego se repite el proceso, pero con la decena del número de la derecha. Se debe tener cuidado de escribir y sumar las reservas cuando corresponda.
\begin{align*}
193\fbox{0}&\cdot 4\fbox{7}2\\
3860&\\
0x&
\end{align*}

\begin{align*}
2\hspace{16pt}&\\
19\fbox{3}0&\cdot 4\fbox{7}2\\
3860&\\
10x&
\end{align*}

\begin{align*}
6\hspace{3pt}2\hspace{13pt}&\\
1\fbox{9}30&\cdot 4\fbox{7}2\\
3860&\\
510x&
\end{align*}

\begin{align*}
6\hspace{3pt}2\hspace{10pt}&\\
\fbox{1}930&\cdot 4\fbox{7}2\\
3860&\\
13510x&
\end{align*}
\hfill \break
Luego se deben dejar dos espacios vacíos (en este caso se pusieron dos x) y se borran las reservas.
\begin{align*}
1930&\cdot 472\\
3860&\\
13510x&\\
xx&
\end{align*}
\hfill \break
Luego se repite el proceso, pero con la centena del número de la derecha. Se debe tener cuidado de escribir y sumar las reservas cuando corresponda.
\begin{align*}
193\fbox{0}&\cdot \fbox{4}72\\
3860&\\
13510x&\\
0xx&
\end{align*}

\begin{align*}
1\hspace{16pt}&\\
19\fbox{3}0&\cdot \fbox{4}72\\
3860&\\
13510x&\\
20xx&
\end{align*}

\begin{align*}
3\hspace{3pt}1\hspace{13pt}&\\
1\fbox{9}30&\cdot \fbox{4}72\\
3860&\\
13510x&\\
720xx&
\end{align*}

\begin{align*}
3\hspace{3pt}1\hspace{10pt}&\\
\fbox{1}930&\cdot \fbox{4}72\\
3860&\\
13510x&\\
7720xx&
\end{align*}
\hfill \break
Luego se consideran los tres resultados obtenidos.
\begin{align*}
3860\\
13510x\\
7720xx
\end{align*}
\hfill \break
Se reemplazan las x con ceros.
\begin{align*}
3860\\
135100\\
772000
\end{align*}
\hfill \break
Finalmente se suman los tres números.
\begin{align*}
3860\\
135100\\
\underline{+\ \ 772000}\\
910960
\end{align*}
\hfill \break
Respuesta: $472\cdot 1930=910960$"""
