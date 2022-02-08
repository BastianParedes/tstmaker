{"cantidad_opciones":1, "cantidad_disponible":50}

def inicio(m, n):
    L_provicional = Recta(Par(0,n),pendiente=m)
    numero = Racional(0)
    while abs(L_provicional.f(numero))<4.5:
        numero = numero - 0.1
        if numero<=-4.5:
            break
    return round(numero,1)

def fin(m, n):
    L_provicional = Recta(Par(0,n),pendiente=m)
    numero = Racional(0)
    while abs(L_provicional.f(numero))<4.5:
        numero = numero + 0.1
        if 4.5<=numero:
            break
    return round(numero,1)

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
m = Racional(choice(list(range(-5, 0))+list(range(1, 6))), randrange(1, 11))
n = Racional(choice(list(range(-7, -2))+list(range(2, 8))), 2)

#================================Aquí va el enunciado================================================================
enunciado = "Dibuja un esbozo de la gráfica de la función "+Matematica("f(x)="+Pol(m*"x",n))+"."

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = fr"""\begin{{tabular}}{{l}}
\begin{{tikzpicture}} [scale=0.15]
\draw [<->] (-5,0) -- (5,0) node[right] {{X}};
\draw [<->] (0,-5) -- (0,5) node[above] {{Y}};
\draw [<->, domain={inicio(m,n)}:{fin(m,n)}] plot (\x ,"""+"{"+Pol(str(round(m,1))+r"*\x", round(n))+r"""}) node[right] {{f}};
\end{tikzpicture} \end{tabular}"""



enunciado_oculto = [m, n]
espacio_para_el_desarrollo = 10











