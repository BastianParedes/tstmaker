{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
r = Racional(randrange(1, 7))
h, k, = choice([-1,1])*Racional(randrange(0, (7-r).numerador)), choice([-1,1])*Racional(randrange(0, (7-r).numerador))



#================================Aquí va el enunciado================================================================
enunciado = fr"""Observa la siguiente circunferencia
\begin{{center}}
\begin{{tikzpicture}} [scale=0.5]

\draw [step=1, thin, gray!50] (-6,-6) grid (6,6);

\draw [<->] (-7,0) -- (7,0) node[above] {{X}};
\draw [<->] (0,-7) -- (0,7) node[right] {{Y}};

\foreach \i in {{1,...,6}}
    \draw
        (\i , 0) node [anchor=north, font=\footnotesize] {{$\i$}}
        (-\i , 0) node [anchor=north, font=\footnotesize] {{$-\i$}}
        (0 , \i) node [anchor=east, font=\footnotesize] {{$\i$}}
        (0 , -\i) node [anchor=east, font=\footnotesize] {{$-\i$}};

\draw ({h},{k}) circle({r});
\end{{tikzpicture}}
\end{{center}}

¿Cuál de las siguientes circunferencias describe mejor a la circunferencia graficada?"""

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(Pol({"x":2}, {"y":2}, -2*h*"x", -2*k*"y", h**2+k**2-r**2)+"=0")

if h==k==0:
    contenido_2 = Matematica(Pol({"x":2}, {"y":2}, -2*h*"x", -2*k*"y", h**2+k**2-r)+"=0")
    contenido_3 = Matematica(Pol({"x":2}, {"y":2}, -2*h*"x", -2*k*"y", h**2+k**2-2*r)+"=0")
    contenido_4 = Matematica(Pol({"x":2}, {"y":2}, -2*h*"x", -2*k*"y", h**2+k**2-(2*r)**2)+"=0")
    contenido_5 = Matematica(Pol({"x":2}, {"y":2}, -2*h*"x", -2*k*"y", h**2+k**2-2*r**2)+"=0")

elif (h==0 or k==0) and r==1:
    contenido_2 = Matematica(Pol({"x":2}, {"y":2}, 2*h*"x", 2*k*"y", h**2+k**2-r**2)+"=0")
    contenido_3 = Matematica(Pol({"x":2}, {"y":2}, -2*h*"x", -2*k*"y", h**2+k**2-2*r)+"=0")
    contenido_4 = Matematica(Pol({"x":2}, {"y":2}, 2*h*"x", 2*k*"y", h**2+k**2-2*r)+"=0")
    contenido_5 = Matematica(Pol({"x":2}, {"y":2}, -2*h*"x", -2*k*"y", h**2+k**2+r)+"=0")

elif r==1:
    contenido_2 = Matematica(Pol({"x":2}, {"y":2}, 2*h*"x", 2*k*"y", h**2+k**2-r**2)+"=0")
    contenido_3 = Matematica(Pol({"x":2}, {"y":2}, -2*h*"x", -2*k*"y", h**2+k**2-2*r)+"=0")
    contenido_4 = Matematica(Pol({"x":2}, {"y":2}, 2*h*"x", 2*k*"y", h**2+k**2-2*r)+"=0")
    contenido_5 = Matematica(Pol({"x":2}, {"y":2}, -h*"x", -k*"y", h**2+k**2-r**2)+"=0")

else:
    contenido_2 = Matematica(Pol({"x":2}, {"y":2}, 2*h*"x", 2*k*"y", h**2+k**2-r**2)+"=0")
    contenido_3 = Matematica(Pol({"x":2}, {"y":2}, -2*h*"x", -2*k*"y", h**2+k**2-r)+"=0")
    contenido_4 = Matematica(Pol({"x":2}, {"y":2}, 2*h*"x", 2*k*"y", h**2+k**2-r)+"=0")
    contenido_5 = Matematica(Pol({"x":2}, {"y":2}, -2*h*"x", -2*k*"y", h**2+k**2-2*r**2)+"=0")


enunciado_oculto = [h, k, r]










