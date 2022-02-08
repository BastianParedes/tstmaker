{"cantidad_opciones":1, "cantidad_disponible":50}

def calcular_razon(angulo, razon):
    while angulo<0:
        angulo += 360
    while 360<=angulo:
        angulo -= 360
    if 0<=angulo<=90:
        _angulo = angulo
    elif 90<angulo<=180:
        _angulo = 180-angulo
    elif 180<angulo<=270:
        _angulo = angulo-180
    elif 270<angulo<=360:
        _angulo = 360-angulo

    if razon=="sin":
        if _angulo==0:
            resultado = Racional(0)
        elif _angulo==30:
            resultado = Racional(1,2)
        elif _angulo==45:
            resultado = Root(2,2,Racional(1,2))
        elif _angulo==60:
            resultado = Root(3,2,Racional(1,2))
        elif _angulo==90:
            resultado = Racional(1)
        if 180<angulo:
            resultado = -1*resultado

    elif razon=="cos":
        if _angulo==0:
            resultado = Racional(1)
        elif _angulo==30:
            resultado = Root(3,2,Racional(1,2))
        elif _angulo==45:
            resultado = Root(2,2,Racional(1,2))
        elif _angulo==60:
            resultado = Racional(1,2)
        elif _angulo==90:
            resultado = Racional(0)
        if 90<angulo<270:
            resultado = -1*resultado

    elif razon=="tan":
        if _angulo==0:
            resultado = Racional(0)
        elif _angulo==30:
            resultado = Root(3,2,Racional(1,3))
        elif _angulo==45:
            resultado = Racional(1)
        elif _angulo==60:
            resultado = Root(3)
        elif _angulo==90:
            return None
        if 90<angulo<180 or 270<angulo<360:
            resultado = -1*resultado

    return resultado

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
x1, razon_1 = choice([0, 30, 45, 60])+choice([-1,1])*choice([1, 2, 3, 4])*choice([0, 90, 180, 270]), choice(["sin", "cos", "tan"])
while razon_1=="tan" and calcular_razon(x1, razon_1)==None:
    x1, razon_1 = choice([0, 30, 45, 60])+choice([-1,1])*choice([1, 2, 3, 4])*choice([0, 90, 180, 270]), choice(["sin", "cos", "tan"])

#================================Aquí va el enunciado================================================================
if x1<0:
    enunciado = "Calcula " + Matematica(fr"\{razon_1}({x1}°)=")
else:
    enunciado = "Calcula " + Matematica(fr"\{razon_1}{x1}°=")

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(calcular_razon(x1, razon_1))


enunciado_oculto = [razon_1, x1]
espacio_para_el_desarrollo = 8











