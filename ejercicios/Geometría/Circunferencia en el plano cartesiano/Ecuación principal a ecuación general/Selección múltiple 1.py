{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
h, k, r = choice([-1,1])*Racional(randrange(1, 7)), choice([-1,1])*Racional(randrange(1, 7)), Racional(randrange(1, 7))
while h==k:
    h, k, r = choice([-1,1])*Racional(randrange(1, 5)), choice([-1,1])*Racional(randrange(1, 5)), Racional(randrange(1, 5))

#================================Aquí va el enunciado================================================================
enunciado = "La ecuación principal de una circunferencia es "+Matematica(potencia(Pol("x",-h),2)+"+"+potencia(Pol("y",-k),2)+"="+r**2)+". La ecuación general de dicha circunferencia es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(Pol({"x":2}, {"y":2}, -2*h*"x", -2*k*"y", h**2+k**2-r**2)+"=0")
contenido_2 = Matematica(Pol({"x":2}, {"y":2}, 2*h*"x", 2*k*"y", h**2+k**2-r**2)+"=0")
contenido_3 = Matematica(Pol({"x":2}, {"y":2}, -2*h*"x", -2*k*"y", h**2+k**2+r**2)+"=0")
contenido_4 = Matematica(Pol({"x":2}, {"y":2}, +2*h*"x", -2*k*"y", h**2+k**2+choice([-r**2,r**2]))+"=0")
contenido_5 = Matematica(Pol({"x":2}, {"y":2}, -2*h*"x", +2*k*"y", h**2+k**2+choice([-r**2,r**2]))+"=0")


enunciado_oculto = [h,k,r]










