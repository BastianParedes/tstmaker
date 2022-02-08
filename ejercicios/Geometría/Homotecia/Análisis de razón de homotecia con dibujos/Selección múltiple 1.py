{"cantidad_opciones":1, "cantidad_disponible":50}

def dibujo(k):
    A, B, C = Par(randrange(6,8),randrange(2,4)), Par(randrange(8,10),randrange(-1,2)), Par(randrange(6,8),randrange(-3,-1))
    while (A.y-B.y)*(B.x-C.x)==(B.y-C.y)*(A.x-B.x):
        A, B, C = Par(randrange(6,8),randrange(2,4)), Par(randrange(8,10),randrange(-1,2)), Par(randrange(6,8),randrange(-3,-1))
    angulo_de_giro = choice(list(range(-10,10))+list(range(170,190)))
    if abs(k)==2:
        resultado = fr"\begin{{tikzpicture}} [scale=0.2, rotate={angulo_de_giro}]"
    elif abs(k)==0.5:
        resultado = fr"\begin{{tikzpicture}} [scale=0.4, rotate={angulo_de_giro}]"
    elif abs(k)==1:
        resultado = fr"\begin{{tikzpicture}} [scale=0.2, rotate={angulo_de_giro}]"
    resultado += "\n"+fr"""
\coordinate [label={choice([90,270])}:O] (O) at (0,0);
\coordinate [label={90+angulo_de_giro}:A] (A) at {A};
\coordinate [label={0+angulo_de_giro}:B] (B) at {B};
\coordinate [label={270+angulo_de_giro}:C] (C) at {C};

\tkzDrawPolygon(A,B,C)
"""
    if k<0:
        resultado += fr"""
\coordinate [label={270+angulo_de_giro}:A',font=\footnotesize] (A') at ($(O)!{k}!(A)$);
\coordinate [label={180+angulo_de_giro}:B',font=\footnotesize] (B') at ($(O)!{k}!(B)$);
\coordinate [label={90+angulo_de_giro}:C',font=\footnotesize] (C') at ($(O)!{k}!(C)$);
\tkzDrawSegment[dashed](A,A')
\tkzDrawSegment[dashed](B,B')
\tkzDrawSegment[dashed](C,C')"""
    elif k==0.5:
        resultado += fr"""
\coordinate [label={90+angulo_de_giro}:A',font=\footnotesize] (A') at ($(O)!{k}!(A)$);
\coordinate [label={angulo_de_giro}:B',font=\footnotesize] (B') at ($(O)!{k}!(B)$);
\coordinate [label={270+angulo_de_giro}:C',font=\footnotesize] (C') at ($(O)!{k}!(C)$);
\tkzDrawSegment[dashed](O,A)
\tkzDrawSegment[dashed](O,B)
\tkzDrawSegment[dashed](O,C)"""
    elif k==2:
        resultado += fr"""
\coordinate [label={90+angulo_de_giro}:A',font=\footnotesize] (A') at ($(O)!{k}!(A)$);
\coordinate [label={angulo_de_giro}:B',font=\footnotesize] (B') at ($(O)!{k}!(B)$);
\coordinate [label={270+angulo_de_giro}:C',font=\footnotesize] (C') at ($(O)!{k}!(C)$);
\tkzDrawSegment[dashed](O,A')
\tkzDrawSegment[dashed](O,B')
\tkzDrawSegment[dashed](O,C')"""

    return resultado + "\n"+r"""\tkzDrawPolygon(A',B',C')
\tkzDrawPoints[fill=black](O,A,B,C,A',B',C')
\end{tikzpicture}"""

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
k_dibujo = choice([-2,-1,-0.5,0.5,2])
if k_dibujo==-2:
    k_enunciado=Racional(-randrange(4,15), choice([1,2,3]), True)
elif k_dibujo==-1:
    k_enunciado=Racional(-1)
elif k_dibujo==-0.5:
    k_enunciado=Racional(-1,2,True)
elif k_dibujo==0.5:
    k_enunciado=Racional(1,2,True)
elif k_dibujo==2:
    k_enunciado=Racional(randrange(4,15), choice([1,2,3]), True)



lista_de_dibujos = [dibujo(-2), dibujo(-1), dibujo(-0.5), dibujo(0.5), dibujo(2)]
diccinario_k_dibujo = {-2:lista_de_dibujos[0], -1:lista_de_dibujos[1], -0.5:lista_de_dibujos[2], 0.5:lista_de_dibujos[3], 2:lista_de_dibujos[4]}
#================================Aquí va el enunciado================================================================
enunciado = f"Al triángulo ABC se le aplica una homotecia con centro O y razón {Matematica(k_enunciado)} obteniendo el triángulo A\'B\'C\'. De las siguientes figuras, la que representa mejor la situación planteada es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = diccinario_k_dibujo[k_dibujo]
lista_de_dibujos.remove(contenido_correcto)

contenido_2 = choice(lista_de_dibujos)
lista_de_dibujos.remove(contenido_2)
contenido_3 = choice(lista_de_dibujos)
lista_de_dibujos.remove(contenido_3)
contenido_4 = choice(lista_de_dibujos)
lista_de_dibujos.remove(contenido_4)
contenido_5 = choice(lista_de_dibujos)
lista_de_dibujos.remove(contenido_5)

contenido_correcto = r"\begin{tabular}{l}"+contenido_correcto+r"\end{tabular}"
contenido_2 = r"\begin{tabular}{l}"+contenido_2+r"\end{tabular}"
contenido_3 = r"\begin{tabular}{l}"+contenido_3+r"\end{tabular}"
contenido_4 = r"\begin{tabular}{l}"+contenido_4+r"\end{tabular}"
contenido_5 = r"\begin{tabular}{l}"+contenido_5+r"\end{tabular}"



enunciado_oculto = k_enunciado











