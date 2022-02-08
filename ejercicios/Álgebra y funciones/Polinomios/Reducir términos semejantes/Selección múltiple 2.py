{"cantidad_opciones":2, "cantidad_disponible":50}

unidad_de_medida = choice(["mm", "cm", "m", "km"])
letra = choice(["x", "y", "z"])

if opcion==1:

    opcion_b = choice([1,2,3])

    if opcion_b==1:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        x1, x2, x3 = randrange(0,3), randrange(6,9), randrange(3,6)
        y1, y2, y3 = randrange(0,3), randrange(0,4), randrange(5,9)
        l1, l2, l3 = randrange(1,10), randrange(1,10), randrange(1,10)
        #================================Aquí va el enunciado================================================================
        enunciado = fr"""A continuación se muestran las medidas, en {unidad_de_medida}, de los lados de un triángulo
        \begin{{center}}
        \begin{{tikzpicture}} [scale=0.5]
        \tkzDefPoint({x1},{y1}){{A}}
        \tkzDefPoint({x2},{y2}){{B}}
        \tkzDefPoint({x3},{y3}){{C}}
        \tkzDrawPolygon(A,B,C)
        \tkzLabelSegment[below](A,B){{{Matematica(Term(l1,letra))}}}
        \tkzLabelSegment[right](B,C){{{Matematica(Term(l2,letra))}}}
        \tkzLabelSegment[left](C,A){{{Matematica(Term(l3,letra))}}}
        \end{{tikzpicture}}
        \end{{center}}
        ¿Cuánto mide el perímetro del triángulo (en {unidad_de_medida})?"""
        #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
        contenido_correcto = Matematica(Term(l1+l2+l3,letra))
        contenido_2 = Matematica(Term(l1*l2*l3,letra))
        contenido_3 = Matematica(Term(3*(l1+l2+l3),letra))
        contenido_4 = Matematica(Term(3*l1*l2*l3,letra))
        contenido_5 = Matematica(Term(Racional(l1+l2+l3)/2,letra))
        enunciado_oculto = [opcion, opcion_b, l1, l2, l3]

    elif opcion_b==2:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        x1, x2, x3, x4 = randrange(0,3), randrange(6,9), randrange(6,9), randrange(0,3)
        y1, y2, y3, y4 = randrange(0,3), randrange(0,3), randrange(6,9), randrange(6,9)
        l1, l2, l3, l4 = randrange(1,10), randrange(1,10), randrange(1,10), randrange(1,10)
        #================================Aquí va el enunciado================================================================
        enunciado = fr"""A continuación se muestran las medidas, en {unidad_de_medida}, de los lados de un cuadrilátero
        \begin{{center}}
        \begin{{tikzpicture}} [scale=0.5]
        \tkzDefPoint({x1},{y1}){{A}}
        \tkzDefPoint({x2},{y2}){{B}}
        \tkzDefPoint({x3},{y3}){{C}}
        \tkzDefPoint({x4},{y4}){{D}}
        \tkzDrawPolygon(A,B,C,D)
        \tkzLabelSegment[below](A,B){{{Matematica(Term(l1,letra))}}}
        \tkzLabelSegment[right](B,C){{{Matematica(Term(l2,letra))}}}
        \tkzLabelSegment[above](C,D){{{Matematica(Term(l3,letra))}}}
        \tkzLabelSegment[left](D,A){{{Matematica(Term(l4,letra))}}}
        \end{{tikzpicture}}
        \end{{center}}
        ¿Cuánto mide el perímetro del cuadrilátero (en {unidad_de_medida})?"""
        #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
        contenido_correcto = Matematica(Term(l1+l2+l3+l4,letra))
        contenido_2 = Matematica(Term(l1*l2*l3*l4,letra))
        contenido_3 = Matematica(Term(4*(l1+l2+l3+l4),letra))
        contenido_4 = Matematica(Term(4*l1*l2*l3*l4,letra))
        contenido_5 = Matematica(Term(Racional(l1+l2+l3+l4)/4,letra))    
        enunciado_oculto = [opcion, opcion_b, l1, l2, l3, l4]

    elif opcion_b==3:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        x1, x2, x3, x4, x5 = randrange(0,3), randrange(4,7), randrange(6,9), randrange(3,5), randrange(-2,1)
        y1, y2, y3, y4, y5 = randrange(0,3), randrange(0,3), randrange(5,8), randrange(7,10), randrange(5,8)
        while y3==y4==y5:
            y1, y2, y3, y4, y5 = randrange(0,3), randrange(0,3), randrange(5,8), randrange(7,10), randrange(5,8)
        l1, l2, l3, l4, l5 = randrange(1,10), randrange(1,10), randrange(1,10), randrange(1,10), randrange(1,10)
        #================================Aquí va el enunciado================================================================
        enunciado = fr"""A continuación se muestran las medidas, en {unidad_de_medida}, de los lados de un pentágono
        \begin{{center}}
        \begin{{tikzpicture}} [scale=0.5]
        \tkzDefPoint({x1},{y1}){{A}}
        \tkzDefPoint({x2},{y2}){{B}}
        \tkzDefPoint({x3},{y3}){{C}}
        \tkzDefPoint({x4},{y4}){{D}}
        \tkzDefPoint({x5},{y5}){{E}}
        \tkzDrawPolygon(A,B,C,D,E)
        \tkzLabelSegment[below](A,B){{{Matematica(Term(l1,letra))}}}
        \tkzLabelSegment[right](B,C){{{Matematica(Term(l2,letra))}}}
        \tkzLabelSegment[above](C,D){{{Matematica(Term(l3,letra))}}}
        \tkzLabelSegment[above](D,E){{{Matematica(Term(l4,letra))}}}
        \tkzLabelSegment[left](E,A){{{Matematica(Term(l5,letra))}}}
        \end{{tikzpicture}}
        \end{{center}}
        ¿Cuánto mide el perímetro del pentágono (en {unidad_de_medida})?"""
        #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
        contenido_correcto = Matematica(Term(l1+l2+l3+l4+l5,letra))
        contenido_2 = Matematica(Term(l1*l2*l3*l4*l5,letra))
        contenido_3 = Matematica(Term(4*(l1+l2+l3+l4+l5),letra))
        contenido_4 = Matematica(Term(4*l1*l2*l3*l4*l5,letra))
        contenido_5 = Matematica(Term(Racional(l1+l2+l3+l4+l5)/5,letra))    
        enunciado_oculto = [opcion, opcion_b, l1, l2, l3, l4, l5]



elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    edadAntes = Pol(Term(randrange(1,10),{"x":1}), elegir(-9,10,0), parentesis=True)
    añosPasado = Racional(randrange(2,10))
    añosFuturo = Racional(randrange(2,10))
    nombre = choice(["Andrés", "Cristiano", "Gerard", "Lionel", "Neymar", "Ana", "Enzo", "Eric", "Eva", "Hugo", "Iván", "Juan", "Lara", "Leo", "Luz", "Mar", "Nora", "Raúl", "Sara", "Héctor", "Helena", "Isis", "Penélope", "Ulises", "Zeus", "Alba", "Alejandro", "Álvaro", "Ana", "Emma", "Lucas", "Lucía", "Manuel", "Mariana", "Martín", "Bernardo", "Esther", "Gabriel", "Isabel", "Jorge", "Lucía", "Marta", "Moisés", "Raquel", "Alberto", "Enrique", "Felipe", "Isabel", "Leticia", "Margarita"])
    #================================Aquí va el enunciado================================================================
    enunciado = f"{nombre} tenía {Matematica(edadAntes)} años hace {Matematica(añosPasado)} años. En {Matematica(añosFuturo)} años {nombre} tendrá"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica("("+(edadAntes+añosPasado+añosFuturo)+") años")
    contenido_2 = Matematica("("+(edadAntes+añosPasado)+") años") # responde con la edad actual
    contenido_3 = Matematica("("+(edadAntes+añosFuturo)+") años") # a la edad en el pasado solo le suma el tiempo que pasará
    contenido_4 = Matematica("("+(edadAntes-añosPasado-añosFuturo)+") años") # resta en lugar de sumar los años
    contenido_5 = Matematica("("+(edadAntes-añosPasado+añosFuturo)+") años") # resta años pasados y suma años en el futuro
    enunciado_oculto = [opcion, edadAntes, añosPasado, añosFuturo]












