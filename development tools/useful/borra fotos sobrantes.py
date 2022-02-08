import shutil
import os



for eje_tematico in os.listdir("Paquete"):
    for unidad in os.listdir(f"Paquete\\{eje_tematico}"):
        for contenido in os.listdir(f"Paquete\\{eje_tematico}\\{unidad}"):
            if os.path.exists(f"Paquete\\{eje_tematico}\\{unidad}\\{contenido}\\Fotos\\build"):#Borra los build
                shutil.rmtree(f"Paquete\\{eje_tematico}\\{unidad}\\{contenido}\\Fotos\\build")
            for foto in os.listdir(f"Paquete\\{eje_tematico}\\{unidad}\\{contenido}\\Fotos"):#Borra fotos sobrantes
                if not os.path.exists(f"Paquete\\{eje_tematico}\\{unidad}\\{contenido}\\{foto.replace('.jpg','.py')}"):
                    print(f"Paquete\\{eje_tematico}\\{unidad}\\{contenido}\\Fotos\\{foto}")
                    os.remove(f"Paquete\\{eje_tematico}\\{unidad}\\{contenido}\\Fotos\\{foto}")
                    