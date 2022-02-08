{"cantidad_opciones":1, "cantidad_disponible":50}

def numero_por(numero):
    if numero==1:
        return ""
    elif numero==-1:
        return "-"
    else:
        return str(numero)+por()

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b = Racional(elegir(-6, 7, 0)), choice([Racional(1, choice([2,4,5,8,10])), Racional(randrange(2,8))])
letra_de_funcion = choice(["f", "g", "h"])
recorridos = [Matematica(letra_conjunto("R")),
    Matematica(letra_conjunto("R")+r"-\{0\}"),
    Matematica(letra_conjunto("R")+r"-\{1\}"),
    Matematica(fr"[0, +{INF()}["),
    Matematica(fr"]0, +{INF()}["),
    Matematica(fr"]-{INF()}, 0]"),
    Matematica(fr"]-{INF()}, 0[")
]

#================================Aquí va el enunciado================================================================
if a<0:
    enunciado = "Sea la función "+Matematica(f"{letra_de_funcion}(x)="+numero_por(a)+potencia(b,"x")) +f". Si el dominio de {letra_de_funcion} es "+Matematica(letra_conjunto("R"))+", su recorrido es"
elif 0<a:    
    enunciado = "Sea la función "+Matematica(f"{letra_de_funcion}(x)="+numero_por(a)+potencia(b,"x")) +f". Si el dominio de {letra_de_funcion} es "+Matematica(letra_conjunto('R'))+", su recorrido es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
if a<0:
    contenido_correcto = Matematica(fr"]-{INF()}, 0[")
elif 0<a:
    contenido_correcto = Matematica(fr"]0, +{INF()}[")

recorridos.remove(contenido_correcto)
contenido_2 = choice(recorridos)
recorridos.remove(contenido_2)
contenido_3 = choice(recorridos)
recorridos.remove(contenido_3)
contenido_4 = choice(recorridos)
recorridos.remove(contenido_4)
contenido_5 = choice(recorridos)
recorridos.remove(contenido_5)



enunciado_oculto = [a,b]










