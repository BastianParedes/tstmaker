from Definiciones import *

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b, d = racional(elegir(1, 6)), racional(elegir(1, 6)), racional(elegir(1, 6))
while a==b:
    a, b, d = racional(elegir(1, 6)), racional(elegir(1, 6)), racional(elegir(1, 6))

#================================Aquí va el enunciado================================================================
enunciado = fr"""
\begin{{center}}
\begin{{tikzpicture}} [scale=0.5]

\tkzDefPoint(-1,0){{A}}
\tkzDefShiftPoint[A](270:{a}){{B}}
\tkzDefShiftPoint[A](270:{b}){{C}}

\tkzDefPoint(0,0){{D}}



\end{{tikzpicture}}
\end{{center}}"""

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica()
contenido_2 = Matematica()
contenido_3 = Matematica()
contenido_4 = Matematica()
contenido_5 = Matematica()




enunciado_oculto = enunciado