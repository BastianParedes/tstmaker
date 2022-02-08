{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a = elegir(-5,6,0,1)
n = elegir(-10,10,0)
letra_de_funcion = choice(["f", "g", "h"])
recorridos = [Matematica(letra_conjunto("R")),
    Matematica(letra_conjunto("R")+r"-\{0\}"),
    Matematica(fr"[0, +{INF()}["),
    Matematica(fr"]0, +{INF()}["),
    Matematica(fr"]-{INF()}, 0]"),
    Matematica(fr"]-{INF()}, 0[")
]

#================================Aquí va el enunciado================================================================
if 0<a and n<0 and n%2==0:#elevado a -2
    enunciado = "Sea la función "+Matematica(f"{letra_de_funcion}(x)="+Racional(a)*potencia("x",n)) +f". Si el dominio de {letra_de_funcion} es "+Matematica(letra_conjunto('R')+r'-\{0\}')+", su recorrido es"
elif 0<a and n<0 and n%2==1 and n!=1:#elevado a -3
    enunciado = "Sea la función "+Matematica(f"{letra_de_funcion}(x)="+Racional(a)*potencia("x",n)) +f". Si el dominio de {letra_de_funcion} es "+Matematica(letra_conjunto('R')+r'-\{0\}')+", su recorrido es"
elif 0<a and 0<n and n%2==0:#elevado a 2
    enunciado = "Sea la función "+Matematica(f"{letra_de_funcion}(x)="+Racional(a)*potencia("x",n)) +f". Si el dominio de {letra_de_funcion} es "+Matematica(letra_conjunto('R'))+", su recorrido es"
elif 0<a and 0<n and n%2==1:#elevado a 3
    enunciado = "Sea la función "+Matematica(f"{letra_de_funcion}(x)="+Racional(a)*potencia("x",n)) +f". Si el dominio de {letra_de_funcion} es "+Matematica(letra_conjunto('R'))+", su recorrido es"

elif a<0 and n<0 and n%2==0:#elevado a -2 negativo
    enunciado = "Sea la función "+Matematica(f"{letra_de_funcion}(x)="+Racional(a)*potencia("x",n)) +f". Si el dominio de {letra_de_funcion} es "+Matematica(letra_conjunto('R')+r'-\{0\}')+", su recorrido es"
elif a<0 and n<0 and n%2==1 and n!=1:#elevado a -3 negativo
    enunciado = "Sea la función "+Matematica(f"{letra_de_funcion}(x)="+Racional(a)*potencia("x",n)) +f". Si el dominio de {letra_de_funcion} es "+Matematica(letra_conjunto('R')+r'-\{0\}')+", su recorrido es"
elif a<0 and 0<n and n%2==0:#elevado a 2 negativo
    enunciado = "Sea la función "+Matematica(f"{letra_de_funcion}(x)="+Racional(a)*potencia("x",n)) +f". Si el dominio de {letra_de_funcion} es "+Matematica(letra_conjunto('R'))+", su recorrido es"
elif a<0 and 0<n and n%2==1:#elevado a 3 negativo
    enunciado = "Sea la función "+Matematica(f"{letra_de_funcion}(x)="+Racional(a)*potencia("x",n)) +f". Si el dominio de {letra_de_funcion} es "+Matematica(letra_conjunto('R'))+", su recorrido es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
if 0<a and n<0 and n%2==0:#elevado a -2
    contenido_correcto = Matematica(fr"]0, +{INF()}[")
elif 0<a and n<0 and n%2==1 and n!=1:#elevado a -3
    contenido_correcto = Matematica(letra_conjunto("R")+r"-\{0\}")
elif 0<a and 0<n and n%2==0:#elevado a 2
    contenido_correcto = Matematica(fr"[0, +{INF()}[")
elif 0<a and 0<n and n%2==1:#elevado a 3
    contenido_correcto = Matematica(letra_conjunto("R"))

elif a<0 and n<0 and n%2==0:#elevado a -2 negativo
    contenido_correcto = Matematica(fr"]-{INF()}, 0[")
elif a<0 and n<0 and n%2==1 and n!=1:#elevado a -3 negativo
    contenido_correcto = Matematica(letra_conjunto("R")+r"-\{0\}")
elif a<0 and 0<n and n%2==0:#elevado a 2 negativo
    contenido_correcto = Matematica(fr"]-{INF()}, 0]")
elif a<0 and 0<n and n%2==1:#elevado a 3 negativo
    contenido_correcto = Matematica(letra_conjunto("R"))

recorridos.remove(contenido_correcto)
contenido_2 = choice(recorridos)
recorridos.remove(contenido_2)
contenido_3 = choice(recorridos)
recorridos.remove(contenido_3)
contenido_4 = choice(recorridos)
recorridos.remove(contenido_4)
contenido_5 = choice(recorridos)
recorridos.remove(contenido_5)



enunciado_oculto = [a,n]










