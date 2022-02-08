{"cantidad_opciones":1, "cantidad_disponible":50}

letra = choice(["x","z"])

suma_de_numeros_sin_letra = 0
polinomio_de_terminos_sin_letra = []
for i in range(0, randrange(1,5)):
    numero = elegir(-9,9, 0)
    suma_de_numeros_sin_letra += Racional(numero)
    polinomio_de_terminos_sin_letra.append(numero)
while suma_de_numeros_sin_letra==0:
    suma_de_numeros_sin_letra = 0
    polinomio_de_terminos_sin_letra = []
    for i in range(0, randrange(1,5)):
        numero = elegir(-9,9, 0)
        suma_de_numeros_sin_letra += Racional(numero)
        polinomio_de_terminos_sin_letra.append(numero)

suma_de_numeros_con_letra = 0
polinomio_de_terminos_con_letra = []
for i in range(0, randrange(2,5)):
    numero = elegir(-9,9, 0)
    suma_de_numeros_con_letra += numero
    polinomio_de_terminos_con_letra.append(Term(numero, letra))
while suma_de_numeros_con_letra==0 or -suma_de_numeros_sin_letra*suma_de_numeros_con_letra<0:
    suma_de_numeros_con_letra = 0
    polinomio_de_terminos_con_letra = []
    for i in range(0, randrange(2,5)):
        numero = elegir(-9,9, 0)
        suma_de_numeros_con_letra += numero
        polinomio_de_terminos_con_letra.append(Term(numero, letra))


while (-suma_de_numeros_sin_letra/suma_de_numeros_con_letra).denominador!=1:
    suma_de_numeros_sin_letra = 0
    polinomio_de_terminos_sin_letra = []
    for i in range(0, randrange(1,5)):
        numero = elegir(-9,9, 0)
        suma_de_numeros_sin_letra += Racional(numero)
        polinomio_de_terminos_sin_letra.append(numero)
    while suma_de_numeros_sin_letra==0:
        suma_de_numeros_sin_letra = 0
        polinomio_de_terminos_sin_letra = []
        for i in range(0, randrange(1,5)):
            numero = elegir(-9,9, 0)
            suma_de_numeros_sin_letra += Racional(numero)
            polinomio_de_terminos_sin_letra.append(numero)

    suma_de_numeros_con_letra = 0
    polinomio_de_terminos_con_letra = []
    for i in range(0, randrange(2,5)):
        numero = elegir(-9,9, 0)
        suma_de_numeros_con_letra += numero
        polinomio_de_terminos_con_letra.append(Term(numero, letra))
    while suma_de_numeros_con_letra==0 or -suma_de_numeros_sin_letra*suma_de_numeros_con_letra<0:
        suma_de_numeros_con_letra = 0
        polinomio_de_terminos_con_letra = []
        for i in range(0, randrange(2,5)):
            numero = elegir(-9,9, 0)
            suma_de_numeros_con_letra += numero
            polinomio_de_terminos_con_letra.append(Term(numero, letra))



#================================Aquí va el enunciado================================================================
enunciado = fr"""¿Cuál es el valor de {letra} que satisface la siguiente ecuación?
\begin{{center}}
{Matematica(ecuacion_azar(lista_de_terminos=polinomio_de_terminos_con_letra+polinomio_de_terminos_sin_letra))}
\end{{center}}"""
#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(-suma_de_numeros_sin_letra/suma_de_numeros_con_letra)
contenido_2 = Matematica(suma_de_numeros_sin_letra/suma_de_numeros_con_letra)
contenido_3 = Matematica(-suma_de_numeros_sin_letra*suma_de_numeros_con_letra)
contenido_4 = Matematica(suma_de_numeros_sin_letra*suma_de_numeros_con_letra)
contenido_5 = Matematica(choice([-1,1])*suma_de_numeros_con_letra/suma_de_numeros_sin_letra)


enunciado_oculto = [polinomio_de_terminos_sin_letra, polinomio_de_terminos_con_letra]











