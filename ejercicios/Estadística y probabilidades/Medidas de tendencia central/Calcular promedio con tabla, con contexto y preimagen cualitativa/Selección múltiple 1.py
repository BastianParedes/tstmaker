{"cantidad_opciones":6, "cantidad_disponible":50}

def tabla(titulo_izquierdo, titulo_derecho, *pares_de_datos):
    resultado = r"""\begin{center} \begin{tabular}{|c|c|}
    \hline
    """+fr"{titulo_izquierdo}&{titulo_derecho}\\ \hline"+"\n"
    for par in pares_de_datos:
        resultado = resultado + str(par[0])+"&"+str(par[1])+r"\\ \hline"+"\n"
    resultado = resultado+r"\end{tabular} \end{center}"+"\n"
    return resultado

lista_de_nombres = ["Aarón", "Ander", "Joaquín", "Abel", "Andrés", "Joel", "Abelardo", "Ángel", "Jon", "Abraham", "Aníbal", "Jordi", "Adalberto", "Antonio", "Jorge", "Adam", "Arnau", "José", "Adán", "Arturo", "Jose", "Antonio", "Adiran", "Asier", "Jose", "Luis", "Adolfo", "Augusto", "Jose", "Manuel", "Adrià", "Aurelio", "Jose", "Maria", "Adrián", "Baltasar", "Juan", "Agustín", "Bartolomé", "Blas", "Aimar", "Basilio", "Juan", "Antonio", "Aitor", "Benito", "Boris", "Alano", "Benjamín", "Juan", "Carlos", "Alberto", "Bernardo", "Borja", "Aldo", "Brahim", "Aleix", "Blas", "Brais", "Alejandro", "Boris", "Bruno", "Alejo", "Borja", "Calisto", "Alex", "Brahim", "Juan", "José", "Alfonso", "Brais", "Camilo", "Alfredo", "Bruno", "Juan", "Manuel", "Alonso", "Calisto", "Carlos", "Álvaro", "Camilo", "Julio", "Amadeo", "Carlos", "Cayetano", "Amado", "Cayetano", "César","Amando", "César", "Christian", "Ambrosio", "Christian", "Claudio", "Amin", "Claudio", "Clemente", "Anastasio", "Clemente", "Conrado", "Ander", "Conrado", "Constantino"]
nombre_1 = choice(lista_de_nombres)
lista_de_nombres.remove(nombre_1)
nombre_2 = choice(lista_de_nombres)
lista_de_nombres.remove(nombre_2)
nombre_3 = choice(lista_de_nombres)
lista_de_nombres.remove(nombre_3)
nombre_4 = choice(lista_de_nombres)
lista_de_nombres.remove(nombre_4)
nombre_5 = choice(lista_de_nombres)
lista_de_nombres.remove(nombre_5)
nombre_6 = choice(lista_de_nombres)
lista_de_nombres.remove(nombre_6)

if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c, d, e = Racional(randrange(2, 11)), Racional(randrange(2, 11)), Racional(randrange(2, 11)), Racional(randrange(2, 11)), Racional(randrange(2, 11))
    while not ((a+b+c+d+e)/4).denominador==1:
        a, b, c, d, e = Racional(randrange(2, 11)), Racional(randrange(2, 11)), Racional(randrange(2, 11)), Racional(randrange(2, 11)), Racional(randrange(2, 11))
    #================================Aquí va el enunciado================================================================
    enunciado = "En un campeonato de fútbol se calcularon las cantidades de goles que hizo cada jugador y se resumió toda la información en la siguiente tabla"+tabla("Jugador","Cantidad de goles", [nombre_1,a], [nombre_2,b], [nombre_3,c], [nombre_4,d], [nombre_5,e])+"El promedio de goles realizados por los jugadores es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(Racional(a+b+c+d+e,5,True))
    contenido_2 = Matematica(Racional(a+b+c+d+e,4,True))
    contenido_3 = Matematica(a+b+c+d+e)
    contenido_4 = Matematica(min(a,b,c,d,e))
    contenido_5 = Matematica(Racional(sorted([a,b,c,d,e])[0]+sorted([a,b,c,d,e])[-1],2,True))
    enunciado_oculto = [opcion, a, b, c, d, e]


elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c, d, e, f = Racional(randrange(11, 71)), Racional(randrange(11, 71)), Racional(randrange(11, 71)), Racional(randrange(11, 71)), Racional(randrange(11, 71)), Racional(randrange(11, 71))
    while not ((a+b+c+d+e+f)/6).denominador==1:
        a, b, c, d, e, f = Racional(randrange(11, 71)), Racional(randrange(11, 71)), Racional(randrange(11, 71)), Racional(randrange(11, 71)), Racional(randrange(11, 71)), Racional(randrange(11, 71))
    #================================Aquí va el enunciado================================================================
    enunciado = f"Los promedios de {nombre_1} fueron resumidos en la siguiente tabla"+tabla("Asignatura","Promedio",["Lenguaje",a] ,[choice(['física','química','biología']),b] ,["Educación física",c] ,["Filosofía",d] ,["Psicología",e] ,["Ciencias sociales",f])+f"El promedio general de {nombre_1} es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(Racional(a+b+c+d+e+f,6,True))
    contenido_2 = Matematica(Racional(a+b+c+2*a,2,True))
    contenido_3 = Matematica(a+b+c+d+e+f)
    contenido_4 = Matematica((a+b+c+d+e+f)*6)
    contenido_5 = Matematica(Racional(sorted([a,b,c,d,e,f])[2]+sorted([a,b,c,d,e,f])[3],2,True))
    enunciado_oculto = [opcion, a, b, c, d, e, f]


