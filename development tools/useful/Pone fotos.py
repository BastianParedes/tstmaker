from Definiciones import *
from pdf2image import convert_from_path



solo_faltantes = True
pre_borrado_de_carpeta = False


class Extraido:
    pass
extraido = Extraido()

for eje_tematico in os.listdir("ejercicios"):
    if eje_tematico in ['__init__.py', '__pycache__']:
        continue
    for unidad in os.listdir(f"ejercicios\\{eje_tematico}"):
        for contenido in os.listdir(f"ejercicios\\{eje_tematico}\\{unidad}"):
            if os.path.exists(f"ejercicios\\{eje_tematico}\\{unidad}\\{contenido}\\Fotos") and pre_borrado_de_carpeta:
                shutil.rmtree(f"ejercicios\\{eje_tematico}\\{unidad}\\{contenido}\\Fotos")

            if not os.path.exists(f"ejercicios\\{eje_tematico}\\{unidad}\\{contenido}\\Fotos"):
                os.mkdir(f"ejercicios\\{eje_tematico}\\{unidad}\\{contenido}\\Fotos")
            for item in ["Selección múltiple", "Desarrollo", "Verdadero y falso", "Completación", "Términos pareados"]:
                for nivel in "123":
                    if not os.path.exists(f"ejercicios\\{eje_tematico}\\{unidad}\\{contenido}\\{item} {nivel}.py"):
                        continue
                    if os.path.exists(fr"ejercicios\{eje_tematico}\{unidad}\{contenido}\Fotos\{item} {nivel}.jpg") and solo_faltantes:
                        print("Sí existe", fr"ejercicios\{eje_tematico}\{unidad}\{contenido}\Fotos\{item} {nivel}.jpg")
                        continue
                    print("No existe", fr"ejercicios\{eje_tematico}\{unidad}\{contenido}\Fotos\{item} {nivel}.jpg")
                    # print(fr"ejercicios\{eje_tematico}\{unidad}\{contenido}\Fotos\{item} {nivel}.jpg")
                    # print(eje_tematico, unidad, contenido, item, nivel)
                    file = open(f"ejercicios\\{eje_tematico}\\{unidad}\\{contenido}\\{item} {nivel}.py", "r", encoding="utf-8")

