{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
h, k, r = choice([-1,1])*Racional(randrange(1, 7)), choice([-1,1])*Racional(randrange(1, 7)), Racional(randrange(2, 8))
#================================Aquí va el enunciado================================================================
enunciado_verdadero = "Sea la circunferencia C cuya ecuación general es "+Matematica(Pol({"x":2}, {"y":2}, -2*h*"x", -2*k*"y", h**2+k**2-r**2)+"=0")+". El centro de C es "+Matematica(Par(h,k))+"."

enunciado_falso = "Sea la circunferencia C cuya ecuación general es "+Matematica(Pol({"x":2}, {"y":2}, -2*h*"x", -2*k*"y", h**2+k**2-r**2)+"=0")+". El centro de C es "+choice([
Matematica(Par(-h,-k)),
Matematica(Par(-h,k)),
Matematica(Par(h,-k)),
Matematica(Par(k,h)),
Matematica(Par(-k,-h)),
Matematica(Par(-k,h)),
Matematica(Par(k,-h)),
Matematica(Par(-k,-h))

])+"."



enunciado_oculto = [h,k,r]











