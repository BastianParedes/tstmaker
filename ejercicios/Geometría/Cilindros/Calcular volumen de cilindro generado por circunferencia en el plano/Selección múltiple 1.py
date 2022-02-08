{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
r, h = Racional(randrange(1, 13)), Racional(randrange(1, 13))

#================================Aquí va el enunciado================================================================
enunciado = "Sea la circunferencia "+Matematica("C:"+potencia("x",2)+"+"+potencia("y",2)+"="+r**2)+f". Sea el cuerpo generado al trasladar C en {h} unidades con un vector perpendicular al plano que contiene a C. El volumen de dicho cuerpo es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(r**2*h*PI()) + " unidades cúbicas"
contenido_2 =        Matematica(2*r*h*PI()) + " unidades cúbicas"
contenido_3 =        Matematica(r**4*h*PI()) + " unidades cúbicas"
contenido_4 =        Matematica(2*r**4*h*PI()) + " unidades cúbicas"
contenido_5 =        Matematica(r**2*h*PI()/3) + " unidades cúbicas"



enunciado_oculto = [r,h]











