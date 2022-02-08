{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
while True:
    a, b, c, d, e, f, g, h = Racional(elegir(-5,7,0)) , Racional(elegir(-5,7,0)) , Racional(elegir(-5,7,0)) , Racional(elegir(-5,7,0)) , Racional(elegir(-5,7,0)) , Racional(elegir(-5,7,0)) , Racional(elegir(-5,7,0)) , Racional(elegir(-5,7,0))
    g = a*c/e
    if g.denominador==1 and a*d+b*c-e*h-f*g!=0 and a*d+c-e*h-f*g!=0:
        break

primero = Pol(a*'x',b,parentesis=True).show + Pol(c*'x',d,parentesis=True).show
segundo = Pol(e*'x',f,parentesis=True).show + Pol(g*'x',h,parentesis=True).show


#================================Aquí va el enunciado================================================================
enunciado = fr'''Despeja x en la siguiente ecuación
\begin{{center}}
{Matematica(primero + '=' + segundo)}
\end{{center}}'''

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica( (f*h-b*d)/(a*d+b*c-e*h-f*g) )
contenido_2 = Matematica( (f*h-b*d)/(d+b*c-e*h-f*g) )
contenido_3 = Matematica( (f*h-b*d)/(a*d+c-e*h-f*g) )
contenido_4 = Matematica( (f*h-d)/(a*d+b*c-e*h-f*g) )
contenido_5 = Matematica( (f-b*d)/(a*d+b*c-e*h-f*g) )

enunciado_oculto = [a,b,c,d,e,f]