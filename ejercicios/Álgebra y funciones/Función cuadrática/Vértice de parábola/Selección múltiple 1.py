{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, x1, x2 = Racional(randrange(-5,5)), Racional(randrange(-5,5)), Racional(randrange(-5,5))
b, c = -a*(x1+x2), a*x1*x2
while a==0 or (x1+x2).numerador%2!=0 or (4*a*c-b**2).numerador%(4*a).numerador!=0:
    a, x1, x2 = Racional(randrange(-5,5)), Racional(randrange(-5,5)), Racional(randrange(-5,5))
    b, c = -a*(x1+x2), a*x1*x2

#================================Aquí va el enunciado================================================================
enunciado = "El vértice de la parábola asociada a la función "+ Matematica("f(x)="+Pol(Term(a,{"x":2}),b*"x",c))+" es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.=
contenido_correcto = Matematica(Par(-b/(2*a), (4*a*c-b**2)/(4*a)))
contenido_2 = Matematica(Par(0,c))
contenido_3 = Matematica(Par(x1, x2))
contenido_4 = Matematica(Par(x2, x1))
contenido_5 = Matematica(Par(b/(2*a),(b**2-4*a*c)/(2*a)))

enunciado_oculto = [a, x1, x2]










