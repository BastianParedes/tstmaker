{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b, c = Racional(elegir(-10,11,0)), Racional(elegir(-10,11)), Racional(elegir(-10, 10))
letra = choice(["f", "g", "h"])

#================================Aquí va el enunciado================================================================
enunciado = "Sea la función "+ Matematica(f"{letra}(x)="+Pol(Term(a,{"x":2}), b*"x", c))+". El discriminante de "+letra+" es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(b**2-4*a*c)
contenido_2 = Matematica(-b/a)
contenido_3 = Matematica(c/a)
contenido_4 = Matematica((4*a*c-b**2)/(4*a))
contenido_5 = Matematica((4*a*c-b**2)/(2*a))


enunciado_oculto = [a,b,c]










