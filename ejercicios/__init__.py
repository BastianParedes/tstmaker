import os
from PIL import Image


items = ['Selección múltiple', 'Desarrollo', 'Verdadero y falso']



class Ejercicio:
    '''self
    eje_tematico                    str
    unidad                          str
    contenido                       str
    cantidades                      dict
    enunciados_ocultos              dict
    rutas                           dict
    existencias                     dict
    opciones                        dict
    cantidades_disponibles          dict
    '''
    def __init__(self, eje_tematico, unidad, contenido):
        self.eje_tematico = eje_tematico
        self.unidad = unidad
        self.contenido = contenido
        path = f'ejercicios/{eje_tematico}/{unidad}/{contenido}'

        self.existencias, self.rutas, self.opciones, self.cantidades_disponibles, self.instrucciones, self.cantidades, self.enunciados_ocultos, self.fotos = {}, {}, {}, {}, {}, {}, {}, {}
        for item in items:
            self.existencias[item], self.rutas[item], self.opciones[item], self.cantidades_disponibles[item], self.instrucciones[item], self.cantidades[item], self.enunciados_ocultos[item], self.fotos[item] = {}, {}, {}, {}, {}, {}, {}, {}
            for nivel in '123':
                self.cantidades[item][nivel] = 0                                                                #cantidad ejercicios solicitada
                self.rutas[item][nivel] = f'{path}/{item} {nivel}.py'  #rutas de las instrucciones
                self.existencias[item][nivel] = os.path.exists(self.rutas[item][nivel])                         #existencias
                if self.existencias[item][nivel]:
                    with open(self.rutas[item][nivel], 'r', encoding='utf-8') as file:
                        diccionario = eval(file.readline())
                        self.opciones[item][nivel] = diccionario['cantidad_opciones']                           #opciones disponibles
                        self.cantidades_disponibles[item][nivel] = diccionario['cantidad_disponible']           #cantidad de ejercicios disponible
                        self.instrucciones[item][nivel] = file.read()                               #instruccioens

                    
                    self.enunciados_ocultos[item][nivel] = []                                                   #guardará los enunciados ocultos
                    self.fotos[item][nivel] = Image.open(f'{path}/Fotos/{item} {nivel}.jpg') if os.path.exists(f'{path}/Fotos/{item} {nivel}.jpg') else None    #guarda las fotos


        #procedimientos y descripción
        self.procedimientos = open(f'{path}/Procedimientos.py', 'r', encoding='utf-8').read() if os.path.exists(f'{path}/Procedimientos.py') else None
        self.descripcion = open(f'{path}/Descripción.py', 'r', encoding='utf-8').read() if os.path.exists(f'{path}/Descripción.py') else None







lista = []
eje_unidad_contenido = {}
for eje_tematico in ['Números', 'Álgebra y funciones', 'Geometría', 'Estadística y probabilidades']:
    eje_unidad_contenido[eje_tematico] = {}
    for unidad in os.listdir(f'ejercicios/{eje_tematico}'):
        eje_unidad_contenido[eje_tematico][unidad] = []
        for contenido in os.listdir(f'ejercicios/{eje_tematico}/{unidad}'):
            eje_unidad_contenido[eje_tematico][unidad].append(contenido)
            lista.append(Ejercicio(eje_tematico, unidad, contenido))




def vaciar_enunciados_ocultos():
    for ejercicio in lista:
        for item in ejercicio.enunciados_ocultos:
            for nivel in ejercicio.enunciados_ocultos[item]:
                ejercicio.enunciados_ocultos[item][nivel] = []



def buscar_ejercicio(eje_tematico, unidad, contenido):
    for ejercicio in lista:
        if ejercicio.eje_tematico==eje_tematico and ejercicio.unidad==unidad and ejercicio.contenido==contenido:
            return ejercicio


def cantidades_ejercicios_por_item():
    cantidades_ejercicios_por_item = {item:0 for item in items}
    for ejercicio in lista:
        for item in items:
            for nivel in '123':
                cantidades_ejercicios_por_item[item] += ejercicio.cantidades[item][nivel]   #Total general por item
    return cantidades_ejercicios_por_item

def cantidad_ejercicios_solicitados():
    total_de_ejercicios = 0
    for ejercicio in lista:
        for item in items:
            for nivel in '123':
                total_de_ejercicios += ejercicio.cantidades[item][nivel]
    
    return total_de_ejercicios
