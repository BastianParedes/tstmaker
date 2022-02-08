{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, h = Racional(elegir(-5,6,0)), Racional(elegir(-10,11))
b, c = -2*a*h, a*h**2
letra = choice(["f", "g", "h"])

#================================Aquí va el enunciado================================================================
enunciado = "Sea la función "+ Matematica(letra+"(x)="+choice([-1,1])*Pol(a*{"x":2}, b*"x", c, azar=True)) +f". El punto de intersección entre la gráfica de {letra} y el eje x es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(r"("+h+", 0)", arreglar_espacios=True)
contenido_2 = Matematica(r"("+2*h+", 0)", arreglar_espacios=True)
contenido_3 = Matematica(r"("+h/2+", 0)", arreglar_espacios=True)
contenido_4 = Matematica(r"("+(-h)+", 0)", arreglar_espacios=True)
contenido_5 = Matematica(r"("+(-2*h)+", 0)", arreglar_espacios=True)



enunciado_oculto = [a,b,c]











