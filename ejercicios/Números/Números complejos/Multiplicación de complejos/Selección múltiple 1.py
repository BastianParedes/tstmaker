{"cantidad_opciones":1, "cantidad_disponible":50}

#===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
z1 = Complex(choice(list(range(-10, 0))+list(range(1, 10))), choice(list(range(-10, 0))+list(range(1, 10))))
z2 = Complex(choice(list(range(-10, 0))+list(range(1, 10))), choice(list(range(-10, 0))+list(range(1, 10))))

#===============================================Aquí va el número del ejercicio y el enunciado.
enunciado = "Considera i como la unidad imaginaria. " + Matematica(f"({z1})({z2})=")

#===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
contenido_correcto = Matematica(z1*z2)
contenido_2 = Matematica(Complex(z1.re, z1.im*z2.re))
contenido_3 = Matematica(Complex(z1.re*z2.re+z1.im*z2.im, z1.re*z2.im+z1.im*z2.re))
contenido_4 = Matematica(Complex(z1.re, z1.im*z2.re*z2.im))
contenido_5 = Matematica(Complex(z1.re, -z1.im*z2.re*z2.im))

enunciado_oculto = [z1, z2]










