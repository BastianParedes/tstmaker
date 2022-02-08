{"cantidad_opciones":1, "cantidad_disponible":50}

#===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
z1 = Complex(randrange(-10, 10), choice(list(range(-10, 0))+list(range(1, 10))))
z2 = Complex(choice(list(range(-10, 0))+list(range(1, 10))),  choice(list(range(-10, 0))+list(range(1, 10))))

while z2.re**2+z2.im**2==0 or z2.re**2-z2.im**2==0 or (z2.re+z2.im)==0:
    z1 = Complex(randrange(-10, 10), choice(list(range(-10, 0))+list(range(1, 10))))
    z2 = Complex(choice(list(range(-10, 0))+list(range(1, 10))),  choice(list(range(-10, 0))+list(range(1, 10))))

#===============================================Aquí va el número del ejercicio y el enunciado.
enunciado = "Considera i como la unidad imaginaria. " + Matematica(fraccion(z1, z2))+" ="

#===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
contenido_correcto = Matematica(z1/z2)
contenido_2 = Matematica(Complex(z1.re/z2.re, z1.im/z2.im))
contenido_3 = Matematica(Complex((z1.re*z2.re-z1.im*z2.im)/(z2.re+z2.im), (z1.re*z2.re+z1.im*z2.im)/(z2.re+z2.im)))
contenido_4 = Matematica(Complex((z1.re*z2.re-z1.im*z2.im)/(z2.re**2+z2.im**2), (z1.re*z2.re+z1.im*z2.im)/(z2.re**2+z2.im**2)))
contenido_5 = Matematica(Complex((z1.re*z2.re-z1.im*z2.im)/(z2.re**2+z2.im**2), (z1.im*z2.re-z1.re*z2.im)/(z2.re**2-z2.im**2)))

enunciado_oculto = [z1, z2]










