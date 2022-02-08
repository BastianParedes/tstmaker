{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b = elegir(100, 1000), elegir(10, 100)
resultado_sin_reservas = ""

menor = str(sorted([a,b])[0])
mayor = str(sorted([a,b])[1])

for espacio in range(0, abs(len(mayor)-len(menor))):
    menor = "0"+menor

for posicion in range(1, len(str(mayor))+1):
    resultado_sin_reservas  = str(  (int(mayor[-posicion])   +int(menor[-posicion])  )%10)+resultado_sin_reservas

#================================Aquí va el enunciado================================================================
enunciado = Matematica(Pol(a,b,azar=True)+"=")

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(a+b)
contenido_2 = Matematica(abs(a-b))
contenido_3 = Matematica(int(resultado_sin_reservas))
contenido_4 = Matematica(choice([a,b]))
contenido_5 = Matematica(str(a)+str(b))


enunciado_oculto = [a,b]










