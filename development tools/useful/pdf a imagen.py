from pdf2image import convert_from_path
import os

for rama in os.listdir("./Paquete"):
    for contenido in os.listdir(f"./Paquete/{rama}"):
        for nombre in os.listdir(f"./Paquete/{rama}/{contenido}"):
            for pdf in os.listdir(f"./Paquete/{rama}/{contenido}/{nombre}/Fotos"):
                try:
                    convert_from_path(f'./Paquete/{rama}/{contenido}/{nombre}/Fotos/{pdf}')[0].save(f'./Paquete/{rama}/{contenido}/{nombre}/Fotos/{pdf[:-4]}.jpg', 'JPEG')
                    os.remove(f"./Paquete/{rama}/{contenido}/{nombre}/Fotos/{pdf}")
                except:
                    pass