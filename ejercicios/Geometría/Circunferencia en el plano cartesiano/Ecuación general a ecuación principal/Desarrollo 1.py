{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
h, k, r = choice([-1,1])*Racional(randrange(1, 7)), choice([-1,1])*Racional(randrange(1, 7)), Racional(randrange(1, 7))
while h==k:
    h, k, r = choice([-1,1])*Racional(randrange(1, 5)), choice([-1,1])*Racional(randrange(1, 5)), Racional(randrange(1, 5))

#================================Aquí va el enunciado================================================================
enunciado = "La ecuación general de una circunferencia es "+Matematica(Pol({"x":2}, {"y":2}, -2*h*"x", -2*k*"y", h**2+k**2-r**2)+"=0")+". La ecuación principal de dicha circunferencia es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(potencia(Pol("x",-h),2)+"+"+potencia(Pol("y",-k),2)+"="+r**2)



enunciado_oculto = [h,k,r]
espacio_para_el_desarrollo = 6











