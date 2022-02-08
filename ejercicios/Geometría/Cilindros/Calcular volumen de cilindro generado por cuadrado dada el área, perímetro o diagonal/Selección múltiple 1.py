{"cantidad_opciones":3, "cantidad_disponible":50}

#===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
lado = Racional(randrange(2,25))
unidad_de_medida = choice(["mm", "cm", "m", "km"])

if opcion==1:
    #===============================================Aquí va el número del ejercicio y el enunciado.
    enunciado = f"El perímetro de un cuadrado mide {Matematica(4*lado+' '+unidad_de_medida)}. El volumen del cuerpo generado al rotar dicho cuadrado en torno a uno de sus lados es"
    #===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
    contenido_correcto = Matematica(lado**3*PI()+" "+potencia(unidad_de_medida,3,parentesis_automatico=False))
    contenido_2 = Matematica(lado**3*PI()/4+" "+potencia(unidad_de_medida,3,parentesis_automatico=False))
    contenido_3 = Matematica((4*lado)**3*PI()+" "+potencia(unidad_de_medida,3,parentesis_automatico=False))
    contenido_4 = Matematica((4*lado)**3*PI()/4+" "+potencia(unidad_de_medida,3,parentesis_automatico=False))
    contenido_5 = Matematica(2*lado**2*PI()+" "+potencia(unidad_de_medida,3,parentesis_automatico=False))

elif opcion==2:
    #===============================================Aquí va el número del ejercicio y el enunciado.
    enunciado = f"El área de un cuadrado mide {Matematica(lado**2+' '+potencia(unidad_de_medida,2,parentesis_automatico=False))}. El volumen del cuerpo generado al rotar dicho cuadrado en torno a uno de sus lados es"
    #===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
    contenido_correcto = Matematica(lado**3*PI()+" "+potencia(unidad_de_medida,3,parentesis_automatico=False))
    contenido_2 = Matematica(lado**3*PI()/4+" "+potencia(unidad_de_medida,3,parentesis_automatico=False))
    contenido_3 = Matematica((lado**2)**3*PI()+" "+potencia(unidad_de_medida,3,parentesis_automatico=False))
    contenido_4 = Matematica((lado**2)**3*PI()/4+" "+potencia(unidad_de_medida,3,parentesis_automatico=False))
    contenido_5 = Matematica(2*lado**2*PI()+" "+potencia(unidad_de_medida,3,parentesis_automatico=False))

elif opcion==3:
    #===============================================Aquí va el número del ejercicio y el enunciado.
    enunciado = f"La diagonal de un cuadrado mide {Matematica(lado*Root(2)+' '+unidad_de_medida)}. El volumen del cuerpo generado al rotar dicho cuadrado en torno a uno de sus lados es"
    #===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
    contenido_correcto = Matematica(lado**3*PI()+" "+potencia(unidad_de_medida,3,parentesis_automatico=False))
    contenido_2 = Matematica(lado**3*PI()/4+" "+potencia(unidad_de_medida,3,parentesis_automatico=False))
    contenido_3 = Matematica((4*lado*Root(2))**3*PI()+" "+potencia(unidad_de_medida,3,parentesis_automatico=False))
    contenido_4 = Matematica((4*lado*Root(2))**3*PI()/4+" "+potencia(unidad_de_medida,3,parentesis_automatico=False))
    contenido_5 = Matematica(2*lado**2*PI()+" "+potencia(unidad_de_medida,3,parentesis_automatico=False))




enunciado_oculto = [opcion, lado]











