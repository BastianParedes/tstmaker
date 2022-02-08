{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
p1, p2 = Par(randrange(-10, 10), randrange(-10, 10)), Par(randrange(-10, 10), randrange(-10, 10))
while p1.x==p2.x and p1.y==p2.y:
    p1, p2 = Par(randrange(-10, 10), randrange(-10, 10)), Par(randrange(-10, 10), randrange(-10, 10))
#================================Aquí va el enunciado================================================================
enunciado = f"La distancia entre los puntos {Matematica(p1)} y {Matematica(p2)} es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(Root((p1.x-p2.x)**2+(p1.y-p2.y)**2))+" unidades"
contenido_2 = Matematica(Root(abs(p1.x-p2.x+p1.y-p2.y)))+" unidades"
contenido_3 = Matematica(Root((p1.x+p2.x)**2+(p1.y+p2.y)**2))+" unidades"
contenido_4 = Matematica(Root((p1.x-p1.y)**2+(p2.x-p2.y)**2))+" unidades"
contenido_5 = Matematica(Root((p1.x-p2.y)**2+(p1.y-p2.x)**2))+" unidades"

enunciado_oculto = [p1, p2]










