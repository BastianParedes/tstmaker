{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
while True:
    a, b, c, d, e, f = Racional(elegir(-5,6,0)) , Racional(elegir(-5,6,0)) , Racional(elegir(-5,6,0)) , Racional(elegir(-5,6,0)) , Racional(elegir(-5,6,0)) , Racional(elegir(-5,6,0))
    g = a - d
    if g!=0 and a*c+a*b-d*f-d*e!=0 and d*e*f-a*b*c!=0 and c+b-f-e!=0 and a*c+a*b-f-e!=0:
        break

primero = a*Pol('x',b,parentesis=True).show + Pol('x',c,parentesis=True).show
segundo = d*Pol('x',e,parentesis=True).show + Pol('x',f,parentesis=True).show


#================================Aquí va el enunciado================================================================
enunciado = fr'''Despeja x en la siguiente ecuación
\begin{{center}}
{Matematica(primero + '=' + Pol(segundo, Term(g,{'x':2}), azar=True))}
\end{{center}}'''

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica( (d*e*f-a*b*c)/(a*c+a*b-d*f-d*e) )
contenido_2 = Matematica( (e*f-b*c)/(c+b-f-e) )
contenido_3 = Matematica( (e*f-a*b*c)/(a*c+a*b-f-e) )
contenido_4 = Matematica( (e*f-b*c)/(a*c+a*b-f-e) )
contenido_5 = Matematica(d*e*f-a*b*c)

enunciado_oculto = [a,b,c,d,e,f]