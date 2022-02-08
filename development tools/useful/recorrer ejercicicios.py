import shutil
import os

for eje_tematico in os.listdir("Paquete"):
    for unidad in os.listdir(f"Paquete\\{eje_tematico}"):
        for contenido in os.listdir(f"Paquete\\{eje_tematico}\\{unidad}"):
            ruta = f"Paquete\\{eje_tematico}\\{unidad}\\{contenido}\\Descripcion.py"
            for item in ["Selección múltiple", "Desarrollo", "Verdadero y falso"]:
                for nivel in "123":
                    path = f"Paquete\\{eje_tematico}\\{unidad}\\{contenido}\\{item} {nivel}.py"
                    if os.path.exists(path):
                        # with open(path, "r", encoding="utf-8") as file:
                        #     interior = file.read()
                        #     if "racional" in interior:
                        #         print(path)


                        
                        with open(path, "r", encoding="utf-8") as file:
                            interior = file.read().replace("racional(","Racional(").replace("term_con_root","TermRoot").replace("root","Root").replace("par(","Par(").replace("complex","Complex").replace("unidad_imaginaria","UnidadImaginaria").replace("recta(","Recta(").replace("circunferencia(","Circunferencia(").replace("fraction(","Fraction(").replace("term(","Term(").replace("pol(","Pol(").replace("natural(","Natural(")

                        interior = interior.split("\n")
                        nuevoInterior = ""
                        for linea in interior:
                            if "log(" in linea and "math.log(" not in linea:
                                linea = linea.replace("log(", "Log(")
                            if "log(" in linea and ".valor" in linea:
                                linea = linea.replace("log(", "Log(")
                            if "racional" in linea and ("isinstance" in linea or "==" in linea):
                                linea = linea.replace("racional", "Racional")
                            if "term" in linea and ("isinstance" in linea or "==" in linea):
                                linea = linea.replace("term", "Term")
                            nuevoInterior += (linea + "\n")


                        with open(path, "w", encoding="utf-8") as file:
                            file.write(nuevoInterior)
                            