elif opcion==3:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c, d, e, f, g = Racional(randrange(100, 10001, 100)), Racional(randrange(100, 10001, 100)), Racional(randrange(100, 10001, 100)), Racional(randrange(100, 10001, 100)), Racional(randrange(100, 10001, 100)), Racional(randrange(100, 10001, 100)), Racional(randrange(100, 10001, 100))
    while not ((a+b+c+d+e+f+g)/7).denominador==1:
        a, b, c, d, e, f, g = Racional(randrange(100, 10001, 100)), Racional(randrange(100, 10001, 100)), Racional(randrange(100, 10001, 100)), Racional(randrange(100, 10001, 100)), Racional(randrange(100, 10001, 100)), Racional(randrange(100, 10001, 100)), Racional(randrange(100, 10001, 100))
    #================================Aquí va el enunciado================================================================
    enunciado = f"En la siguiente tabla se resume los gastos diarios de {nombre_1}"+tabla("Día","Dinero gastado en pesos",["Lunes",a], ["Martes",b], ["Miércoles",c], ["Jueves",d], ["Viernes",e], ["Sábado",f], ["Domingo",g])
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(Racional(a+b+c+d+e+f+g,7,True)+" pesos")
    contenido_2 = Matematica(Racional(a+b+c+d+e+f+g,2,True)+" pesos")
    contenido_3 = Matematica(a+b+c+d+e+f+g+" pesos")
    contenido_4 = Matematica((a+b+c+d+e+f+g)*6+" pesos")
    contenido_5 = Matematica(Racional(sorted([a,b,c,d,e,f,g])[3])+" pesos")
    enunciado_oculto = [opcion, a, b, c, d, e, f, g]


elif opcion==4:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c = Racional(randrange(150, 181)), Racional(randrange(150, 181)), Racional(randrange(150, 181))
    while not ((a+b+c)/3).denominador==1:
        a, b, c = Racional(randrange(150, 181)), Racional(randrange(150, 181)), Racional(randrange(150, 181))
    #================================Aquí va el enunciado================================================================
    enunciado = "En cierta escuela se decidió medir la estatura a tres estudiantes. Los resultados se muestran en la siguiente tabla"+tabla("Estudiante", "Estatura en cm",[nombre_1,a], [nombre_2,b], [nombre_3,c])+"La estatura promedio entre los tres es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(Racional(a+b+c,3,True)+" cm")
    contenido_2 = Matematica(Racional(a+b+c,2,True)+" cm")
    contenido_3 = Matematica(a+b+c+" cm")
    contenido_4 = Matematica(Racional(a*b*c,3,True)+" cm")
    contenido_5 = Matematica(a*b*c+" cm")
    enunciado_oculto = [opcion, a, b, c]


elif opcion==5:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c, d = Racional(randrange(2000, 10001)), Racional(randrange(2000, 10001)), Racional(randrange(2000, 10001)), Racional(randrange(2000, 10001))
    while not ((a+b+c+d)/4).denominador==1:
        a, b, c, d = Racional(randrange(2000, 10001)), Racional(randrange(2000, 10001)), Racional(randrange(2000, 10001)), Racional(randrange(2000, 10001))
    #================================Aquí va el enunciado================================================================
    enunciado = "Cierta empresa de buses desea revisar el estado de sus vehículos, para ello construye la siguiente tabla"+tabla("Número del vehículo","Kilometraje", [1,a], [2,b], [3,c], [4,d])+"El promedio de los kilometrajes entre las máquinas es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(Racional(a+b+c+d,4,True)+" km")
    contenido_2 = Matematica(Racional(a+b+c+d,2,True)+" km")
    contenido_3 = Matematica(a+b+c+d+" km")
    contenido_4 = Matematica(Racional(a*b*c*d,4,True)+" km")
    contenido_5 = Matematica(Racional(sorted([a,b,c,d])[1]+sorted([a,b,c,d])[2], 2, True)+" km")
    enunciado_oculto = [opcion, a, b, c, d]


elif opcion==6:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c = Racional(randrange(100, 201)), Racional(randrange(100, 201)), Racional(randrange(100, 201))
    while not ((a+b+c)/3).denominador==1:
        a, b, c = Racional(randrange(100, 201)), Racional(randrange(100, 201)), Racional(randrange(100, 201))
    #================================Aquí va el enunciado================================================================
    enunciado = "Para los teatros es importante determinar la cantidad de espectadores por función, porque ese dato les sirve para determinar si hay que hacer cambios en las horas y cantidad de funciones. Para controlar este dato se hizo un estudio y se obtuvo la siguiente tabla"+tabla("Día", "Cantidad de espectadores", ["Lunes",a], ["Miércoles",b], ["Viernes",c])+"La cantidad promedio de espectadores por día es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(Racional(a+b+c,3,True))
    contenido_2 = Matematica(Racional(a+b+c,2,True))
    contenido_3 = Matematica(a+b+c)
    contenido_4 = Matematica(Racional(sorted([a,b,c])[0]+sorted([a,b,c])[2], 2, True))
    contenido_5 = Matematica(sorted([a,b,c])[1])
    enunciado_oculto = [opcion, a, b, c]











