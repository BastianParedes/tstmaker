salto_automatico = False

procedimiento = fr"""Si la ecuación de la circunferencia es de la forma general, se debe transformar a su forma principal. Luego se observan los números que están sumando/restando a las variables X e Y. Las coordenadas del centro serán los negativos de dichos números
\begin{{center}}
{Matematica(pol(potencia("x",2), potencia("y",2), -racional(14)*"x", racional(6)*"y", 52) + "=0")}\\
{Matematica(pol(potencia("x-7",2) , potencia("y+3",2))+"=6")}
\end{{center}}
Las coordenadas del centro son {Matematica(par(7,-3))}"""
