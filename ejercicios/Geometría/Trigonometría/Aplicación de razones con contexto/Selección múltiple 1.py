{"cantidad_opciones":4, "cantidad_disponible":50}


if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a = Racional(randrange(100,201))
    angulo = elegir(20,81, 15,30,45,60,75)
    razon = Racional(round(tan(angulo),2))
    #================================Aquí va el enunciado================================================================
    enunciado = f"Un topógrafo está acostado en el suelo a {a} metros de un poste de luz observando su tope. Si el ángulo de elevación de su línea de visión es de {Matematica(str(angulo)+'°')}, ¿Cuál es la altura del poste en metros?. Considera {Matematica('tan('+str(angulo)+'°)='+razon)}."
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(razon*a)
    contenido_2 = Matematica(razon/a)
    contenido_3 = Matematica(a/razon)
    contenido_4 = Matematica(Root(a**2+razon**2))
    contenido_5 = Matematica(Root(abs(a**2-razon**2)))

elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a1 = Racional(randrange(100,201))
    a2 = Racional(randrange(100,201))
    while not a1>a2:
        a1 = Racional(randrange(100,201))
        a2 = Racional(randrange(100,201))
    angulo = elegir(20,81, 15,30,45,60,75)
    razon1 = Racional(round(cos(angulo),2))
    razon2 = Racional(round(cos(90-angulo),2))
    #================================Aquí va el enunciado================================================================
    enunciado = f"Un globo aerostático se encuentra a una altura de {a1} metros. Un tripulante ata el globo al tope de un edificio de {a2} metros con un cable de modo que esté tensado y formando un ángulo de depresión de {Matematica(str(angulo)+'°')}, ¿Cuánto mide el cable en metros?. Considera {Matematica('cos('+str(angulo)+'°)='+razon1)} y {Matematica('cos('+str(90-angulo)+'°)='+razon2)}."
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica((a1-a2)/razon2)
    contenido_2 = Matematica((a1)/razon2)
    contenido_3 = Matematica((a2)/razon2)
    contenido_4 = Matematica(Root(abs(((a1-a2)/razon2)**2-(a1-a2)**2)))
    contenido_5 = Matematica(Root(abs(((a1-a2)/razon2)**2-a1**2)))


elif opcion==3:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a = Racional(randrange(100,201))
    angulo1 = elegir(20,81, 15,30,45,60,75)
    angulo2 = elegir(20,81, 15,30,45,60,75)
    razon1 = Racional(round(tan(angulo1),2))
    razon2 = Racional(round(tan(angulo2),2))
    #================================Aquí va el enunciado================================================================
    enunciado = f"Se tiene un edificio \"A\" de {a} metros y un edificio \"B\". Hay dos cables tensados uniendo a los edificios, uno une el tope del edificio \"A\" con la base del edificio \"B\" formando un ángulo de elevación de {Matematica(str(angulo1)+'°')} y el otro une el tope del edificio \"B\" con la base del edificio \"A\" formando un ángulo de elevación de {Matematica(str(angulo2)+'°')}. ¿Cuál es la altura del edificio \"B\" en metros?. Considera {Matematica('tan('+str(angulo1)+'°)='+razon1)} y {Matematica('tan('+str(angulo2)+'°)='+razon2)}."
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(a*razon2/razon1)
    contenido_2 = Matematica(a*razon2)
    contenido_3 = Matematica(razon2/a)
    contenido_4 = Matematica(a*razon1/razon2)
    contenido_5 = Matematica(razon1/(a*razon2))



elif opcion==4:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    p = Racional(randrange(150,201),100,True)
    v = Racional(randrange(50,201))
    angulo = elegir(20,81, 15,30,45,60,75)
    razon1 = Racional(round(sin(angulo),2))
    razon2 = Racional(round(cos(angulo),2))
    razon3 = Racional(round(tan(angulo),2))
    #================================Aquí va el enunciado================================================================
    enunciado = f"Una persona de {p} metros está parada mirando el tope de un edificio. Dicha persona estima que la longitud de su línea de visión es de {v} metros y su ángulo de elevación es de {Matematica(str(angulo)+'°')}. ¿Cuánto mide la altura del edificio en metros?. Considera {Matematica('sin('+str(angulo)+'°)='+razon1)}, {Matematica('cos('+str(angulo)+'°)='+razon2)} y {Matematica('tan('+str(angulo)+'°)='+razon3)}."
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(v*razon1+p)
    contenido_2 = Matematica(v*razon2+p)
    contenido_3 = Matematica(v*razon3+p)
    contenido_4 = Matematica(v/razon1+p)
    contenido_5 = Matematica(razon1/v+p)




enunciado_oculto = enunciado











