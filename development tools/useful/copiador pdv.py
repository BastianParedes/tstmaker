import shutil
import os
                        
if not os.path.exists("Paquete temporal"):
    os.mkdir("Paquete temporal")

for eje_tematico in os.listdir("Paquete"):
    for unidad in os.listdir(f"Paquete\\{eje_tematico}"):
        for contenido in os.listdir(f"Paquete\\{eje_tematico}\\{unidad}"):
            for archivo in os.listdir(f"Paquete\\{eje_tematico}\\{unidad}\\{contenido}"):
                for item in ["Selección múltiple"]:
                    for nivel in "3":
                        if os.path.exists(f"Paquete\\{eje_tematico}\\{unidad}\\{contenido}\\{item} {nivel}.py"):
                            file = open(f"Paquete\\{eje_tematico}\\{unidad}\\{contenido}\\{item} {nivel}.py", "r", encoding="utf-8")
                            interior = file.read()
                            file.close()
                            if "#pdv" in interior.lower():
                                try:
                                    os.mkdir(f"Paquete temporal\\{eje_tematico}")
                                except:
                                    pass
                                try:
                                    os.mkdir(f"Paquete temporal\\{eje_tematico}\\{unidad}")
                                except:
                                    pass

                                try:
                                    shutil.copytree(f"Paquete\\{eje_tematico}\\{unidad}\\{contenido}"    , f"Paquete temporal\\{eje_tematico}\\{unidad}\\{contenido}")
                                except:
                                    pass
                               
                            
                            

