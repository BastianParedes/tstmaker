{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
a, b, c, d, e, f = Racional(elegir(-2, 3,0)), Racional(elegir(-10, 10,0)), Racional(elegir(-10, 10,0)), Racional(elegir(-2, 3,0)), Racional(elegir(-10, 10,0)), Racional(elegir(-10, 10,0))
while d**2*f-a**2*c==0 or d*f-a*c==0 or d**2*f+a**2*c==0 or d*f+a*c==0 or a**2*b-d**2*e==0 or a*b-d*e==0 or a**2*b+d**2*e==0 or a*b+d*e==0:
    a, b, c, d, e, f = Racional(elegir(-10, 10,0)), Racional(elegir(-10, 10,0)), Racional(elegir(-10, 10,0)), Racional(elegir(-2, 2,0)), Racional(elegir(-10, 10,0)), Racional(elegir(-10, 10,0))

#================================Aquí va el enunciado================================================================
enunciado = "El valor de x que satisface la ecuación "+Matematica(a*raiz(Pol(b*"x",c,azar=True)) +"="+ d*raiz(Pol(e*"x",f,azar=True)))+" es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica((d**2*f-a**2*c)/(a**2*b-d**2*e))
contenido_2 = Matematica((d*f-a*c)/(a*b-d*e))
contenido_3 = Matematica((d**2*f+a**2*c)/(a**2*b+d**2*e))
contenido_4 = Matematica((d*f+a*c)/(a*b+d*e))
contenido_5 = Matematica(choice([-1,1])*choice([(d*f-a*c)/(a*b-d*e), (d**2*f+a**2*c)/(a**2*b+d**2*e), (d*f+a*c)/(a*b+d*e)])**(Racional(-1)))




enunciado_oculto = [a,b,c,d,e,f]










