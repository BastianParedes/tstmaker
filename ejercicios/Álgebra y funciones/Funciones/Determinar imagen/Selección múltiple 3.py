{"cantidad_opciones":3, "cantidad_disponible":3}

if opcion==1:#Propio
    #================================Aquí va el enunciado================================================================
    enunciado = f"Sean las funciones f y g. Se cumple que {Matematica('f(a)=g(b)')} si:"
    #================================Aquí están los contenidos de las informaciones. También la alternativa correcta=====
    informacion_1 = Matematica("f(a)=g(a)")
    informacion_2 = Matematica("f(b)=g(b)")
    alternativa_correcta = "E"


elif opcion==2:#Propio
    m = Racional(elegir(-9,10, 0))
    while True:
        x1, x2, y1, y2 = randrange(-9,10), randrange(-9,10), randrange(-9,10), randrange(-9,10)
        if x1!=x2 and y1!=y2:
            break
    #================================Aquí va el enunciado================================================================
    enunciado = "Sea la función "+Matematica(f"f(x+a)={m*'x'}")+". Se puede determinar el valor de a si:"
    #================================Aquí están los contenidos de las informaciones. También la alternativa correcta=====
    informacion_1 = Matematica(f"f({x1})={y1}")
    informacion_2 = Matematica(f"f({x2})={y2}")
    alternativa_correcta = "D"


elif opcion==3:#Propio
    m = elegir(-9,10, 0,1)
    while True:
        x1, x2 = randrange(-9,10), randrange(-9,10)
        if x1!=x2:
            break
    #================================Aquí va el enunciado================================================================
    enunciado = "Sea la función "+Matematica("f(x)=mx+n")+f". Se cumple que {Matematica('n=0')} si:"
    #================================Aquí están los contenidos de las informaciones. También la alternativa correcta=====
    informacion_1 = Matematica(f"f({x1})={m*x1}")
    informacion_2 = Matematica(f"f({x2})={m*x2}")
    alternativa_correcta = "C"














