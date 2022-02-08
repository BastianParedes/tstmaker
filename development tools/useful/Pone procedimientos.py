import os

pre_borrado = False

for eje_tematico in os.listdir("ejercicios"):
    if eje_tematico == '__init__.py':
        continue
    for unidad in os.listdir(f"ejercicios\\{eje_tematico}"):
        for contenido in os.listdir(f"ejercicios\\{eje_tematico}\\{unidad}"):
            ruta = f"ejercicios\\{eje_tematico}\\{unidad}\\{contenido}\\Procedimientos.py"
            if os.path.exists(ruta) and pre_borrado:
                os.remove(ruta)
                print(ruta)
            if not os.path.exists(ruta):
                file = open(ruta, "w", encoding="utf-8")
                file.write("salto_automatico = False\n\nprocedimiento = \"No se ha creado esta explicación\"")
                file.close()
