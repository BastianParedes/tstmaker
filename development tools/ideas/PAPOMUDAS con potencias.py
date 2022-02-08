from Definiciones import *

opcion = choice([1,2,3,4,5,6])
opcion = choice([5])

if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c, d, e = racional(elegir(-10,10)), racional(elegir(-10,10,-1,1)), racional(elegir(1,10)), racional(elegir(2,5)), racional(elegir(-10,10))
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(pol(a, pol(b+por()+potencia(c,d), e, parentesis=True).show)+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(    a+b*c**d+e    )
    contenido_2 = Matematica(           a+(b*c)**d+e    )
    contenido_3 = Matematica(           (a+b)*c**d+e    )
    contenido_4 = Matematica(           (a+b*c)**d+e    )
    contenido_5 = Matematica(           (a+b)*(c+e)**d    )



elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c, d, e, f = racional(elegir(-10,10)), racional(elegir(1,10)), racional(elegir(2,5)), racional(elegir(1,10)), racional(elegir(1,10)), racional(elegir(1,10))
    b, e, = b*d, e*f
    b_signo = racional(choice([-1,1]))
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(pol(a, b_signo*potencia(b,c))+":"+pol(d, e*":")+f    +"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(a+b_signo*b**c/d+e/f)
    contenido_2 = Matematica(a-b_signo*b**c/d+e/f)
    contenido_3 = Matematica(   a+(b_signo*b/d)**c+e/f    )
    contenido_4 = Matematica(   (a+b_signo*b)**c/(d+e)/f    )
    contenido_5 = Matematica(   (a+b_signo*b)**c/d+e/f    )



elif opcion==3:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c, d, c_signo = racional(elegir(1,6)), racional(elegir(2,8)), racional(elegir(1,6)), racional(elegir(2,7)), racional(choice([-1,1]))
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(    pol(potencia(a,b), c_signo*potencia(c,d))     +"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(a**b+c_signo*c**d)
    contenido_2 = Matematica((a+c_signo*c)**b)
    contenido_3 = Matematica((a+c_signo*c)**d)
    contenido_4 = Matematica(a*b+c_signo*c*d)
    contenido_5 = Matematica(a**b-c_signo*c**d)



elif opcion==4:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c, d, e, f, g = racional(elegir(-10,10)), racional(elegir(2,10)), racional(elegir(2,5)), racional(elegir(0,10)), racional(elegir(-10,10)), racional(elegir(-10,10)), racional(elegir(1,10))
    f = f*g
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(pol(a, racional(-1)*(potencia(b,c)+por()+d), e, f*f":{g}"             )+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(a-b**c*d+e+f/g)
    contenido_2 = Matematica((a-b)**c*d+e+f/g)
    contenido_3 = Matematica(a+b**c*d+e+f/g)
    contenido_4 = Matematica(a-(b*d)**c+e+f/g)
    contenido_5 = Matematica(a-b**c*d+e+f)



elif opcion==5:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c, d = racional(elegir(-10,10)), racional(elegir(-10,10)), racional(elegir(1,10)), racional(elegir(1,10))
    b = b*c
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(potencia(pol(a, b*f":{c+por()+d}"),2)+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica((a+b/c*d)**2)
    contenido_2 = Matematica((a+b/c*d)*2)
    contenido_3 = Matematica((a+b/(c*d))**2)
    contenido_4 = Matematica((a+b/(c*d))*2)
    contenido_5 = Matematica(a+b/c*d)



elif opcion==6:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c, d, e, f, g = racional(elegir(-10,10)), racional(elegir(-10,10)), racional(elegir(-10,10)), racional(elegir(-10,10)), racional(elegir(-10,10)), racional(elegir(-10,10)), racional(elegir(-10,10))

    #================================Aquí va el enunciado================================================================
    enunciado = Matematica()

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica()
    contenido_2 = Matematica()
    contenido_3 = Matematica()
    contenido_4 = Matematica()
    contenido_5 = Matematica()



elif opcion==7:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c, d, e, f, g = racional(elegir(-10,10)), racional(elegir(-10,10)), racional(elegir(-10,10)), racional(elegir(-10,10)), racional(elegir(-10,10)), racional(elegir(-10,10)), racional(elegir(-10,10))

    #================================Aquí va el enunciado================================================================
    enunciado = Matematica()

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica()
    contenido_2 = Matematica()
    contenido_3 = Matematica()
    contenido_4 = Matematica()
    contenido_5 = Matematica()




enunciado_oculto = enunciado