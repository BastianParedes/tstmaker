{"cantidad_opciones":3, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
lista_trios = [
[3, 4, 5]
, [6, 8, 10]
, [9, 12, 15]
, [5, 12, 13]
, [10, 24, 26]
, [8, 15, 17]
, [7, 24, 25]
, [1, Root(2), Root(3)]
, [1, Root(3), 2]
, [1, 2, Root(5)]
, [1, Root(5), Root(6)]
, [1, Root(6), Root(7)]
, [1, Root(7), Root(8)]
, [1, Root(8), 3]
, [2, Root(2), Root(6)]
, [2, Root(3), Root(7)]
, [2, Root(5), 3]
, [2, Root(6), Root(10)]
, [2, 3, Root(13)]
, [2, 4, Root(20)]
, [2, 5, Root(29)]
, [3, 5, Root(34)]
, [4, 5, Root(41)]
]
trio = choice(lista_trios)
AB = trio[0]
CA = trio[1]
BC = trio[2]
if isinstance(AB, int):
    AB = Racional(AB)
if isinstance(BC, int):
    BC = Racional(BC)
if isinstance(CA, int):
    CA = Racional(CA)



unidad_de_medida = choice(["mm", "cm", "m", "km"])
angulo_de_giro = randrange(0, 360)

#================================Aquí va el enunciado================================================================
enunciado = fr"""
\begin{{center}} \begin{{tikzpicture}} [scale=1, rotate={angulo_de_giro}]
\coordinate [label={randrange(180,270)+angulo_de_giro}:A] (A) at (0,0);
\coordinate [label={randrange(-90,45)+angulo_de_giro}:B] (B) at ({randrange(15,40)/10},0);
\coordinate [label={randrange(45,180)+angulo_de_giro}:C] (C) at (0,{randrange(15,40)/10});
\tkzDrawPolygon(A,B,C)
\tkzMarkRightAngle[size=0.2](B,A,C)
"""

if opcion==1:
    enunciado = f"En el siguiente triángulo rectángulo se tiene que {Matematica(linea('AB'))} mide {Matematica(AB+' '+unidad_de_medida,arreglar_espacios=True)}  y {Matematica(linea('CA'))} mide {Matematica(CA+' '+unidad_de_medida,arreglar_espacios=True)}" + enunciado+fr"""
    \coordinate [label={270+angulo_de_giro}:{Matematica(AB)} {unidad_de_medida}] (AB) at ($(A)!.5!(B)$);
    \coordinate [label={180+angulo_de_giro}:{Matematica(CA)} {unidad_de_medida}] (CA) at ($(C)!.5!(A)$);
        \end{{tikzpicture}} \end{{center}}
    {Matematica(linea('BC'))} mide"""

elif opcion==2:
    enunciado = f"En el siguiente triángulo rectángulo se tiene que {Matematica(linea('AB'))} mide {Matematica(AB+' '+unidad_de_medida,arreglar_espacios=True)} y {Matematica(linea('BC'))} mide {Matematica(BC+' '+unidad_de_medida,arreglar_espacios=True)}" + enunciado+fr"""
    \coordinate [label={270+angulo_de_giro}:{Matematica(AB)} {unidad_de_medida}] (AB) at ($(A)!.5!(B)$);
    \coordinate [label={45+angulo_de_giro}:{Matematica(BC)} {unidad_de_medida}] (BC) at ($(B)!.5!(C)$);
    \end{{tikzpicture}} \end{{center}}
    {Matematica(linea('CA'))} mide"""

elif opcion==3:
    enunciado = f"En el siguiente triángulo rectángulo se tiene que {Matematica(linea('BC'))} mide {Matematica(BC+' '+unidad_de_medida,arreglar_espacios=True)} y {Matematica(linea('CA'))} mide {Matematica(CA+' '+unidad_de_medida,arreglar_espacios=True)}" + enunciado+fr"""
    \coordinate [label={45+angulo_de_giro}:{Matematica(BC)} {unidad_de_medida}] (BC) at ($(B)!.5!(C)$);
    \coordinate [label={180+angulo_de_giro}:{Matematica(CA)} {unidad_de_medida}] (CA) at ($(C)!.5!(A)$);
    \end{{tikzpicture}} \end{{center}}
    {Matematica(linea('AB'))} mide"""
#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
if opcion==1:#pide la hipotenusa
    contenido_correcto = Matematica(BC+' '+unidad_de_medida,arreglar_espacios=True)
    contenido_2 =        Matematica(Pol(AB,CA,reducir=True)+' '+unidad_de_medida,arreglar_espacios=True)#suma los catetos
    contenido_3 =        Matematica(Root(abs(AB**2-CA**2))+' '+unidad_de_medida,arreglar_espacios=True)#raiz de la resta de los cuadrados de los catetos
    contenido_4 =        Matematica(abs(AB**2-CA**2)+' '+unidad_de_medida,arreglar_espacios=True)#resta de los cuadrados de los catetos
    contenido_5 =        Matematica(choice([AB,CA])+' '+unidad_de_medida,arreglar_espacios=True)#uno de los catetos

elif opcion==2:
    contenido_correcto = Matematica(CA+' '+unidad_de_medida,arreglar_espacios=True)
    contenido_2 =        Matematica(Pol(AB,BC,reducir=True)+' '+unidad_de_medida,arreglar_espacios=True)#raiz de suma de cuadrados de hipotenusa y cateto
    contenido_3 =        Matematica(Root(AB**2+BC**2)+' '+unidad_de_medida,arreglar_espacios=True)#raiz de suma de cuadrados de cateto e hipotenusa
    contenido_4 =        Matematica(AB**2+BC**2+' '+unidad_de_medida,arreglar_espacios=True)#suma de cuadrados de cateto e hipotenusa
    contenido_5 =        Matematica(choice([AB,BC])+' '+unidad_de_medida,arreglar_espacios=True)#el cateto dado o hipotenusa

elif opcion==3:
    contenido_correcto = Matematica(AB+' '+unidad_de_medida,arreglar_espacios=True)
    contenido_2 =        Matematica(Pol(BC,CA,reducir=True)+' '+unidad_de_medida,arreglar_espacios=True)#raiz de suma de cuadrados de hipotenusa y cateto
    contenido_3 =        Matematica(Root(BC**2+CA**2)+' '+unidad_de_medida,arreglar_espacios=True)#raiz de suma de cuadrados de cateto e hipotenusa
    contenido_4 =        Matematica(BC**2+CA**2+' '+unidad_de_medida,arreglar_espacios=True)#suma de cuadrados de cateto e hipotenusa
    contenido_5 =        Matematica(choice([BC,CA])+' '+unidad_de_medida,arreglar_espacios=True)#el cateto dado o hipotenusa



enunciado_oculto = [opcion, AB, BC, CA]











