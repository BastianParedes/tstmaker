{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
p = randrange(0, 101)

if p==10 or p==20 or p==30 or p==40 or p==50 or p==60 or p==70 or p==80 or p==80 or p==90:
    n = 100
elif p==0 or p==100:
    n=10
else:
    n = 10000

for primo in Natural(p*(100-p)).lista_primos_divisores:
    if (Natural(p).lista_descomposicion_en_primos.count(primo)+Natural(100-p).lista_descomposicion_en_primos.count(primo)) %2 == 1:
        n *= primo
p=Racional(p)
#================================Aquí va el enunciado================================================================
enunciado = "Sea la variable aleatoria X tal que "+Matematica(fr"X\sim B({n}; {Racional(p,100,True)})", arreglar_espacios=True)+ ". La esperanza matemática de X es"

#================================Aquí se escriben los contenidos 0de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(n*p)
contenido_2 = Matematica(n*(p/100)*(1-p/100))
contenido_3 = Matematica(Racional(n*p,100))
contenido_4 = Matematica(Root(n*(p/100)*(1-p/100)))
contenido_5 = Matematica(p)

enunciado_oculto = [n, p]










