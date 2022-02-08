{"cantidad_opciones":4, "cantidad_disponible":4}



if opcion==1:
    a = randrange(-10,10)
    b, c = a+1, a+2
    #================================Aquí va el enunciado================================================================
    enunciado = r"Sea X el promedio de tres números a, b y c enteros consecutivos. Se puede determinar el valor de X si:"
    #================================Aquí están los contenidos de las informaciones. También la alternativa correcta=====
    informacion_1 = Matematica(f"c={c}")
    informacion_2 = Matematica(f"a={a}")
    alternativa_correcta = r"B"




elif opcion==2:
    n = randrange(3, 10)
    #================================Aquí va el enunciado================================================================
    enunciado = fr"Se puede determinar la suma de {Matematica(n)} números si:"
    #================================Aquí están los contenidos de las informaciones. También la alternativa correcta=====
    informacion_1 = r"se conoce el promedio de los números"
    informacion_2 = r"los números son enteros pares consecutivos"
    alternativa_correcta = r"A"



elif opcion==3:
    #================================Aquí va el enunciado================================================================
    enunciado = r"Sean los cursos X e Y. Se forma un nuevo curso Z conformado por todos los estudiantes de X e Y. Se puede saber el promedio de los estudiantes de Z si:"
    #================================Aquí están los contenidos de las informaciones. También la alternativa correcta=====
    informacion_1 = r"se conocen los promedios de las notas de los estudiantes de X e Y"
    informacion_2 = r"se conocen las notas de los estudiantes de X e Y"
    alternativa_correcta = r"B"




elif opcion==4:
    p = randrange(10, 50)
    #================================Aquí va el enunciado================================================================
    enunciado = f"Sean los números enteros {Matematica('x')}, {Matematica('2x')}, {Matematica('(x+1)')}, {Matematica('(x-1)')} y {Matematica('2x')}. Se puede determinar el promedio de dichos números si:"
    #================================Aquí están los contenidos de las informaciones. También la alternativa correcta=====
    informacion_1 = f"se conoce el promedio entre los números {Matematica('2x')}, {Matematica('4x')} y {Matematica('x')}"
    informacion_2 = f"se conoce el promedio entre los números {Matematica('x')}, {Matematica('2x')}, {Matematica('3x')} y {Matematica('x')}"
    alternativa_correcta = r"D"











