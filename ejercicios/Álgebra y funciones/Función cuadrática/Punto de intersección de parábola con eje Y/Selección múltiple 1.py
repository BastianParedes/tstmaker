{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, x1, x2 = Racional(randrange(-7,8)), Racional(randrange(-7,8)), Racional(randrange(-7,8))
b, c = -a*(x1+x2), a*x1*x2
while a==0 or (x1+x2).numerador%2!=0 or (4*a*c-b**2).numerador%(4*a).numerador!=0:
    a, x1, x2 = Racional(randrange(-7,8)), Racional(randrange(-7,8)), Racional(randrange(-7,8))
    b, c = -a*(x1+x2), a*x1*x2

#================================Aquí va el enunciado================================================================
enunciado = "El punto de intersección entre el eje Y y la parábola asociada a la función "+ Matematica(f"f(x)="+Pol(Term(a,{"x":2}),b*"x",c))+" es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.=
contenido_correcto = Matematica(Par(0, c))
contenido_2 = Matematica(Par(0,(4*a*c-b**2)/(4*a)))
contenido_3 = Matematica(Par(0, x1))
contenido_4 = Matematica(Par(0, a))
contenido_5 = Matematica(Par(0, (x1+x2)/2))

enunciado_oculto = [a, x1, x2]










