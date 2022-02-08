{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
L = Racional(randrange(3, 7))
P1 = Par(randrange(-5,6), randrange(-5,6))
P2 = Par(P1.x , P1.y-L)
P3 = Par(P1.x+L , P1.y-L)
P4 = Par(P1.x+L , P1.y)

O = Par(randrange(1,5), randrange(1,5))
k = elegir(-3,4 ,0,1)

L2 = L*k

#================================Aquí va el enunciado================================================================
enunciado = f'Sean los puntos A{Matematica(P1)}, B{Matematica(P2)}, C{Matematica(P3)}, D{Matematica(P4)} y P{Matematica(O)}. A la figura ABCD se le aplica una homotecia respecto de P con razón {Matematica(k)}, ¿cuánto mide la superficie del homotético de dicha figura?'

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(L2**2) + ' unidades'
contenido_2 =        Matematica(L2) + ' unidades'
contenido_3 =        Matematica(L2 * Root(2)) + ' unidades'
contenido_4 =        Matematica(4*L2) + ' unidades'
contenido_5 =        Matematica(L**2) + ' unidades'



enunciado_oculto = [L, O, k]


