{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b = Racional(choice([-1,1])*randrange(1, 13)), Racional(choice([-1,1])*randrange(1, 13))

#================================Aquí va el enunciado================================================================
enunciado = Matematica(Pol({"x":2}, 2*a*"x", a**2+b)+"=")

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(Pol(potencia(Pol("x",a),2), b))
contenido_2 = Matematica(Pol(potencia(Pol("x",-a),2), -b))
contenido_3 = Matematica(Pol(potencia(Pol("x",-a),2), b))
contenido_4 = Matematica(Pol(potencia(Pol("x", a),2), -b))
contenido_5 = Matematica(potencia(Pol("x",choice([a,-a])),2))

enunciado_oculto = [a,b]










