{"cantidad_opciones":2, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
z1, z2, z3, z4 = Complex(randrange(-10,11),elegir(-10,11,0)), Complex(randrange(-10,11),elegir(-10,11,0)), Complex(randrange(-10,11),elegir(-10,11,0)), Complex(randrange(-10,11),elegir(-10,11,0))

if opcion==1:
    opcion_b = choice([1, 2, 3, 4, 5, 6])
    if opcion_b==1:
        #================================Aquí va el enunciado================================================================
        enunciado = f"Considera i como la unidad imaginaria. Sean {Matematica(sub('z',1)+'='+z1)}, {Matematica(sub('z',2)+'='+z2)}, {Matematica(sub('z',3)+'='+z3)} y {Matematica(sub('z',4)+'='+z4)}. {Matematica(Pol(sub('z',1),sub('z',2),sub('z',3),sub('z',4))+'=')}"
        #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
        contenido_correcto = Matematica(z1+z2+z3+z4)
        contenido_2 = Matematica((z1+z2+z3+z4).re+(z1+z2+z3+z4).im)
        contenido_3 = Matematica(((z1+z2+z3+z4).re+(z1+z2+z3+z4).im)*"i")
        contenido_4 = Matematica(z1-z2+z3-z4)
        contenido_5 = Matematica(z1+z2-z3-z4)

    elif opcion_b==2:
        #================================Aquí va el enunciado================================================================
        enunciado = f"Considera i como la unidad imaginaria. Sean {Matematica(sub('z',1)+'='+z1)}, {Matematica(sub('z',2)+'='+z2)}, {Matematica(sub('z',3)+'='+z3)} y {Matematica(sub('z',4)+'='+z4)}. {Matematica(Pol(sub('z',1),-1*sub('z',2),sub('z',3),-1*sub('z',4))+'=')}"
        #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
        contenido_correcto = Matematica(z1-z2+z3-z4)
        contenido_2 = Matematica((z1-z2+z3-z4).re+(z1-z2+z3-z4).im)
        contenido_3 = Matematica(((z1+z2-z3-z4).re+(z1-z2+z3-z4).im)*"i")
        contenido_4 = Matematica(z1+z2+z3+z4)
        contenido_5 = Matematica(z1-z2+z3+z4)

    elif opcion_b==3:
        #================================Aquí va el enunciado================================================================
        enunciado = f"Considera i como la unidad imaginaria. Sean {Matematica(sub('z',1)+'='+z1)}, {Matematica(sub('z',2)+'='+z2)}, {Matematica(sub('z',3)+'='+z3)} y {Matematica(sub('z',4)+'='+z4)}. {Matematica(Pol(sub('z',1),sub('z',2)+por()+sub('z',3),-1*sub('z',4))+'=')}"
        #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
        contenido_correcto = Matematica(z1+z2*z3-z4)
        contenido_2 = Matematica(z1+z2+z3+z4)
        contenido_3 = Matematica(z1+z2*z3+z4)
        contenido_4 = Matematica(z1+z2-z3-z4)
        contenido_5 = Matematica(z1*z2+z3-z4)

    elif opcion_b==4:
        #================================Aquí va el enunciado================================================================
        enunciado = f"Considera i como la unidad imaginaria. Sean {Matematica(sub('z',1)+'='+z1)}, {Matematica(sub('z',2)+'='+z2)}, {Matematica(sub('z',3)+'='+z3)} y {Matematica(sub('z',4)+'='+z4)}. {Matematica(Pol(sub('z',1)+por()+sub('z',2),sub('z',3)+por()+sub('z',4))+'=')}"
        #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
        contenido_correcto = Matematica(z1*z2+z3*z4)
        contenido_2 = Matematica(z1*z2+z3+z4)
        contenido_3 = Matematica(z1+z2+z3+z4)
        contenido_4 = Matematica(z1*z2*z3*z4)
        contenido_5 = Matematica(z1+z2*z3+z4)

    elif opcion_b==5:
        #================================Aquí va el enunciado================================================================
        enunciado = f"Considera i como la unidad imaginaria. Sean {Matematica(sub('z',1)+'='+z1)}, {Matematica(sub('z',2)+'='+z2)} y {Matematica(sub('z',3)+'='+z3)}. {Matematica(fraccion(sub('z',1)+por()+sub('z',2),sub('z',3))+'=')}"
        #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
        contenido_correcto = Matematica((z1*z2)/z3)
        contenido_2 = Matematica((z1*z2)/z3.conjugate())
        contenido_3 = Matematica((z1+z2)/z3.conjugate())
        contenido_4 = Matematica(z1*z2*z3)
        contenido_5 = Matematica((z1+z2)/z3)

    elif opcion_b==6:
        #================================Aquí va el enunciado================================================================
        enunciado = f"Considera i como la unidad imaginaria. Sean {Matematica(sub('z',1)+'='+z1)}, {Matematica(sub('z',2)+'='+z2)} y {Matematica(sub('z',3)+'='+z3)}. {Matematica(fraccion(sub('z',1)+'+'+sub('z',2),sub('z',3))+'=')}"
        #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
        contenido_correcto = Matematica((z1+z2)/z3)
        contenido_2 = Matematica((z1*z2)/z3.conjugate())
        contenido_3 = Matematica((z1+z2)/z3.conjugate())
        contenido_4 = Matematica(z1+z2*z3)
        contenido_5 = Matematica((z1*z2)/z3)



elif opcion==2:
    opcion_b = choice([1, 2, 3, 4, 5, 6])
    if opcion_b==1:
        #================================Aquí va el enunciado================================================================
        enunciado = f"Considera i como la unidad imaginaria. {Matematica(Pol(z1,z2,z3,z4)+'=')}"
        #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
        contenido_correcto = Matematica(z1+z2+z3+z4)
        contenido_2 = Matematica((z1+z2+z3+z4).re+(z1+z2+z3+z4).im)
        contenido_3 = Matematica(((z1+z2+z3+z4).re+(z1+z2+z3+z4).im)*"i")
        contenido_4 = Matematica(z1-z2+z3-z4)
        contenido_5 = Matematica(z1+z2-z3-z4)

    elif opcion_b==2:
        #================================Aquí va el enunciado================================================================
        enunciado = f"Considera i como la unidad imaginaria. {Matematica(Pol(z1,Racional(-1)*('('+z2+')'),z3,Racional(-1)*('('+z4+')'))+'=')}"
        #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
        contenido_correcto = Matematica(z1-z2+z3-z4)
        contenido_2 = Matematica((z1-z2+z3-z4).re+(z1-z2+z3-z4).im)
        contenido_3 = Matematica(((z1+z2-z3-z4).re+(z1-z2+z3-z4).im)*"i")
        contenido_4 = Matematica(z1+z2+z3+z4)
        contenido_5 = Matematica(z1-z2+z3+z4)

    elif opcion_b==3:
        #================================Aquí va el enunciado================================================================
        enunciado = f"Considera i como la unidad imaginaria. {Matematica(Pol(z1,'('+z2+')'+'('+z3+')',Racional(-1)*('('+z4+')'))+'=')}"
        #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
        contenido_correcto = Matematica(z1+z2*z3-z4)
        contenido_2 = Matematica(z1+z2+z3+z4)
        contenido_3 = Matematica(z1+z2*z3+z4)
        contenido_4 = Matematica(z1+z2-z3-z4)
        contenido_5 = Matematica(z1*z2+z3-z4)

    elif opcion_b==4:
        #================================Aquí va el enunciado================================================================
        enunciado = f"Considera i como la unidad imaginaria. {Matematica('('+z1+')'+'('+z2+')+('+z3+')'+'('+z4+')'+'=')}"
        #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
        contenido_correcto = Matematica(z1*z2+z3*z4)
        contenido_2 = Matematica(z1*z2+z3+z4)
        contenido_3 = Matematica(z1+z2+z3+z4)
        contenido_4 = Matematica(z1*z2*z3*z4)
        contenido_5 = Matematica(z1+z2*z3+z4)

    elif opcion_b==5:
        #================================Aquí va el enunciado================================================================
        enunciado = f"Considera i como la unidad imaginaria. {Matematica(fraccion('('+z1+')'+'('+z2+')',z3)+'=')}"
        #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
        contenido_correcto = Matematica((z1*z2)/z3)
        contenido_2 = Matematica((z1*z2)/z3.conjugate())
        contenido_3 = Matematica((z1+z2)/z3.conjugate())
        contenido_4 = Matematica(z1*z2*z3)
        contenido_5 = Matematica((z1+z2)/z3)

    elif opcion_b==6:
        #================================Aquí va el enunciado================================================================
        enunciado = f"Considera i como la unidad imaginaria. {Matematica(fraccion('('+z1+')+('+z2+')',z3)+'=')}"
        #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
        contenido_correcto = Matematica((z1+z2)/z3)
        contenido_2 = Matematica((z1*z2)/z3.conjugate())
        contenido_3 = Matematica((z1+z2)/z3.conjugate())
        contenido_4 = Matematica(z1+z2*z3)
        contenido_5 = Matematica((z1*z2)/z3)





enunciado_oculto = enunciado










