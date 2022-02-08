{"cantidad_opciones":1, "cantidad_disponible":50}

#===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
a, b, = Racional(elegir(-10,11 ,0)), Racional(elegir(-10,11, 0))

#===============================================Aquí va el número del ejercicio y el enunciado.
enunciado = f"¿Cuál es el valor de x que satisface la ecuación {choice([Matematica(Pol('x',a)+'='+b), Matematica(b+'='+Pol('x',a))])}?"

#===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
contenido_correcto = Matematica(b-a)
contenido_2 = Matematica(a-b)
contenido_3 = Matematica(a*b)
contenido_4 = Matematica(-a)
contenido_5 = Matematica(-b)


enunciado_oculto = [a,b]











