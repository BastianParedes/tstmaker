{"cantidad_opciones":3, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b, c, d = Racional(randrange(2, 7)), Racional(randrange(2, 7)), Racional(randrange(2, 7)), Racional(randrange(2, 7))
while a==b:
    a, b = Racional(randrange(2, 7)), Racional(randrange(2, 7))

if opcion==1:
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(potencia(potencia("x",a),b)+"=")

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(potencia("x",a*b,quitar_1=True))
    contenido_2 = Matematica(potencia("x",a+b,quitar_1=True))
    contenido_3 = Matematica(potencia("x",a-b,quitar_1=True))
    contenido_4 = Matematica(potencia("x",-a+b,quitar_1=True))
    contenido_5 = Matematica(potencia("x",Racional(b,a,True),quitar_1=True))


elif opcion==2:
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(potencia(potencia(potencia("x",a),b),c)+"=")

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(potencia("x",a*b*c,quitar_1=True))
    contenido_2 = Matematica(potencia("x",a+b+c,quitar_1=True))
    contenido_3 = Matematica(potencia("x",a-b-c,quitar_1=True))
    contenido_4 = Matematica(potencia("x",-a+b+c,quitar_1=True))
    contenido_5 = Matematica(potencia("x",Racional(c/b/a,1,True),quitar_1=True))


elif opcion==3:
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(potencia(potencia(potencia(potencia("x",a),b),c),d)+"=")

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(potencia("x",a*b*c*d,quitar_1=True))
    contenido_2 = Matematica(potencia("x",a+b+c+d,quitar_1=True))
    contenido_3 = Matematica(potencia("x",a-b-c-d,quitar_1=True))
    contenido_4 = Matematica(potencia("x",-a+b+c+d,quitar_1=True))
    contenido_5 = Matematica(potencia("x",Racional(d/c/b/a,1,True),quitar_1=True))

enunciado_oculto = enunciado










