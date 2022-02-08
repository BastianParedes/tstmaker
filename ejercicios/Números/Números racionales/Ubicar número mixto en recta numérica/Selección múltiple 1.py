{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
f = Racional(randrange(3, 100), randrange(2, 10))
while f<=1 or f==2 or f==3 or f==4 or f==5 or 6<=f:
    f = Racional(randrange(3, 100), randrange(2, 10))
lista_de_letras = ["V", "W", "X", "Y", "Z"]

#================================Aquí va el enunciado================================================================
enunciado = r"""Observa la siguiente recta numérica
\begin{center} \begin{tikzpicture} [scale=0.5]
\draw [->] (0,0) -- (13,0) node[right] {{}};
\foreach \i in {0,...,6}
    \draw
        (2*\i , 5pt) -- +(0, -10pt)  node [anchor=north, font=\footnotesize] {$\i$};
\draw (3 , -5pt) -- +(0, 10pt)  node [anchor=south, font=\footnotesize] {V};
\draw (5 , -5pt) -- +(0, 10pt)  node [anchor=south, font=\footnotesize] {W};
\draw (7 , -5pt) -- +(0, 10pt)  node [anchor=south, font=\footnotesize] {X};
\draw (9 , -5pt) -- +(0, 10pt)  node [anchor=south, font=\footnotesize] {Y};
\draw (11 , -5pt) -- +(0, 10pt)  node [anchor=south, font=\footnotesize] {Z};
\end{tikzpicture} \end{center}
¿Cuál de las siguientes letras representa mejor la posición del número """+Matematica(f.show_mixto)+"?"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
if 1<f<2:
    contenido_correcto = "V"
elif 2<f<3:
    contenido_correcto = "W"
elif 3<f<4:
    contenido_correcto = "X"
elif 4<f<5:
    contenido_correcto = "Y"
elif 5<f<6:
    contenido_correcto = "Z"

lista_de_letras.remove(contenido_correcto)

contenido_2 = choice(lista_de_letras)
lista_de_letras.remove(contenido_2)
contenido_3 = choice(lista_de_letras)
lista_de_letras.remove(contenido_3)
contenido_4 = choice(lista_de_letras)
lista_de_letras.remove(contenido_4)
contenido_5 = choice(lista_de_letras)
lista_de_letras.remove(contenido_5)



enunciado_oculto = f











