{"cantidad_opciones":2, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b, c, d, e, f = Racional(randrange(-10, 10)), Racional(randrange(-10, 10)), Racional(randrange(-10, 10)), Racional(randrange(-10, 10)), Racional(randrange(-10, 10)), Racional(randrange(-10, 10))
while a==c or c==e or a==e or b==d or d==f or b==f:
    a, b, c, d, e, f = Racional(randrange(-10, 10)), Racional(randrange(-10, 10)), Racional(randrange(-10, 10)), Racional(randrange(-10, 10)), Racional(randrange(-10, 10)), Racional(randrange(-10, 10))


if opcion==1:
    #================================Aquí va el enunciado================================================================
    enunciado = "La recta L pasa por por puntos "+Matematica(Par(a, b))+", "+Matematica(f"({c}, k)", arreglar_espacios=True)+" y "+Matematica(Par(e, f))+". El valor de k es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(((f-b)*(c-a)+b*(e-a))/(e-a))
    contenido_2 = Matematica(((f-b)*(c-a)+b*(a-e))/(a-e))
    contenido_3 = Matematica(((c-a)*(e-a)+b*(f-b))/(f-b))
    contenido_4 = Matematica((f-b)/(e-a))
    contenido_5 = Matematica((e*(b-f)+f*(e-a))/(e-a))


elif opcion==2:
    #================================Aquí va el enunciado================================================================
    enunciado = "La recta L pasa por por puntos "+Matematica(Par(a, b))+", "+Matematica(f"(k, {d})", arreglar_espacios=True)+" y "+Matematica(Par(e, f))+". El valor de K es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(((d-b)*(e-a)+a*(f-b))/(f-b))
    contenido_2 = Matematica(((d-b)*(e-a)+a*(b-f))/(b-f))
    contenido_3 = Matematica(((f-b)*(d-b)+a*(e-a))/(e-a))
    contenido_4 = Matematica((f-b)/(e-a))
    contenido_5 = Matematica((e*(b-f)+f*(e-a))/(e-a))

enunciado_oculto = enunciado










