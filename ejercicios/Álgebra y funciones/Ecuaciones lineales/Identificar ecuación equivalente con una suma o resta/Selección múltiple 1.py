{"cantidad_opciones":2, "cantidad_disponible":50}

#===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
a, b, c = Racional(elegir(-10,11 ,0)), Racional(elegir(-10,11)), Racional(elegir(-5,6 ,0))
while a==b or a+c==0:
    a, b, c = Racional(elegir(-10,11 ,0)), Racional(elegir(-10,11)), Racional(elegir(-5,6 ,0))

c2i, c2d, c3i, c3d, c4i, c4d, c5i, c5d = Racional(elegir(-10,11)), Racional(elegir(-10,11)), Racional(elegir(-10,11)), Racional(elegir(-10,11)), Racional(elegir(-10,11)), Racional(elegir(-10,11)), Racional(elegir(-10,11)), Racional(elegir(-10,11))
while c2i==c2d or c3i==c3d or c4i==c4d or c5i==c5d:
    c2i, c2d, c3i, c3d, c4i, c4d, c5i, c5d = Racional(elegir(-10,11)), Racional(elegir(-10,11)), Racional(elegir(-10,11)), Racional(elegir(-10,11)), Racional(elegir(-10,11)), Racional(elegir(-10,11)), Racional(elegir(-10,11)), Racional(elegir(-10,11))

if opcion==1:
    #===============================================Aquí va el número del ejercicio y el enunciado.
    enunciado = f"¿Cuál de las siguientes ecuaciones puede obtenerse a partir de la ecuación {Matematica(Pol('x',a)+'='+b)}?"
    #===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
    contenido_correcto = Matematica(Pol('x',a+c)+'='+(b+c))
    contenido_2 = Matematica(Pol('x',a+c2i)+'='+(b+c2d))
    contenido_3 = Matematica(Pol('x',a+c3i)+'='+(b+c3d))
    contenido_4 = Matematica(Pol('x',a+c4i)+'='+(b+c4d))
    contenido_5 = Matematica(Pol('x',a+c5i)+'='+(b+c5d))


elif opcion==2:
    #===============================================Aquí va el número del ejercicio y el enunciado.
    enunciado = f"¿Cuál de las siguientes ecuaciones puede obtenerse a partir de la ecuación {Matematica(b+'='+Pol('x',a))}?"
    #===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
    contenido_correcto = Matematica(b+c+'='+Pol('x',a+c))
    contenido_2 = Matematica(b+c2i+'='+Pol('x',a+c2d))
    contenido_3 = Matematica(b+c3i+'='+Pol('x',a+c3d))
    contenido_4 = Matematica(b+c4i+'='+Pol('x',a+c4d))
    contenido_5 = Matematica(b+c5i+'='+Pol('x',a+c5d))



enunciado_oculto = [a,b]











