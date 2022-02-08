{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a = Natural(randrange(6, 37))
while not 3<=len(a.lista_de_divisores):
    a = Natural(randrange(6, 37))
a1 = a.lista_de_divisores[randrange(1, len(a.lista_de_divisores)-1)]
a2 = a/a1
b, c, d, e = Racional(elegir(-5,6)), Racional(elegir(-5,6)), Racional(elegir(-5,6)), Racional(elegir(-5,6))
while b+d==0 or b+2*d==0 or b+d**2==0:
    b, c, d, e = Racional(elegir(-5,6)), Racional(elegir(-5,6)), Racional(elegir(-5,6)), Racional(elegir(-5,6))

lista_de_potencias = [potencia(a,Pol(b*"x",c,azar=True)), potencia(a1,Pol(d*"x",e,azar=True)), potencia(a2,Pol(d*"x",e,azar=True))]
shuffle(lista_de_potencias)

#================================Aquí va el enunciado================================================================
enunciado = "El valor de x que satisface la ecuación "+Matematica(choice([
    lista_de_potencias[0]+por()+lista_de_potencias[1]+por()+lista_de_potencias[2]+"=1",
    "1="+lista_de_potencias[0]+por()+lista_de_potencias[1]+por()+lista_de_potencias[2]
        ]))+" es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica((-c-e)/(b+d))
contenido_2 =        Matematica((1-c-e)/(b+d))
contenido_3 =        Matematica((-c-2*e)/(b+2*d))
contenido_4 =        Matematica((1-c-2*e)/(b+2*d))
contenido_5 =        Matematica((-c-e**2)/(b+d**2))



enunciado_oculto = [a, b, c, d, e]











