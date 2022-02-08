{"cantidad_opciones":3, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b, c, d = Racional(randrange(2, 7)), Racional(randrange(2, 7)), Racional(randrange(2, 7)), Racional(randrange(2, 7))
while a==b:
    a, b = Racional(randrange(2, 7)), Racional(randrange(2, 7))

if opcion==1:
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(raiz(raiz("x",a),b)+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(raiz("x",a*b))
    contenido_2 = Matematica(raiz("x",a+b))
    contenido_3 = Matematica(raiz("x",a-b))
    contenido_4 = Matematica(raiz("x",-a+b))
    contenido_5 = Matematica(raiz("x",Racional(b,a,True)))


elif opcion==2:
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(raiz(raiz(raiz("x",a),b),c)+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(raiz("x",a*b*c))
    contenido_2 = Matematica(raiz("x",a+b+c))
    contenido_3 = Matematica(raiz("x",a-b-c))
    contenido_4 = Matematica(raiz("x",-a+b+c))
    contenido_5 = Matematica(raiz("x",Racional(c/b/a,1,True)))


elif opcion==3:
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(raiz(raiz(raiz(raiz("x",a),b),c),d)+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(raiz("x",a*b*c*d))
    contenido_2 = Matematica(raiz("x",a+b+c+d))
    contenido_3 = Matematica(raiz("x",a-b-c-d))
    contenido_4 = Matematica(raiz("x",-a+b+c+d))
    contenido_5 = Matematica(raiz("x",Racional(d/c/b/a,1,True)))

enunciado_oculto = enunciado










