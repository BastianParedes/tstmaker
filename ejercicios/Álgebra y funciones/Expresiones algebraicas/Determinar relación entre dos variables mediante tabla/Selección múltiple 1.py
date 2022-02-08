{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b = Racional(randrange(1, 10)), Racional(randrange(-10, 10))
x1 = Racional(randrange(1,6))
x2, x3, x4 = x1+1, x1+2, x1+3
while a*x1+b<0:
    a, b = Racional(randrange(1, 10)), Racional(randrange(-10, 10))
    x1 = Racional(randrange(1,6))
    x2, x3, x4 = x1+1, x1+2, x1+3

pares_de_letras = choice([["a","b","y"], ["m","n","y"], ["p","q","y"], ["r","s","y"], ["x","y","e"]])
primera_letra = pares_de_letras[0]
segunda_letra = pares_de_letras[1]
conector = pares_de_letras[2]

#================================Aquí va el enunciado================================================================
enunciado = fr"""Observa la siguiente tabla
\begin{{center}} \begin{{tabular}}{{|c|c|}}
\hline
{primera_letra} & {segunda_letra} \\ \hline
{Matematica(x1)} & {Matematica(a*x1+b)} \\ \hline
{Matematica(x2)} & {Matematica(a*x2+b)} \\ \hline
{Matematica(x3)} & {Matematica(a*x3+b)} \\ \hline
{Matematica(x4)} & {Matematica(a*x4+b)} \\ \hline
\end{{tabular}} \end{{center}}
¿Qué expresión algebraica representa las relación entre {primera_letra} {conector} {segunda_letra}?"""

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(segunda_letra+"="+Pol(a*primera_letra, b))
contenido_2 =        Matematica(segunda_letra+"="+Pol(Racional(randrange(1,10))*primera_letra, randrange(-10,10)))
contenido_3 =        Matematica(segunda_letra+"="+Pol(Racional(randrange(1,10))*primera_letra, randrange(-10,10)))
contenido_4 =        Matematica(segunda_letra+"="+Pol(Racional(randrange(1,10))*primera_letra, randrange(-10,10)))
contenido_5 =        Matematica(segunda_letra+"="+Pol(Racional(randrange(1,10))*primera_letra, randrange(-10,10)))



enunciado_oculto = [a,b]











