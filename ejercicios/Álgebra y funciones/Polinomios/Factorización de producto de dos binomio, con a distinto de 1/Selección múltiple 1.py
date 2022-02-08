{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
ab = []
cd = []
a, b, c, d = 0, 0, 0, 0
while a*d+b*c==0 or a*c<0 or a*c==1 or len(ab)!=0 or len(cd)!=0 or a<0 or c<0 or a==b:
    ab = []
    cd = []
    a = Racional(elegir(-6,7,0))
    b = Racional(elegir(-6,7,0))
    c = Racional(elegir(-6,7,0))
    d = Racional(elegir(-6,7,0))
    for i in range(2, abs(a.numerador)+abs(b.numerador)+1):
        if a.numerador%i==b.numerador%i==0:
            ab.append(i)
    for i in range(2, abs(c.numerador)+abs(d.numerador)+1):
        if c.numerador%i==d.numerador%i==0:
            cd.append(i)

#================================Aquí va el enunciado================================================================
enunciado = "La factorización de " + Matematica(Pol(Term(a*c,{"x":2}), (a*d+b*c)*"x", b*d)) + " es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.=
if a==c and b==d:
    contenido_correcto = Matematica(potencia(Pol(a*"x", b), 2))
else:
    contenido_correcto = Matematica("("+ Pol(a*"x", b)+")("+ Pol(c*"x", d)+")")


if b==d:
    contenido_2 = Matematica(potencia(Pol("x",b), 2))
else:
    contenido_2 = Matematica("("+ Pol("x",b)+")("+ Pol("x",d)+")")

contenido_3 = Matematica("("+ Pol("x",a)+")("+ Pol("x",c)+")")
contenido_4 = Matematica("("+ Pol(a*"x",a)+")("+ Pol(c*"x",d)+")")
contenido_5 = Matematica(potencia(Pol(b*"x", a), 2))

enunciado_oculto = [a, b, c, d]










