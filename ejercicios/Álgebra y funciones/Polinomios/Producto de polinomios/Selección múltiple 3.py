{"cantidad_opciones":2, "cantidad_disponible":2}

if opcion==1:#PVD modificado
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica("(x+a)(b+x)")+" es igual a "+Matematica(Pol({"x":2},Term(9,{"x":1}),18))+", si:"
    #================================Aquí están los contenidos de las informaciones. También la alternativa correcta=====
    informacion_1 = Matematica("ab=18")
    informacion_2 = Matematica("a+b=9")
    alternativa_correcta = "C"



elif opcion==2:#PVD modificado
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(potencia("a+b",2))+" es igual a "+Matematica(Pol({"b":2},{"a":2}))+", si:"
    #================================Aquí están los contenidos de las informaciones. También la alternativa correcta=====
    informacion_1 = Matematica("ab=0")
    informacion_2 = Matematica("a+b=0")
    alternativa_correcta = "A"











