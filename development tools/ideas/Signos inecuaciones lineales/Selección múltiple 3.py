{"cantidad_opciones":5, "cantidad_disponible":5}

if opcion==1:#PDV modificado
    #================================Aquí va el enunciado================================================================
    enunciado = "Sean a,b y c números reales distintos de 0. La expresión "+Matematica(fraccion("a","bc"))+" es negativa, si:"
    #================================Aquí están los contenidos de las informaciones. También la alternativa correcta=====
    informacion_1 = Matematica(fraccion("a","b")+"<0") + " y " + Matematica("c>0")
    informacion_2 = Matematica("0<bc") + " y " + Matematica("ac<0")
    alternativa_correcta = "A"

elif opcion==2:#PDV modificado
    #================================Aquí va el enunciado================================================================
    enunciado = "Sea x un número real distinto de 1. La expresión "+Matematica(fraccion("x-1",potencia("x",2))) + " es positiva, si:"
    #================================Aquí están los contenidos de las informaciones. También la alternativa correcta=====
    informacion_1 = Matematica(potencia("x",2)+">0")
    informacion_2 = Matematica("x-1>2")
    alternativa_correcta = "B"


elif opcion==3:#PDV modificado
    #================================Aquí va el enunciado================================================================
    enunciado = "En una caja hay x botellas. Se puede determinar el valor exacto de x, si:"
    #================================Aquí están los contenidos de las informaciones. También la alternativa correcta=====
    informacion_1 = Matematica("10<x<16")
    informacion_2 = Matematica("14<x")
    alternativa_correcta = "C"


elif opcion==4:#PDV modificado
    #================================Aquí va el enunciado================================================================
    enunciado = "Sean a y b números reales positivos distintos de cero. Se puede determinar que "+ Matematica("a<b") +", si:"
    #================================Aquí están los contenidos de las informaciones. También la alternativa correcta=====
    informacion_1 = Matematica("2a+4b<8b")
    informacion_2 = Matematica(fraccion("1","a")+">"+fraccion("1","b"))
    alternativa_correcta = "B"


elif opcion==5:#PDV modificado
    #================================Aquí va el enunciado================================================================
    enunciado = "Sean x e y números reales distintos. Se puede determinar que la expresión "+Matematica(fraccion("x+y","x-y"))+" es negativa si:"
    #================================Aquí están los contenidos de las informaciones. También la alternativa correcta=====
    informacion_1 = Matematica("x<y")
    informacion_2 = "x e y son positivos"
    alternativa_correcta = "C"

