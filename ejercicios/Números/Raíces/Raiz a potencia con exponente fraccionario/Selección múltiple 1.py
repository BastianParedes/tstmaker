{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
e, b = Racional(elegir(2, 10), elegir(2, 10)), elegir(2, 10)
while e.denominador==1:
    e = Racional(elegir(2, 10), elegir(2, 10))

#================================Aquí va el enunciado================================================================
enunciado = Matematica(raiz(potencia(b, e.numerador), e.denominador)+"=")

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(potencia(b, e))
contenido_2 = Matematica(potencia(b, e**(-1)))
contenido_3 = Matematica(potencia(b, e.numerador+e.denominador))
contenido_4 = Matematica(potencia(b, e.numerador*e.denominador))
contenido_5 = Matematica(potencia(b, e.numerador-e.denominador))



enunciado_oculto = [e, b]










