{"cantidad_opciones":6, "cantidad_disponible":50}


if opcion==1:
    #===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
    a, b, c, d = Racional(randrange(10, 100)), Racional(randrange(20, 40)), Racional(randrange(10, 100)), Racional(randrange(10, 100))
    while a==0 or c*d>b or c>b or a-b-c*d<0:
        a, b, c, d = Racional(randrange(100, 1000)), Racional(randrange(200, 400)), Racional(randrange(10, 100)), Racional(randrange(10, 100))
    #===============================================Aquí va el número del ejercicio y el enunciado.
    enunciado = Matematica(f"{a}+({b}-{c}{por()}{d})=")
    #===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
    contenido_correcto = Matematica(a+(b-c*d))
    contenido_2 = Matematica(a+((b-c)*d))
    contenido_3 = Matematica(c*d)
    contenido_4 = Matematica(a-b-c*d)
    contenido_5 = Matematica((a+b-c)*d)

elif opcion==2:
    #===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
    a, b, c, d = Racional(randrange(10, 100)), Racional(randrange(10, 100)), Racional(randrange(2, 15)), Racional(randrange(10, 100))
    while a<b+d or a<b:
        a, b, c, d = Racional(randrange(10, 100)), Racional(randrange(10, 100)), Racional(randrange(2, 15)), Racional(randrange(10, 100))
    #===============================================Aquí va el número del ejercicio y el enunciado.
    enunciado = Matematica(f"{a}-({b*c}:{c}+{d})=")
    #===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
    contenido_correcto = Matematica(a-(b+d))
    contenido_2 = Matematica(a-b)
    contenido_3 = Matematica(a-(round(b*c/(c+d))))
    contenido_4 = Matematica(b+d)
    contenido_5 = Matematica(a+b+d)

elif opcion==3:
    #===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
    a, b, c, d = Racional(randrange(1, 10)), Racional(randrange(1, 100)), Racional(randrange(1, 10)), Racional(randrange(1, 10))
    #===============================================Aquí va el número del ejercicio y el enunciado.
    enunciado = Matematica(f"{a}{por()}({b}+{c*d}:{d})=")
    #===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
    contenido_correcto = Matematica(a*(b+c))
    contenido_2 = Matematica(c)
    contenido_3 = Matematica(b+c)
    contenido_4 = Matematica(a*b+c)
    contenido_5 = Matematica(a+b+c)


elif opcion==4:
    #===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
    a, b, c, d = Racional(randrange(1, 100)), Racional(randrange(1, 100)), Racional(randrange(1, 100)), Racional(randrange(1, 10))
    while a-b*c<0 or a-(b*c+d)<0 or a-(b*c+d)==a+b*c+d or a-(b*c+d)==a+b*c+d:
        a, b, c, d = Racional(randrange(1, 100)), Racional(randrange(1, 100)), Racional(randrange(1, 100)), Racional(randrange(1, 10))
    #===============================================Aquí va el número del ejercicio y el enunciado.
    enunciado = Matematica(f"{a}-{b}{por()}{c}+{d}=")
    #===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
    contenido_correcto = Matematica(a-b*c+d)
    contenido_2 = Matematica(b*c)
    contenido_3 = Matematica((abs(a-b))*c+d)
    contenido_4 = Matematica(a-(b*c+d))
    contenido_5 = Matematica(a+b*c+d)

elif opcion==5:
    #===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
    a, b, c, d = Racional(randrange(1, 100)), Racional(randrange(1, 100)), Racional(randrange(1, 100)), Racional(randrange(1, 100))
    while a-b<0 or a-b*c<0 or a*c-b*d<0:
        a, b, c, d = Racional(randrange(1, 100)), Racional(randrange(1, 100)), Racional(randrange(1, 100)), Racional(randrange(1, 100))
    #===============================================Aquí va el número del ejercicio y el enunciado.
    enunciado = Matematica(f"({a}-{b}){por()}({c}+{d})=")
    #===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
    contenido_correcto = Matematica((a-b)*(c+d))
    contenido_2 = Matematica(a-b*c+d)
    contenido_3 = Matematica(a+b*c+d)
    contenido_4 = Matematica(a*c+b*d)
    contenido_5 = Matematica(a*c-b*d)

elif opcion==6:
    #===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
    a, b, c, d, e = Racional(randrange(1, 100)), Racional(randrange(1, 100)), Racional(randrange(1, 100)), Racional(randrange(1, 100)), Racional(randrange(1, 7))
    while a*b+c-d<0 or ((a*b+c-d*e)/e).denominador!=1 or b+c-d<0 or a*b+c-d==(a*b+c-d*e)/e:
        a, b, c, d, e = Racional(randrange(1, 100)), Racional(randrange(1, 100)), Racional(randrange(1, 100)), Racional(randrange(1, 100)), Racional(randrange(1, 7))
    #===============================================Aquí va el número del ejercicio y el enunciado.
    enunciado = Matematica(f"{a}{por()}{b}+{c}-{d*e}:{e}=")
    #===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
    contenido_correcto = Matematica(a*b+c-d)
    contenido_2 = Matematica((a*b+c-d*e)/e)
    contenido_3 = Matematica(abs(a*(b+c)-d))
    contenido_4 = Matematica(a*(b+c-d))
    contenido_5 = Matematica(a*b+c)




enunciado_oculto = enunciado










