{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
inicio = randrange(0, 8)
fin = randrange(60, 100)
def elevar(exponente):
    if exponente == 0:
           return "1"
    else:
        return potencia("i", exponente, quitar_1=True)

#================================Aquí va el enunciado================================================================
enunciado = "Considera i como la unidad imaginaria. "+ Matematica(elevar(inicio)+"+"+elevar(inicio+1)+"+"+elevar(inicio+2)+"+"+elevar(inicio+3)+"+...+"+elevar(fin)+"=")

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
if inicio%4==0:
    diccionario = {0:"1", 1:"1+i", 2:"i", 3:"0", 4:"-i"}
    if fin%4==0:
        contenido_correcto = Matematica(diccionario[0])
        contenido_2 = Matematica(diccionario[1])
        contenido_3 = Matematica(diccionario[2])
        contenido_4 = Matematica(diccionario[3])
        contenido_5 = Matematica(diccionario[4])

    elif fin%4==1:
        contenido_correcto = Matematica(diccionario[1])
        contenido_2 = Matematica(diccionario[2])
        contenido_3 = Matematica(diccionario[3])
        contenido_4 = Matematica(diccionario[4])
        contenido_5 = Matematica(diccionario[0])

    elif fin%4==2:
        contenido_correcto = Matematica(diccionario[2])
        contenido_2 = Matematica(diccionario[3])
        contenido_3 = Matematica(diccionario[4])
        contenido_4 = Matematica(diccionario[0])
        contenido_5 = Matematica(diccionario[1])

    elif fin%4==3:
        contenido_correcto = Matematica(diccionario[3])
        contenido_2 = Matematica(diccionario[4])
        contenido_3 = Matematica(diccionario[0])
        contenido_4 = Matematica(diccionario[1])
        contenido_5 = Matematica(diccionario[2])

if inicio%4==1:
    diccionario = {1:"i", 2:"-1+i", 3:"-i", 0:"0", 4:"1-i"}
    if fin%4==0:
        contenido_correcto = Matematica(diccionario[0])
        contenido_2 = Matematica(diccionario[1])
        contenido_3 = Matematica(diccionario[2])
        contenido_4 = Matematica(diccionario[3])
        contenido_5 = Matematica(diccionario[4])

    elif fin%4==1:
        contenido_correcto = Matematica(diccionario[1])
        contenido_2 = Matematica(diccionario[2])
        contenido_3 = Matematica(diccionario[3])
        contenido_4 = Matematica(diccionario[4])
        contenido_5 = Matematica(diccionario[0])

    elif fin%4==2:
        contenido_correcto = Matematica(diccionario[2])
        contenido_2 = Matematica(diccionario[3])
        contenido_3 = Matematica(diccionario[4])
        contenido_4 = Matematica(diccionario[0])
        contenido_5 = Matematica(diccionario[1])

    elif fin%4==3:
        contenido_correcto = Matematica(diccionario[3])
        contenido_2 = Matematica(diccionario[4])
        contenido_3 = Matematica(diccionario[0])
        contenido_4 = Matematica(diccionario[1])
        contenido_5 = Matematica(diccionario[2])
        
if inicio%4==2:
    diccionario = {2:"-1", 3:"-1-i", 0:"-i", 1:"0", 4:"i"}
    if fin%4==0:
        contenido_correcto = Matematica(diccionario[0])
        contenido_2 = Matematica(diccionario[1])
        contenido_3 = Matematica(diccionario[2])
        contenido_4 = Matematica(diccionario[3])
        contenido_5 = Matematica(diccionario[4])

    elif fin%4==1:
        contenido_correcto = Matematica(diccionario[1])
        contenido_2 = Matematica(diccionario[2])
        contenido_3 = Matematica(diccionario[3])
        contenido_4 = Matematica(diccionario[4])
        contenido_5 = Matematica(diccionario[0])

    elif fin%4==2:
        contenido_correcto = Matematica(diccionario[2])
        contenido_2 = Matematica(diccionario[3])
        contenido_3 = Matematica(diccionario[4])
        contenido_4 = Matematica(diccionario[0])
        contenido_5 = Matematica(diccionario[1])

    elif fin%4==3:
        contenido_correcto = Matematica(diccionario[3])
        contenido_2 = Matematica(diccionario[4])
        contenido_3 = Matematica(diccionario[0])
        contenido_4 = Matematica(diccionario[1])
        contenido_5 = Matematica(diccionario[2])
        
if inicio%4==3:
    diccionario = {3:"-i", 0:"1-i", 1:"1", 2:"0", 4:"-1"}
    if fin%4==0:
        contenido_correcto = Matematica(diccionario[0])
        contenido_2 = Matematica(diccionario[1])
        contenido_3 = Matematica(diccionario[2])
        contenido_4 = Matematica(diccionario[3])
        contenido_5 = Matematica(diccionario[4])

    elif fin%4==1:
        contenido_correcto = Matematica(diccionario[1])
        contenido_2 = Matematica(diccionario[2])
        contenido_3 = Matematica(diccionario[3])
        contenido_4 = Matematica(diccionario[4])
        contenido_5 = Matematica(diccionario[0])

    elif fin%4==2:
        contenido_correcto = Matematica(diccionario[2])
        contenido_2 = Matematica(diccionario[3])
        contenido_3 = Matematica(diccionario[4])
        contenido_4 = Matematica(diccionario[0])
        contenido_5 = Matematica(diccionario[1])

    elif fin%4==3:
        contenido_correcto = Matematica(diccionario[3])
        contenido_2 = Matematica(diccionario[4])
        contenido_3 = Matematica(diccionario[0])
        contenido_4 = Matematica(diccionario[1])
        contenido_5 = Matematica(diccionario[2])

enunciado_oculto = [inicio, fin]










