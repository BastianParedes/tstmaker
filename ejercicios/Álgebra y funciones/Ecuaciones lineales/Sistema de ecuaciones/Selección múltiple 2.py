{"cantidad_opciones":2, "cantidad_disponible":2}

if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    x, y = Racional(randrange(10, 20)), Racional(randrange(10, 20))
    #================================Aquí va el enunciado================================================================
    enunciado = f'En un corral hay gallinas y conejos. En total hay {x+y} cabezas y {2*x+4*y} patas, ¿Cuántas gallinas hay?'
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto =    y
    contenido_2 =           x       #responde los conejos
    contenido_3 =           x+y     #cantidad de animales
    contenido_4 =           x*y
    contenido_5 =           abs(x-y)
    enunciado_oculto = opcion

elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    x, y = Racional(randrange(-10, 10)), Racional(randrange(-10, 10))
    #================================Aquí va el enunciado================================================================
    enunciado = f'La suma de dos números es {x+y} y la resta de ellos es {x-y}. El mayor de ellos es'
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto =    max([x,y])
    contenido_2 =           min([x,y])  #menor de los núemros
    contenido_3 =           x-y
    contenido_4 =           y-x
    contenido_5 =           x+y         #la suma de lso números
    enunciado_oculto = opcion








