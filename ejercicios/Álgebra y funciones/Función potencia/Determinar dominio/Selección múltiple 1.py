{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a = elegir(-5,6,0,1)
n = elegir(-10,10,0)
letra_de_funcion = choice(["f", "g", "h"])
dominios = [Matematica(letra_conjunto("R")),
    Matematica(letra_conjunto("R")+r"-\{0\}"),
    Matematica(fr"[0, +{INF()}["),
    Matematica(fr"]0, +{INF()}["),
    Matematica(fr"]-{INF()}, 0]"),
    Matematica(fr"]-{INF()}, 0[")
]
#================================Aquí va el enunciado================================================================
enunciado = "Sea la función "+Matematica(f"{letra_de_funcion}(x)="+Racional(a)*potencia("x",n)) +f". De los siguientes dominios, el mayor que puede tener {letra_de_funcion} es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
if n<0 and n%2==0:
    contenido_correcto = dominios[1]
elif n<0 and n%2==1 and n!=1:
    contenido_correcto = dominios[1]
elif n==1:
    contenido_correcto = dominios[0]
elif 0<n and n%2==0:
    contenido_correcto = dominios[0]
elif 0<n and n%2==1:
    contenido_correcto = dominios[0]

dominios.remove(contenido_correcto)
contenido_2 = choice(dominios)
dominios.remove(contenido_2)
contenido_3 = choice(dominios)
dominios.remove(contenido_3)
contenido_4 = choice(dominios)
dominios.remove(contenido_4)
contenido_5 = choice(dominios)
dominios.remove(contenido_5)



enunciado_oculto = [a,n]










