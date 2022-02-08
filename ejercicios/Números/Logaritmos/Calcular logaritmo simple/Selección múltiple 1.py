{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
diccionario_de_topes_de_exponentes = {2:8, 3:6, 4:5, 5:5, 6:4, 7:3, 8:3, 9:3, 10:5, 11:3, 12:3, 13:3, 14:3, 15:3, 16:3, 17:3, 18:3, 19:3, 20:3, 21:3, 22:3, 23:3, 24:3, 25:3, 26:3, 27:3, 28:3, 29:3, 30:3, 31:3, 32:3}
a = Racional(randrange(2, 33))
b = Racional(randrange(0, diccionario_de_topes_de_exponentes[abs(int(a))]+1))

#================================Aquí va el enunciado================================================================
enunciado = Matematica(logaritmo(a**b, a,False)+"=")

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
if b==0:
    contenido_correcto = Matematica(0)
    contenido_2 =        Matematica(1)
    contenido_3 =        Matematica(-1)
    contenido_4 =        Matematica(a)
    contenido_5 =        Matematica(-a)

elif b==1:
    contenido_correcto = Matematica(1)
    contenido_2 =        Matematica(0)
    contenido_3 =        Matematica(-1)
    contenido_4 =        Matematica(a)
    contenido_5 =        Matematica(-a)

else:
    contenido_correcto = Matematica(b)
    contenido_2 =        Matematica(2*b)
    contenido_3 =        Matematica(-b)
    contenido_4 =        Matematica(b**-1)
    contenido_5 =        Matematica(-b**-1)



enunciado_oculto = [a, b]











