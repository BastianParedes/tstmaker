from Definiciones import *

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a = randrange(40, 100)
b = randrange(40, 180-a)
c = 180-(a+b)
while a<40 or b<40 or c<40:
    a = randrange(40, 120)
    b = randrange(30, 180-a)
    c = 180-(a+b)
angulo_de_giro = randrange(0,360)
opcion = choice([1, 2, 3])

#================================Aquí va el enunciado================================================================
if opcion==1:
    enunciado = fr"En el siguiente cuadrilátero el ángulo BAC mide $\alpha$, el ángulo CBA mide {Matematica(b)}° y el ángulo mide ACB mide {Matematica(c)}°."
elif opcion==2:
    enunciado = fr"En el siguiente cuadrilátero el ángulo BAC mide {Matematica(a)}°, el ángulo CBA mide $beta$ y el ángulo mide ACB mide {Matematica(c)}°."
elif opcion==3:
    enunciado = fr"En el siguiente cuadrilátero el ángulo BAC mide {Matematica(a)}°, el ángulo CBA mide {Matematica(b)}° y el ángulo mide ACB mide $\gamma$."

enunciado += fr"""
\begin{{center}}
\begin{{tikzpicture}}[scale=2]
\tkzDefPoint({(180+angulo_de_giro)%360}:1){{A}}
\tkzDefPoint({angulo_de_giro}:1){{B}}
\tkzDefTriangle[two angles= {a} and {b}](A,B) \tkzGetPoint{{C}}
\tkzDrawPolygon(A,B,C)
\node [label={(210+angulo_de_giro)%360}:A] at (A){{}};
\node [label={angulo_de_giro}:B] at (B){{}};
\node [label={(90+angulo_de_giro)%360}:C] at (C){{}};

"""

if opcion==1:
    letra = r"\alpha"
    enunciado += fr"""
    \draw pic["$\alpha$",draw,angle radius=1cm] {{angle=B--A--C}};
    \draw pic["{Matematica(b)}°",draw,angle radius=1cm] {{angle=C--B--A}};
    \draw pic["{Matematica(c)}°",draw,angle radius=1cm] {{angle=A--C--B}};
    """

elif opcion==2:
    letra = r"\beta"
    enunciado += fr"""
    \draw pic["{Matematica(a)}°",draw,angle radius=1cm] {{angle=B--A--C}};
    \draw pic["$\beta$",draw,angle radius=1cm] {{angle=C--B--A}};
    \draw pic["{Matematica(c)}°",draw,angle radius=1cm] {{angle=A--C--B}};
    """

elif opcion==3:
    letra = r"\gamma"
    enunciado += fr"""
    \draw pic["{Matematica(a)}°",draw,angle radius=1cm] {{angle=B--A--C}};
    \draw pic["{Matematica(b)}°",draw,angle radius=1cm] {{angle=C--B--A}};
    \draw pic["$\gamma$",draw,angle radius=1cm] {{angle=A--C--B}};
    """
enunciado += fr"""
\end{{tikzpicture}} \end{{center}} 
En valor del ángulo {Matematica(letra)} es"""

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
if opcion==1:
    contenido_correcto = Matematica(str(a))+"°"
    contenido_2 = Matematica(str(b))+"°"
    contenido_3 = Matematica(str(c))+"°"
    contenido_4 = Matematica(str(b+c))+"°"
    contenido_5 = Matematica(str(abs(b-c)))+"°"

elif opcion==2:
    contenido_correcto = Matematica(str(b))+"°"
    contenido_2 = Matematica(str(a))+"°"
    contenido_3 = Matematica(str(c))+"°"
    contenido_4 = Matematica(str(a+c))+"°"
    contenido_5 = Matematica(str(abs(a-c)))+"°"

elif opcion==3:
    contenido_correcto = Matematica(str(c))+"°"
    contenido_2 = Matematica(str(a))+"°"
    contenido_3 = Matematica(str(b))+"°"
    contenido_4 = Matematica(str(a+b))+"°"
    contenido_5 = Matematica(str(abs(a-b)))+"°"

enunciado_oculto = [a, b, c]