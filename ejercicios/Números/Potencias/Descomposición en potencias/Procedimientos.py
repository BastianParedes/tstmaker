salto_automatico = False

procedimiento = r"""Existen varios métodos, aquí solo se presenta uno.\\
Recuerda que los primeros números primos son 2, 3, 5, 7, 11 y 13.\\
Consideremos el número 588. Se empieza siempre con el menos número primo: 2\\
¿Es 2 un factor (divisor) de 588? sí, por lo que se divide 588 por 2, cuyo resultado es 294.
\begin{center}$588=2\cdot294$\end{center}
Luego el mismo procedimiento se realiza con 294.\\
¿Es 2 un factor (divisor) de 588? sí, por lo que se divide 294 por 2, cuyo resultado es 147.
\begin{center}$588=2\cdot2\cdot147$\end{center}
Luego el mismo procedimiento se realiza con 147.\\
¿Es 2 un factor (divisor) de 147? no, por lo que la misma pregunta se realiza, pero con el siguiente número primo: 3.\\
¿Es 3 un factor (divisor) de 174? sí, por lo que se divide 147 por 3, cuyo resultado es 49.
\begin{center}$588=2\cdot2\cdot3\cdot49$\end{center}
Luego el mismo procedimiento se realiza con 49.\\
¿Es 3 un factor (divisor) de 49? no, por lo que la misma pregunta se realiza, pero con el siguiente número primo: 5.\\
¿Es 5 un factor (divisor) de 49? no, por lo que la misma pregunta se realiza, pero con el siguiente número primo: 7.\\
¿Es 7 un factor (divisor) de 49? sí, por lo que se divide 49 por 7, cuyo resultado es 7.
\begin{center}$588=2\cdot2\cdot3\cdot7\cdot7$\end{center}
Todos los números que hay en el lado derecho son números primos, por lo que se termina el procedimiento.\\
Ahora hay que generar las potencias.\\
¿Cuántas veces está escrito el número 2? 2 veces, por lo que el número 2 se escribe una vez, pero elevado a 2.
\begin{center}$588={2}^{2}\cdot3\cdot7\cdot7$\end{center}
¿Cuántas veces está escrito el número 3? 1 vez, por lo que el número 3 se escribe una vez, pero elevado a 1.
\begin{center}$588={2}^{2}\cdot{3}^{1}\cdot7\cdot7$\end{center}
El 1 se borra ya que en potencias si el exponente es 1, puede borrarse.
\begin{center}$588={2}^{2}\cdot3\cdot7\cdot7$\end{center}
¿Cuántas veces está escrito el número 7? 2 veces, por lo que el número 7 se escribe una vez, pero elevado a 2.
\begin{center}$588={2}^{2}\cdot3\cdot{7}^{2}$\end{center}"""
