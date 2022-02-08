{"cantidad_opciones":1, "cantidad_disponible":50}

#===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
p = Racional(choice([2,5,10,15,20,25,30,35,40,50,60,70,75,80,90,100])*choice([1,2,3,4]))
while p==100:
    p = Racional(choice([2,5,10,15,20,25,30,35,40,50,60,70,75,80,90,100])*choice([1,2,3,4]))
n = Racional(randrange(25,300)*2)
n2 = p*n/100
#===============================================Aquí va el número del ejercicio y el enunciado.
enunciado = fr"El {Matematica(p)}\% de X es {Matematica(n2)}. El valor de X es"
#===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
contenido_correcto = Matematica(n)
contenido_2 = Matematica(p*n2/100)
contenido_3 = Matematica(p*n2*100)
contenido_4 = Matematica(p*100/n2)
contenido_5 = Matematica(100/(p*n2))


enunciado_oculto = [p,n]











