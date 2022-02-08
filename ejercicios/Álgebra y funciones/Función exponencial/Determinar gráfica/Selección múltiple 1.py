{"cantidad_opciones":4, "cantidad_disponible":50}

def numero_por(numero):
    if numero==1:
        return ""
    elif numero==-1:
        return "-"
    else:
        return str(numero)+por()

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
letra = choice(["f", "g", "h"])

if opcion==1:
    a, b = Racional(randrange(1, 10)), Racional(randrange(2, 10))
elif opcion==2:
    a, b = Racional(randrange(1, 10)), Racional(1, choice([2,4,5,8,10]), True)
elif opcion==3:
    a, b = -Racional(randrange(1, 10)), Racional(randrange(2, 10))
elif opcion==4:
    a, b = -Racional(randrange(1, 10)), Racional(1, choice([2,4,5,8,10]), True)

#================================Aquí va el enunciado================================================================
enunciado = "La gráfica que mejor representa a la función "+Matematica(f"{letra}(x)="+numero_por(a)+potencia(b,"x", parentesis_automatico=False)) +" es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
graficos = [
    # a positivo, b mayor que 1
    fr"""\begin{{tabular}}{{l}}
    \begin{{tikzpicture}} [scale=0.15]
    \draw [<->] (-5,0) -- (5,0) node[right] {{X}};
    \draw [<->] (0,-5) -- (0,5) node[above] {{Y}};
    \draw [domain={-4.8}:{2.1}] plot (\x , 2^\x);
    \end{{tikzpicture}} \end{{tabular}}""",

    # a positivo, b menor que 1
    fr"""\begin{{tabular}}{{l}}
    \begin{{tikzpicture}} [scale=0.15]
    \draw [<->] (-5,0) -- (5,0) node[right] {{X}};
    \draw [<->] (0,-5) -- (0,5) node[above] {{Y}};
    \draw [domain={-2.1}:{4.8}] plot (\x , 0.5^\x);
    \end{{tikzpicture}} \end{{tabular}}""",

    # a negativo, b mayor que 1
    fr"""\begin{{tabular}}{{l}}
    \begin{{tikzpicture}} [scale=0.15]
    \draw [<->] (-5,0) -- (5,0) node[right] {{X}};
    \draw [<->] (0,-5) -- (0,5) node[above] {{Y}};
    \draw [domain={-4.8}:{2.1}] plot (\x , -2^\x);
    \end{{tikzpicture}} \end{{tabular}}""",

    # a negativo, b menor que 1
    fr"""\begin{{tabular}}{{l}}
    \begin{{tikzpicture}} [scale=0.15]
    \draw [<->] (-5,0) -- (5,0) node[right] {{X}};
    \draw [<->] (0,-5) -- (0,5) node[above] {{Y}};
    \draw [domain={-2.1}:{4.8}] plot (\x , -0.5^\x);
    \end{{tikzpicture}} \end{{tabular}}""",

    fr"""\begin{{tabular}}{{l}}
    \begin{{tikzpicture}} [scale=0.15]
    \draw [<->] (-5,0) -- (5,0) node[right] {{X}};
    \draw [<->] (0,-5) -- (0,5) node[above] {{Y}};
    \draw [domain={-4.8}:{2.1}] plot (2^\x , \x);
    \end{{tikzpicture}} \end{{tabular}}""",

    fr"""\begin{{tabular}}{{l}}
    \begin{{tikzpicture}} [scale=0.15]
    \draw [<->] (-5,0) -- (5,0) node[right] {{X}};
    \draw [<->] (0,-5) -- (0,5) node[above] {{Y}};
    \draw [domain={-2.1}:{4.8}] plot (0.5^\x , \x);
    \end{{tikzpicture}} \end{{tabular}}""",

    fr"""\begin{{tabular}}{{l}}
    \begin{{tikzpicture}} [scale=0.15]
    \draw [<->] (-5,0) -- (5,0) node[right] {{X}};
    \draw [<->] (0,-5) -- (0,5) node[above] {{Y}};
    \draw [domain={-4.8}:{2.1}] plot (-2^\x , \x);
    \end{{tikzpicture}} \end{{tabular}}""",

    fr"""\begin{{tabular}}{{l}}
    \begin{{tikzpicture}} [scale=0.15]
    \draw [<->] (-5,0) -- (5,0) node[right] {{X}};
    \draw [<->] (0,-5) -- (0,5) node[above] {{Y}};
    \draw [domain={-2.1}:{4.8}] plot (-0.5^\x , \x);
    \end{{tikzpicture}} \end{{tabular}}"""
]

if opcion==1:
    contenido_correcto = graficos[0]
elif opcion==2:
    contenido_correcto = graficos[1]
elif opcion==3:
    contenido_correcto = graficos[2]
elif opcion==4:
    contenido_correcto = graficos[3]


graficos.remove(contenido_correcto)
contenido_2 = choice(graficos)
graficos.remove(contenido_2)
contenido_3 = choice(graficos)
graficos.remove(contenido_3)
contenido_4 = choice(graficos)
graficos.remove(contenido_4)
contenido_5 = choice(graficos)
graficos.remove(contenido_5)



enunciado_oculto = [a,b]










