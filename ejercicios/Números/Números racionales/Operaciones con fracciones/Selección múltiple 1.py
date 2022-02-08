{"cantidad_opciones":7, "cantidad_disponible":50}

if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    f1, f2, f3, f4 = Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11))
    while (f1.denominador==1 and f2.denominador==1 and f3.denominador==1) or f3+f4==0:
        f1, f2, f3, f4 = Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11))
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(fraccion(Pol(f1,f2), Pol(f3,f4))+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica((f1+f2)/(f3+f4))
    contenido_2 = Matematica((f1-f2)/(f3+f4))
    contenido_3 = Matematica((f1+f2)*(f3+f4))
    contenido_4 = Matematica((f1-f2)*(f3+f4))
    contenido_5 = Matematica((f1+f2)+(f3+f4))


elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    f1, f2, f3, f4, f5, f6 = Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11))
    while f1.denominador==1 or f2.denominador==1 or f3.denominador==1 or f6.denominador==1 or (f4+f5)*f6==0 or f4+f5*f6==0:
        f1, f2, f3, f4, f5, f6 = Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11))
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica("("+Pol(f1,f2)+por()+f3+"):(("+Pol(f4,f5)+")"+por()+f6+")=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica((f1+f2*f3)/((f4+f5)*f6))
    contenido_2 = Matematica(((f1+f2)*f3)/((f4+f5)*f6))
    contenido_3 = Matematica((f1+f2*f3)/(f4+f5*f6))
    contenido_4 = Matematica(((f1+f2)*f3)/(f4+f5*f6))
    contenido_5 = Matematica((f1+f2*f3)*((f4+f5)*f6))



elif opcion==3:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    f1, f2, f3, f4 = Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-10,10, -7,0,7),elegir(-10,10, 0),True), Racional(elegir(-12,13, 0),choice([2,4,5,6,8,9,10]),True)
    while f1.denominador==1 or f2.denominador==1 or f3.denominador==1 or f4.denominador==1:
        f1, f2, f3, f4 = Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-10,10, -7,0,7),elegir(-10,10, 0),True), Racional(elegir(-12,13, 0),choice([2,4,5,6,8,9,10]),True)
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(Pol(f1,f2,f3,f4,azar=True)+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(f1+f2+f3+f4)
    contenido_2 = Matematica(f1*f2*f3*f4)
    contenido_3 = Matematica(f1/f2/f3/f4)
    contenido_4 = Matematica(f1-f2-f3-f4)
    contenido_5 = Matematica(f1-f2+f3-f4)


elif opcion==4:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    f1, f2, f3, f4 = Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11))
    while [f1.denominador==1,f2.denominador==1,f3.denominador,f4.denominador].count(1) != 1 or f3+f4==0:
        f1, f2, f3, f4 = Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11))
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(Pol(f1,f2,parentesis=True).show+Pol(f3,f4,parentesis=True).show+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica((f1+f2)*(f3+f4))
    contenido_2 = Matematica(f1+(f2*f3)+f4)
    contenido_3 = Matematica(f1*f2*f3*f4)
    contenido_4 = Matematica(f1+f2+f3+f4)
    contenido_5 = Matematica((f1+f2)/(f3+f4))




elif opcion==5:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    f1, f2, f3 = Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11))
    while [f1.denominador==1,f2.denominador==1,f3.denominador].count(1) != 0:
        f1, f2, f3 = Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11))
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(f1+":"+f2+":"+f3+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(f1/f2/f3)
    contenido_2 = Matematica(f1/f2*f3)
    contenido_3 = Matematica(f1*f2*f3)
    contenido_4 = Matematica(f1*f2/f3)
    contenido_5 = Matematica(f1/(f2/f3))



elif opcion==6:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    f1, f2, f3, f4, f5, f6, f7 = Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11))
    while f1.denominador==1 or f2.denominador==1 or f3.denominador==1 or f4.denominador==1 or f5.denominador==1 or f6.denominador==1 or f7.denominador==1 or f3+f4==0 or f3+f4==0 or f2/(f3+f4)+f5*(f6+f7)==0 or f6+f7==0 or f2/(f3+f4)+f5/(f6+f7)==0:
        f1, f2, f3, f4, f5, f6, f7 = Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11)), Racional(elegir(-12,13, 0),elegir(2,11))
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(fraccion(f1,Pol(f2+":"+Pol(f3,f4,parentesis=True).show,Term(f5,Pol(f6,f7,parentesis=True).show)))+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(f1/(f2/(f3+f4)+f5*(f6+f7)))
    contenido_2 = Matematica(f1*(f2/(f3+f4)+f5*(f6+f7)))
    contenido_3 = Matematica(f1*(f2*(f3+f4)+f5*(f6+f7)))
    contenido_4 = Matematica(f1/(f2/(f3+f4)+f5/(f6+f7)))
    contenido_5 = Matematica(f1*(f2/(f3+f4)+f5/(f6+f7)))



elif opcion==7:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    f1, f2, f3, f4 = Racional(elegir(3,20),elegir(2,19)), Racional(elegir(3,20),elegir(2,19)), Racional(elegir(3,20),elegir(2,19)), Racional(elegir(3,20),elegir(2,19))
    while f1.denominador==1 or f2.denominador==1 or f3.denominador==1 or f4.denominador==1 or f1.numerador<=f1.denominador or f2.numerador<=f2.denominador or f3.numerador<=f3.denominador or f4.numerador<=f4.denominador or f3+f4==0:
        f1, f2, f3, f4 = Racional(elegir(3,20),elegir(2,19)), Racional(elegir(3,20),elegir(2,19)), Racional(elegir(3,20),elegir(2,19)), Racional(elegir(3,20),elegir(2,19))
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(fraccion(Pol(f1.show_mixto,f2.show_mixto).show,Pol(f3.show_mixto,f4.show_mixto).show)+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(((f1+f2)/(f3+f4)).show_mixto)
    contenido_2 = Matematica(((f1+f2)*(f3+f4)).show_mixto)
    contenido_3 = Matematica((f1+f2+f3+f4).show_mixto)
    contenido_4 = Matematica(abs((f1+f2)-(f3+f4)).show_mixto)
    contenido_5 = Matematica((abs(f1-f2)*(f3+f4)).show_mixto)



enunciado_oculto = enunciado











