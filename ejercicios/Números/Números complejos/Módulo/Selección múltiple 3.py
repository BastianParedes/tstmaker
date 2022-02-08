{"cantidad_opciones":2, "cantidad_disponible":2}

if opcion==1:#PSU 2020 ejercicio 17
    #================================Aquí va el enunciado================================================================
    enunciado = r"Sea el número complejo $\mathrm{z=a+bi}$, con a y b números reales distintos de cero, tal que $\mathrm{a>b}$. Se puede determinar los valores de a y b, si se sabe que:"
    #================================Aquí están los contenidos de las informaciones. También la alternativa correcta=====
    informacion_1 = r"$\sqrt{13}$ es el módulo de z."
    informacion_2 = r"a y b son números enteros y $\mathrm{a+b=5}$"
    alternativa_correcta = "C"


elif opcion==2:#Propio
    #================================Aquí va el enunciado================================================================
    enunciado = r"Sean z y w números complejos distintos de 0. Se puede determinar que el módulo de w es igual a 1 si:"
    #================================Aquí están los contenidos de las informaciones. También la alternativa correcta=====
    informacion_1 = Matematica("w="+fraccion("z","|z|"))
    informacion_2 = Matematica(fraccion("|w|","|z|")+"=1")
    alternativa_correcta = "A"















