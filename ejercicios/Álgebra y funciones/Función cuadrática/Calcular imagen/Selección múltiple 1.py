{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b, c = Racional(elegir(-10,11,0)), Racional(elegir(-10,11)), Racional(elegir(-10, 10))
x = elegir(-5, 5)
letra = choice(["f", "g", "h"])

#================================Aquí va el enunciado================================================================
enunciado = "Sea la función "+ Matematica(f"{letra}(x)="+Pol(Term(a,{"x":2}), b*"x", c))+". El valor de "+Matematica(letra+f"({x})")+" es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(a*x**2+b*x+c)
contenido_2 = Matematica(-a*x**2+b*x+c)
contenido_3 = Matematica(a*x+b*x+c)
contenido_4 = Matematica(x**2+b*x+c)
contenido_5 = Matematica(a*x**2+b*x)



enunciado_oculto = [a,b,c,x]










