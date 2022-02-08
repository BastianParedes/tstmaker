{"cantidad_opciones":1, "cantidad_disponible":50}

#===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
p = Racional(choice([2,5,10,15,20,25,30,35,40,50,60,70,75,80,90,100])*choice([1,2,3,4]))
n = Racional(randrange(25,300)*2)
#===============================================Aquí va el número del ejercicio y el enunciado.
enunciado = fr"El {Matematica(p)}\% de {Matematica(n)} es"
#===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
contenido_correcto = Matematica(Racional(p*n/100, cargar_decimal=choice([True,False])))
contenido_2 = Matematica(Racional(p*n*100, cargar_decimal=choice([True,False])))
contenido_3 = Matematica(Racional(p/(n*100)))
contenido_4 = Matematica(Racional(n/(p*100)))
contenido_5 = Matematica(choice([p/n,n/p]))


enunciado_oculto = [n,p]











