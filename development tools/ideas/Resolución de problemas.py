from Definiciones import *

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
r = racional(randrange(1, 5))*3
precio = racional(randrange(1, 10))*100
opcion = choice([1,2])
unidad_de_medida = choice("mm", "cm", "m", "km")


if opcion==1:
    #================================Aquí va el enunciado================================================================
    enunciado = "Se quieres pintar un edificio con forma de semiesfera cuyo "+choice(["radio mide "+r, "diámetro mide "+2*r])+" metros. Si pintar "+Matematica("1 "+potencia("m",2))+" cuesta "+precio+" pesos se va a gastar"

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(4*r**2*PI()*precio)+" pesos"
    contenido_2 = Matematica(racional(4,3)*r**3*PI()*precio)+" pesos"
    contenido_3 = Matematica(2*r*PI()*precio)+" pesos"
    contenido_4 = Matematica(4*(2*r)**2*PI()*precio)+" pesos"
    contenido_5 = Matematica(r**2*PI()*precio)+" pesos"


elif opcion==2:
    #================================Aquí va el enunciado================================================================
    enunciado = "Una esfera rellena cuyo "+choice(["radio mide "+r, "diámetro mide "+2*r])+unidad_de_medida+" es cortada a la mitad y se conserva una parte. La superficie de la figura que queda mide"

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica((4*r**2+r**2)*PI()+" "+potencia(unidad_de_medida,2))
    contenido_2 = Matematica(4*r**2*PI()+" "+potencia(unidad_de_medida,2))
    contenido_3 = Matematica(r**2*PI()+" "+potencia(unidad_de_medida,2))
    contenido_4 = Matematica(racional(4,3)*r**3*PI()+" "+potencia(unidad_de_medida,2))
    contenido_5 = Matematica(2*r*PI()+" "+potencia(unidad_de_medida,2))


elif opcion==3:
    radio_menor = racional(randrange(1, 5))*3
    while not radio_menor<r:
        r = racional(randrange(1, 5))*3
        radio_menor = racional(randrange(1, 5))*3

    #================================Aquí va el enunciado================================================================
    enunciado = "Se mete una esfera de cuyo "+choice(["radio mide "+r, "diámetro mide "+2*r])+unidad_de_medida+" dentro de otra cuyo "+choice(["radio mide "+r, "diámetro mide "+2*r])+unidad_de_medida+". El espacio que queda entre las dos esferas mide"

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(racional(4,3)*r**3*PI()-racional(4,3)*radio_menor**3*PI()+" "+potencia(unidad_de_medida,3))
    contenido_2 = Matematica(racional(4,3)*r**3*PI()+" "+potencia(unidad_de_medida,3))
    contenido_3 = Matematica(racional(4,3)*radio_menor**3*PI()+" "+potencia(unidad_de_medida,3))
    contenido_4 = Matematica(4*r**2*PI()-4*radio_menor**2*PI()+" "+potencia(unidad_de_medida,3))
    contenido_5 = Matematica(4*r**2*PI()+" "+potencia(unidad_de_medida,3))


elif opcion==4:
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica()

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica()
    contenido_2 = Matematica()
    contenido_3 = Matematica()
    contenido_4 = Matematica()
    contenido_5 = Matematica()


elif opcion==5:
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica()

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica()
    contenido_2 = Matematica()
    contenido_3 = Matematica()
    contenido_4 = Matematica()
    contenido_5 = Matematica()


elif opcion==:
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica()

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica()
    contenido_2 = Matematica()
    contenido_3 = Matematica()
    contenido_4 = Matematica()
    contenido_5 = Matematica()


elif opcion==:
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica()

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica()
    contenido_2 = Matematica()
    contenido_3 = Matematica()
    contenido_4 = Matematica()
    contenido_5 = Matematica()


elif opcion==:
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica()

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica()
    contenido_2 = Matematica()
    contenido_3 = Matematica()
    contenido_4 = Matematica()
    contenido_5 = Matematica()


elif opcion==:
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica()

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica()
    contenido_2 = Matematica()
    contenido_3 = Matematica()
    contenido_4 = Matematica()
    contenido_5 = Matematica()


elif opcion==:
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica()

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica()
    contenido_2 = Matematica()
    contenido_3 = Matematica()
    contenido_4 = Matematica()
    contenido_5 = Matematica()


elif opcion==:
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica()

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica()
    contenido_2 = Matematica()
    contenido_3 = Matematica()
    contenido_4 = Matematica()
    contenido_5 = Matematica()


elif opcion==:
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica()

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica()
    contenido_2 = Matematica()
    contenido_3 = Matematica()
    contenido_4 = Matematica()
    contenido_5 = Matematica()




enunciado_oculto = enunciado



