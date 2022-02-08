{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
x1, x2, y1, y2 = randrange(0,10), randrange(0,10), randrange(0,10), randrange(0,10)
while not x1<x2 or not y1<y2:
    x1, x2, y1, y2 = randrange(0,10), randrange(0,10), randrange(0,10), randrange(0,10)

base = x2-x1
altura = y2-y1
#================================Aquí va el enunciado================================================================
enunciado = fr"""¿Cuánto mide la superficie combreada?
\begin{{center}} \begin{{tikzpicture}} [scale=0.5]
\draw [step=1, thin, gray!50] (0,0) grid (9,9);
\filldraw[draw=black,fill=gray!100] plot coordinates{{({x1},{y1})({x1},{y2})({x2},{y2})({x2},{y1})({x1},{y1})}};
\end{{tikzpicture}} \end{{center}}"""

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(base*altura)+" unidades cuadradas"
contenido_2 = Matematica(Racional(base*altura,2,True))+" unidades cuadradas"
contenido_3 = Matematica(base*altura*2)+" unidades cuadradas"
contenido_4 = Matematica(2*base+2*altura)+" unidades cuadradas"
contenido_5 = Matematica(base+altura)+" unidades cuadradas"



enunciado_oculto = enunciado











