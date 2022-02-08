{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
def numero_por(numero):
    if numero==1:
        return ""
    elif numero==-1:
        return "-"
    else:
        return str(numero)+por()

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b, h = Racional(elegir(-6, 7, 0)), choice([Racional(1, choice([2,4,5,8,10])), Racional(randrange(2,8))]), Racional(elegir(-5,6,0))
letra_de_funcion = choice(["f", "g", "h"])

#================================Aquí va el enunciado================================================================
enunciado = "Sean las funciones "+Matematica(f"{letra_de_funcion}(x)="+numero_por(a)+potencia(b,"x")) +" y "+Matematica(f"{letra_de_funcion.upper()}(x)="+numero_por(a)+potencia(b,Pol("x",-h)))+". Es verdadero que si la gráfica de"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
if h<0:
    contenido_correcto = choice([f"{letra_de_funcion} se traslada {abs(h)} unidades a la izquierda se obtiene la gráfica de {letra_de_funcion.upper()}"  , f"{letra_de_funcion.upper()} se traslada {abs(h)} unidades a la derecha se obtiene la gráfica de {letra_de_funcion}"])
    contenido_2 = choice([f"{letra_de_funcion} se traslada {abs(h)} unidades a la derecha se obtiene la gráfica de {letra_de_funcion.upper()}"  , f"{letra_de_funcion.upper()} se traslada {abs(h)} unidades a la izquierda se obtiene la gráfica de {letra_de_funcion}"])
elif 0<h:
    contenido_correcto = choice([f"{letra_de_funcion} se traslada {abs(h)} unidades a la derecha se obtiene la gráfica de {letra_de_funcion.upper()}"  , f"{letra_de_funcion.upper()} se traslada {abs(h)} unidades a la izquierda se obtiene la gráfica de {letra_de_funcion}"])
    contenido_2 = choice([f"{letra_de_funcion} se traslada {abs(h)} unidades a la izquierda se obtiene la gráfica de {letra_de_funcion.upper()}"  , f"{letra_de_funcion.upper()} se traslada {abs(h)} unidades a la derecha se obtiene la gráfica de {letra_de_funcion}"])
contenido_3 = choice([f"{letra_de_funcion} se traslada {abs(h)} unidades a hacia abajo se obtiene la gráfica de {letra_de_funcion.upper()}"  , f"{letra_de_funcion.upper()} se traslada {abs(h)} unidades a hacia arriba se obtiene la gráfica de {letra_de_funcion}"])
contenido_4 = choice([f"{letra_de_funcion} se traslada {abs(h)} unidades hacia arriba se obtiene la gráfica de {letra_de_funcion.upper()}"  , f"{letra_de_funcion.upper()} se traslada {abs(h)} unidades hacia abajo se obtiene la gráfica de {letra_de_funcion}"])
contenido_5 = choice([f"{letra_de_funcion} se contrae verticalmente {abs(h)} unidades se obtiene la gráfica de {letra_de_funcion.upper()}",
f"{letra_de_funcion.upper()} se dilata verticalmente {abs(h)} unidades se obtiene la gráfica de {letra_de_funcion}",
f"{letra_de_funcion} se dilata verticalmente {abs(h)} unidades se obtiene la gráfica de {letra_de_funcion.upper()}",
f"{letra_de_funcion.upper()} se contrae verticalmente {abs(h)} unidades se obtiene la gráfica de {letra_de_funcion}",
f"{letra_de_funcion} se contrae horizontalmente {abs(h)} unidades se obtiene la gráfica de {letra_de_funcion.upper()}",
f"{letra_de_funcion.upper()} se dilata horizontalmente {abs(h)} unidades se obtiene la gráfica de {letra_de_funcion}",
f"{letra_de_funcion} se dilata horizontalmente {abs(h)} unidades se obtiene la gráfica de {letra_de_funcion.upper()}",
f"{letra_de_funcion.upper()} se contrae horizontalmente {abs(h)} unidades se obtiene la gráfica de {letra_de_funcion}"])



enunciado_oculto = [a,b,h]










