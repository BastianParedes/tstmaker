{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
while True:
    a, b, c, d = Racional(elegir(-5,6,0)) , Racional(elegir(-5,6,0)) , Racional(elegir(-5,6,0)) , Racional(elegir(-5,6,0))
    d = a
    if b+a-d-c!=0 and b+d-c!=0 and a-d-c!=0 and b+a-d!=0 and b+a-c!=0:
        break

primero = Pol('x',a,parentesis=True).show + Pol('x',b,parentesis=True).show
segundo = Pol('x',c,parentesis=True).show + Pol('x',d,parentesis=True).show


#================================Aquí va el enunciado================================================================
enunciado = fr'''Despeja x en la siguiente ecuación
\begin{{center}}
{Matematica(primero + '=' + segundo)}
\end{{center}}'''

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica( (c*d-a*b)/(b+a-d-c) )
contenido_2 = Matematica( (c*d-b)/(b+d-c) )
contenido_3 = Matematica( (c*d-a)/(a-d-c) )
contenido_4 = Matematica( (d-a*b)/(b+a-d) )
contenido_5 = Matematica( (c-a*b)/(b+a-c) )

enunciado_oculto = [a,b,c,d]