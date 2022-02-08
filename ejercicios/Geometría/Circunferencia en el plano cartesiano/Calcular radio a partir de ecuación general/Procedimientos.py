salto_automatico = False

procedimiento = fr"""Si la ecuación de la circunferencia es de la forma general, se debe transformar a su forma principal. Luego se calcula la raiz cuadrada del número despejado.
\begin{{center}}
{Matematica(pol(potencia("x",2), potencia("y",2), -racional(14)*"x", racional(6)*"y", 52) + "=0")}\\
{Matematica(pol(potencia("x-7",2) , potencia("y+3",2))+"=6")}\\
{Matematica(potencia("r",2)+"=6")}\\
{Matematica("r="+raiz(6))}
\end{{center}}
Se calcula la raiz si es exacta, en este ejemplo la raiz es inexacta."""
