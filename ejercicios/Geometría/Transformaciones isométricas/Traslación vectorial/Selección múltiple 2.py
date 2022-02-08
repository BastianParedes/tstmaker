{"cantidad_opciones":2, "cantidad_disponible":50}

# pp = p + v
#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
p, v = Par(elegir(-9,10,0), elegir(-9,10,0)) , Par(elegir(-9,10,0), elegir(-9,10,0))
pp = p + v
letra = choice(['A', 'B', 'C', 'P', 'Q'])


if opcion==1:
    #================================Aquí va el enunciado================================================================
    enunciado = f'Si el punto {letra} es la imagen que se obtiene al trasladar el punto {Matematica(p)} según el vector {Matematica(v)}, ¿cuál es la distancia entre el vector  y {letra}?'
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(pp.distancia(v))
    contenido_2 =        Matematica(pp.distancia(p))
    contenido_3 =        Matematica(p.distancia(v))
    contenido_4 =        Matematica(abs(pp+p))
    contenido_5 =        Matematica(abs(pp+v))


elif opcion==2:
    #================================Aquí va el enunciado================================================================
    enunciado = f'Si el punto {Matematica(pp)} es la imagen que se obtiene al trasladar el punto {Matematica(letra+p)}, la distancia entre {letra} y el vector de traslación, es'
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(p.distancia(v))
    contenido_2 =        Matematica(p.distancia(pp))
    contenido_3 =        Matematica(v.distancia(pp))
    contenido_4 =        Matematica(abs(pp+p))
    contenido_5 =        Matematica(abs(pp+v))



enunciado_oculto = [p, v]
