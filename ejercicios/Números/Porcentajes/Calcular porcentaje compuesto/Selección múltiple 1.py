{"cantidad_opciones":2, "cantidad_disponible":50}


if opcion==1:
    #===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
    p1, p2 = Racional(choice([2,5,10,15,20,25,30,35,40,50,60,70,75,80,90,100])), Racional(choice([2,5,10,15,20,25,30,35,40,50,60,70,75,80,90,100]))
    n = Racional(randrange(25,300)*2)
    #===============================================Aquí va el número del ejercicio y el enunciado.
    enunciado = fr"El {Matematica(p1)}\% del {Matematica(p2)}\% de {Matematica(n)} es"
    #===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
    contenido_correcto = Matematica(p1*p2*n/10000)
    contenido_2 = Matematica(p1*n/100)
    contenido_3 = Matematica(p2*n/n*100)
    contenido_4 = Matematica(p1*p2/(n*10000))
    contenido_5 = Matematica(p1*p2*n)



elif opcion==2:
    #===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
    p1, p2, p3 = Racional(choice([2,5,10,15,20,25,30,35,40,50,60,70,75,80,90,100])), Racional(choice([2,5,10,15,20,25,30,35,40,50,60,70,75,80,90,100])), Racional(choice([2,5,10,15,20,25,30,35,40,50,60,70,75,80,90,100]))
    n = Racional(randrange(25,300)*2)
    #===============================================Aquí va el número del ejercicio y el enunciado.
    enunciado = fr"El {Matematica(p1)}\% del {Matematica(p2)}\%  del {Matematica(p3)}\% de {Matematica(n)} es"
    #===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
    contenido_correcto = Matematica(p1*p2*p3*n/1000000)
    contenido_2 = Matematica(p1*n/100)
    contenido_3 = Matematica(p2*n/100)
    contenido_4 = Matematica(p3*n/100)
    contenido_5 = Matematica(p1*p2*n)



enunciado_oculto = enunciado











