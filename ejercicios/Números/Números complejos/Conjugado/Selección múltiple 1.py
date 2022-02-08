{"cantidad_opciones":2, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
z = Complex(randrange(-10, 10), choice(list(range(-10, 0))+list(range(1, 11))))

if opcion==1:
    #================================Aquí va el enunciado================================================================
    enunciado = "Sea el número complejo "+Matematica("Z="+z)+", con i la unidad imaginaria. El conjugado de Z es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(z.conjugate())
    contenido_2 = Matematica(-z)
    contenido_3 = Matematica(-z.conjugate())
    contenido_4 = Matematica(abs(z))
    contenido_5 = Matematica(choice([z.re, z.im]))

elif opcion==2:
    #================================Aquí va el enunciado================================================================
    enunciado = "Sea el número complejo Z cuyo conjugado es "+Matematica(z.conjugate())+", con i la unidad imaginaria. El número Z es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(z)
    contenido_2 = Matematica(-z)
    contenido_3 = Matematica(-z.conjugate())
    contenido_4 = Matematica(abs(z))
    contenido_5 = Matematica(choice([z.re, z.im]))

enunciado_oculto = z










