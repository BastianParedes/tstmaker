salto_automatico = False

procedimiento = fr"""Se mantiene la base de las potencias, pero al exponente del numerador se le resta el exponente del denominador. A continuación se muestran dos ejemplos\\
\begin{{center}}
{Matematica(fraccion(potencia(9,4), potencia(9,15))+"="+potencia(9,"9-15")+"="+potencia(9,-6))}
{Matematica(fraccion(potencia("x",7), potencia("x",-2))+"="+potencia("x","7-(-2)")+"="+potencia("x",9))}
\end{{center}}"""


