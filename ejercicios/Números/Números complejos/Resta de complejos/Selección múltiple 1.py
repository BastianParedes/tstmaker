{"cantidad_opciones":3, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
z1 = Complex(choice(list(range(-10, 0))+list(range(1, 10))), choice(list(range(-10, 0))+list(range(1, 10))))
z2 = Complex(choice(list(range(-10, 0))+list(range(1, 10))), choice(list(range(-10, 0))+list(range(1, 10))))

#================================Aquí va el enunciado================================================================
enunciado = "Considera i como la unidad imaginaria. "
if opcion==1:
    enunciado += choice([Matematica("("+z1+")-("+z2+")="), "Sean "+Matematica(sub("Z",1)+"="+z1)+" y "+Matematica(sub("Z",2)+"="+z2)+". "+Matematica(sub("Z",1)+"-"+sub("Z",2)+"=")])

elif opcion==2:
    enunciado += choice([Matematica("-("+z1+")+("+z2+")="), "Sean "+Matematica(sub("Z",1)+"="+z1)+" y "+Matematica(sub("Z",2)+"="+z2)+". "+Matematica("-"+sub("Z",1)+"+"+sub("Z",2)+"=")])

else:
    enunciado += choice([Matematica("-("+z1+")-("+z2+")="), "Sean "+Matematica(sub("Z",1)+"="+z1)+" y "+Matematica(sub("Z",2)+"="+z2)+". "+Matematica("-"+sub("Z",1)+"-"+sub("Z",2)+"=")])

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.=
if opcion==1:
    contenido_correcto = Matematica(z1-z2)
    contenido_2 = Matematica(Complex(z1.re+z1.im, -z2.re-z2.im))
    contenido_3 = Matematica(Complex(0, z1.re+z1.im-z2.re-z2.im))
    contenido_4 = Matematica(Complex(z1.re+z2.re, z1.im+z2.im))
    contenido_5 = Matematica(Complex(z1.re*(-z2.re)+z1.im*z2.im, z1.re*(-z2.im)-z1.im*z2.re))
elif opcion==2:
    contenido_correcto = Matematica(-z1+z2)
    contenido_2 = Matematica(Complex(-z1.re-z1.im, z2.re+z2.im))
    contenido_3 = Matematica(Complex(0, -z1.re-z1.im+z2.re+z2.im))
    contenido_4 = Matematica(Complex(z1.re+z2.re, z1.im+z2.im))
    contenido_5 = Matematica(Complex(-z1.re*z2.re+z1.im*z2.im, -z1.re*z2.im-z1.im*z2.re))
elif opcion==3:
    contenido_correcto = Matematica(-z1-z2)
    contenido_2 = Matematica(Complex(-z1.re-z1.im, -z2.re-z2.im))
    contenido_3 = Matematica(Complex(0, -z1.re-z1.im-z2.re-z2.im))
    contenido_4 = Matematica(Complex(z1.re+z2.re, z1.im+z2.im))
    contenido_5 = Matematica(Complex(z1.re*z2.re-z2.im*z1.im, z1.re*z2.im+z1.im*z2.re))

enunciado_oculto = enunciado










