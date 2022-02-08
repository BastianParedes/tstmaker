{"cantidad_opciones":6, "cantidad_disponible":50}

if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c, d = Racional(randrange(2, 11)), Racional(randrange(2, 11)), Racional(randrange(2, 11)), Racional(randrange(2, 11))
    while not ((a+a+b+c+2*a)/4).denominador==1:
        a, b, c, d = Racional(randrange(2, 11)), Racional(randrange(2, 11)), Racional(randrange(2, 11)), Racional(randrange(2, 11))
    lista_datos = [a,a+b,c,a*2]
    suma_de_datos = 0
    for dato in lista_datos:
        suma_de_datos += dato
    #================================Aquí va el enunciado================================================================
    enunciado = f"En un campeonato de fútbol, Alejandro hizo {a} goles, {choice(['Marcelo','Cristian'])} hizo {b} más que Alejandro, {choice(['Pedro','Flavio'])} anotó {c} y {choice(['Ricardo','Francisco'])} hizo el doble de Alejandro. ¿Cuál es el promedio en las cantidades de goles de los jugadores?"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(Racional(suma_de_datos,len(lista_datos),True))#promedio
    contenido_2 = Matematica(max(lista_datos)-min(lista_datos))#rango
    contenido_3 = Matematica(suma_de_datos)#suma de todos los datos
    contenido_4 = Matematica(suma_de_datos*len(lista_datos))#suma los datos y multiplica
    contenido_5 = Matematica(Racional(max(lista_datos)-min(lista_datos),2,True))#mitad del rango


elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c, d, e, f = Racional(randrange(11, 71)), Racional(randrange(11, 71)), Racional(randrange(11, 71)), Racional(randrange(11, 71)), Racional(randrange(11, 71)), Racional(randrange(11, 71))
    while not ((a+b+c+d+e+f)/6).denominador==1:
        a, b, c, d, e, f = Racional(randrange(11, 71)), Racional(randrange(11, 71)), Racional(randrange(11, 71)), Racional(randrange(11, 71)), Racional(randrange(11, 71)), Racional(randrange(11, 71))
    lista_datos = [a,b,c,d,e,f]
    suma_de_datos = 0
    for dato in lista_datos:
        suma_de_datos += dato
    #================================Aquí va el enunciado================================================================
    enunciado = f"El promedio en matemática, de cierto estudiante, es {a} en lenguaje {b}, en {choice(['física','química','biología'])} {c}, en educación física {d}, en filosofía {e} y en ciencias sociales {f}. El promedio entre sus asignaturas es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(Racional(suma_de_datos,len(lista_datos),True))#promedio
    contenido_2 = Matematica(max(lista_datos)-min(lista_datos))#rango
    contenido_3 = Matematica(suma_de_datos)#suma de todos los datos
    contenido_4 = Matematica(suma_de_datos*len(lista_datos))#suma los datos y multiplica
    contenido_5 = Matematica(Racional(max(lista_datos)-min(lista_datos),2,True))#mitad del rango



elif opcion==3:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c, d, e, f, g = Racional(randrange(100, 10001, 100)), Racional(randrange(100, 10001, 100)), Racional(randrange(100, 10001, 100)), Racional(randrange(100, 10001, 100)), Racional(randrange(100, 10001, 100)), Racional(randrange(100, 10001, 100)), Racional(randrange(100, 10001, 100))
    while not ((a+b+c+d+e+f+g)/7).denominador==1:
        a, b, c, d, e, f, g = Racional(randrange(100, 10001, 100)), Racional(randrange(100, 10001, 100)), Racional(randrange(100, 10001, 100)), Racional(randrange(100, 10001, 100)), Racional(randrange(100, 10001, 100)), Racional(randrange(100, 10001, 100)), Racional(randrange(100, 10001, 100))
    lista_datos = [a,b,c,d,e,f,g]
    suma_de_datos = 0
    for dato in lista_datos:
        suma_de_datos += dato
    #================================Aquí va el enunciado================================================================
    enunciado = f"{choice(['Ricardo', 'Flavio', 'Marcelo', 'Javier', 'Cristian'])} gastó {a} pesos el día lunes, {b} el martes, {c} el miércoles, {d} el jueves, {e} el viernes, {f} el sábado y {g} el domingo. El promedio de dinero gastado durante la semana es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(Racional(suma_de_datos,len(lista_datos),True))+" pesos"#promedio
    contenido_2 = Matematica(max(lista_datos)-min(lista_datos))+" pesos"#rango
    contenido_3 = Matematica(suma_de_datos)+" pesos"#suma de todos los datos
    contenido_4 = Matematica(suma_de_datos*len(lista_datos))+" pesos"#suma los datos y multiplica
    contenido_5 = Matematica(Racional(max(lista_datos)-min(lista_datos),2,True))+" pesos"#mitad del rango


