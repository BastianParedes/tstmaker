{"cantidad_opciones":8, "cantidad_disponible":50}

if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c, d, e = Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0))
    while a*b-d==0 or a*b+a*c==0 or a*b+c==0 or a-d==0:
        a, b, c, d, e = Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0))
    #================================Aquí va el enunciado================================================================
    enunciado = "El valor de x que satisface la ecuación "+Matematica((a*"(").show+Pol(b*"x", c)+")="+Pol(d*"x", e))+" es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica((e-a*c)/(a*b-d))
    contenido_2 = Matematica((e-c)/(a*b-d))
    contenido_3 = Matematica((d+e)/(a*b+a*c))
    contenido_4 = Matematica((d+e)/(a*b+c))
    contenido_5 = Matematica((e-a*c)/(a-d))
    enunciado_oculto = [opcion,a,b,c,d,e]



elif opcion==2:
    a, b, c, d, e = Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0))
    while c*d-b==0 or c*d+b==0 or c*d-b==0 or d-b==0:
        a, b, c, d, e = Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0))
    #================================Aquí va el enunciado================================================================
    enunciado = "El valor de x que satisface la ecuación "+Matematica(Pol(a, b*"x")+"="+(c*"(").show+Pol(d*"x", e)+")")+" es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica((a-c*e)/(c*d-b))
    contenido_2 = Matematica((a+c*e)/(c*d+b))
    contenido_3 = Matematica(a+b-c*d-e)
    contenido_4 = Matematica((a-e)/(c*d-b))
    contenido_5 = Matematica((a-c*e)/(d-b))
    enunciado_oculto = [opcion,a,b,c,d,e]




elif opcion==3:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c, d, e, f = Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0))
    while a*b-d*e==0 or a*b+d*e==0 or a*b-d*e==0 or a*b+d*e==0 or a+b-d+e==0:
        a, b, c, d, e, f = Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0))
    #================================Aquí va el enunciado================================================================
    enunciado = "El valor de x que satisface la ecuación "+Matematica((a*"(").show+Pol(b*"x", c)+")="+(d*"(").show+Pol(e*"x", f)+")")+" es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica((d*f-a*c)/(a*b-d*e))
    contenido_2 = Matematica((d*f+a*c)/(a*b+d*e))
    contenido_3 = Matematica((f-c)/(a*b-d*e))
    contenido_4 = Matematica((f+c)/(a*b+d*e))
    contenido_5 = Matematica((d+f-a+c)/(a+b-d+e))
    enunciado_oculto = [opcion,a,b,c,d,e,f]



elif opcion==4:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c, d, e, f, g, h, i, j = Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0))
    while a+b*c-e*f-h*i==0 or a+b*c+e*f+h*i==0 or a+b+c-e+f-h+i==0 or a+b+c+e+f+h+i==0:
        a, b, c, d, e, f, g, h, i, j = Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0))
        
    #================================Aquí va el enunciado================================================================
    enunciado = "El valor de x que satisface la ecuación "+Matematica(Pol(a*"x", b*"(").show+Pol(c*"x", d)+")="+e*"("+Pol(f*"x", g)+")"+h*"("+Pol(i*"x", j)+")")+" es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica((e*g+h*j-b*d)/(a+b*c-e*f-h*i))
    contenido_2 = Matematica((e*g+h*j+b*d)/(a+b*c+e*f+h*i))
    contenido_3 = Matematica((e+g+h+j-b+d)/(a+b+c-e+f-h+i))
    contenido_4 = Matematica((e+g+h+j+b+d)/(a+b+c+e+f+h+i))
    contenido_5 = Matematica((g+j-d)/(a+b*c-e*f-h*i))
    enunciado_oculto = [opcion,a,b,c,d,e,f,g,h,i,j]



