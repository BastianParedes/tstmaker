{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b = randrange(-5, 5), randrange(-5, 5)
while a==0 or b==0:
    a, b = randrange(-5, 5), randrange(-5, 5)

if -b/a<0:
    inicio = round((a*b-5.5*a)/b, 1)
    if round((a*b-5.5*a)/b, 1)<-5.5:
        inicio = -5.5

    fin = round((5.5*a+a*b)/b, 1)
    if round((5.5*a+a*b)/b, 1)>5.5:
        fin = 5.5

else:
    inicio = round((5.5*a+a*b)/b, 1)
    if round((5.5*a+a*b)/b, 1)<-5.5:
        inicio = -5.5

    fin = round((a*b-5.5*a)/b, 1)
    if round((a*b-5.5*a)/b, 1)>5.5:
        fin = 5.5

#================================Aquí va el enunciado================================================================
enunciado = fr"""Observa la recta L graficada en el siguiente plano cartesiano
\begin{{center}}
\begin{{tikzpicture}} [scale=0.5]

\draw [step=1, thin, gray!50]  ({{-5}},{{-5}}) grid ({{5}},{{5}});

\draw
    ({a}, 0) node [anchor=north, font=\footnotesize] {{${a}$}}
    (0, {b}) node [anchor=east, font=\footnotesize] {{${b}$}};

\draw [<->] (-6,0) -- (6,0) node[right] {{X}};
\draw [<->] (0,-6) -- (0,6) node[above] {{Y}};

\draw [domain={inicio}:{fin}, <->] plot (\x ,{{ {-b}*\x/{a}+{b}}}) node[right] {{f}};

\end{{tikzpicture}}
\end{{center}}
La función que mejor describe a la recta L es"""


#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
a, b = Racional(a), Racional(b)

contenido_correcto = Matematica(Recta(Par(a,0),Par(0,b)).show_funcion)
contenido_2 = Matematica("f(x)="+Pol(b/a*"x",b))
contenido_3 = Matematica("f(x)="+Pol(-a/b*"x", a**2/b))
contenido_4 = Matematica("f(x)="+Pol(a*"x",b))
contenido_5 = Matematica("f(x)="+Pol(b*"x",a))

enunciado_oculto = [a, b]










