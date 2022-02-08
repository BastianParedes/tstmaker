{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b, c, d = Racional(randrange(-10, 10)), Racional(randrange(-10, 10)), Racional(randrange(-10, 10)), Racional(randrange(-10, 10))
while c-a==0 or d-b==0 or c-d==0 or d-b==0 or b-a==0:
    a, b, c, d = Racional(randrange(-10, 10)), Racional(randrange(-10, 10)), Racional(randrange(-10, 10)), Racional(randrange(-10, 10))

#================================Aquí va el enunciado================================================================
enunciado = "La función de la recta que pasa por los puntos "+Matematica(Par(a,b))+" y "+Matematica(Par(c,d))+" es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto =    Matematica(Recta(Par(a,b), Par(c,d)).show_funcion)
contenido_2 =           Matematica("f(x)="+Pol((d-b)/(a-c)*"x",(a*(b-d)+b*(c-a))/(a-c)))
contenido_3 =           Matematica("f(x)="+Pol((c-a)/(d-b)*"x",(a*(c-a)+b*(b-d))/(b-d)))
contenido_4 =           Matematica("f(x)="+Pol((c-a)/(b-d)*"x",(a*(c-a)+b*(d-b))/(b-d)))
contenido_5 =           Matematica("f(x)="+Pol((b-a)/(d-c)*"x",(a*(b-a)+b*(c-d))/(c-d)))

enunciado_oculto = [a, b, c, d]










