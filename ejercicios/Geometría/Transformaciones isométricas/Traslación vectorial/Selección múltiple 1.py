{"cantidad_opciones":3, "cantidad_disponible":50}

# pp = p + v
#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
p, v = Par(elegir(-9,10,0), elegir(-9,10,0)) , Par(elegir(-9,10,0), elegir(-9,10,0))
pp = p+v
letra = choice(['A', 'B', 'C', 'P', 'Q'])


if opcion==1:
    #================================Aquí va el enunciado================================================================
    enunciado = f'Si el punto {letra} es la imagen que se obtiene al trasladar el punto {Matematica(p)} según el vector {Matematica(v)}, ¿cuáles son las coordenadas de {letra}?'
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(pp)
    contenido_2 =        Matematica(p*v)
    contenido_3 =        Matematica(-pp)
    contenido_4 =        Matematica(p-v)
    contenido_5 =        Matematica(v-p)


elif opcion==2:
    #================================Aquí va el enunciado================================================================
    enunciado = f'Si el punto {Matematica(pp)} es la imagen que se obtiene al trasladar el punto {letra} según el vector {Matematica(v)}, ¿cuáles son las coordenadas de {letra}?'
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(p)
    contenido_2 =        Matematica(v-pp)
    contenido_3 =        Matematica(Par(pp.x*v.x , pp.y*v.y))
    contenido_4 =        Matematica(pp+v)
    contenido_5 =        Matematica((pp+v)/2)



elif opcion==3:
    #================================Aquí va el enunciado================================================================
    enunciado = f'Si el punto {Matematica(pp)} es la imagen que se obtiene al trasladar el punto {Matematica(p)}, el vector de traslación es'
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(v)
    contenido_2 =        Matematica(p-pp)
    contenido_3 =        Matematica(pp+p)
    contenido_4 =        Matematica(Par(pp.x*p.x , pp.y*p.y))
    contenido_5 =        Matematica((p+pp)/2)



enunciado_oculto = [p, v]
