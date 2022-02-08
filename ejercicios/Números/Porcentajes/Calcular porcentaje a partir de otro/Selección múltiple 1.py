{"cantidad_opciones":1, "cantidad_disponible":50}

#===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
p1, p2 = Racional(choice([2,5,10,15,20,25,30,35,40,50,60,70,75,80,90])), Racional(choice([2,5,10,15,20,25,30,35,40,50,60,70,75,80,90]))
n = Racional(randrange(25,300)*2)
n2 = p1*n/100
#===============================================Aquí va el número del ejercicio y el enunciado.
enunciado = fr"El {Matematica(p1)}\% de X es {Matematica(n2)}, entonces el {Matematica(p2)}\% de X es"
#===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
contenido_correcto = Matematica(p2*n/100)
contenido_2 = Matematica(n)
contenido_3 = Matematica(p1*p2/100)
contenido_4 = Matematica(p1*p2*100)
contenido_5 = Matematica(p1*p2*n2/10000)


enunciado_oculto = [p1,p2,n]











