$\mathrm{ \left(  \right) }$

["Andrés", "Cristiano", "Gerard", "Lionel", "Neymar", "Ana", "Enzo", "Eric", "Eva", "Hugo", "Iván", "Juan", "Lara", "Leo", "Luz", "Mar", "Nora", "Raúl", "Sara", "Héctor", "Helena", "Isis", "Penélope", "Ulises", "Zeus", "Alba", "Alejandro", "Álvaro", "Ana", "Emma", "Lucas", "Lucía", "Manuel", "Mariana", "Martín", "Bernardo", "Esther", "Gabriel", "Isabel", "Jorge", "Lucía", "Marta", "Moisés", "Raquel", "Alberto", "Enrique", "Felipe", "Isabel", "Leticia", "Margarita"]

lista_de_letras = ["A","B","C","D","E"]

shuffle(lista_de_letras)

letra_A, letra_B, letra_C, letra_D, letra_E = lista_de_letras[0], lista_de_letras[1], lista_de_letras[2], lista_de_letras[3], lista_de_letras[4]
letra_A, letra_B, letra_C, letra_D, letra_E = "A", "B", "C", "D", "E"


unidadDeMedida = choice(["mm", "cm", "m", "km"])




#Tamaños de letras
\tiny
\scriptsize
\footnotesize
\small
\normalsize
\large
\Large
\LARGE
\huge
\Huge




# Inicio y término
\begin{{center}} \begin{{tikzpicture}} [scale=0.5, rotate={randrange(0,360)}]
\end{{tikzpicture}} \end{{center}}
\begin{center} \begin{tikzpicture} [scale=0.5, rotate={randrange(0,360)}]
\end{tikzpicture} \end{center}



#Punto
\coordinate (A) at (0,0);
\coordinate (A) at (angulo:radio);
\tkzDrawPoints[fill=black](A,B,C)
\tkzDefShiftPoint[A](a,b){B}        #: Se define el punto B con respecto al punto A con respecto a las coordenadas cartesianas (a, b)
\tkzDefPointWith[orthogonal](I,M)
\tkzDefMidPoint(PUNTO_1,PUNTO_2)
\tkzGetPoint{H} \tkzGetFirstPoint{B} \tkzGetSecondPoint{Z}
\tkzDefPointBy[rotation=center O angle 100](A) \tkzGetPoint{C}
\tkzDefPointBy[homothety=center A ratio 3](A)\tkzGetPoint{A};
\tkzDefPointBy[symmetry=center O](A){B};


#Label
\node at ($(a)+(b)$) {label};

#Segmento
\tkzDrawSegment(A,B)
\tkzDrawPolygon(A,B,C)
\draw (A) -- (B);
\coordinate (E) at (intersection of {c} and {lado});

#Ángulo
\tkzMarkRightAngle[size=0.15](B,C,A)
\tkzMarkAngle[size=0.15](B,A,C)
\draw pic["$\alpha$",draw,<->,angle radius=0.8cm] {angle=a--b--c};      #La etiqueta debe ir entre comillas

#Circunferencia
\draw (0,0) circle(radio);
\tkzDrawCircle(CENTRO, PUNTO DEL BORDE)
\tkzDrawArc(centro,inicio)(fin)
\node (circulo) [circle through=(1,0)] at (O) {};
\node (E) [draw,circle through=(A),label=right:$E$] at (B) {};

#Intersección
\tkzInterLC(PUNTO_1,PUNTO_2)(PUNTO_CENTRO,PUNTO_BORDE)
\tkzInterLC(LINEA)(CIRCULO)
\tkzInterLL(LINEA)(LINEA)
\tkzInterLL(PUNTO_1,PUNTO_2)(PUNTO_3,PUNTO_4)
\tkzGetFirstPoint{B} \tkzGetSecondPoint{Z}
\coordinate [label=above:$C$] (C) at (intersection 2 of D and E);
\fill [red, name intersections={of=c and lado}] (intersection-1) circle (2pt);
\coordinate (B) at ($(A)!(D)!(C)$);     #genera punto B en segmento AC tal que BD es perpendicular a AC

#Rejilla de plano cartesiano
\draw [step=1, thin, gray!50] (,) grid (,);

#Comando for
\foreach \i in {1,...,10}
    #Números en eje de plano cartesiano
    \draw
        (\i , 0) node [anchor=north, font=\footnotesize] {{$\i$}}
        (-\i , 0) node [anchor=north, font=\footnotesize] {{$-\i$}}
        (0 , \i) node [anchor=east, font=\footnotesize] {{$\i$}}
        (0 , -\i) node [anchor=east, font=\footnotesize] {{$-\i$}};

#Eje
\draw [<->] (-5,0) -- (5,0) node[right] {{X}};
\draw [<->] (0,-5) -- (0,5) node[above] {{Y}};

#Dibuja la funcion
\draw [domain=DESDE:HASTA] plot (\x , {\x});





#Cosas útiles
[dashed] #hace que sea interlineado

#Letras griegas. Las mayúsculas se pueden obtener escribiendo las ltras en mayúsculas
\alpha
\beta
\epsilon
\delta
\gamma
\lambda
\mu
\omega
\phi
\theta


# Símbolos de desigualdades
< #menor
> #mayor
\leq #menor o igual
\geq #mayor o igual




#homotecia con razon k desde O hasta A
\coordinate (A') at ($(O)!{k}!(A)$);
#90 grados respecto a segmento CD
at ($ (C)!1cm!90:(B) $);



#Rectangulo
\draw [pattern=north west lines] (2,0) rectangle (2.5,3.0);







\filldraw [black] (,) circle (4pt)

