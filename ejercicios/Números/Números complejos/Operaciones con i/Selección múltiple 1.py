{"cantidad_opciones":4, "cantidad_disponible":50}

if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    i = UnidadImaginaria()
    a, b, c = randrange(10, 101), randrange(10, 101), randrange(10, 101)
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(fraccion(Pol(potencia(i,a), potencia(i,b)), potencia(i, c))+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica((i**a+i**b/i**c))
    contenido_2 = Matematica((i**a+i**b+i**c))
    contenido_3 = Matematica((i**a-i**b/i**c))
    contenido_4 = Matematica((i**a+i**b-i**c))
    contenido_5 = Matematica((i**a-i**b)*i**c)

elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    i = UnidadImaginaria()
    a, b, c, d = Racional(elegir(-10, 10, 0)), Racional(elegir(-10, 10, 0)), randrange(10, 101), randrange(10, 101)
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(Pol(a*{"i":c}, b*{"i":d})+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(a*i**c+b*i**d)
    contenido_2 = Matematica(i**c+i**d)
    contenido_3 = Matematica((a+b)*i**(c+d))
    contenido_4 = Matematica(a*i**c)
    contenido_5 = Matematica(b*i**d)

elif opcion==3:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    i = UnidadImaginaria()
    a, b, c, d, e, f = Racional(elegir(-10, 10, 0)), Racional(elegir(-10, 10, 0)), Racional(elegir(-10, 10, 0)), randrange(10, 101), randrange(10, 101), randrange(10, 101)
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(Pol(a*{"i":d}, b*{"i":e}, c*{"i":f})+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(a*i**d+b*i**e+c*i**f)
    contenido_2 = Matematica(i**d+i**e+i**f)
    contenido_3 = Matematica((a+b+c)*i**(d+e+f))
    contenido_4 = Matematica(a+b+c)
    contenido_5 = Matematica(a*b*c)

elif opcion==4:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    i = UnidadImaginaria()
    a, b, c = randrange(10, 101), randrange(10, 101), randrange(10, 101)
    d, e, f = Racional(choice([-1,1])), Racional(choice([-1,1])), Racional(choice([-1,1]))
    while d==e==f==1 or e*i**b+f*i**c==0 or i**b+i**c==0:
        a, b, c = randrange(10, 101), randrange(10, 101), randrange(10, 101)
        d, e, f = Racional(choice([-1,1])), Racional(choice([-1,1])), Racional(choice([-1,1]))
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(fraccion(d*{"i":a}, Pol(e*{"i":b}, f*{"i":c}))+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(d*i**a/(e*i**b+f*i**c))
    contenido_2 = Matematica(i**a/(i**b+i**c))
    contenido_3 = Matematica(i**(a-b-c))
    contenido_4 = Matematica(3*i**(a-b-c))
    contenido_5 = Matematica(a+b+c)




enunciado_oculto = enunciado










