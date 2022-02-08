{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a = choice([-1, 1])
h = randrange(-7, 8)
k = choice([-a*1, -a*4, -a*9])

#================================Aquí va el enunciado================================================================
enunciado = r"""Considera la siguiente parábola
\begin{center}
\begin{tikzpicture}[scale=0.5]
"""
if a==1:

    enunciado += fr"""\draw [step=1, thin, gray!50]  ({-5+h},{k-1}) grid ({5+h},{k+11});
    """

    if h<-5:
        enunciado += fr"""\foreach \i in {{{str(h-5)+",...,"+str(h+5)}}}
        \draw
        (\i , 0) node [anchor=north, font=\footnotesize] {{$\i$}};
        """

    elif h==-5:
        enunciado += fr"""\foreach \i in {{{str(h-5)+",...,"+str(h+4)}}}
        \draw
        (\i , 0) node [anchor=north, font=\footnotesize] {{$\i$}};
        """

    elif -5<h<5:
        enunciado += fr"""\foreach \i in {{{"1,...,"+str(5+h)}}}
        \draw
        (\i , 0) node [anchor=north, font=\small]{{$\i$}};

        \foreach \i in {{{"1,...,"+str(5-h)}}}
        \draw
        (-\i , 0) node [anchor=north, font=\small] {{$-\i$}};
        """

    elif h==5:
        enunciado += fr"""\foreach \i in {{{str(h-4)+",...,"+str(h+5)}}}
        \draw
        (\i , 0) node [anchor=north, font=\small] {{$\i$}};
        """

    elif 5<h:
        enunciado += fr"""\foreach \i in {{{str(h-5)+",...,"+str(h+5)}}}
        \draw
        (\i , 0) node [anchor=north, font=\small] {{$\i$}};
        """

    enunciado += fr"""\draw [<->] ({-6+h},0) -- ({6+h},0) node[right] {{$\mathrm{{X}}$}};
    """

    if h<-5:
        enunciado += fr"""\foreach \i in {{{"1,...,"+str(11+k)}}}
        \draw
        ({str(h+5)} , \i ) node [anchor=east, font=\small] {{$\i$}};

        \foreach \i in {{{"1,...,"+str(abs(k-1))}}}
        \draw
        ({str(h+5)} , -\i ) node [anchor=east, font=\small] {{$-\i$}};
        """

    if -5<=h<=5:
        enunciado += fr"""\foreach \i in {{{"1,...,"+str(11+k)}}}
        \draw
        (0, \i ) node [anchor=east, font=\small] {{$\i$}};

        \foreach \i in {{{"1,...,"+str(abs(k-1))}}}
        \draw
        (0, -\i ) node [anchor=east, font=\small] {{$-\i$}};

        \draw [<->] (0,{k-2}) -- (0,{k+12}) node[above] {{$\mathrm{{Y}}$}};
        """

    if 5<h:
        enunciado += fr"""\foreach \i in {{{"1,...,"+str(11+k)}}}
        \draw
        ({str(h-5)} , \i ) node [anchor=east, font=\small] {{$\i$}};

        \foreach \i in {{{"1,...,"+str(abs(k-1))}}}
        \draw
        ({str(h-5)} , -\i ) node [anchor=east, font=\small] {{$-\i$}};
        """










elif a==-1:
    enunciado += fr"""\draw [step=1, thin, gray!50]  ({-5+h},{k-11}) grid ({5+h},{k+1});
    """

    if h<-5:#Eje X-
        enunciado += fr"""\foreach \i in {{{str(h-5)+",...,"+str(h+5)}}}
        \draw
        (\i , 0) node [anchor=north, font=\footnotesize] {{$\i$}};
        """

    elif h==-5:#Eje X-
        enunciado += fr"""\foreach \i in {{{str(h-5)+",...,"+str(h+4)}}}
        \draw
        (\i , 0)  node [anchor=north, font=\footnotesize] {{$\i$}};
        """

    elif -5<h<5:#Eje X
        enunciado += fr"""\foreach \i in {{{"1,...,"+str(5+h)}}}
        \draw
        (\i , 0) node [anchor=north, font=\small]{{$\i$}};

        \foreach \i in {{{"1,...,"+str(5-h)}}}
        \draw
        (-\i , 0) node [anchor=north, font=\small] {{$-\i$}};
        """

    elif h==5:#Eje X+
        enunciado += fr"""\foreach \i in {{{str(h-4)+",...,"+str(h+5)}}}
        \draw
        (\i , 0) node [anchor=north, font=\small] {{$\i$}};
        """

    elif 5<h:#Eje X+
        enunciado += fr"""\foreach \i in {{{str(h-5)+",...,"+str(h+5)}}}
        \draw
        (\i , 0) node [anchor=north, font=\small] {{$\i$}};
        """

    enunciado += fr"""\draw [<->] ({-6+h},0) -- ({6+h},0) node[right] {{$\mathrm{{X}}$}};
    """

    if h<-5:#Eje Y-
        enunciado += fr"""\foreach \i in {{{"1,...,"+str(k+1)}}}
        \draw
        ({str(h+5)} , \i ) node [anchor=east, font=\small] {{$\i$}};

        \foreach \i in {{{"1,...,"+str(abs(k-11))}}}
        \draw
        ({str(h+5)} , -\i ) node [anchor=east, font=\small] {{$-\i$}};
        """

    elif -5<=h<=5:#Eje Y
        enunciado += fr"""\foreach \i in {{{"1,...,"+str(k+1)}}}
        \draw
        (0, \i ) node [anchor=east, font=\small] {{$\i$}};

        \foreach \i in {{{"1,...,"+str(abs(k-11))}}}
        \draw
        (0, -\i ) node [anchor=east, font=\small] {{$-\i$}};

        \draw [<->] (0,{k-12}) -- (0,{k+2}) node[above] {{$\mathrm{{Y}}$}};
        """

    elif 5<h:#Eje Y+
        enunciado += fr"""\foreach \i in {{{"1,...,"+str(k+1)}}}
        \draw
        ({str(h-5)} , \i ) node [anchor=east, font=\small] {{$\i$}};

        \foreach \i in {{{"1,...,"+str(abs(k-11))}}}
        \draw
        ({str(h-5)} , -\i ) node [anchor=east, font=\small] {{$-\i$}};
        """







enunciado += fr"""
\draw [domain={-3.2+h}:{3.2+h}] plot (\x ,"""+"{"+str(a)+r"*\x*\x+"+str(-2*a*h)+r"*\x+"+str(a*h**2+k)+r"""});
\end{tikzpicture}
\end{center}
La función que mejor describe dicha parábola es"""


#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
a, h, k = Racional(a), Racional(h), Racional(k)


contenido_correcto = Matematica("f(x)="+Pol(Term(a,{"x":2}),-2*a*h*"x",a*h**2+k))
contenido_2 = Matematica("f(x)="+Pol(Term(a,{"x":2}),-2*a*h*"x",-a*h**2+k))
contenido_3 = Matematica("f(x)="+Pol(Term(-a,{"x":2}),-2*a*h*"x",a*h**2+k))
contenido_4 = Matematica("f(x)="+Pol(Term(-a,{"x":2}),-2*a*h*"x",-a*h**2+k))
contenido_5 = Matematica("f(x)="+Pol(Term(a,{"x":2}),a*h*"x",a*h**2+k))

enunciado_oculto = [a, h, k]










