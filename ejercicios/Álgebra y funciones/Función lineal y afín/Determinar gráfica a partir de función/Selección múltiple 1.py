{"cantidad_opciones":1, "cantidad_disponible":50}

def par_ordenado(m,n):
    if -5 < m*(-5)+n < 5:
        primer_par = [-5, float(Racional(m*(-5)+n))]
    else:
        if -5 <= (-5-n)/m <= 5:
            y = -5
        else:
            y = 5
        primer_par = [float((y-n)/m) , y]

    if -5 < m*(5)+n < 5:
        segundo_par = [5, float(Racional(m*(5)+n))]
    else:
        if -5<= (5-n)/m <=5:
            y = 5
        else:
            y = -5
        segundo_par = [float((y-n)/m) , y]

    return [primer_par, segundo_par]


#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
while True:
    m = Racional(elegir(-10,10,0) ,elegir(-10,10,0))
    if 0.3<=abs(m)<0.7 or 1.3<abs(m):
        break
n = randrange(-5,6)

letra = choice(["f", "g", "h"])

#================================Aquí va el enunciado================================================================
enunciado = "Sea la función "+Matematica(letra+"(x)="+Pol(m*"x",n)) +f". La alternativa que mejor representa la gráfica de {letra} es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = r"""\begin{tabular}{l}
\begin{tikzpicture} [scale=0.15]
\draw [<->] (-5,0) -- (5,0) node[right] {X};
\draw [<->] (0,-5) -- (0,5) node[above] {Y};
"""
pares = par_ordenado(m,n)
contenido_correcto += fr"""\draw [<->] ({pares[0][0]}, {pares[0][1]}) -- ({pares[1][0]}, {pares[1][1]});
\end{{tikzpicture}} \end{{tabular}}"""


contenido_2 = r"""\begin{tabular}{l}
\begin{tikzpicture} [scale=0.15]
\draw [<->] (-5,0) -- (5,0) node[right] {X};
\draw [<->] (0,-5) -- (0,5) node[above] {Y};
"""
pares = par_ordenado(-m,n)
contenido_2 += fr"""\draw [<->] ({pares[0][0]}, {pares[0][1]}) -- ({pares[1][0]}, {pares[1][1]});
\end{{tikzpicture}} \end{{tabular}}"""#m está negativo


contenido_3 = r"""\begin{tabular}{l}
\begin{tikzpicture} [scale=0.15]
\draw [<->] (-5,0) -- (5,0) node[right] {X};
\draw [<->] (0,-5) -- (0,5) node[above] {Y};
"""
pares = par_ordenado(m,-n)
contenido_3 += fr"""\draw [<->] ({pares[0][0]}, {pares[0][1]}) -- ({pares[1][0]}, {pares[1][1]});
\end{{tikzpicture}} \end{{tabular}}"""#n está negativo


contenido_4 = r"""\begin{tabular}{l}
\begin{tikzpicture} [scale=0.15]
\draw [<->] (-5,0) -- (5,0) node[right] {X};
\draw [<->] (0,-5) -- (0,5) node[above] {Y};
"""
pares = par_ordenado(-m,-n)
contenido_4 += fr"""\draw [<->] ({pares[0][0]}, {pares[0][1]}) -- ({pares[1][0]}, {pares[1][1]});
\end{{tikzpicture}} \end{{tabular}}"""#m y n están negativos


contenido_5 = r"""\begin{tabular}{l}
\begin{tikzpicture} [scale=0.15]
\draw [<->] (-5,0) -- (5,0) node[right] {X};
\draw [<->] (0,-5) -- (0,5) node[above] {Y};
"""
pares = par_ordenado(1/m,n)
contenido_5 += fr"""\draw [<->] ({pares[0][0]}, {pares[0][1]}) -- ({pares[1][0]}, {pares[1][1]});
\end{{tikzpicture}} \end{{tabular}}"""# se usa el recíproco de m





enunciado_oculto = [m,n]













