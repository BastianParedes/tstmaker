{"cantidad_opciones":6, "cantidad_disponible":50}

if opcion==1:#cuadrado de binomio con a=1
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    b = Racional(elegir(-10,20,0))
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(choice([potencia(Pol("x",b,azar=True),2), "("+Pol("x",b,azar=True)+")("+Pol("x",b,azar=True)+")"])+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.=
    contenido_correcto = Matematica(Pol({"x":2}, 2*b*"x", b**2))
    contenido_2 = Matematica(Pol({"x":2}, b*"x", b**2))
    contenido_3 = Matematica(Pol({"x":2}, "x", b**2))
    contenido_4 = Matematica(Pol({"x":2}, "x", b))
    contenido_5 = Matematica(Term(b**2,{"x":2}))
    enunciado_oculto = [opcion,b]


elif opcion==2:#cuadrado de binomio con a!=1
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a = Racional(elegir(-5,6,0,1))
    b = Racional(elegir(-5,6,0))
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(choice([potencia(Pol(a*"x",b,azar=True),2), "("+Pol(a*"x",b,azar=True)+")("+Pol(a*"x",b,azar=True)+")"])+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.=
    contenido_correcto = Matematica(Pol(a**2*{"x":2}, 2*a*b*"x", b**2))
    contenido_2 = Matematica(Pol(a*{"x":2}, 2*a*b*"x", b**2))
    contenido_3 = Matematica(Pol({"x":2}, 2*a*b*"x", b**2))
    contenido_4 = Matematica(Pol(a**2*{"x":2}, 2*b*"x", b**2))
    contenido_5 = Matematica(Pol(a**2*{"x":2}, -b**2))
    enunciado_oculto = [opcion,a,b]




elif opcion==3:#producto de binomios con a=1
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    b, c = Racional(randrange(-11, 12)), Racional(randrange(-11, 12))
    while abs(b)==abs(c) or b==0 or c==0:
        b, c = Racional(randrange(-11, 12)), Racional(randrange(-11, 12))
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica("("+Pol("x", b)+")("+Pol("x", c)+")=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.=
    contenido_correcto =   Matematica(Pol({"x":2}, (b+c)*"x", b*c))
    contenido_2 =          Matematica(Pol((1+b)*"x" , c))
    contenido_3 =          Matematica(Pol({"x":2}, b*c))
    contenido_4 =          Matematica(Pol({"x":2}, c*"x", b))
    contenido_5 =          Matematica(Pol("x", (b+c)))
    enunciado_oculto = [opcion,b,c]




elif opcion==4:#producto de binomios con a!=1
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a1, a2, b, c = Racional(elegir(-5,6,0,1)), Racional(elegir(-5,6,0,1)), Racional(elegir(-5,6,0)), Racional(elegir(-5,6,0))
    while abs(b)==abs(c):
        a1, a2, b, c = Racional(elegir(-5,6,0,1)), Racional(elegir(-5,6,0,1)), Racional(elegir(-5,6,0)), Racional(elegir(-5,6,0))
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica("("+Pol(a1*"x", b)+")("+Pol(a2*"x", c)+")=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.=
    contenido_correcto =   Matematica(Pol(a1*a2*{"x":2}, (a1*c+b*a2)*"x", b*c))
    contenido_2 =          Matematica(Pol(a1*a2*{"x":2}, (b+c)*"x", b*c))
    contenido_3 =          Matematica(Pol(a1*a2*{"x":2}, b*c))
    contenido_4 =          Matematica(Pol({"x":2}, a1*a2*"x", b*c))
    contenido_5 =          Matematica(Pol("x", (b+c)))
    enunciado_oculto = [opcion,a1,a2,b,c]




elif opcion==5:#suma por diferencia con a=1
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    y = Racional(elegir(-17,18,0))
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica("("+ Pol("x", y, azar=True) + ")(" + Pol("x", -y, azar=True) + ")=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.=
    contenido_correcto = Matematica(Pol({"x":2}, -y**2))
    contenido_2 = Matematica(Pol({"x":2}, y**2))
    contenido_3 = Matematica(Pol({"x":2}, 2*y*"x", y**2))
    contenido_4 = Matematica(Pol({"x":2}, -y*"x", y**2))
    contenido_5 = Matematica(Pol("x", -y))
    enunciado_oculto = [opcion,y]




elif opcion==6:#suma por diferencia con a=/1
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b = Racional(elegir(-5,6,0,1)), Racional(elegir(-7,8,0))
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica("("+ Pol(a*"x", b, azar=True) + ")(" + Pol(a*"x", -b, azar=True) + ")=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.=
    contenido_correcto = Matematica(Pol(a**2*{"x":2}, -b**2))
    contenido_2 = Matematica(Pol({"x":2}, -b**2))
    contenido_3 = Matematica(Pol(a**2*{"x":2}, b**2))
    contenido_4 = Matematica(Pol(a**2*{"x":2}, 2*a*b*"x", b**2))
    contenido_5 = Matematica(Pol(a**2*{"x":2}, -2*a*b*"x", b**2))
    enunciado_oculto = [opcion,a,abs(b)]


















