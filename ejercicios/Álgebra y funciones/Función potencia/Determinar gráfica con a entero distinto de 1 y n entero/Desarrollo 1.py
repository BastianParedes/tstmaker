{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a = elegir(-5,6,0,1)
n = elegir(-10,10,0)
graficos = [
    # a positivo, n negativo par
    fr"""\begin{{tabular}}{{l}}
    \begin{{tikzpicture}} [scale=0.15]
    \draw [<->] (-5,0) -- (5,0) node[right] {{X}};
    \draw [<->] (0,-5) -- (0,5) node[above] {{Y}};
    \draw [domain={-5}:{-0.5}] plot (\x , {{1/(\x*\x)}});
    \draw [domain={0.5}:{5}] plot (\x , {{1/(\x*\x)}});
    \end{{tikzpicture}} \end{{tabular}}""",

    # a positivo, n negativo impar
    fr"""\begin{{tabular}}{{l}}
    \begin{{tikzpicture}} [scale=0.15]
    \draw [<->] (-5,0) -- (5,0) node[right] {{X}};
    \draw [<->] (0,-5) -- (0,5) node[above] {{Y}};
    \draw [domain=-5:-0.2] plot (\x , {{1/(\x)}});
    \draw [domain=0.2:5] plot (\x , {{1/(\x)}});
    \end{{tikzpicture}} \end{{tabular}}""",

    # a positivo, n=1
    fr"""\begin{{tabular}}{{l}}
    \begin{{tikzpicture}} [scale=0.15]
    \draw [<->] (-5,0) -- (5,0) node[right] {{X}};
    \draw [<->] (0,-5) -- (0,5) node[above] {{Y}};
    \draw [domain=-4.9:4.9] plot (\x , {{\x}});
    \end{{tikzpicture}} \end{{tabular}}""",

    # a positivo, n positivo par
    fr"""\begin{{tabular}}{{l}}
    \begin{{tikzpicture}} [scale=0.15]
    \draw [<->] (-5,0) -- (5,0) node[right] {{X}};
    \draw [<->] (0,-5) -- (0,5) node[above] {{Y}};
    \draw [domain=-2.2:2.2] plot (\x , {{\x*\x}});
    \end{{tikzpicture}} \end{{tabular}}""",

    # a positivo, n positivo impar
    fr"""\begin{{tabular}}{{l}}
    \begin{{tikzpicture}} [scale=0.15]
    \draw [<->] (-5,0) -- (5,0) node[right] {{X}};
    \draw [<->] (0,-5) -- (0,5) node[above] {{Y}};
    \draw [domain=-1.7:1.7] plot (\x , {{\x*\x*\x}});
    \end{{tikzpicture}} \end{{tabular}}""",

    # a negativo, n negativo par
    fr"""\begin{{tabular}}{{l}}
    \begin{{tikzpicture}} [scale=0.15]
    \draw [<->] (-5,0) -- (5,0) node[right] {{X}};
    \draw [<->] (0,-5) -- (0,5) node[above] {{Y}};
    \draw [domain={-5}:{-0.5}] plot (\x , {{-1/(\x*\x)}});
    \draw [domain={0.5}:{5}] plot (\x , {{-1/(\x*\x)}});
    \end{{tikzpicture}} \end{{tabular}}""",

    # a negativo, n negativo impar
    fr"""\begin{{tabular}}{{l}}
    \begin{{tikzpicture}} [scale=0.15]
    \draw [<->] (-5,0) -- (5,0) node[right] {{X}};
    \draw [<->] (0,-5) -- (0,5) node[above] {{Y}};
    \draw [domain=-5:-0.2] plot (\x , {{-1/(\x)}});
    \draw [domain=0.2:5] plot (\x , {{-1/(\x)}});
    \end{{tikzpicture}} \end{{tabular}}""",

    # a negativo, n=1
    fr"""\begin{{tabular}}{{l}}
    \begin{{tikzpicture}} [scale=0.15]
    \draw [<->] (-5,0) -- (5,0) node[right] {{X}};
    \draw [<->] (0,-5) -- (0,5) node[above] {{Y}};
    \draw [domain=-4.9:4.9] plot (\x , {{-\x}});
    \end{{tikzpicture}} \end{{tabular}}""",

    # a negativo, n positivo par
    fr"""\begin{{tabular}}{{l}}
    \begin{{tikzpicture}} [scale=0.15]
    \draw [<->] (-5,0) -- (5,0) node[right] {{X}};
    \draw [<->] (0,-5) -- (0,5) node[above] {{Y}};
    \draw [domain=-2.2:2.2] plot (\x , {{-\x*\x}});
    \end{{tikzpicture}} \end{{tabular}}""",

    # a negativo, n positivo impar
    fr"""\begin{{tabular}}{{l}}
    \begin{{tikzpicture}} [scale=0.15]
    \draw [<->] (-5,0) -- (5,0) node[right] {{X}};
    \draw [<->] (0,-5) -- (0,5) node[above] {{Y}};
    \draw [domain=-1.7:1.7] plot (\x , {{-\x*\x*\x}});
    \end{{tikzpicture}} \end{{tabular}}"""
]

#================================Aquí va el enunciado================================================================
enunciado = "Dibuja un esbozo de la gráfica de la función "+Matematica("f(x)="+Racional(a)*potencia("x",n)) +"."

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
if 0<a and n<0 and n%2==0:
    contenido_correcto = graficos[0]
elif 0<a and n<0 and n%2==1 and n!=1:
    contenido_correcto = graficos[1]
elif 0<a and n==1:
    contenido_correcto = graficos[2]
elif 0<a and 0<n and n%2==0:
    contenido_correcto = graficos[3]
elif 0<a and 0<n and n%2==1:
    contenido_correcto = graficos[4]
elif a<0 and n<0 and n%2==0:
    contenido_correcto = graficos[5]
elif a<0 and n<0 and n%2==1 and n!=1:
    contenido_correcto = graficos[6]
elif a<0 and n==1:
    contenido_correcto = graficos[7]
elif a<0 and 0<n and n%2==0:
    contenido_correcto = graficos[8]
elif a<0 and 0<n and n%2==1:
    contenido_correcto = graficos[9]



enunciado_oculto = [a,n]










