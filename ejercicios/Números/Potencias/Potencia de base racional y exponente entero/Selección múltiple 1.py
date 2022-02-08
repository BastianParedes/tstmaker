{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
while True:
    f = Racional(elegir(-10,11,0), elegir(-10,11,0))
    exponente = randrange(-4,5)
    a = Racional(choice([-1,1]))
    if f.denominador != 1:
        break


#================================Aquí va el enunciado================================================================
enunciado = Matematica(a*potencia(f,exponente)+"=")
#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(a*f**exponente)
contenido_2 =        Matematica(-a*f**exponente)#resultado negativo
contenido_3 =        Matematica(a*f**(-exponente))# invierte la fracción, o lo hace cuando no corresponde
contenido_4 =        Matematica(-a*f**(-exponente))#resultado negativo. invierte la fracción, o lo hace cuando no corresponde
contenido_5 =        Matematica(a  *  Racional(f.numerador)**exponente / f.denominador)



if exponente in [0,1]:
    enunciado_oculto = [0,1]
else:
    enunciado_oculto = [a, f, exponente]










