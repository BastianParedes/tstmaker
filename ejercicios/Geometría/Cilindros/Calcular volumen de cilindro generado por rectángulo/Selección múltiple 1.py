{"cantidad_opciones":2, "cantidad_disponible":50}

#===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
lado_menor = Racional(randrange(1,15))
lado_mayor = Racional(randrange(1,15))
while not lado_menor<lado_mayor:
    lado_menor = Racional(randrange(1,15))
    lado_mayor = Racional(randrange(1,15))
unidad_de_medida = choice(["mm", "cm", "m", "km"])

perimetro = 2*lado_menor+2*lado_mayor
area = lado_menor*lado_mayor
diagonal = Root(lado_menor**2+lado_mayor**2)



if opcion==1:
    #===============================================Aquí va el número del ejercicio y el enunciado.
    enunciado = f"Uno de los lados de un rectángulo mide {Matematica(choice([lado_menor,lado_mayor])+' '+unidad_de_medida)} y "+choice([f"su perímetro mide {Matematica(perimetro+' '+unidad_de_medida)}",
        f"su área mide {Matematica(area+' '+potencia(unidad_de_medida,2,parentesis_automatico=False))}",
        f"su diagonal mide {Matematica(diagonal+' '+unidad_de_medida)}"])+". El volumen del cilindro generado al rotar el rectángulo, usando como eje su lado menor, es"
    #===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
    contenido_correcto = Matematica(lado_mayor**2*lado_menor*PI()+" "+potencia(unidad_de_medida,3,parentesis_automatico=False))
    contenido_2 =        Matematica((lado_mayor*2)**2*lado_menor*PI()+" "+potencia(unidad_de_medida,3,parentesis_automatico=False))
    contenido_3 =        Matematica((lado_mayor/2)**2*lado_menor*PI()+" "+potencia(unidad_de_medida,3,parentesis_automatico=False))
    contenido_4 =        Matematica(lado_menor**2*lado_mayor*PI()+" "+potencia(unidad_de_medida,3,parentesis_automatico=False))
    contenido_5 =        Matematica(choice([(lado_menor*2)**2*lado_mayor*PI(),(lado_menor/2)**2*lado_mayor*PI()])+" "+potencia(unidad_de_medida,3,parentesis_automatico=False))


elif opcion==2:
    #===============================================Aquí va el número del ejercicio y el enunciado.
    enunciado = f"Uno de los lados de un rectángulo mide {Matematica(choice([lado_menor,lado_mayor])+' '+unidad_de_medida)} y "+choice([f"su perímetro mide {Matematica(perimetro+' '+unidad_de_medida)}",
        f"su área mide {Matematica(area+' '+potencia(unidad_de_medida,2,parentesis_automatico=False))}",
        f"su diagonal mide {Matematica(diagonal+' '+unidad_de_medida)}"])+". El volumen del cilindro generado al rotar el rectángulo, usando como eje su lado mayor, es"
    #===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
    contenido_correcto = Matematica(lado_menor**2*lado_mayor*PI()+" "+potencia(unidad_de_medida,3,parentesis_automatico=False))
    contenido_2 =        Matematica((lado_menor*2)**2*lado_mayor*PI()+" "+potencia(unidad_de_medida,3,parentesis_automatico=False))
    contenido_3 =        Matematica((lado_menor/2)**2*lado_mayor*PI()+" "+potencia(unidad_de_medida,3,parentesis_automatico=False))
    contenido_4 =        Matematica(lado_mayor**2*lado_menor*PI()+" "+potencia(unidad_de_medida,3,parentesis_automatico=False))
    contenido_5 =        Matematica(choice([(lado_mayor*2)**2*lado_menor*PI(),(lado_mayor/2)**2*lado_menor*PI()])+" "+potencia(unidad_de_medida,3,parentesis_automatico=False))


enunciado_oculto = [lado_mayor, lado_menor]











