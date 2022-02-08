{"cantidad_opciones":5, "cantidad_disponible":50}

unidad_de_medida = choice(["mm", "cm", "m", "km"])

if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    A = Racional(randrange(1, 10))
    k = Racional(elegir(-10,11,0,1,-1))
    #================================Aquí va el enunciado================================================================
    enunciado = f"Un polígono tiene una superficie de {Matematica(A+' '+potencia(unidad_de_medida,2,parentesis_automatico=False), arreglar_espacios=True)}. Si se le aplica una homotecia con una razón de homotecia {Matematica(k)}, entonces la superficie de la figura homotética mide"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    k = abs(k)
    contenido_correcto = Matematica(A*k**2+" "+potencia(unidad_de_medida,2,parentesis_automatico=False))
    contenido_2 =        Matematica(A*k+" "+potencia(unidad_de_medida,2,parentesis_automatico=False))
    contenido_3 =        Matematica(A/k**2+" "+potencia(unidad_de_medida,2,parentesis_automatico=False))
    contenido_4 =        Matematica(A/k+" "+potencia(unidad_de_medida,2,parentesis_automatico=False))
    contenido_5 =        Matematica(Root(A*k)+" "+potencia(unidad_de_medida,2,parentesis_automatico=False))
    enunciado_oculto = [opcion, k, A]


elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    L = Racional(randrange(1, 10))
    k = Racional(elegir(-10,11,0,1,-1))
    #================================Aquí va el enunciado================================================================
    enunciado = f"Una circunferencia tiene un "+choice(["radio que mide "+Matematica(L+" "+unidad_de_medida, arreglar_espacios=True),"diámetro que mide "+Matematica(2*L+" "+unidad_de_medida, arreglar_espacios=True)])+f". Si se le aplica una homotecia con una razón de homotecia {Matematica(k)}, entonces la superficie de la figura homotética mide"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    k = abs(k)
    contenido_correcto = Matematica((L*k)**2      *PI()+" "+potencia(unidad_de_medida,2,parentesis_automatico=False))
    contenido_2 =        Matematica((L**2*k)      *PI()+" "+potencia(unidad_de_medida,2,parentesis_automatico=False))
    contenido_3 =        Matematica((2*L*k)**2    *PI()+" "+potencia(unidad_de_medida,2,parentesis_automatico=False))
    contenido_4 =        Matematica(2*L*k         *PI()+" "+potencia(unidad_de_medida,2,parentesis_automatico=False))
    contenido_5 =        Matematica(2*(L*k)**2    *PI()+" "+potencia(unidad_de_medida,2,parentesis_automatico=False))
    enunciado_oculto = [opcion, k, L]


elif opcion==3:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    L = Racional(randrange(1, 10))
    k = Racional(elegir(-10,11,0,1,-1))
    opcion_b = choice([1,2])
    if opcion_b==1:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        L = Racional(randrange(1, 10))
        k = Racional(elegir(-10,11,0,1,-1))
        #================================Aquí va el enunciado================================================================
        enunciado = f"Una circunferencia tiene una superficie de {Matematica(L**2*PI()+' '+potencia(unidad_de_medida,2,parentesis_automatico=False), arreglar_espacios=True)}. Si se le aplica una homotecia con una razón de homotecia {Matematica(k)}, entonces el radio de la circunferencia homotética mide"
        #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
        k = abs(k)
        contenido_correcto = Matematica(k*L+" "+unidad_de_medida,arreglar_espacios=True)
        contenido_2 =        Matematica(2*k*L+" "+unidad_de_medida,arreglar_espacios=True)
        contenido_3 =        Matematica(L+" "+unidad_de_medida,arreglar_espacios=True)
        contenido_4 =        Matematica(2*L+" "+unidad_de_medida,arreglar_espacios=True)
        contenido_5 =        Matematica(L/2+" "+unidad_de_medida,arreglar_espacios=True)
    elif opcion_b==2:
        #================================Aquí va el enunciado================================================================
        enunciado = f"Una circunferencia tiene una superficie de {Matematica(L**2*PI()+' '+potencia(unidad_de_medida,2,parentesis_automatico=False), arreglar_espacios=True)}. Si se le aplica una homotecia con una razón de homotecia {Matematica(k)}, entonces el diámetro de la circunferencia homotética mide"
        #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
        k = abs(k)
        contenido_correcto = Matematica(2*k*L+" "+unidad_de_medida,arreglar_espacios=True)
        contenido_2 =        Matematica(k*L+" "+unidad_de_medida,arreglar_espacios=True)
        contenido_3 =        Matematica(2*L+" "+unidad_de_medida,arreglar_espacios=True)
        contenido_4 =        Matematica(L+" "+unidad_de_medida,arreglar_espacios=True)
        contenido_5 =        Matematica(L/2+" "+unidad_de_medida,arreglar_espacios=True)
    enunciado_oculto = [opcion, k, L]


elif opcion==4:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    L = Racional(randrange(1, 10))
    k = Racional(elegir(1,11))
    #================================Aquí va el enunciado================================================================
    enunciado = f"Un cubo ocupa un espacio de {Matematica(L**3+' '+potencia(unidad_de_medida,3,parentesis_automatico=False), arreglar_espacios=True)}. Se le aplica una homotecia con una razón de homotecia k de modo que la figura homotética tiene un superficie que mide {Matematica(6*(L*k)**2+' '+potencia(unidad_de_medida,2,parentesis_automatico=False), arreglar_espacios=True)}. El valor positivo de k es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(k)
    contenido_2 =        Matematica(k**2)
    contenido_3 =        Matematica(Root(k))
    contenido_4 =        Matematica(L)
    contenido_5 =        Matematica(L*k)
    enunciado_oculto = [opcion, k, L]


elif opcion==5:
    L = Racional(randrange(1, 10))
    k = Racional(elegir(1,11))
    #================================Aquí va el enunciado================================================================
    enunciado = f"Un cuadrado tiene un perímetro que mide {Matematica(4*L+' '+unidad_de_medida, arreglar_espacios=True)}. Se le aplica una homotecia con una razón de homotecia k de modo que la figura homotética tiene un superficie que mide {Matematica((L*k)**2+' '+potencia(unidad_de_medida,2,parentesis_automatico=False), arreglar_espacios=True)}. El valor positivo de k es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(k)
    contenido_2 =        Matematica(k**2)
    contenido_3 =        Matematica(Root(k))
    contenido_4 =        Matematica(L)
    contenido_5 =        Matematica(L*k)
    enunciado_oculto = [opcion, k, L]


















