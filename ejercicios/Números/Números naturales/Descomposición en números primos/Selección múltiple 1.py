{"cantidad_opciones":1, "cantidad_disponible":50}

def multiplicar(lista, simbolo):
    multiplicaciones = ""
    n=0
    for i in range(0, len(lista)):
        multiplicaciones = multiplicaciones + str(lista[i])
        if not n == len(lista)-1:
            multiplicaciones = multiplicaciones + simbolo
            n += 1
    return multiplicaciones

#===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
n = Natural(randrange(6, 1000))
while not 2<=len(n.lista_descomposicion_en_primos)<=6 or 7<max(n.lista_descomposicion_en_primos):
    n = Natural(randrange(6, 1000))

#===============================================Aquí va el número del ejercicio y el enunciado.
enunciado = f"La descomposición en factores primos de {n} es"

#===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
contenido_correcto = Matematica(multiplicar(n.lista_descomposicion_en_primos, por()))
contenido_2 = Matematica(multiplicar(n.lista_primos_divisores, por()))
contenido_3 = Matematica(multiplicar(n.lista_descomposicion_en_primos, "+"))
contenido_4 = Matematica(multiplicar(n.lista_primos_divisores, "+"))
contenido_5 = Matematica("1"+por()+"2"+por()+"3"+por()+"4"+por()+"..."+por()+f"{n}")

enunciado_oculto = n










