{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
z = Complex(choice(list(range(-10, 0))+list(range(1, 10))), choice(list(range(-10, 0))+list(range(1, 10))))

#================================Aquí va el enunciado================================================================
enunciado = "Considera el número complejo "+ Matematica("z="+z) + " con i la unidad imaginaria. Es verdadero respecto a su parte real y su parte imaginaria que"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.=
contenido_correcto = r"\begin{tabular}{p{1.3 cm} p{0.1 cm} p{1.3 cm}}"+ Matematica("Re(z)="+z.re)+                  "&;&"+Matematica("Im(z)="+z.im)+r"\\ \end{tabular}"
contenido_2 = r"\begin{tabular}{p{1.3 cm} p{0.1 cm} p{1.3 cm}}"+        Matematica("Re(z)="+z.re)+                  "&;&"+Matematica("Im(z)="+(z.im*"i"))+r"\\ \end{tabular}"
contenido_3 = r"\begin{tabular}{p{1.3 cm} p{0.1 cm} p{1.3 cm}}"+        Matematica("Re(z)="+(z.re*"i")) +      "&;&"+Matematica("Im(z)="+z.im)+r"\\ \end{tabular}"
contenido_4 = r"\begin{tabular}{p{1.3 cm} p{0.1 cm} p{1.3 cm}}"+        Matematica("Re(z)=0")+                      "&;&"+Matematica("Im(z)="+(z.re*z.im*"i"))+r"\\ \end{tabular}"
contenido_5 = r"\begin{tabular}{p{1.3 cm} p{0.1 cm} p{1.3 cm}}"+        Matematica("Re(z)="+(-z.im))+               "&;&"+Matematica("Im(z)="+(-z.re))+r"\\ \end{tabular}"

enunciado_oculto = z










