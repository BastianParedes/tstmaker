{"cantidad_opciones":5, "cantidad_disponible":50}

if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c, d, e, f = Racional(elegir(-10,11,0)), Racional(elegir(-10,11,0)), Racional(elegir(-10,11,0)), Racional(elegir(-10,11,0)), Racional(elegir(-10,11,0)), Racional(elegir(-10,11,0))
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(Pol(a*"x", b*"x", c*"x", d, e, f, azar=True)+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(Pol((a+b+c)*"x",d+e+f,azar=True))
    contenido_2 = Matematica(Pol((a-b+c)*"x",d+e+f,azar=True))
    contenido_3 = Matematica(Pol((a+b+c)*"x",d-e+f,azar=True))
    contenido_4 = Matematica(Pol((a+b-c)*"x",d+e-f,azar=True))
    contenido_5 = Matematica(Pol((a-b+c)*"x",d-e+f,azar=True))



elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c, d = Racional(elegir(-10,11,0)), Racional(elegir(-10,11,0)), Racional(elegir(-10,11,0)), Racional(elegir(-10,11,0))
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(Pol(a*"x", b*"x", Term(c,{"x":1,"y":1},True), Term(d,{"x":1,"y":1},True), azar=True)+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(Pol((a+b)*"x",Term(c+d,{"x":1,"y":1},True),azar=True))
    contenido_2 = Matematica(Pol((a-b)*"x",Term(c+d,{"x":1,"y":1},True),azar=True))
    contenido_3 = Matematica(Pol((a+b)*"x",Term(-c+d,{"x":1,"y":1},True),azar=True))
    contenido_4 = Matematica(Pol((a-b)*"x",Term(c+d,{"x":1,"y":1},True),azar=True))
    contenido_5 = Matematica(Pol((-a+b)*"x",Term(c+d,{"x":1,"y":1},True),azar=True))



elif opcion==3:
#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c, d, e = Racional(elegir(-10,11,0)), Racional(elegir(-10,11,0)), Racional(elegir(-10,11,0)), Racional(elegir(-10,11,0)), Racional(elegir(-10,11,0))
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(Pol(a*"x", b*"x", c*"y", d*"y", Term(e,{"x":1,"y":1},True), azar=True)+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(Pol((a+b)*"x",(c+d)*"y",e*"xy",azar=True))
    contenido_2 = Matematica(Pol((a+b)*"x",(c-d)*"y",e*"xy",azar=True))
    contenido_3 = Matematica(Pol((a+b)*"x",(c+d)*"y",-e*"xy",azar=True))
    contenido_4 = Matematica(Pol((-a+b)*"x",(c+d)*"y",e*"xy",azar=True))
    contenido_5 = Matematica(Pol((a+b)*"x",(-c+d)*"y",e*"xy",azar=True))



elif opcion==4:
#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c, d, e = Racional(elegir(-10,11,0)), Racional(elegir(-10,11,0)), Racional(elegir(-10,11,0)), Racional(elegir(-10,11,0)), Racional(elegir(-10,11,0))
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(Pol(Term(a,{"x":1,"y":2},True),Term(b,{"x":1,"y":2},True), Term(c,{"x":2,"y":1},True), Term(d,{"x":2,"y":1},True), Term(e,{"x":1,"y":1},True), azar=True)+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(Pol(Term(a+b,{"x":1,"y":2},True), Term(c+d,{"x":2,"y":1},True), Term(e,{"x":1,"y":1}),azar=True))
    contenido_2 = Matematica(Pol(Term(a-b,{"x":1,"y":2},True), Term(c+d,{"x":2,"y":1},True), Term(e,{"x":1,"y":1},True),azar=True))
    contenido_3 = Matematica(Pol(Term(a+b,{"x":1,"y":2},True), Term(-c+d,{"x":2,"y":1},True), Term(e,{"x":1,"y":1},True),azar=True))
    contenido_4 = Matematica(Pol(Term(a+b,{"x":1,"y":2},True), Term(c+d,{"x":2,"y":1},True), Term(-e,{"x":1,"y":1},True),azar=True))
    contenido_5 = Matematica(Pol(Term(a-b,{"x":1,"y":2},True), Term(c-d,{"x":2,"y":1},True), Term(e,{"x":1,"y":1},True),azar=True))



elif opcion==5:
#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c, d, e, f, g = Racional(elegir(-10,11,0)), Racional(elegir(-10,11,0)), Racional(elegir(-10,11,0)), Racional(elegir(-10,11,0)), Racional(elegir(-10,11,0)), Racional(elegir(-10,11,0)), Racional(elegir(-10,11,0))
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(Pol(Term(a,{"x":2}), Term(b,{"x":2}), c*"x", d*"x", e*"x", f, g, azar=True)+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(Pol(Term(a+b,{"x":2}), (c+d+e)*"x", f+g,azar=True))
    contenido_2 = Matematica(Pol(Term(a-b,{"x":2}), (c+d+e)*"x", f+g,azar=True))
    contenido_3 = Matematica(Pol(Term(a+b,{"x":2}), (c-d+e)*"x", f+g,azar=True))
    contenido_4 = Matematica(Pol(Term(a+b,{"x":2}), (c+d+e)*"x", f-g,azar=True))
    contenido_5 = Matematica(Pol(Term(-a+b,{"x":2}), (c-d+e)*"x", -f+g,azar=True))


enunciado_oculto = enunciado










