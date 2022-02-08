{"cantidad_opciones":2, "cantidad_disponible":50}

p = Par(randrange(-10, 10), randrange(-10, 10))
while p.x==p.y:
    p = Par(randrange(-10, 10), randrange(-10, 10))

if opcion==1:
    #================================Aquí va el enunciado================================================================
    enunciado = "La coordenada X del par ordenado "+Matematica(p)+" es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(p.x)
    contenido_2 = Matematica(p.y)
    contenido_3 = Matematica(-p.x)
    contenido_4 = Matematica(-p.y)
    contenido_5 = Matematica(Root(p.x**2+p.y**2))

if opcion==2:
    #================================Aquí va el enunciado================================================================
    enunciado = "La coordenada Y del par ordenado "+Matematica(p)+" es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(p.y)
    contenido_2 = Matematica(p.x)
    contenido_3 = Matematica(-p.y)
    contenido_4 = Matematica(-p.x)
    contenido_5 = Matematica(Root(p.x**2+p.y**2))

enunciado_oculto = [p.x, p.y]










