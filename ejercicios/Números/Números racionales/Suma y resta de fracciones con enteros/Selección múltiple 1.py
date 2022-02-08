{"cantidad_opciones":4, "cantidad_disponible":50}

a, b, c, d = Racional(choice(list(range(-10, 0))+list(range(2, 11)))), Racional(choice(list(range(-10, 0))+list(range(2, 11)))), Racional(choice(list(range(-10, 0))+list(range(2, 11)))), Racional(choice(list(range(-10, 0))+list(range(2, 11))))
while (a/b).denominador==1 or a/b==c/d or abs(b)==abs(d):
    a, b, c, d = Racional(choice(list(range(-10, 0))+list(range(2, 11)))), Racional(choice(list(range(-10, 0))+list(range(2, 11)))), Racional(choice(list(range(-10, 0))+list(range(2, 11)))), Racional(choice(list(range(-10, 0))+list(range(2, 11))))


if opcion==1:
    if 0<a and 0<b and 0<c and 0<d:
        if a/b<c/d:
            #================================Aquí va el enunciado================================================================
            enunciado = Matematica(f"{fraccion(a,b)}-{fraccion(c,d)}=")

            #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
            contenido_correcto = Matematica(a/b-c/d)
            contenido_2 = Matematica(a/b+c/d)
            contenido_3 = Matematica((a-c)/(b-d))
            contenido_4 = Matematica((a-c)/(b+d))
            contenido_5 = Matematica((a-c)/(b*d))
        else:
            #================================Aquí va el enunciado================================================================
            enunciado = Matematica(f"{fraccion(c,d)}-{fraccion(a,b)}=")

            #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
            contenido_correcto = Matematica(c/d-a/b)
            contenido_2 = Matematica(c/d+a/b)
            contenido_3 = Matematica((c-a)/(d-b))
            contenido_4 = Matematica((c-a)/(d+b))
            contenido_5 = Matematica((c-a)/(d*b))
            
    else:
        #================================Aquí va el enunciado================================================================
        enunciado = Matematica(f"{fraccion(a,b)}-{fraccion(c,d)}=")

        #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
        contenido_correcto = Matematica(a/b-c/d)
        contenido_2 = Matematica(a/b+c/d)
        contenido_3 = Matematica((a-c)/(b-d))
        contenido_4 = Matematica((a-c)/(b+d))
        contenido_5 = Matematica((a-c)/(b*d))

elif opcion==2:
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(f"-{fraccion(a,b)}+{fraccion(c,d)}=")

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(-a/b+c/d)
    contenido_2 = Matematica(a/b+c/d)
    contenido_3 = Matematica((-a+c)/(-b+d))
    contenido_4 = Matematica((-a+c)/(b+d))
    contenido_5 = Matematica((-a+c)/(b*d))



elif opcion==3:
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(f"-{fraccion(a,b)}-{fraccion(c,d)}=")

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(-a/b-c/d)
    contenido_2 = Matematica(-a/b+c/d)
    contenido_3 = Matematica((-a-c)/(-b-d))
    contenido_4 = Matematica((-a-c)/(-b+d))
    contenido_5 = Matematica((-a-c)/(b*d))


elif opcion==4:
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(f"{fraccion(a,b)}+{fraccion(c,d)}=")

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(a/b+c/d)
    contenido_2 = Matematica(a/b-c/d)
    contenido_3 = Matematica((a+c)/(b-d))
    contenido_4 = Matematica((a+c)/(b+d))
    contenido_5 = Matematica((a+c)/(b*d))




enunciado_oculto = [a, b, c, d]










