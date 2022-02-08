{"cantidad_opciones":2, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
if opcion==1:#Exponentes positivos
    e = randrange(50, 150)
elif opcion==2:#Exponentes negativos
    e = randrange(-150, -50)


i = UnidadImaginaria()
#================================Aquí va el enunciado================================================================
enunciado = "Considera i como la unidad imaginaria. "+Matematica(potencia("i", e)+"=")
#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(i**e)
contenido_2 = Matematica(i**(e+1))
contenido_3 = Matematica(i**(e+2))
contenido_4 = Matematica(i**(e+3))
contenido_5 = Matematica(0)
enunciado_oculto = e










