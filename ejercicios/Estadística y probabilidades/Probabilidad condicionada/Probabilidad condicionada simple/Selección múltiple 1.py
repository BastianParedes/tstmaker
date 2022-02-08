{"cantidad_opciones":3, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
p1 = choice([5, 10, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90, 95])
p2 = choice([5, 10, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90, 95])
py = choice([5, 10, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90, 95])
po = p1+p2-py
while not py<p1 or not py<p2 or p1==p2 or 100<=po:
    p1 = choice([5, 10, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90, 95])
    p2 = choice([5, 10, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90, 95])
    py = choice([5, 10, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90, 95])
    po = p1+p2-py
p1, p2, py, po = Racional(p1), Racional(p2), Racional(py), Racional(po)




if opcion==1:
    lista_de_sucesos = ["español", "inglés", "francés", "italiano", "griego", "japonés", "chino mandarín", "árabe"]
    shuffle(lista_de_sucesos)
    suceso_1, suceso_2 = lista_de_sucesos[0], lista_de_sucesos[1]
    opcion_b = choice([1,2])
    #================================Aquí va el enunciado================================================================
    if choice([True,False]):
        if opcion_b==1:
            enunciado = f"De un grupo de estudiantes, el {Matematica(p1+'%')} de los integrantes habla {suceso_1}, el {Matematica(p2+'%')} de los integrantes habla {suceso_2} y el {Matematica(py+'%')} habla ambos idiomas. Si se escoge un estudiante al azar entre los que hablan {suceso_1}, la probabilidad de que dicho estudiante hable {suceso_2} es"
        else:
            enunciado = f"De un grupo de estudiantes, el {Matematica(p1+'%')} de los integrantes habla {suceso_1}, el {Matematica(p2+'%')} de los integrantes habla {suceso_2} y el {Matematica(py+'%')} habla ambos idiomas. Si se escoge un estudiante al azar entre los que hablan {suceso_2}, la probabilidad de que dicho estudiante hable {suceso_1} es"
    else:
        if opcion_b==1:
            enunciado = f"De un grupo de estudiantes, el {Matematica(p1+'%')} de los integrantes habla {suceso_1}, el {Matematica(p2+'%')} de los integrantes habla {suceso_2} y el {Matematica(po+'%')} habla al menos uno de los mencionados. Si se escoge un estudiante al azar entre los que hablan {suceso_1}, la probabilidad de que dicho estudiante hable {suceso_2} es"
        else:
            enunciado = f"De un grupo de estudiantes, el {Matematica(p1+'%')} de los integrantes habla {suceso_1}, el {Matematica(p2+'%')} de los integrantes habla {suceso_2} y el {Matematica(po+'%')} habla al menos uno de los mencionados. Si se escoge un estudiante al azar entre los que hablan {suceso_2}, la probabilidad de que dicho estudiante hable {suceso_1} es"


elif opcion==2:
    lista_de_sucesos = ["buceo", "natación", "fútbol", "básquetbol", "tenis", "boxeo", "patinaje artístico", "hockey", "arquería"]
    shuffle(lista_de_sucesos)
    suceso_1, suceso_2 = lista_de_sucesos[0], lista_de_sucesos[1]
    opcion_b = choice([1,2])
    #================================Aquí va el enunciado================================================================
    if choice([True,False]):
        if opcion_b==1:
            enunciado = f"De un grupo de deportistas, el {Matematica(p1+'%')} de los integrantes practica {suceso_1}, el {Matematica(p2+'%')} de los integrantes practica {suceso_2} y el {Matematica(py+'%')} practica ambos deportes. Si se escoge un deportista al azar entre los que practican {suceso_1}, la probabilidad de que dicho deportista practique {suceso_2} es"
        else:
            enunciado = f"De un grupo de deportistas, el {Matematica(p1+'%')} de los integrantes practica {suceso_1}, el {Matematica(p2+'%')} de los integrantes practica {suceso_2} y el {Matematica(py+'%')} practica ambos deportes. Si se escoge un deportista al azar entre los que practican {suceso_2}, la probabilidad de que dicho deportista practique {suceso_1} es"
    else:
        if opcion_b==1:
            enunciado = f"De un grupo de deportistas, el {Matematica(p1+'%')} de los integrantes practica {suceso_1}, el {Matematica(p2+'%')} de los integrantes practica {suceso_2} y el {Matematica(po+'%')} practica al menos uno de los mencionados. Si se escoge un deportista al azar entre los que practican {suceso_1}, la probabilidad de que dicho deportista practique {suceso_2} es"
        else:
            enunciado = f"De un grupo de deportistas, el {Matematica(p1+'%')} de los integrantes practica {suceso_1}, el {Matematica(p2+'%')} de los integrantes practica {suceso_2} y el {Matematica(po+'%')} practica al menos uno de los mencionados. Si se escoge un deportista al azar entre los que practican {suceso_2}, la probabilidad de que dicho deportista practique {suceso_1} es"




elif opcion==3:
    lista_de_sucesos = ["aventura", "ciencia ficción", "hadas", "gótico", "policíaco", "paranormal", "distópico", "fantástico"]
    shuffle(lista_de_sucesos)
    suceso_1, suceso_2 = lista_de_sucesos[0], lista_de_sucesos[1]
    opcion_b = choice([1,2])
    #================================Aquí va el enunciado================================================================
    if choice([True,False]):
        if opcion_b==1:
            enunciado = f"En una biblioteca se pueden encontrar libros de distintos géneros, el {Matematica(p1+'%')} de los libros es del género {suceso_1}, el {Matematica(p2+'%')} de los libros es del género {suceso_2} y el {Matematica(py+'%')} es de ambos géneros. Si se escoge un libro al azar entre los del género {suceso_1}, la probabilidad de que dicho libro sea de {suceso_2} es"
        else:
            enunciado = f"En una biblioteca se pueden encontrar libros de distintos géneros, el {Matematica(p1+'%')} de los libros es del género {suceso_1}, el {Matematica(p2+'%')} de los libros es del género {suceso_2} y el {Matematica(py+'%')} es de ambos géneros. Si se escoge un libro al azar entre los del género {suceso_2}, la probabilidad de que dicho libro sea de {suceso_1} es"
    else:
        if opcion_b==1:
            enunciado = f"En una biblioteca se pueden encontrar libros de distintos géneros, el {Matematica(p1+'%')} de los libros es del género {suceso_1}, el {Matematica(p2+'%')} de los libros es del género {suceso_2} y el {Matematica(po+'%')} pertenece al menos a uno de los géneros. Si se escoge un libro al azar entre los del género {suceso_1}, la probabilidad de que dicho libro sea de {suceso_2} es"
        else:
            enunciado = f"En una biblioteca se pueden encontrar libros de distintos géneros, el {Matematica(p1+'%')} de los libros es del género {suceso_1}, el {Matematica(p2+'%')} de los libros es del género {suceso_2} y el {Matematica(po+'%')} pertenece al menos a uno de los géneros. Si se escoge un libro al azar entre los del género {suceso_2}, la probabilidad de que dicho libro sea de {suceso_1} es"










#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
if opcion_b==1:
    contenido_correcto = Matematica(py/p1)
    contenido_2 =        Matematica(py/p2)
    contenido_3 =        Matematica(p1)
    contenido_4 =        Matematica(p1/po)
    contenido_5 =        Matematica(p2/po)
else:
    contenido_correcto = Matematica(py/p2)
    contenido_2 =        Matematica(py/p1)
    contenido_3 =        Matematica(p2)
    contenido_4 =        Matematica(p2/po)
    contenido_5 =        Matematica(p1/po)



enunciado_oculto = [p1, p2, py]











