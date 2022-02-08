{"cantidad_opciones":2, "cantidad_disponible":50}

x5 = "x"**Racional(5)
x4 = "x"**Racional(4)
x3 = "x"**Racional(3)
x2 = "x"**Racional(2)
x1 = "x"**Racional(1)

if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c = Racional(elegir(-4,5,0)), Racional(elegir(-4,5,0)), Racional(elegir(-4,5,0))
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(Pol(x3, (a+b+c)*x2, (b*c+a*c+a*b)*x1, a*b*c, azar=True)+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica("("+Pol("x",a)+")("+Pol("x",b)+")("+Pol("x",c)+")")
    contenido_2 = Matematica("("+Pol("x",a+b+c)+")("+Pol("x",b*c+a*c+a*b)+")("+Pol("x",a*b*c)+")")
    contenido_3 = Matematica(potencia(Pol("x",a*b*c),3))
    contenido_4 = Matematica("("+Pol("x",elegir(-4,5,0))+")("+Pol("x",elegir(-4,5,0))+")")
    contenido_5 = Matematica("("+Pol("x",elegir(-4,5,0))+")("+Pol("x",elegir(-4,5,0))+")("+Pol("x",elegir(-4,5,0))+")("+Pol("x",elegir(-4,5,0))+")")

elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c, d = Racional(elegir(-4,5,0)), Racional(elegir(-4,5,0)), Racional(elegir(-4,5,0)), Racional(elegir(-4,5,0))
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(Pol(x4, (a+b+c+d)*x3, (a*b+b*c+c*d+a*c+b*d+a*d)*x2, (b*c*d+a*c*d+a*b*d+a*b*c)*x1, a*b*c*d, azar=True)+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica("("+Pol("x",a)+")("+Pol("x",b)+")("+Pol("x",c)+")("+Pol("x",d)+")")
    contenido_2 = Matematica("("+Pol("x",a+b+c+d)+")("+Pol("x",a*b+b*c+c*d+a*c+b*d+a*d)+")("+Pol("x",b*c*d+a*c*d+a*b*d+a*b*c)+")("+Pol("x",a*b*c*d)+")")
    contenido_3 = Matematica(potencia(Pol("x",a*b*c*d),4))
    contenido_4 = Matematica("("+Pol("x",elegir(-4,5,0))+")("+Pol("x",elegir(-4,5,0))+")("+Pol("x",elegir(-4,5,0))+")")
    contenido_5 = Matematica("("+Pol("x",elegir(-4,5,0))+")("+Pol("x",elegir(-4,5,0))+")("+Pol("x",elegir(-4,5,0))+")("+Pol("x",elegir(-4,5,0))+")("+Pol("x",elegir(-4,5,0))+")")

elif opcion==3:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c, d, e = Racional(elegir(-4,5,0)), Racional(elegir(-4,5,0)), Racional(elegir(-4,5,0)), Racional(elegir(-4,5,0)), Racional(elegir(-4,5,0))
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(Pol(x5, (a+b+c+d+e)*x4, (a*b+b*c+c*d+a*c+b*d+a*d+a*e+b*e+c*e+d*e)*x3, (a*b*c+a*b*d+a*c*d+b*c*d+a*b*e+b*c*e+c*d*e+a*c*e+b*d*e+a*d*e)*x2, (b*c*d*e+a*c*d*e+a*b*d*e+a*b*c*e+a*b*c*d*e)*x1, a*b*c*d*e, azar=True)+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica("("+Pol("x",a)+")("+Pol("x",b)+")("+Pol("x",c)+")("+Pol("x",d)+")("+Pol("x",e)+")")
    contenido_2 = Matematica("("+Pol("x",a+b+c+d+e)+")("+Pol("x",a*b+b*c+c*d+a*c+b*d+a*d+a*e+b*e+c*e+d*e)+")("+Pol("x",a*b*c+a*b*d+a*c*d+b*c*d+a*b*e+b*c*e+c*d*e+a*c*e+b*d*e+a*d*e)+")("+Pol("x",b*c*d*e+a*c*d*e+a*b*d*e+a*b*c*e+a*b*c*d*e)+")("+Pol("x",a*b*c*d*e)+")")
    contenido_3 = Matematica(potencia(Pol("x",a*b*c*d*e),5))
    contenido_4 = Matematica("("+Pol("x",elegir(-4,5,0))+")("+Pol("x",elegir(-4,5,0))+")("+Pol("x",elegir(-4,5,0))+")("+Pol("x",elegir(-4,5,0))+")")
    contenido_5 = Matematica("("+Pol("x",elegir(-4,5,0))+")("+Pol("x",elegir(-4,5,0))+")("+Pol("x",elegir(-4,5,0))+")("+Pol("x",elegir(-4,5,0))+")("+Pol("x",elegir(-4,5,0))+")("+Pol("x",elegir(-4,5,0))+")")


enunciado_oculto = enunciado










