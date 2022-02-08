{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
n = elegir(-27,28,0)

#================================Aquí va el enunciado================================================================
enunciado = "Dibuja un esbozo es la gráfica de la función "+Matematica("f(x)="+potencia("x",n)) +"."

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
if n<0 and n%2==0:
    contenido_correcto = fr"""\begin{{tabular}}{{l}}
    \begin{{tikzpicture}} [scale=0.15]
    \draw [<->] (-5,0) -- (5,0) node[right] {{X}};
    \draw [<->] (0,-5) -- (0,5) node[above] {{Y}};
    \draw [domain={-5}:{-0.5}] plot (\x , {{1/(\x*\x)}});
    \draw [domain={0.5}:{5}] plot (\x , {{1/(\x*\x)}});
    \end{{tikzpicture}} \end{{tabular}}"""



elif n<0 and n%2==1 and n!=1:
    contenido_correcto = fr"""\begin{{tabular}}{{l}}
    \begin{{tikzpicture}} [scale=0.15]
    \draw [<->] (-5,0) -- (5,0) node[right] {{X}};
    \draw [<->] (0,-5) -- (0,5) node[above] {{Y}};
    \draw [domain=-5:-0.2] plot (\x , {{1/(\x)}});
    \draw [domain=0.2:5] plot (\x , {{1/(\x)}});
    \end{{tikzpicture}} \end{{tabular}}"""


elif n==1:
    contenido_correcto = fr"""\begin{{tabular}}{{l}}
    \begin{{tikzpicture}} [scale=0.15]
    \draw [<->] (-5,0) -- (5,0) node[right] {{X}};
    \draw [<->] (0,-5) -- (0,5) node[above] {{Y}};
    \draw [domain=-4.9:4.9] plot (\x , {{\x}});
    \end{{tikzpicture}} \end{{tabular}}"""



elif 0<n and n%2==0:
    contenido_correcto = fr"""\begin{{tabular}}{{l}}
    \begin{{tikzpicture}} [scale=0.15]
    \draw [<->] (-5,0) -- (5,0) node[right] {{X}};
    \draw [<->] (0,-5) -- (0,5) node[above] {{Y}};
    \draw [domain=-2.2:2.2] plot (\x , {{\x*\x}});
    \end{{tikzpicture}} \end{{tabular}}"""


elif 0<n and n%2==1:
    contenido_correcto = fr"""\begin{{tabular}}{{l}}
    \begin{{tikzpicture}} [scale=0.15]
    \draw [<->] (-5,0) -- (5,0) node[right] {{X}};
    \draw [<->] (0,-5) -- (0,5) node[above] {{Y}};
    \draw [domain=-1.7:1.7] plot (\x , {{\x*\x*\x}});
    \end{{tikzpicture}} \end{{tabular}}"""




enunciado_oculto = n










