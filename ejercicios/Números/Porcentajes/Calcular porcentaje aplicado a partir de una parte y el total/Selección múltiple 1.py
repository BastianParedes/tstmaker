{"cantidad_opciones":1, "cantidad_disponible":50}

#===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
p = Racional(choice([2,5,10,15,20,25,30,35,40,50,60,70,75,80,90,100])*choice([1,2,3,4]))
n = Racional(randrange(25,300)*2)
n2 = p*n/100
#===============================================Aquí va el número del ejercicio y el enunciado.
enunciado = fr"El X\% de {Matematica(n)} es {Matematica(n2)}. El valor de X es"
#===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
contenido_correcto = Matematica(p)
contenido_2 = Matematica(n*n2/100)
contenido_3 = Matematica(n/(n2*100))
contenido_4 = Matematica(n*100/n2)
contenido_5 = Matematica(choice([n/n2,n2/n]))


enunciado_oculto = [n,p]