#Selección múltiple
                    if item == "Selección múltiple":
                        if nivel in "12":
                            interior = file.read()
                            diccionario = eval(interior.split("\n")[0])
                            interior = f"opcion=randrange(1,{diccionario['cantidad_opciones']+1})\n"     +interior + """\nextraido.enunciado = enunciado
extraido.contenido_correcto = contenido_correcto
extraido.contenido_2 = contenido_2
extraido.contenido_3 = contenido_3
extraido.contenido_4 = contenido_4
extraido.contenido_5 = contenido_5"""
                            file.close()

                            exec(interior)
                            enunciado = extraido.enunciado
                            contenido_correcto = extraido.contenido_correcto
                            contenido_2 = extraido.contenido_2
                            contenido_3 = extraido.contenido_3
                            contenido_4 = extraido.contenido_4
                            contenido_5 = extraido.contenido_5

                            while contenido_correcto==contenido_2 or contenido_correcto==contenido_3 or contenido_correcto==contenido_4 or contenido_correcto==contenido_5 or contenido_2==contenido_3 or contenido_2==contenido_4 or contenido_2==contenido_5 or contenido_3==contenido_4 or contenido_3==contenido_5 or contenido_4==contenido_5:
                                print("repetición")
                                exec(interior)
                                enunciado = extraido.enunciado
                                contenido_correcto = extraido.contenido_correcto
                                contenido_2 = extraido.contenido_2
                                contenido_3 = extraido.contenido_3
                                contenido_4 = extraido.contenido_4
                                contenido_5 = extraido.contenido_5

                            doc = pylatex.Document(page_numbers=None, documentclass="standalone", document_options=pylatex.NoEscape(r"varwidth=true, border=0pt, convert={size=640x}"))
                            for ejercicios in [r"\usepackage{ragged2e}", r"\usepackage{setspace}", r"\usepackage{longtable}", r"\usepackage{tabularx}", r"\usepackage{gensymb}", r"\usepackage{amsmath}", r"\usepackage{amssymb}", r"\usepackage{enumitem}", r"\usepackage{graphicx}", r"\usepackage{tikz}", r"\usepackage{tkz-euclide}", r"\usepackage{siunitx}", r"\usepackage{fourier}", r"\usetikzlibrary{fit, shapes.geometric, quotes, angles, through, intersections}"]:
                                doc.preamble.append(pylatex.NoEscape(ejercicios))

                            doc.append(pylatex.NoEscape(r"\begin{longtable}{p{8.3 cm}}"))
                            doc.append(pylatex.NoEscape(enunciado))

                            doc.append(pylatex.NoEscape(r"\begin{enumerate}[label=\Alph*)]"))

                            doc.append(pylatex.NoEscape(r"\item"))
                            doc.append(pylatex.NoEscape(contenido_correcto))

                            doc.append(pylatex.NoEscape(r"\item"))
                            doc.append(pylatex.NoEscape(contenido_2))

                            doc.append(pylatex.NoEscape(r"\item"))
                            doc.append(pylatex.NoEscape(contenido_3))

                            doc.append(pylatex.NoEscape(r"\item"))
                            doc.append(pylatex.NoEscape(contenido_4))

                            doc.append(pylatex.NoEscape(r"\item"))
                            doc.append(pylatex.NoEscape(contenido_5))


                            doc.append(pylatex.NoEscape(r"\end{enumerate}"))
                            doc.append(pylatex.NoEscape(r"\end{longtable}"))        
                            if os.path.exists(f"ejercicios\\{eje_tematico}\\{unidad}\\{contenido}\\Fotos\\{item} {nivel}.jpg"):
                                os.remove(f"ejercicios\\{eje_tematico}\\{unidad}\\{contenido}\\Fotos\\{item} {nivel}.jpg")
                            doc.generate_pdf(f"ejercicios\\{eje_tematico}\\{unidad}\\{contenido}\\Fotos\\{item} {nivel}", clean=True, compiler="pdflatex")
                            convert_from_path(f"ejercicios\\{eje_tematico}\\{unidad}\\{contenido}\\Fotos\\{item} {nivel}.pdf")[0].save(f"ejercicios\\{eje_tematico}\\{unidad}\\{contenido}\\Fotos\\{item} {nivel}.jpg", 'JPEG')
                            os.remove(f"ejercicios\\{eje_tematico}\\{unidad}\\{contenido}\\Fotos\\{item} {nivel}.pdf")




                        elif nivel == "3":
                            interior = file.read()
                            diccionario = eval(interior.split("\n")[0])
                            interior = f"opcion=randrange(1,{diccionario['cantidad_opciones']+1})\n"     +interior+"\nextraido.enunciado, extraido.informacion_1, extraido.informacion_2, extraido.enunciado_oculto_actual, extraido.alternativa_correcta = enunciado, informacion_1, informacion_2, opcion, alternativa_correcta"
                            file.close()
                            
                            exec(interior)
                            enunciado = extraido.enunciado

                            doc = pylatex.Document(page_numbers=None, documentclass="standalone", document_options=pylatex.NoEscape(r"varwidth=true, border=0pt, convert={size=640x}"))
                            for ejercicios in [r"\usepackage{ragged2e}", r"\usepackage{setspace}", r"\usepackage{longtable}", r"\usepackage{tabularx}", r"\usepackage{gensymb}", r"\usepackage{amsmath}", r"\usepackage{amssymb}", r"\usepackage{enumitem}", r"\usepackage{graphicx}", r"\usepackage{tikz}", r"\usepackage{tkz-euclide}", r"\usepackage{siunitx}", r"\usepackage{fourier}", r"\usetikzlibrary{fit, shapes.geometric, quotes, angles, through, intersections}"]:
                                doc.preamble.append(pylatex.NoEscape(ejercicios))

                            doc.append(pylatex.NoEscape(r"\begin{longtable}{p{8.3 cm}}"))
                            doc.append(pylatex.NoEscape(enunciado))

                            doc.append(pylatex.NoEscape(r"\begin{enumerate}[label=(\arabic*),start=1]"))
                            doc.append(pylatex.NoEscape(r"\item"))
                            doc.append(pylatex.NoEscape(extraido.informacion_1))
                            doc.append(pylatex.NoEscape(r"\item"))
                            doc.append(pylatex.NoEscape(extraido.informacion_2))
                            doc.append(pylatex.NoEscape(r"\end{enumerate}"))

                           
                            doc.append(pylatex.NoEscape(r"\begin{enumerate}[label=\Alph*)]"))
                            for respuesta in ["(1) por sí sola", "(2) por sí sola", "Ambas juntas, (1) y (2)", "Cada una por sí sola, (1) ó (2)", "Se requiere información adicional"]:
                                doc.append(pylatex.NoEscape(r"\item"))
                                doc.append(pylatex.NoEscape(respuesta))
                            doc.append(pylatex.NoEscape(r"\end{enumerate}"))

                            doc.append(pylatex.NoEscape(r"\end{longtable}"))        
                            if os.path.exists(f"ejercicios\\{eje_tematico}\\{unidad}\\{contenido}\\Fotos\\{item} {nivel}.jpg"):
                                os.remove(f"ejercicios\\{eje_tematico}\\{unidad}\\{contenido}\\Fotos\\{item} {nivel}.jpg")
                            doc.generate_pdf(f"ejercicios\\{eje_tematico}\\{unidad}\\{contenido}\\Fotos\\{item} {nivel}", clean=True, compiler="pdflatex")
                            convert_from_path(f"ejercicios\\{eje_tematico}\\{unidad}\\{contenido}\\Fotos\\{item} {nivel}.pdf")[0].save(f"ejercicios\\{eje_tematico}\\{unidad}\\{contenido}\\Fotos\\{item} {nivel}.jpg", 'JPEG')
                            os.remove(f"ejercicios\\{eje_tematico}\\{unidad}\\{contenido}\\Fotos\\{item} {nivel}.pdf")