elif opcion==5:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c, d, e, f, g, h, i, j, k, l = Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0))
    while a*b+d*e-g*h-j*k==0 or a*b+d*e+g*h+j*k==0 or a+b+d+e-g+h-j+k==0 or a+b+d+e+g+h+j+k==0:
        a, b, c, d, e, f, g, h, i, j, k, l = Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0))
    #================================Aquí va el enunciado================================================================
    enunciado = "El valor de x que satisface la ecuación "+Matematica((a*"(").show+Pol(b*"x", c)+")"+d*"("+Pol(e*"x", f)+")="+g*"("+Pol(h*"x", i)+")"+j*"("+Pol(k*"x", l)+")")+" es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica((g*i+j*l-a*c-d*f)/(a*b+d*e-g*h-j*k))
    contenido_2 = Matematica((g*i+j*l+a*c+d*f)/(a*b+d*e+g*h+j*k))
    contenido_3 = Matematica((g+i+j+l-a+c-d+f)/(a+b+d+e-g+h-j+k))
    contenido_4 = Matematica((g+i+j+l+a+c+d+f)/(a+b+d+e+g+h+j+k))
    contenido_5 = Matematica((i+l-c-f)/(a*b+d*e-g*h-j*k))
    enunciado_oculto = [opcion,a,b,c,d,e,f,g,h,i,j,k,l]



elif opcion==6:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c, d, e, f = Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0))
    while a*b+a*d-e==0 or a*b+a*d+e==0 or a+b+a+d-e==0 or a*b+d-e==0:
        a, b, c, d, e, f = Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0))
    #================================Aquí va el enunciado================================================================
    enunciado = "El valor de x que satisface la ecuación "+Matematica((a*"(").show+Pol(b*"x", c, d*"x")+")="+Pol(e*"x", f))+" es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica((f-a*c)/(a*b+a*d-e))
    contenido_2 = Matematica((f+a*c)/(a*b+a*d+e))
    contenido_3 = Matematica((f-a+c)/(a+b+a+d-e))
    contenido_4 = Matematica((f+a+c)/(a+b+a+d-e))
    contenido_5 = Matematica((f-c)/(a*b+d-e))
    enunciado_oculto = [opcion,a,b,c,d,e,f]




elif opcion==7:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c, d, e, f, g = Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0))
    while a*b+d*e==0 or a+b+d+e==0:
        a, b, c, d, e, f, g = Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0))        
    #================================Aquí va el enunciado================================================================
    enunciado = "El valor de x que satisface la ecuación "+Matematica((a*"(").show+Pol(b*"x", c)+")"+d*"("+Pol(e*"x", f)+")="+g)+" es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica((g-a*c-d*f)/(a*b+d*e))
    contenido_2 = Matematica((g-a+c-d+f)/(a+b+d+e))
    contenido_3 = Matematica((g+a*c+d*f)/(a*b+d*e))
    contenido_4 = Matematica((g+a+c+d+f)/(a+b+d+e))
    contenido_5 = Matematica((g-c-f)/(a*b+d*e))
    enunciado_oculto = [opcion,a,b,c,d,e,f,g]




elif opcion==8:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c, d, e, f, g, h, i, j = Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0))
    while a*b+d*e+g*h==0 or a+b+d+e+g+h==0:
        a, b, c, d, e, f, g, h, i, j = Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0)), Racional(elegir(-10, 11, 0))
    #================================Aquí va el enunciado================================================================
    enunciado = "El valor de x que satisface la ecuación "+Matematica((a*"(").show+Pol(b*"x", c)+")"+d*"("+Pol(e*"x", f)+")"+g*"("+Pol(h*"x", i)+")="+j)+" es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica((j-a*c-d*f-g*i)/(a*b+d*e+g*h))
    contenido_2 = Matematica((j-a+c-d+f-g+i)/(a+b+d+e+g+h))
    contenido_3 = Matematica((j-a*c+d*f+g*i)/(a*b+d*e+g*h))
    contenido_4 = Matematica((j+a+c+d+f+g+i)/(a+b+d+e+g+h))
    contenido_5 = Matematica((j-c-f-i)/(a*b+d*e+g*h))
    enunciado_oculto = [opcion,a,b,c,d,e,f,g,h,i,j]













