{"cantidad_opciones":1, "cantidad_disponible":50}

#===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
b, h = Racional(randrange(1,10))*2, Racional(randrange(1,20))

unidad_de_medida = choice(["mm", "cm", "m", "km"])
angulo_de_giro = randrange(0,360)
medida_dibujo_1 = randrange(10,30)/10

#================================Aquí va el enunciado================================================================
enunciado = choice(["El triángulo ABC es isósceles de base AB", r"En el siguiente triángulo se cumple que $\angle \mathrm{BAC} \cong \angle \mathrm{CBA}$", r"En el siguiente triángulo se cumple que $\overline{\mathrm{CA}} \cong \overline{\mathrm{CB}}$"])+fr"""
\begin{{center}} \begin{{tikzpicture}} [scale=1]
\tkzDefPoint({180+angulo_de_giro}:{medida_dibujo_1}){{A}}
\tkzDefPoint({0+angulo_de_giro}:{medida_dibujo_1}){{B}}
\tkzDefPoint({90+angulo_de_giro}:{randrange(10,30)/10}){{C}}
\tkzDefPoint(0,0){{D}}

\tkzDrawPolygon(A,B,C)
\tkzDrawSegment(C,D);
\tkzMarkRightAngle[size=0.2]({choice(["C,D,A","B,D,C"])})

\node [label={180+angulo_de_giro}:A] at (A){{}};
\node [label={0+angulo_de_giro}:B] at (B){{}};
\node [label={90+angulo_de_giro}:C] at (C){{}};
\node [label={270+angulo_de_giro}:D] at (D){{}};

\end{{tikzpicture}} \end{{center}}
{Matematica(linea("AB"))} mide {Matematica(b+' '+unidad_de_medida)} y {Matematica(linea("CD"))} mide {Matematica(h+' '+unidad_de_medida)}. El volumen del cuerpo generado al rotar el triángulo ABC en torno a {Matematica(linea("CD"))} es"""

#===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
contenido_correcto = Matematica((b/2)**2*h*PI()/3+' '+potencia(unidad_de_medida,3,parentesis_automatico=False))
contenido_2 = Matematica((b/2)**2*h*PI()+' '+potencia(unidad_de_medida,3,parentesis_automatico=False))
contenido_3 = Matematica((b)**2*h*PI()/3+' '+potencia(unidad_de_medida,3,parentesis_automatico=False))
contenido_4 = Matematica((b)**2*h*PI()+' '+potencia(unidad_de_medida,3,parentesis_automatico=False))
contenido_5 = Matematica((h/2)**2*b*PI()/3+' '+potencia(unidad_de_medida,3,parentesis_automatico=False))


enunciado_oculto = [b,h]











