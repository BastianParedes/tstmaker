import shutil
import os

#Junta main y definiciones
contenido_nueva_main = ""
with open("Definiciones.py", "r", encoding="utf-8") as file:
    for linea in file.read().split("\n"):
        if "print(" not in linea and "from Definiciones import *" not in linea:
            contenido_nueva_main += linea+"\n"
    file.close()
with open("main.py", "r", encoding="utf-8") as file:
    contenido_nueva_main += "\n"*40
    for linea in file.read().split("\n"):
        if "cantidad_a_establecer_para_todos" in linea or "boton_establecer" in linea:
            continue
        if "print(" in linea or linea=="from Definiciones import *":
            for letra in linea:
                if letra == " ":
                    contenido_nueva_main += " "
                else:
                    contenido_nueva_main += "pass\n"
                    break
        else:
            contenido_nueva_main += linea+"\n"
    file.close()

#Escribe la nueva main
with open("main temporal.py", "w", encoding="utf-8") as file:
    file.write(contenido_nueva_main)
    file.close()


#Crea .exe
os.system('pyinstaller --noconsole --onefile --uac-admin "main temporal.py"')
shutil.rmtree("./build")

os.rename("./dist/main temporal.exe", "./dist/main.exe")

#Copia carpetas y archivos a la carpeta temporal SOLO IMPORTANTES
for carpeta in ["ejercicios"]:
    shutil.copytree("./"+carpeta, "./dist/"+carpeta)
for archivo in ["Configuracion.txt", "Imagen previa inicial.jpg"]:
    shutil.copyfile("./"+archivo, "./dist/"+archivo)


#Compila
shutil.make_archive("TstMaker", "zip", "dist")

#Borra carpeta temporal y la main temporal
shutil.rmtree("./dist")
os.remove("./main temporal.py")
os.remove("./main temporal.spec")
print("Compilación terminada")



#cantidad_a_establecer_para_todos = Entry_datos(sub_frame_1_datos, "Cantidad global", next(fila_de_frame_datos), Configuracion.cantidad_a_establecer_para_todos, largo=6)
#boton_establecer.grid(row=5, column=1, padx=0, sticky="e")

# quitar
# cantidad_a_establecer_para_todos
# boton_establecer


