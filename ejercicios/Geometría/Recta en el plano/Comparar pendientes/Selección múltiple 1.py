{"cantidad_opciones":2, "cantidad_disponible":50}

#Rectas paralelas
if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    m1 = Racional(elegir(-10,10,0),elegir(-10,10,0))
    n1 = Racional(elegir(-10,10,0),elegir(-10,10,0))
    m2 = m1
    n2 = Racional(elegir(-10,10,0),elegir(-10,10,0))
    L1 = Recta(Par(0,n1), pendiente=m1)
    L2 = Recta(Par(0,n2), pendiente=m1)
    while n1==n2:
        n2 = Racional(elegir(-10,10,0),elegir(-10,10,0))

    #================================Aquí va el enunciado================================================================
    enunciado = fr"""Sean las rectas ${sub("L",1)}$ y ${sub("L",2)}$ tales que
${sub("L",1)}:\ """+"\\"+fr"""{{{choice([L1.show_ecuacion_principal, L1.show_ecuacion_general])}$
${sub("L",2)}:\ """+"\\"+fr"""{{{choice([L2.show_ecuacion_principal, L2.show_ecuacion_general])}$
Es verdadero que {Matematica(sub("L",1))} y {Matematica(sub("L",2))} son"""
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = "paralelas entre sí"
    contenido_2 = "perpendiculares entre sí"
    contenido_3 = "coincidentes"
    contenido_4 = "curvas"
    contenido_5 = f"{choice(['paralelas','perpendiculares'])} al eje {choice(['X','Y'])}"



#Rectas perpendiculares
elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    m1 = Racional(elegir(-10,10,0),elegir(-10,10,0))
    n1 = Racional(elegir(-10,10,0),elegir(-10,10,0))
    m2 = -1/m1
    n2 = Racional(elegir(-10,10,0),elegir(-10,10,0))
    L1 = Recta(Par(0,n1), pendiente=m1)
    L2 = Recta(Par(0,n2), pendiente=m1)
    #================================Aquí va el enunciado================================================================
    enunciado = fr"""Sean las rectas ${sub("L",1)}$ y ${sub("L",2)}$ tales que
${sub("L",1)}:\ """+"\\"+fr"""{{{choice([L1.show_ecuacion_principal, L1.show_ecuacion_general])}$
${sub("L",2)}:\ """+"\\"+fr"""{{{choice([L2.show_ecuacion_principal, L2.show_ecuacion_general])}$
Es verdadero que {Matematica(sub("L",1))} y {Matematica(sub("L",2))} son"""
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = "perpendiculares entre sí"
    contenido_2 = "paralelas entre sí"
    contenido_3 = "coincidentes"
    contenido_4 = "curvas"
    contenido_5 = f"{choice(['paralelas','perpendiculares'])} al eje {choice(['X','Y'])}"






enunciado_oculto = [L1, L2, opcion]










