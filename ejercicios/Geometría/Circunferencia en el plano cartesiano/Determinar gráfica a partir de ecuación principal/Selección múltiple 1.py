{"cantidad_opciones":1, "cantidad_disponible":50}

def graficar_Circunferencia(h,k,r):
    return fr"""\begin{{tabular}}{{l}} 
\begin{{tikzpicture}} [scale=0.3]
\draw [step=1, thin, gray!50] (-5,-5) grid (5,5);
\draw [<->] (-6,0) -- (6,0) node[above] {{X}};
\draw [<->] (0,-6) -- (0,6) node[right] {{Y}};
\foreach \i in {{1,...,5}} \draw
    (\i , 0) node [anchor=north, font=\scriptsize] {{$\i$}}
    (-\i , 0) node [anchor=north, font=\scriptsize] {{$-\i$}}
    (0 , \i) node [anchor=east, font=\scriptsize] {{$\i$}}
    (0 , -\i) node [anchor=east, font=\scriptsize] {{$-\i$}};
\draw ({h},{k}) circle({r});
\end{{tikzpicture}}
\end{{tabular}}"""




#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
r = Racional(randrange(1, 5))
h, k, = choice([-1,1])*Racional(randrange(0, (5-r).numerador)), choice([-1,1])*Racional(randrange(0, (5-r).numerador))



#================================Aquí va el enunciado================================================================
enunciado = f"¿Cuál de las siguientes gráficas representa mejor a la circunferencia C cuya ecuación principal es {Matematica(potencia(Pol('x',-h),2)+'+'+potencia(Pol('y',-k),2)+'='+r**2)}?"


#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = graficar_Circunferencia(h,k,r)

if h==k==0:
    contenido_2 = graficar_Circunferencia(1,1,r)
    contenido_3 = graficar_Circunferencia(-1,1,r)
    contenido_4 = graficar_Circunferencia(1,-1,r)
    contenido_5 = graficar_Circunferencia(-1,-1,r)

elif (h==0 or k==0) and r==1:
    contenido_2 = graficar_Circunferencia(-h,-k,r)
    contenido_3 = graficar_Circunferencia(k,h,r)
    contenido_4 = graficar_Circunferencia(-k,-h,r)
    contenido_5 = graficar_Circunferencia(0,0,r)

elif r==1:
    contenido_2 = graficar_Circunferencia(-h,-k,r)
    contenido_3 = graficar_Circunferencia(-h,k,r)
    contenido_4 = graficar_Circunferencia(h,-k,r)
    contenido_5 = graficar_Circunferencia(0,0,r)

else:
    contenido_2 = graficar_Circunferencia(-h,-k,r)
    contenido_3 = graficar_Circunferencia(-h,k,r)
    contenido_4 = graficar_Circunferencia(h,-k,r)
    contenido_5 = graficar_Circunferencia(0,0,r)


enunciado_oculto = [h, k, r]










