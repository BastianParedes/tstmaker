{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
l1, l2, h = Racional(randrange(1, 10)), Racional(randrange(1, 10)), Racional(randrange(2, 10))

unidad_de_medida = choice(["mm", "cm", "m", "km"])

angulo_de_giro = randrange(0,360)

lado_menor_dibujo, lado_mayor_dibujo = randrange(2, 8), randrange(2, 8)

if l1!=l2:
    while not lado_menor_dibujo<lado_mayor_dibujo:
        lado_menor_dibujo, lado_mayor_dibujo = randrange(2, 8), randrange(2, 8)
elif l1==l2:
    while not lado_menor_dibujo==lado_mayor_dibujo:
        lado_menor_dibujo = randrange(4, 8)
        lado_mayor_dibujo = lado_menor_dibujo


#================================Aquí va el enunciado================================================================
enunciado = fr"""Observa el siguiente cuadrilátero
\begin{{center}} \begin{{tikzpicture}} [scale=0.5, rotate={angulo_de_giro}]
\tkzDefPoint(0,0){{A}}
\tkzDefPoint({lado_mayor_dibujo},0){{B}}
\tkzDefPoint({lado_mayor_dibujo},{lado_menor_dibujo}){{C}}
\tkzDefPoint(0,{lado_menor_dibujo}){{D}}
\tkzDrawPolygon(A,B,C,D)
"""+choice([
    fr"\node [label={180+angulo_de_giro}:{str(min(l1,l2))} {unidad_de_medida}] at (0, {lado_menor_dibujo/2}){{}};",
    fr"\node [label={0+angulo_de_giro}:{str(min(l1,l2))} {unidad_de_medida}] at ({lado_mayor_dibujo}, {lado_menor_dibujo/2}){{}};"])+"\n"+choice([
    
    fr"\node [label={270+angulo_de_giro}:{str(max(l1,l2))} {unidad_de_medida}] at ({lado_mayor_dibujo/2}, 0){{}};",
    fr"\node [label={90+angulo_de_giro}:{str(max(l1,l2))} {unidad_de_medida}] at ({lado_mayor_dibujo/2}, {lado_menor_dibujo}){{}};"])+fr"""

\tkzMarkRightAngle[size=0.4](B,A,D)
\tkzMarkRightAngle[size=0.4](C,B,A)
\tkzMarkRightAngle[size=0.4](D,C,B)
\tkzMarkRightAngle[size=0.4](A,D,C)

\end{{tikzpicture}} \end{{center}}
Sea el cuerpo generado al trasladar el cuadrilátero {Matematica(h+" "+unidad_de_medida,arreglar_espacios=True)} con un vector de traslación perpendicular al plano que contiene a dicho cuadrilátero. El volumen de dicho cuerpo es"""

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(l1*l2*h+" "+potencia(unidad_de_medida,3,parentesis_automatico=False),arreglar_espacios=True)
contenido_2 =        Matematica(l1*l2*h/2+" "+potencia(unidad_de_medida,3,parentesis_automatico=False),arreglar_espacios=True)
contenido_3 =        Matematica(l1*l2+" "+potencia(unidad_de_medida,3,parentesis_automatico=False),arreglar_espacios=True)
contenido_4 =        Matematica(l1+l2+h+" "+potencia(unidad_de_medida,3,parentesis_automatico=False),arreglar_espacios=True)
contenido_5 =        Matematica((l1+l2)*h+" "+potencia(unidad_de_medida,3,parentesis_automatico=False),arreglar_espacios=True)



enunciado_oculto = [l1, l2, h]











