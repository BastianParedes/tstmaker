import os

pre_borrado = True

for eje_tematico in os.listdir("Paquete"):
    for unidad in os.listdir(f"Paquete\\{eje_tematico}"):
        for contenido in os.listdir(f"Paquete\\{eje_tematico}\\{unidad}"):
            ruta = f"Paquete\\{eje_tematico}\\{unidad}\\{contenido}\\Descripción.py"
            if os.path.exists(ruta) and pre_borrado:
                os.remove(ruta)
                print(ruta)
            if not os.path.exists(ruta):
                file = open(ruta, "w", encoding="utf-8")
                file.write("Objetivo de evaluación\n\n\nIndicador de evaluación\n\n\nHabilidad(es)\n\n\nNivel de complejidad en la taxonomía de Bloom\n\n\nOtros contenidos relacionados\n\n\n")
                file.close()
                            
