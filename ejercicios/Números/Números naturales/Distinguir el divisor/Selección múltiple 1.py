{"cantidad_opciones":1, "cantidad_disponible":50}

#===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
numero = Natural(elegir(1, 41))
while len(numero.lista_de_no_divisores)<=3:
    numero = Natural(elegir(1, 41))

no_divisores = numero.lista_de_no_divisores

a=choice(numero.lista_de_divisores)
b=choice(no_divisores)
no_divisores.remove(b)
c=choice(no_divisores)
no_divisores.remove(c)
d=choice(no_divisores)
no_divisores.remove(d)
e=choice(no_divisores)
no_divisores.remove(e)

#===============================================Aquí va el número del ejercicio y el enunciado.
enunciado = f"Un divisor de {numero} es"

#===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
contenido_correcto = Matematica(a)
contenido_2 = Matematica(b)
contenido_3 = Matematica(c)
contenido_4 = Matematica(d)
contenido_5 = Matematica(e)

enunciado_oculto = [numero,contenido_correcto]