#Desarrollo
                    elif item == "Desarrollo":
                        interior = file.read()
                        diccionario = eval(interior.split("\n")[0])
                        interior = f"opcion=randrange(1,{diccionario['cantidad_opciones']+1})\n"     +interior + """\nextraido.enunciado = enunciado"""
                        file.close()

                        exec(interior)
                        enunciado = extraido.enunciado

                        doc = pylatex.Document(page_numbers=None, documentclass="standalone", document_options=pylatex.NoEscape(r"varwidth=true, border=0pt, convert={size=640x}"))
                        for ejercicios in [r"\usepackage{ragged2e}", r"\usepackage{setspace}", r"\usepackage{longtable}", r"\usepackage{tabularx}", r"\usepackage{gensymb}", r"\usepackage{amsmath}", r"\usepackage{amssymb}", r"\usepackage{enumitem}", r"\usepackage{graphicx}", r"\usepackage{tikz}", r"\usepackage{tkz-euclide}", r"\usepackage{siunitx}", r"\usepackage{fourier}", r"\usetikzlibrary{fit, shapes.geometric, quotes, angles, through, intersections}"]:
                            doc.preamble.append(pylatex.NoEscape(ejercicios))

                        doc.append(pylatex.NoEscape(r"\begin{longtable}{p{8.3 cm}}"))
                        doc.append(pylatex.NoEscape(enunciado))

                        doc.append(pylatex.NoEscape(r"\end{longtable}"))        
                        if os.path.exists(f"ejercicios\\{eje_tematico}\\{unidad}\\{contenido}\\Fotos\\{item} {nivel}.jpg"):
                            os.remove(f"ejercicios\\{eje_tematico}\\{unidad}\\{contenido}\\Fotos\\{item} {nivel}.jpg")
                        doc.generate_pdf(f"ejercicios\\{eje_tematico}\\{unidad}\\{contenido}\\Fotos\\{item} {nivel}", clean=True, compiler="pdflatex")
                        convert_from_path(f"ejercicios\\{eje_tematico}\\{unidad}\\{contenido}\\Fotos\\{item} {nivel}.pdf")[0].save(f"ejercicios\\{eje_tematico}\\{unidad}\\{contenido}\\Fotos\\{item} {nivel}.jpg", 'JPEG')
                        os.remove(f"ejercicios\\{eje_tematico}\\{unidad}\\{contenido}\\Fotos\\{item} {nivel}.pdf")










