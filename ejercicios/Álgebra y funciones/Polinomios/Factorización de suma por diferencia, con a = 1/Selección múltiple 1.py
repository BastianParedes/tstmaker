{"cantidad_opciones":2, "cantidad_disponible":50}

#===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
b = Racional(elegir(-50, 51, 0))

#===============================================Aquí va el número del ejercicio b el enunciado.
if opcion == 1:
    enunciado = "La factorización de " + Matematica(Pol({"x":2}, -b**2)) + " es"

elif opcion == 2:
    enunciado = "La factorización de " + Matematica(Pol(b**2, Term(-1,{"x":2}))) + " es"

#===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
if opcion == 1:
    contenido_correcto = Matematica("("+ Pol("x", b)+ ")("+ Pol("x",-b)+ ")")
    contenido_2 = Matematica(potencia(Pol("x",b), 2))
    contenido_3 = Matematica(potencia(Pol("x",-b), 2))
    contenido_4 = Matematica("("+ Pol({"x":2},2*b) + ")(" + Pol({"x":2},b**2) + ")")
    contenido_5 = Matematica("("+ Pol({"x":2},b) + ")(" + Pol({"x":2},-b) + ")")

elif opcion == 2:
    contenido_correcto = Matematica("(" +Pol(b,"x")+")("+Pol(b,-1*"x")+")")
    contenido_2 = Matematica(potencia(Pol(b,"x"), 2))
    contenido_3 = Matematica(potencia(Pol(b,-1*"x"), 2))
    contenido_4 = Matematica("("+Pol(2*b, {"x":2})+")("+Pol(b**2, {"x":2})+")")
    contenido_5 = Matematica("("+Pol(b,{"x":2})+")("+Pol(b, Term(-1,{"x":2}))+")")

enunciado_oculto = enunciado










