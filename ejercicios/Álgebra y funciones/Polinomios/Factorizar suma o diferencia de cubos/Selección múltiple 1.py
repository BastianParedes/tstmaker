{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a = Racional(elegir(-5,6,0))
b = Racional(elegir(-10,11,0))
while abs(a)==abs(b):
    a = Racional(elegir(-5,6,0))
    b = Racional(elegir(-10,11,0))

#================================Aquí va el enunciado================================================================
enunciado = Matematica(Pol(a**3*"x"**Racional(3), b**3, azar=True)+"=")

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica("("+Pol(a*"x",b)+")("+Pol(a**2*"x"**Racional(2), -b*a*"x", b**2)+")")
contenido_2 =        Matematica("("+Pol(a*"x",b)+")("+Pol(a**2*"x"**Racional(2), -2*b*a*"x", b**2)+")")
contenido_3 =        Matematica(potencia(Pol(a*"x",b), 3))
contenido_4 =        Matematica("("+Pol(a*"x",choice([-1,1])*b)+")("+Pol(a**2*"x"**Racional(2), -b*"x", choice([b, b**2]))+")")
contenido_5 =        Matematica("("+Pol("x",choice([-1,1])*b)+")("+Pol(a**2*"x"**Racional(2), choice([-2,2])*b*"x", choice([b, b**2]))+")")

enunciado_oculto = [a,b]