#Verdadero y falso
                    elif item == "Verdadero y falso":
                        interior = file.read()
                        diccionario = eval(interior.split("\n")[0])
                        interior = f"opcion=randrange(1,{diccionario['cantidad_opciones']+1})\n"     +interior + """\nextraido.enunciado_verdadero = enunciado_verdadero
extraido.enunciado_falso = enunciado_falso"""
                        file.close()

                        exec(interior)
                        enunciado_verdadero = extraido.enunciado_verdadero
                        enunciado_falso = extraido.enunciado_falso
                        while enunciado_verdadero == enunciado_falso:
                            print("repetición")
                            exec(interior)
                        enunciado_verdadero = extraido.enunciado_verdadero
                        enunciado_falso = extraido.enunciado_falso


                        doc = pylatex.Document(page_numbers=None, documentclass="standalone", document_options=pylatex.NoEscape(r"varwidth=true, border=0pt, convert={size=640x}"))
                        for ejercicios in [r"\usepackage{ragged2e}", r"\usepackage{setspace}", r"\usepackage{longtable}", r"\usepackage{tabularx}", r"\usepackage{gensymb}", r"\usepackage{amsmath}", r"\usepackage{amssymb}", r"\usepackage{enumitem}", r"\usepackage{graphicx}", r"\usepackage{tikz}", r"\usepackage{tkz-euclide}", r"\usepackage{siunitx}", r"\usepackage{fourier}", r"\usetikzlibrary{fit, shapes.geometric, quotes, angles, through, intersections}"]:
                            doc.preamble.append(pylatex.NoEscape(ejercicios))

                        doc.append(pylatex.NoEscape(r"\begin{longtable}{p{8.3 cm}}"))
                        if choice([True, False]):
                            doc.append(pylatex.NoEscape(r"V\ \ \ \ F\ \ \ \ "+enunciado_verdadero))
                        else:
                            doc.append(pylatex.NoEscape(r"V\ \ \ \ F\ \ \ \ "+enunciado_falso))
                        doc.append(pylatex.NoEscape(r"\end{longtable}"))


                        if os.path.exists(f"ejercicios\\{eje_tematico}\\{unidad}\\{contenido}\\Fotos\\{item} {nivel}.jpg"):
                            os.remove(f"ejercicios\\{eje_tematico}\\{unidad}\\{contenido}\\Fotos\\{item} {nivel}.jpg")
                        doc.generate_pdf(f"ejercicios\\{eje_tematico}\\{unidad}\\{contenido}\\Fotos\\{item} {nivel}", clean=True, compiler="pdflatex")
                        convert_from_path(f"ejercicios\\{eje_tematico}\\{unidad}\\{contenido}\\Fotos\\{item} {nivel}.pdf")[0].save(f"ejercicios\\{eje_tematico}\\{unidad}\\{contenido}\\Fotos\\{item} {nivel}.jpg", 'JPEG')
                        os.remove(f"ejercicios\\{eje_tematico}\\{unidad}\\{contenido}\\Fotos\\{item} {nivel}.pdf")

