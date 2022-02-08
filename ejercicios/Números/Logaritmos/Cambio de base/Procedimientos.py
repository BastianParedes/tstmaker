salto_automatico = False

procedimiento = r"""Los logaritmos pueden cambiar su base por otra cualquiera, pero para ello se debe generar una fracción donde tanto el numerador como el denominador sean logaritmos. Esto se realiza mediante la ecuación
$\log_{b}a=\dfrac{\log_{x}a}{\log_{x}b}$\\
Recordatorio: La nueva base x puede ser cualquiera.\\\\
Ejemplo 1: Cambia la base del logaritmo $\log_{3}7$.\\
Desarrollo: Dado que no se especifica la nueva base para el logaritmo, puede escogerse cualquiera. En este ejemplo se elegirá más de una base.
\begin{center}
$\log_{3}7=\dfrac{\log_{2}7}{\log_{2}3}=\dfrac{\log_{5}7}{\log_{5}3}=\dfrac{\log_{12}7}{\log_{12}3}=\dfrac{\log_{}7}{\log_{}3}$
\end{center}
\hfill \break
Ejemplo 2: Determina la veracidad de la afirmación $\log_{8}9=\dfrac{\log_{2}9}{3}$.\\
Desarrollo: Cuando se tienen logaritmos de distinta base es recomendable utilizar la propiedad explicada anteriormente para igualar las bases. En este caso se aplicará dicha propiedad sobre $\log_{8}9$ para que tenga base 2, ya que esta es la base del otro logaritmo.
\begin{center}
$\log_{8}9=\dfrac{\log_{2}9}{\log_{2}8}$
\end{center}
Luego se observa que $\log_{2}8$ es igual a $3$, por lo que
\begin{center}
$\dfrac{\log_{2}9}{\log_{2}8}=\dfrac{\log_{2}9}{3}$
\end{center}
Luego juntanto todas las expresiones se obtiene la cadena
\begin{center}
$\log_{8}9=\dfrac{\log_{2}9}{\log_{2}8}=\dfrac{\log_{2}9}{3}$
\end{center}
\hfill \break
Respuesta: Es verdadero que $\log_{8}9=\dfrac{\log_{2}9}{3}$"""
