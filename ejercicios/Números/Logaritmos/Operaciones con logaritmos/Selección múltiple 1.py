{"cantidad_opciones":3, "cantidad_disponible":50}


if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    base, exponente_de_base, exponente_de_argumento = Racional(randrange(1,6),randrange(1,3)), Racional(randrange(1,5),randrange(1,3)), Racional(randrange(1,5),randrange(1,3))
    while base**exponente_de_base==0 or base**exponente_de_base==1:
        base, exponente_de_base, exponente_de_argumento = Racional(randrange(1,6),randrange(1,3)), Racional(randrange(1,5),randrange(1,3)), Racional(randrange(1,5),randrange(1,3))
    log_1 = Log(base**exponente_de_argumento, base**exponente_de_base)

    base, exponente_de_base, exponente_de_argumento = Racional(randrange(1,6),randrange(1,3)), Racional(randrange(1,5),randrange(1,3)), Racional(randrange(1,5),randrange(1,3))
    while base**exponente_de_base==0 or base**exponente_de_base==1:
        base, exponente_de_base, exponente_de_argumento = Racional(randrange(1,6),randrange(1,3)), Racional(randrange(1,5),randrange(1,3)), Racional(randrange(1,5),randrange(1,3))
    log_2 = Log(base**exponente_de_argumento, base**exponente_de_base)

    a_1, a_2 = Racional(elegir(-5,6,0)), Racional(elegir(-5,6,0))

    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(Pol(a_1*log_1.show, a_2*log_2.show+"="))
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(a_1*log_1.valor + a_2*log_2.valor)
    contenido_2 =        Matematica(a_1*log_1.valor**(-1) + a_2*log_2.valor)
    contenido_3 =        Matematica(a_1*log_1.valor + a_2*log_2.valor**(-1))
    contenido_4 =        Matematica(a_1*log_1.valor**(-1) + a_2*log_2.valor**(-1))
    contenido_5 =        Matematica(a_1*log_1.valor - a_2*log_2.valor)
    enunciado_oculto = [opcion,log_1.valor,log_2.valor]


elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    base, exponente_de_base, exponente_de_argumento = Racional(randrange(1,6),randrange(1,3)), Racional(randrange(1,5)), Racional(randrange(1,5))
    while base**exponente_de_base==0 or base**exponente_de_base==1:
        base, exponente_de_base, exponente_de_argumento = Racional(randrange(1,6),randrange(1,3)), Racional(randrange(1,5)), Racional(randrange(1,5))
    log_1 = Log(base**exponente_de_argumento, base**exponente_de_base)

    base, exponente_de_base, exponente_de_argumento = Racional(randrange(1,6),randrange(1,3)), Racional(randrange(1,5)), Racional(randrange(1,5))
    while base**exponente_de_base==0 or base**exponente_de_base==1:
        base, exponente_de_base, exponente_de_argumento = Racional(randrange(1,6),randrange(1,3)), Racional(randrange(1,5)), Racional(randrange(1,5))
    log_2 = Log(base**exponente_de_argumento, base**exponente_de_base)

    base, exponente_de_base, exponente_de_argumento = Racional(randrange(1,6),randrange(1,3)), Racional(randrange(1,5)), Racional(randrange(1,5))
    while base**exponente_de_base==0 or base**exponente_de_base==1:
        base, exponente_de_base, exponente_de_argumento = Racional(randrange(1,6),randrange(1,3)), Racional(randrange(1,5)), Racional(randrange(1,5))
    log_3 = Log(base**exponente_de_argumento, base**exponente_de_base)

    a_1, a_2, a_3 = Racional(elegir(-5,6,0)), Racional(elegir(-5,6,0)), Racional(elegir(-5,6,0))

    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(Pol(a_1*log_1.show, a_2*log_2.show, a_3*log_3.show+"="))
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(a_1*log_1.valor + a_2*log_2.valor + a_3*log_3.valor)
    contenido_2 =        Matematica(a_1*log_1.valor**(-1) + a_2*log_2.valor + a_3*log_3.valor)
    contenido_3 =        Matematica(a_1*log_1.valor + a_2*log_2.valor**(-1) + a_3*log_3.valor)
    contenido_4 =        Matematica(a_1*log_1.valor + a_2*log_2.valor + a_3*log_3.valor**(-1))
    contenido_5 =        Matematica(a_1*log_1.valor**(-1) + a_2*log_2.valor**(-1) + a_3*log_3.valor**(-1))
    enunciado_oculto = [opcion,log_1.valor,log_2.valor,log_3.valor]