elif opcion==4:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c = Racional(randrange(150, 181)), Racional(randrange(150, 181)), Racional(randrange(150, 181))
    while not ((a+b+c)/3).denominador==1:
        a, b, c = Racional(randrange(150, 181)), Racional(randrange(150, 181)), Racional(randrange(150, 181))
    lista_datos = [a,b,c]
    suma_de_datos = 0
    for dato in lista_datos:
        suma_de_datos += dato
    #================================Aquí va el enunciado================================================================
    enunciado = f"En cierta escuela decidieron medir la estatura de tres estudiantes. {choice(['Ricardo','Flavio'])} mide {a} cm, {choice(['Marcelo','Alejandro'])} mide {b} cm y {choice(['Mauricio','Javier'])} mide {c} cm. El promedio en las estaturas es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(Racional(suma_de_datos,len(lista_datos),True))+" cm"#promedio
    contenido_2 = Matematica(max(lista_datos)-min(lista_datos))+" cm"#rango
    contenido_3 = Matematica(suma_de_datos)+" cm"#suma de todos los datos
    contenido_4 = Matematica(suma_de_datos*len(lista_datos))+" cm"#suma los datos y multiplica
    contenido_5 = Matematica(Racional(max(lista_datos)-min(lista_datos),2,True))+" cm"#mitad del rango


elif opcion==5:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c, d = Racional(randrange(2000, 10001)), Racional(randrange(2000, 10001)), Racional(randrange(2000, 10001)), Racional(randrange(2000, 10001))
    while not ((a+b+c+d)/4).denominador==1:
        a, b, c, d = Racional(randrange(2000, 10001)), Racional(randrange(2000, 10001)), Racional(randrange(2000, 10001)), Racional(randrange(2000, 10001))
    lista_datos = [a,b,c,d]
    suma_de_datos = 0
    for dato in lista_datos:
        suma_de_datos += dato
    #================================Aquí va el enunciado================================================================
    enunciado = f"Cierta empresa de buses desea revisar el estado de sus vehículos, para ello basta con calcular el promedio de los kilometrajes de cuatro máquinas. Al revisarlas se determina que el primer bus tiene un kilometraje de {a} km, el segundo {b} km, el tercero {c} km y el cuarto {d} km. ¿Cuál es el resultado del estudio de la empresa?"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(Racional(suma_de_datos,len(lista_datos),True))+" km"#promedio
    contenido_2 = Matematica(max(lista_datos)-min(lista_datos))+" km"#rango
    contenido_3 = Matematica(suma_de_datos)+" km"#suma de todos los datos
    contenido_4 = Matematica(suma_de_datos*len(lista_datos))+" km"#suma los datos y multiplica
    contenido_5 = Matematica(Racional(max(lista_datos)-min(lista_datos),2,True))+" km"#mitad del rango


elif opcion==6:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c = Racional(randrange(100, 201)), Racional(randrange(100, 201)), Racional(randrange(100, 201))
    while not ((a+b+c)/3).denominador==1:
        a, b, c = Racional(randrange(100, 201)), Racional(randrange(100, 201)), Racional(randrange(100, 201))
    lista_datos = [a,b,c]
    suma_de_datos = 0
    for dato in lista_datos:
        suma_de_datos += dato
    #================================Aquí va el enunciado================================================================
    enunciado = f"Para los teatros es importante determinar la cantidad de espectadores por función, porque ese dato les sirve para determinar si hay que hacer cambios en las horas y cantidad de funciones. El día lunes hubo {a} espectadores, el miércoles {b} y el viernes {c}. ¿Cuál es el promedio de espectadores?"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(Racional(suma_de_datos,len(lista_datos),True))#promedio
    contenido_2 = Matematica(max(lista_datos)-min(lista_datos))#rango
    contenido_3 = Matematica(suma_de_datos)#suma de todos los datos
    contenido_4 = Matematica(suma_de_datos*len(lista_datos))#suma los datos y multiplica
    contenido_5 = Matematica(Racional(max(lista_datos)-min(lista_datos),2,True))#mitad del rango



enunciado_oculto = [opcion, lista_datos]











