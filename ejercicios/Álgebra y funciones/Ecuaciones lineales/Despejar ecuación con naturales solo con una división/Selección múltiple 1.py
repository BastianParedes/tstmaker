{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b = Racional(randrange(2,10)), Racional(randrange(2,10))
#================================Aquí va el enunciado================================================================
enunciado = "El valor de x que satisface la ecuación "+choice([
    Matematica(a*"x"+"="+b),
    Matematica(b+"="+a*"x")
])+" es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(b/a)
contenido_2 =        Matematica(a/b)
contenido_3 =        Matematica(b-a)
contenido_4 =        Matematica(a-b)
contenido_5 =        Matematica(b+a)



enunciado_oculto = [a,b]











