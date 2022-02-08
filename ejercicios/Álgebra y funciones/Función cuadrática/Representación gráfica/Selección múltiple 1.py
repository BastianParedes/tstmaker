{"cantidad_opciones":1, "cantidad_disponible":50}

def extra(_a, _h, _k):
    mas = Racional(0)
    while -5<_a*(mas**2)+_k<5:
        mas = mas + 0.2
    return mas

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a = Racional(choice(list(range(-2, 0))+list(range(1, 3))))
h = Racional(choice(list(range(-3, 0))+list(range(1, 3))))
k = Racional(choice(list(range(-3, 0))+list(range(1, 3))))

#================================Aquí va el enunciado================================================================
enunciado = "La gráfica que mejor representa a la función "+Matematica("f(x)="+Pol(Term(a,{"x":2}),-2*a*h*"x",a*h**2+k))+" es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = fr"""\begin{{tabular}}{{l}}
\begin{{tikzpicture}} [scale=0.15]
\draw [<->] (-5,0) -- (5,0) node[right] {{X}};
\draw [<->] (0,-5) -- (0,5) node[above] {{Y}};
\draw [domain={Racional(h-extra(a, h, k),1,True).show.replace(",",".")}:{Racional(h+extra(a, h, k),1,True).show.replace(",",".")}] plot (\x ,"""+"{"+a+"*("+Pol(r"\x",-h)+")"+"*("+Pol(r"\x",-h)+")"+k.signo+abs(k)+r"""});
\end{tikzpicture} \end{tabular}
"""
lista_de_contenidos = [
fr"""\begin{{tabular}}{{l}}
\begin{{tikzpicture}} [scale=0.15]
\draw [<->] (-5,0) -- (5,0) node[right] {{X}};
\draw [<->] (0,-5) -- (0,5) node[above] {{Y}};
\draw [domain={Racional(-h-extra(a, -h, -k),1,True).show.replace(",",".")}:{Racional(-h+extra(a, -h, -k),1,True).show.replace(",",".")}] plot (\x ,"""+"{"+a+"*("+Pol(r"\x",h)+")"+"*("+Pol(r"\x",h)+")"+(-k).signo+abs(k)+r"""});
\end{tikzpicture} \end{tabular}
""",
fr"""\begin{{tabular}}{{l}}
\begin{{tikzpicture}} [scale=0.15]
\draw [<->] (-5,0) -- (5,0) node[right] {{X}};
\draw [<->] (0,-5) -- (0,5) node[above] {{Y}};
\draw [domain={Racional(h-extra(-a, h, -k),1,True).show.replace(",",".")}:{Racional(h+extra(a, h, k),1,True).show.replace(",",".")}] plot (\x ,"""+"{"+(-a)+"*("+Pol(r"\x",-h)+")"+"*("+Pol(r"\x",-h)+")"+(-k).signo+abs(k)+r"""});
\end{tikzpicture} \end{tabular}
""",
fr"""\begin{{tabular}}{{l}}
\begin{{tikzpicture}} [scale=0.15]
\draw [<->] (-5,0) -- (5,0) node[right] {{X}};
\draw [<->] (0,-5) -- (0,5) node[above] {{Y}};
\draw [domain={Racional(h-extra(-a, -h, -k),-1,True).show.replace(",",".")}:{Racional(h+extra(a, h, k),-1,True).show.replace(",",".")}] plot (\x ,"""+"{"+(-a)+"*("+Pol(r"\x",h)+")"+"*("+Pol(r"\x",h)+")"+(-k).signo+abs(k)+r"""});
\end{tikzpicture} \end{tabular}
""",
fr"""\begin{{tabular}}{{l}}
\begin{{tikzpicture}} [scale=0.15]
\draw [<->] (-5,0) -- (5,0) node[right] {{X}};
\draw [<->] (0,-5) -- (0,5) node[above] {{Y}};
\draw [domain={Racional(h-extra(-a, h, k),1,True).show.replace(",",".")}:{Racional(h+extra(-a, h, k),1,True).show.replace(",",".")}] plot (\x ,"""+"{"+(-a)+"*("+Pol(r"\x",-h)+")"+"*("+Pol(r"\x",-h)+")"+k.signo+abs(k)+r"""});
\end{tikzpicture} \end{tabular}
""",
fr"""\begin{{tabular}}{{l}}
\begin{{tikzpicture}} [scale=0.15]
\draw [<->] (-5,0) -- (5,0) node[right] {{X}};
\draw [<->] (0,-5) -- (0,5) node[above] {{Y}};
\draw [domain={Racional(-h-extra(a, -h, k),1,True).show.replace(",",".")}:{Racional(-h+extra(a, -h, k),1,True).show.replace(",",".")}] plot (\x ,"""+"{"+a+"*("+Pol(r"\x",h)+")"+"*("+Pol(r"\x",h)+")"+k.signo+abs(k)+r"""});
\end{tikzpicture} \end{tabular}
""",
fr"""\begin{{tabular}}{{l}}
\begin{{tikzpicture}} [scale=0.15]
\draw [<->] (-5,0) -- (5,0) node[right] {{X}};
\draw [<->] (0,-5) -- (0,5) node[above] {{Y}};
\draw [domain={Racional(h-extra(a, h, -k),1,True).show.replace(",",".")}:{Racional(h+extra(a, h, -k),1,True).show.replace(",",".")}] plot (\x ,"""+"{"+a+"*("+Pol(r"\x",-h)+")"+"*("+Pol(r"\x",-h)+")"+(-k).signo+abs(-k)+r"""});
\end{tikzpicture} \end{tabular}
""",
fr"""\begin{{tabular}}{{l}}
\begin{{tikzpicture}} [scale=0.15]
\draw [<->] (-5,0) -- (5,0) node[right] {{X}};
\draw [<->] (0,-5) -- (0,5) node[above] {{Y}};
\draw [domain={Racional(-h-extra(-a, -h, k),1,True).show.replace(",",".")}:{Racional(-h+extra(-a, -h, k),1,True).show.replace(",",".")}] plot (\x ,"""+"{"+(-a)+"*("+Pol(r"\x",h)+")"+"*("+Pol(r"\x",h)+")"+k.signo+abs(k)+r"""});
\end{tikzpicture} \end{tabular}
"""
]
contenido_2 = choice(lista_de_contenidos)
lista_de_contenidos.remove(contenido_2)
contenido_3 = choice(lista_de_contenidos)
lista_de_contenidos.remove(contenido_3)
contenido_4 = choice(lista_de_contenidos)
lista_de_contenidos.remove(contenido_4)
contenido_5 = choice(lista_de_contenidos)
lista_de_contenidos.remove(contenido_5)

enunciado_oculto = [a, h, k]










