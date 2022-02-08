{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, n = Racional(elegir(-5,6,0)), Racional(elegir(-3,4,0))
x1, x2, x3 = Racional(elegir(-3,4,0)), Racional(elegir(-3,4,0)), Racional(elegir(-3,4,0))
while not x1<x2<x3:
    x1, x2, x3 = Racional(elegir(-3,4,0)), Racional(elegir(-3,4,0)), Racional(elegir(-3,4,0))
letra = choice(["f", "g", "h"])

#================================Aquí va el enunciado================================================================
enunciado = fr"""A continuación se presenta una tabla con datos de una función potencia
\begin{{center}}
\begin{{tabular}}{{|c|c|}}
\hline
{Matematica("x")}&{Matematica(letra+"(x)")}\\
\hline
{Matematica(x1)}&{Matematica(a*x1**n)}\\
\hline
{Matematica(x2)}&{Matematica(a*x2**n)}\\
\hline
{Matematica(x3)}&{Matematica(a*x3**n)}\\
\hline
\end{{tabular}}
\end{{center}}"""

if (a*x1**n).denominador!=1 or (a*x2**n).denominador!=1 or (a*x3**n).denominador!=1:
    enunciado = r"""{
\extrarowheight = -0.5ex
\renewcommand{\arraystretch}{2.5}
""" + enunciado +"""
}"""

enunciado += f"Determina la función {letra}."

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(letra+"(x)="+Term(a, {"x":int(n)}))




enunciado_oculto = [a,n,x1,x2,x3]










