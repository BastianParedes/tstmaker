{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
f = Racional(randrange(3, 100), randrange(2, 10))
while f<1 or f.denominador==1:
    f = Racional(randrange(3, 100), randrange(2, 10))
n = f.numerador
d = f.denominador
p = int(f.parte_entera)
r = f.resto

#================================Aquí va el enunciado================================================================
enunciado = Matematica(f.show_mixto+"=")

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(fraccion(n,d))
contenido_2 = Matematica(fraccion(p*d, d))
contenido_3 = Matematica(fraccion(p*n+d, d))
contenido_4 = Matematica(fraccion(abs(p*d-n), d))
contenido_5 = Matematica(fraccion(n*d+p, d))



enunciado_oculto = [n,d]











