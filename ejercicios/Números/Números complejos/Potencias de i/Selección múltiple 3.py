{"cantidad_opciones":3, "cantidad_disponible":3}

if opcion==1:#PSU 2019 ejercicio 17
    #================================Aquí va el enunciado================================================================
    enunciado = "Sea n un número entero positivo mayor que 64, se puede determinar el valor del número complejo "+Matematica(Pol(1, "i", potencia("i",2), potencia("i",3), potencia("i",4), "...", potencia("i","n-1"), potencia("i","n")))+", si:"
    #================================Aquí están los contenidos de las informaciones. También la alternativa correcta=====
    informacion_1 = "n es un número par."
    informacion_2 = "Se conoce el resto al dividir n por 64."
    alternativa_correcta = "B"

elif opcion==2:#PSU 2018, ejercicio 17
    #================================Aquí va el enunciado================================================================
    enunciado = "Sean x e y números enteros e "+Matematica(potencia("i",2)+"=-1")+". La expresión "+Matematica(potencia(Pol(potencia("i","10x"),potencia("i","14x"),parentesis=True), "y",parentesis_automatico=False))+" representa un número real positivo, si se sabe que:"
    #================================Aquí están los contenidos de las informaciones. También la alternativa correcta=====
    informacion_1 = "x es un número par."
    informacion_2 = "y es un número par."
    alternativa_correcta = "D"

elif opcion==3:#PDV modificado
    #================================Aquí va el enunciado================================================================
    enunciado = r"$\mathrm{{\left({i}^{n+1}\right)}^{2} \cdot {i}^{m+1}}$ es igual a $-1$, si"
    #================================Aquí están los contenidos de las informaciones. También la alternativa correcta=====
    informacion_1 = r"$\mathrm{m+2n=0}$"
    informacion_2 = r"$\mathrm{m=2}$ y $\mathrm{n=\dfrac{1}{2}}$"
    alternativa_correcta = "B"












