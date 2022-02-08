{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
h, k, r = choice([-1,1])*Racional(randrange(1, 7)), choice([-1,1])*Racional(randrange(1, 7)), Racional(randrange(2, 8))
#================================Aquí va el enunciado================================================================
enunciado_verdadero = "Sea la circunferencia C cuya ecuación general es "+Matematica(Pol({"x":2}, {"y":2}, -2*h*"x", -2*k*"y", h**2+k**2-r**2)+"=0")+". El radio de C es "+Matematica(r+" unidades", arreglar_espacios=True)+"."

enunciado_falso = "Sea la circunferencia C cuya ecuación general es "+Matematica(Pol({"x":2}, {"y":2}, -2*h*"x", -2*k*"y", h**2+k**2-r**2)+"=0")+". El radio de C es "+choice([

Matematica(-r+" unidades", arreglar_espacios=True),
Matematica(r**2+" unidades", arreglar_espacios=True),
Matematica(-r**2+" unidades", arreglar_espacios=True),
Matematica(h**2+k**2-r**2+" unidades", arreglar_espacios=True),
Matematica(-(h**2+k**2-r**2)+" unidades", arreglar_espacios=True),
Matematica(h+" unidades", arreglar_espacios=True),
Matematica(k+" unidades", arreglar_espacios=True),
Matematica(-h+" unidades", arreglar_espacios=True),
Matematica(-k+" unidades", arreglar_espacios=True)
])+"."



enunciado_oculto = [h,k,r]










