{"cantidad_opciones":1, "cantidad_disponible":50}

#===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
a = Racional(randrange(1,100)*choice([10,100,1000]))
#===============================================Aquí va el número del ejercicio y el enunciado.
enunciado = Matematica(a+" m=")
#===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
contenido_correcto = Matematica(Racional(a*100,cargar_decimal=True)+" cm")
contenido_2 = Matematica(Racional(a*10,cargar_decimal=True)+" cm")
contenido_3 = Matematica(Racional(a*1000,cargar_decimal=True)+" cm")
contenido_4 = Matematica(Racional(a/1000,cargar_decimal=True)+" cm")
contenido_5 = Matematica(Racional(a/100,cargar_decimal=True)+" cm")



enunciado_oculto = a











