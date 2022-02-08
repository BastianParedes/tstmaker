{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
n, b, i, e = Racional(randrange(2, 10)), Racional(randrange(2, 60)), Racional(randrange(3, 10)), Racional(randrange(2, 8))
while type(Root(b))==Racional or not e<i:
    n, b, i, e = Racional(randrange(2, 10)), Racional(randrange(2, 60)), Racional(randrange(3, 10)), Racional(randrange(2, 8))

#================================Aquí va el enunciado================================================================
enunciado = Matematica(fraccion(n,raiz(potencia(b,e),i))+"=")

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(fraccion(Racional(Racional(n,b).numerador)*raiz(potencia(b,i-e), i), Racional(n,b).denominador))
contenido_2 = Matematica(n*Root(b)/b)
contenido_3 = Matematica(fraccion(Racional(Racional(n,b).numerador)*raiz(potencia(b,e),i), Racional(n,b).denominador))
contenido_4 = Matematica(fraccion(Racional(Racional(n,b).numerador)*raiz(potencia(b,e),2), Racional(n,b).denominador))
contenido_5 = Matematica(fraccion(Racional(Racional(n,b).numerador)*raiz(potencia(b,i),e), Racional(n,b).denominador))

enunciado_oculto = [b,i,e]










