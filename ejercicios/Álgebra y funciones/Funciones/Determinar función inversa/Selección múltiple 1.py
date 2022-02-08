{"cantidad_opciones":5, "cantidad_disponible":50}

letra = choice(["f", "g", "h"])

if opcion==1:#Funcion de la recta
    #===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
    m, n = Racional(elegir(-10,11, 0), randrange(1,11)), Racional(elegir(-10,11, 0))
    #===============================================Aquí va el número del ejercicio y el enunciado.
    enunciado = fr'Determina la inversa de la función {Matematica(letra+"(x)="+Pol(m*"x",n,azar=True))}'
    #===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
    contenido_correcto = Matematica(potencia(letra,-1)+"(x)="+Pol("x",-n)/m)
    contenido_2 = Matematica(potencia(letra,-1)+"(x)="+Pol("x",-n)*m)
    contenido_3 = Matematica(potencia(letra,-1)+"(x)="+Pol("x",n)/m)
    contenido_4 = Matematica(potencia(letra,-1)+"(x)="+Pol("x",n)*m)
    contenido_5 = Matematica(potencia(letra,-1)+"(x)="+Pol("x",choice([1,-1])*m)/n)

    enunciado_oculto = [opcion,m,n]



elif opcion==2:#Funcion cuadrática con b igual a 0
    #===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
    a, c = Racional(elegir(-10,11, 0)), Racional(elegir(-10,11))
    #===============================================Aquí va el número del ejercicio y el enunciado.
    enunciado = fr'Determina la inversa de la función {Matematica(letra+"(x)="+Pol(Term(a,{"x":2}),c,azar=True))}'
    #===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
    contenido_correcto = Matematica(potencia(letra,-1)+"(x)="+raiz(Pol("x",-c)/a))
    contenido_2 = Matematica(potencia(letra,-1)+"(x)="+raiz(Pol("x",c)/a))
    contenido_3 = Matematica(potencia(letra,-1)+"(x)="+raiz(Pol("x",-c)*a))
    contenido_4 = Matematica(potencia(letra,-1)+"(x)="+Pol("x",-c)*choice([a,a**(-1)]))
    contenido_5 = Matematica(potencia(letra,-1)+"(x)="+Pol("x",c)*choice([a,a**(-1)]))

    enunciado_oculto = [opcion,a,c]



elif opcion==3:#a/(bx+c)
    #===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
    a, b, c = Racional(elegir(-10,11, 0)), Racional(elegir(-10,11, 0)), Racional(elegir(-10,11))
    while a-c==0:
        a, b, c = Racional(elegir(-10,11, 0)), Racional(elegir(-10,11, 0)), Racional(elegir(-10,11))
    #===============================================Aquí va el número del ejercicio y el enunciado.
    enunciado = fr'Determina la inversa de la función {Matematica(letra+"(x)="+fraccion(a,Pol(b*"x",c,azar=True)))}'
    #===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
    contenido_correcto = Matematica(potencia(letra,-1)+"(x)="+choice([fraccion(Pol(-c*"x",a),b*"x"), Pol(-c*"x",a)/(b*"x")]))
    contenido_2 = Matematica(potencia(letra,-1)+"(x)="+choice([fraccion(Pol(c*"x",a),b*"x"), Pol(c*"x",a)/(b*"x")]))
    contenido_3 = Matematica(potencia(letra,-1)+"(x)="+choice([fraccion(Pol(-c*"x",a),-b*"x"), Pol(-c*"x",a)/(-b*"x")]))
    contenido_4 = Matematica(potencia(letra,-1)+"(x)="+choice([fraccion(Pol(c*"x",a),-b*"x"), Pol(c*"x",a)/(-b*"x")]))
    contenido_5 = Matematica(potencia(letra,-1)+"(x)="+choice([fraccion(Pol(-c*"x",-a),b*"x"), Pol(-c*"x",-a)/(b*"x")]))

    enunciado_oculto = [opcion,a,b,c]



elif opcion==4:#(ax+b)/(cx+d)
    #===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
    a, b, c, d = Racional(elegir(-10,11, 0)), Racional(elegir(-10,11, 0)), Racional(elegir(-10,11, 0)), Racional(elegir(-10,11, 0))
    while a*d==b*c:
        a, b, c, d = Racional(elegir(-10,11, 0)), Racional(elegir(-10,11, 0)), Racional(elegir(-10,11, 0)), Racional(elegir(-10,11, 0))
    #===============================================Aquí va el número del ejercicio y el enunciado.
    enunciado = fr'Determina la inversa de la función {Matematica(letra+"(x)="+fraccion(Pol(a*"x",b,azar=True),Pol(c*"x",d,azar=True)))}'
    #===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
    contenido_correcto = Matematica(potencia(letra,-1)+"(x)="+Pol(d*"x",-b)/Pol(-c*"x",a))
    contenido_2 = Matematica(potencia(letra,-1)+"(x)="+Pol(-c*"x",a)/Pol(d*"x",-b))
    contenido_3 = Matematica(potencia(letra,-1)+"(x)="+Pol(d*"x",b)/Pol(-c*"x",a))
    contenido_4 = Matematica(potencia(letra,-1)+"(x)="+Pol(d*"x",-b)/Pol(-c*"x",-a))
    contenido_5 = Matematica(potencia(letra,-1)+"(x)="+Pol(-d*"x",-b)/Pol(c*"x",a))

    enunciado_oculto = [opcion,a,b,c,d]



elif opcion==5:#a*sqrt(bx+c)+d
    #===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
    a, b, c, d = Racional(elegir(-10,11, 0)), Racional(elegir(-10,11, 0)), Racional(elegir(-10,11)), Racional(elegir(-10,11))
    #===============================================Aquí va el número del ejercicio y el enunciado.
    enunciado = fr'Determina la inversa de la función {Matematica(letra+"(x)="+Pol(a*raiz(Pol(b*"x",c,azar=True)),d,azar=True))}'
    #===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
    contenido_correcto = Matematica(potencia(letra,-1)+"(x)="+Pol(Term(1,{"x":2}),-2*d*"x",d**2-a**2*c)/(a**2*b))
    contenido_2 = Matematica(potencia(letra,-1)+"(x)="+       Pol(Term(1,{"x":2}),2*d*"x",d**2-a**2*c)/(-a**2*b))
    contenido_3 = Matematica(potencia(letra,-1)+"(x)="+       Pol(Term(1,{"x":2}),-2*d*"x",d-a**2*c)/(a**2*b))
    contenido_4 = Matematica(potencia(letra,-1)+"(x)="+       Pol(Term(1,{"x":2}),Term(-2,{"x":1}),d**2-a**2*c)/(a**2*b))
    contenido_5 = Matematica(potencia(letra,-1)+"(x)="+       Pol((2*d+1)*"x",d**2-c*a)/(a**2*b))

    enunciado_oculto = [opcion,a,b,c,d]











