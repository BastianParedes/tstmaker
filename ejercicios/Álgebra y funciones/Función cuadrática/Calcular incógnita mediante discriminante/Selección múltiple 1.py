{"cantidad_opciones":4, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b, c = Racional(randrange(-5, 6)), Racional(randrange(-5, 6)), Racional(randrange(-5, 6))
while a==0 or c==0:
    a, b, c = Racional(randrange(-5, 6)), Racional(randrange(-5, 6)), Racional(randrange(-5, 6))

if opcion==1:
    #================================Aquí va el enunciado================================================================
    enunciado = "La parábola que está asociada a la función "+ Matematica("f(x)="+Pol(a*{"x":2},b*"x",c,"k",azar=True)) +" intersecta al eje X en un único punto. El valor de k es"

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica((b**2-4*a*c)/(4*a))
    contenido_2        = Matematica((b**2)/(4*a*c))
    contenido_3        = Matematica((b**2-4*a*c)/(2*a))
    contenido_4        = Matematica((b**2+4*a*c)/(2*a))
    contenido_5        = Matematica((4*a*c-b**2)/(4*a))



elif opcion==2:
    #================================Aquí va el enunciado================================================================
    enunciado = "La parábola que está asociada a la función "+ Matematica(f"f(x)=({Pol(a,'k',azar=True)})"+Pol({"x":2},b*"x",c)) +" intersecta al eje X en un único punto. El valor de k es"

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica((b**2-4*a*c)/(4*a))
    contenido_2        = Matematica((b**2)/(4*a*c))
    contenido_3        = Matematica((b**2-4*a*c)/(2*a))
    contenido_4        = Matematica((b**2+4*a*c)/(2*a))
    contenido_5        = Matematica((4*a*c-b**2)/(4*a))



elif opcion==3:
    #================================Aquí va el enunciado================================================================
    enunciado = "La parábola que está asociada a la función "+ Matematica("f(x)="+Pol(a*{"k":1,"x":2},b*"x",c,azar=True)) +" intersecta al eje X en un único punto. El valor de k es"

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica((b**2)/(4*a*c))
    contenido_2        = Matematica((b**2-4*a*c)/(4*a))
    contenido_3        = Matematica((b**2-4*a*c)/(2*a))
    contenido_4        = Matematica((b**2+4*a*c)/(2*a))
    contenido_5        = Matematica((4*a*c-b**2)/(4*a))



elif opcion==4:
    #================================Aquí va el enunciado================================================================
    enunciado = "La parábola que está asociada a la función "+ Matematica("f(x)="+Pol(a*{"x":2},b*"x",c*"k",azar=True)) +" intersecta al eje X en un único punto. El valor de k es"

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica((b**2)/(4*a*c))
    contenido_2        = Matematica((b**2-4*a*c)/(4*a))
    contenido_3        = Matematica((b**2-4*a*c)/(2*a))
    contenido_4        = Matematica((b**2+4*a*c)/(2*a))
    contenido_5        = Matematica((4*a*c-b**2)/(4*a))



enunciado_oculto = enunciado