elif opcion==3:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a,b,c,d,e = Racional(randrange(2,8)), Racional(randrange(1,5)), Racional(randrange(1,5)), Racional(randrange(2,8)), Racional(randrange(1,5))
    while d in[0,1] or a**c in[0,1] or a**b in[0,1] or d**e in[0,1]:
        a,b,c,d,e = Racional(randrange(2,8)), Racional(randrange(1,5)), Racional(randrange(1,5)), Racional(randrange(2,8)), Racional(randrange(1,5))
    log_1, log_2 = Log(a**b,a**c), Log(d**e,d)
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(choice([logaritmo(a**b,d)+por()+logaritmo(d**e,a**c),  logaritmo(d**e,a**c)+por()+logaritmo(a**b,d) ]))+"="
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(log_1.valor*log_2.valor)
    contenido_2 =        Matematica(a**b/(a**c)*d**e/d)
    contenido_3 =        Matematica(a**b/(a**c)+d**e/d)
    contenido_4 =        Matematica(log_1.valor-log_2.valor)
    contenido_5 =        Matematica(log_1.valor**log_2.valor)
    enunciado_oculto = [log_1.valor,log_2.valor]



# elif opcion==4:
#     #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========

#     #================================Aquí va el enunciado================================================================
#     enunciado = 
#     #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
#     contenido_correcto = Matematica()
#     contenido_2 =        Matematica()
#     contenido_3 =        Matematica()
#     contenido_4 =        Matematica()
#     contenido_5 =        Matematica()
#     enunciado_oculto = 



# elif opcion==5:
#     #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========

#     #================================Aquí va el enunciado================================================================
#     enunciado = 
#     #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
#     contenido_correcto = Matematica()
#     contenido_2 =        Matematica()
#     contenido_3 =        Matematica()
#     contenido_4 =        Matematica()
#     contenido_5 =        Matematica()
#     enunciado_oculto = 



# elif opcion==6:
#     #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========

#     #================================Aquí va el enunciado================================================================
#     enunciado = 
#     #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
#     contenido_correcto = Matematica()
#     contenido_2 =        Matematica()
#     contenido_3 =        Matematica()
#     contenido_4 =        Matematica()
#     contenido_5 =        Matematica()
#     enunciado_oculto = 



# elif opcion==7:
#     #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========

#     #================================Aquí va el enunciado================================================================
#     enunciado = 
#     #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
#     contenido_correcto = Matematica()
#     contenido_2 =        Matematica()
#     contenido_3 =        Matematica()
#     contenido_4 =        Matematica()
#     contenido_5 =        Matematica()
#     enunciado_oculto = 



# elif opcion==8:
#     #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========

#     #================================Aquí va el enunciado================================================================
#     enunciado = 
#     #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
#     contenido_correcto = Matematica()
#     contenido_2 =        Matematica()
#     contenido_3 =        Matematica()
#     contenido_4 =        Matematica()
#     contenido_5 =        Matematica()
#     enunciado_oculto = 



# elif opcion==9:
#     #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========

#     #================================Aquí va el enunciado================================================================
#     enunciado = 
#     #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
#     contenido_correcto = Matematica()
#     contenido_2 =        Matematica()
#     contenido_3 =        Matematica()
#     contenido_4 =        Matematica()
#     contenido_5 =        Matematica()
#     enunciado_oculto = 



# elif opcion==10:
#     #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========

#     #================================Aquí va el enunciado================================================================
#     enunciado = 
#     #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
#     contenido_correcto = Matematica()
#     contenido_2 =        Matematica()
#     contenido_3 =        Matematica()
#     contenido_4 =        Matematica()
#     contenido_5 =        Matematica()
#     enunciado_oculto = 












