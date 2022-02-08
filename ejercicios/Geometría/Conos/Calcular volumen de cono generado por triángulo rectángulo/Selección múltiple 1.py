{"cantidad_opciones":2, "cantidad_disponible":50}

#===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
opcion_b = choice([1,2,3])
if opcion_b==1:
    a, b = Racional(randrange(1,8)), Racional(randrange(1,8))
    while not a<b:
        a, b = Racional(randrange(1,8)), Racional(randrange(1,8))
    c = Root(a**2+b**2)

elif opcion_b==2:
    a, c = Racional(randrange(1,8)), Racional(randrange(1,8))
    while not a<c:
        a, c = Racional(randrange(1,8)), Racional(randrange(1,8))
    b = Root(c**2-a**2)
elif opcion_b==3:
    b, c = Racional(randrange(1,8)), Racional(randrange(1,8))
    while not b<c:
        b, c = Racional(randrange(1,8)), Racional(randrange(1,8))
    a = Root(c**2-b**2)

a, b = sorted([a,b])[0], sorted([a,b])[1]

unidad_de_medida = choice(["mm", "cm", "m", "km"])
angulo_de_giro = randrange(0,360)
medida_dibujo_1 = randrange(10,30)/10
catetos = ["AB","CA"]
shuffle(catetos)
medidas_de_triangulo = [Matematica(linea(catetos[0]))+" mide "+Matematica(b+' '+unidad_de_medida), Matematica(linea(catetos[1]))+" mide "+Matematica(b+' '+unidad_de_medida), Matematica(linea("BC"))+" mide "+Matematica(c+' '+unidad_de_medida)]
shuffle(medidas_de_triangulo)



if opcion==1:
    #===============================================Aquí va el número del ejercicio y el enunciado.
    enunciado = fr"""El triángulo ABC es rectángulo en A
    \begin{{center}} \begin{{tikzpicture}} [scale=1]
    \tkzDefPoint(0,0){{A}}
    \tkzDefPoint({0+angulo_de_giro}:{randrange(15,30)/10}){{B}}
    \tkzDefPoint({90+angulo_de_giro}:{randrange(15,30)/10}){{C}}

    \tkzDrawPolygon(A,B,C)
    \tkzMarkRightAngle[size=0.2](B,A,C)

    \node [label={225+angulo_de_giro}:A] at (A){{}};
    \node [label={0+angulo_de_giro}:B] at (B){{}};
    \node [label={90+angulo_de_giro}:C] at (C){{}};

    \end{{tikzpicture}} \end{{center}}
    {medidas_de_triangulo[0]} y {medidas_de_triangulo[1]}. El volumen del cuerpo generado al rotar el triángulo ABC en torno al cateto menor es"""
    #===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
    contenido_correcto = Matematica(b**2*PI()*a/3)
    contenido_2 = Matematica(b**2*PI()*a)
    contenido_3 = Matematica(b**2*PI()*a*3)
    contenido_4 = Matematica(a**2*PI()*b/3)
    contenido_5 = Matematica(a**2*PI()*b)


elif opcion==2:
    #===============================================Aquí va el número del ejercicio y el enunciado.
    enunciado = fr"""El triángulo ABC es rectángulo en A
    \begin{{center}} \begin{{tikzpicture}} [scale=1]
    \tkzDefPoint(0,0){{A}}
    \tkzDefPoint({0+angulo_de_giro}:{randrange(15,30)/10}){{B}}
    \tkzDefPoint({90+angulo_de_giro}:{randrange(15,30)/10}){{C}}

    \tkzDrawPolygon(A,B,C)
    \tkzMarkRightAngle[size=0.2](B,A,C)

    \node [label={225+angulo_de_giro}:A] at (A){{}};
    \node [label={0+angulo_de_giro}:B] at (B){{}};
    \node [label={90+angulo_de_giro}:C] at (C){{}};

    \end{{tikzpicture}} \end{{center}}
    {medidas_de_triangulo[0]} y {medidas_de_triangulo[1]}. El volumen del cuerpo generado al rotar el triángulo ABC en torno al cateto mayor es"""
    #===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
    contenido_correcto = Matematica(a**2*PI()*b/3)
    contenido_2 = Matematica(a**2*PI()*b)
    contenido_3 = Matematica(a**2*PI()*b*3)
    contenido_4 = Matematica(b**2*PI()*a/3)
    contenido_5 = Matematica(b**2*PI()*a)



enunciado_oculto = [opcion, a,b,c]











