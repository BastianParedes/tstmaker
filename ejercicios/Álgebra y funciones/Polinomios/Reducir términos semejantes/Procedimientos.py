salto_automatico = False

procedimiento = r"""La reducción de términos se realiza sumando y restando las partes numéricas de los términos semejantes (los términos semejantes son aquellos que tienen la misma parte literal)\\
Ejemplo:
\begin{center}
$\mathrm{-9x+8x-10x+6{x}^{2}-6-6{x}^{2}-10}$
\end{center}
El primer término $\mathrm{-9x}$ es semejante al segundo término $\mathrm{8x}$ y al tercer término $\mathrm{-10x}$. Para reducir los tres términos hay que sumar (o restar) las partes numéricas, pero mantener la parte literal.
\begin{center}
$\mathrm{-9x+8x-10x=-11x}$
\end{center}
Por lo tanto
\begin{center}
$\mathrm{-9x+8x-10x+6{x}^{2}-6-6{x}^{2}-10=-11x+6{x}^{2}-6-6{x}^{2}-10}$
\end{center}
En este nuevo polinomio el primer término $\mathrm{-11x}$ no es semejante a otro, por lo que no puede reducirse más.\\
El término $\mathrm{6{x}^{2}}$ es semejante al término $\mathrm{-6{x}^{2}}$ por lo que deben sumarse (o restarse)
\begin{center}
$\mathrm{6{x}^{2}-6{x}^{2}=0{x}^{2}}$
\end{center}
En este caso se tiene que la parte numérica resulta 0. Se debe recordar que 0 al multiplicar cualquier cosa, el resultado siempre es 0, por tanto
\begin{center}
$\mathrm{6{x}^{2}-6{x}^{2}=0{x}^{2}=0}$
\end{center}
Luego el polinomio del ejercicio queda
\begin{center}
$\mathrm{-11x+6{x}^{2}-6-6{x}^{2}-10=-11x+0-6-10}$
\end{center}
En este nuevo polinomio se tiene que el término $0$ es semejante al término $6$ y al término $10$ ya que ninguno de ellos tiene parte literal. Tan solo hay que sumarlos (o restarlos)
\begin{center}
$0-6-10=-16$
\end{center}
Por lo tanto el polinomio queda
\begin{center}
$\mathrm{-11x+0-6-10=-11x-16}$
\end{center}
Finalmente se tiene que la respuesta es
\begin{center}
$\mathrm{-11x-16}$
\end{center}"""
