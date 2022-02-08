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
enunciado = Matematica(f+"=")

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(f.show_mixto)
contenido_2 = Matematica((p+Racional(n,d)).show_mixto)
contenido_3 = Matematica((p+Racional(n,r)).show_mixto)
contenido_4 = Matematica((n+Racional(p,d)).show_mixto)
contenido_5 = Matematica((n+Racional(r,d)).show_mixto)


enunciado_oculto = [n,d]











