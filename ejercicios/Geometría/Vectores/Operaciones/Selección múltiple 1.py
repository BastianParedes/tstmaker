{"cantidad_opciones":2, "cantidad_disponible":50}


if opcion == 1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    v1 = Par( elegir(-9,10,0) , elegir(-9,10,0)  )
    v2 = Par( elegir(-9,10,0) , elegir(-9,10,0)  )

    n1 = Racional(elegir(-9,10,0))
    n2 = Racional(elegir(-9,10,0))

    #================================Aquí va el enunciado================================================================
    enunciado = f"Sean los vectores " + Matematica(vector("u")+"="+v1) + " y " + Matematica(vector("v")+"="+v2) + ". ¿Cuál de los siguientes vectores corresponde al vector " + Matematica(Pol(n1*vector("u") , n2*vector("v"), azar=True, parentesis=True)) + "?"

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(n1*v1 + n2*v2)
    contenido_2 =        Matematica(v1+v2) # solo suma los vectores
    contenido_3 =        Matematica(Par(n1,n1) + v1 + Par(n2,n2) + v2) #en lugar de multiplicar, suma
    contenido_4 =        Matematica(Par(n1*v1.x , v1.y) + Par(n2*v2.x , v2.y)) #Solo multiplican al eje x
    contenido_5 =        Matematica(Par(v1.x , n1*v1.y) + Par(v2.x , n2*v2.y)) #Solo multiplican al eje y

    enunciado_oculto = [v1,v2]



elif opcion == 2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    v1 = Par( elegir(-9,10,0) , elegir(-9,10,0)  )
    v2 = Par( elegir(-9,10,0) , elegir(-9,10,0)  )
    v3 = Par( elegir(-9,10,0) , elegir(-9,10,0)  )

    n1 = Racional(elegir(-9,10,0))
    n2 = Racional(elegir(-9,10,0))
    n3 = Racional(elegir(-9,10,0))

    #================================Aquí va el enunciado================================================================
    enunciado = f"Sean los vectores " + Matematica(vector("u")+"="+v1) + ", " + Matematica(vector("v")+"="+v2) + " y " + Matematica(vector("w")+"="+v3) + ". ¿Cuál de los siguientes vectores corresponde al vector " + Matematica(Pol(n1*vector("u") , n2*vector("v") , n3*vector("w"), azar=True, parentesis=True)) + "?"

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(n1*v1 + n2*v2 + n3*v3)
    contenido_2 =        Matematica(v1+v2+v3) # solo suma los vectores
    contenido_3 =        Matematica(Par(n1,n1) + v1 + Par(n2,n2) + v2 + Par(n3,n3) + v3) #en lugar de multiplicar, suma
    contenido_4 =        Matematica(Par(n1*v1.x , v1.y) + Par(n2*v2.x , v2.y) + Par(n3*v3.x , v3.y)) #Solo multiplican al eje x
    contenido_5 =        Matematica(Par(v1.x , n1*v1.y) + Par(v2.x , n2*v2.y) + Par(v3.x , n3*v3.y)) #Solo multiplican al eje y

    enunciado_oculto = [v1,v2,v3]











