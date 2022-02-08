#HAY QUE ARREGLARLO PORQUE HAY VARIABLES NO CREADAS
{"cantidad_opciones":1, "cantidad_disponible":50}

#===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
n = randrange(2,14)**2
cantidad_raices = choice([2,3,4])

divisores = natural(n)




#===============================================Aquí va el enunciado.
enunciado = r"Si x es un número positivo siempre se cumple que\ \ " + Matematica(raiz(potencia("x", a, quitar_1=True), b) +" "+por() + raiz(potencia("x", c, quitar_1=True), d), arreglar_espacios=True) + r"\ \ es igual a"

#===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero. No abrir ningún entorno.
contenido_correcto = Matematica("x"**racional(a*d+b*c, b*d))
contenido_2 =        Matematica("x"**racional(b*d, a*d+b*c))
contenido_3 =        Matematica("x"**racional(a*c, b*d))
contenido_4 =        Matematica("x"**racional(a+c, b+d))
contenido_5 =        Matematica("x"**racional(a-c, b+d))

enunciado_oculto = [a, b, c, d]