{"cantidad_opciones":2, "cantidad_disponible":50}


if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    z1, z2, z3, z4, z5 = Complex(elegir(-10,10), elegir(-10,10)), Complex(elegir(-10,10), elegir(-10,10)), Complex(elegir(-10,10), elegir(-10,10)), Complex(elegir(-10,10), elegir(-10,10)), Complex(elegir(-10,10), elegir(-10,10))
    while not abs(z1)<abs(z2) or not abs(z1)<abs(z3) or not abs(z1)<abs(z4) or not abs(z1)<abs(z5):
        z1, z2, z3, z4, z5 = Complex(elegir(-10,10), elegir(-10,10)), Complex(elegir(-10,10), elegir(-10,10)), Complex(elegir(-10,10), elegir(-10,10)), Complex(elegir(-10,10), elegir(-10,10)), Complex(elegir(-10,10), elegir(-10,10))
    #================================Aquí va el enunciado================================================================
    enunciado = "Considera i como la unidad imaginaria, ¿Cuál de los siguientes números complejos tiene el menor módulo?"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(z1)
    contenido_2 = Matematica(z2)
    contenido_3 = Matematica(z3)
    contenido_4 = Matematica(z4)
    contenido_5 = Matematica(z5)


elif opcion==2:
    z1, z2, z3, z4, z5 = Complex(elegir(-10,10), elegir(-10,10)), Complex(elegir(-10,10), elegir(-10,10)), Complex(elegir(-10,10), elegir(-10,10)), Complex(elegir(-10,10), elegir(-10,10)), Complex(elegir(-10,10), elegir(-10,10))
    while not abs(z1)<abs(z5) or not abs(z2)<abs(z5) or not abs(z3)<abs(z5) or not abs(z4)<abs(z5):
        z1, z2, z3, z4, z5 = Complex(elegir(-10,10), elegir(-10,10)), Complex(elegir(-10,10), elegir(-10,10)), Complex(elegir(-10,10), elegir(-10,10)), Complex(elegir(-10,10), elegir(-10,10)), Complex(elegir(-10,10), elegir(-10,10))
    #================================Aquí va el enunciado================================================================
    enunciado = "Considera i como la unidad imaginaria, ¿Cuál de los siguientes números complejos tiene el mayor módulo?"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(z5)
    contenido_2 = Matematica(z4)
    contenido_3 = Matematica(z3)
    contenido_4 = Matematica(z2)
    contenido_5 = Matematica(z1)




enunciado_oculto = [z1, z2, z3, z4 ,z5]










