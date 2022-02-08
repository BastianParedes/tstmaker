{"cantidad_opciones":3, "cantidad_disponible":50}

class Juguete:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad
    def __lt__(self, other):
        return self.cantidad < other.cantidad
    def __str__(self):
        return self.nombre


#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
#Cantidad de esferas
cantidades_de_circulos = []
for _ in range(5):
    cantidades_de_circulos.append(randrange(0,8))
lista_ordenada = sorted(cantidades_de_circulos)
while 1<cantidades_de_circulos.count(0) or lista_ordenada[0]==lista_ordenada[1] or lista_ordenada[3]==lista_ordenada[4]:
    cantidades_de_circulos = []
    for _ in range(5):
        cantidades_de_circulos.append(randrange(0,8))
    lista_ordenada = sorted(cantidades_de_circulos)

#juguetes vendidos
lista_de_juguetes = ["Bicicleta", "Auto", "Moto", "Tren", "Lápiz", "Muñeco", "Lego", "Pirámide", "Cometa", "Robot", "Micrófono", "Plastilina"]
shuffle(lista_de_juguetes)
lista_de_juguetes = lista_de_juguetes[0:5]

lista_de_clases = []
for i in range(5):
    lista_de_clases.append(Juguete(lista_de_juguetes[i], cantidades_de_circulos[i]))
lista_de_clases = sorted(lista_de_clases)



grafico = "\draw (-1.5,-0.5) -- (12.7,-0.5);"
for i in range(5):
    grafico += fr"\node at ({i*2.8},-1) {{{lista_de_juguetes[i]}}};"+"\n"
    for elemento in range(0, cantidades_de_circulos[i]):
        grafico += fr"\filldraw [black] ({i*2.8},{elemento*0.5}) circle (4pt);"+"\n"





#================================Aquí va el enunciado================================================================
enunciado = r"""A continuación se muestra un diagrama de puntos de los juguetes vendidos en una tienda
\begin{center}Cantidad de juguetes vendidos \end{center} \begin{center} \begin{tikzpicture}[scale=0.5]
""" + grafico + r"\end{tikzpicture} \end{center}"

if opcion==1:
    enunciado += "El juguete más vendido es "

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(lista_de_clases[4])
    contenido_2 =        Matematica(lista_de_clases[3])
    contenido_3 =        Matematica(lista_de_clases[2])
    contenido_4 =        Matematica(lista_de_clases[1])
    contenido_5 =        Matematica(lista_de_clases[0])



elif opcion==2:
    #================================Aquí va el enunciado================================================================
    enunciado += "El juguete menos vendido es "

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(lista_de_clases[0])
    contenido_2 =        Matematica(lista_de_clases[1])
    contenido_3 =        Matematica(lista_de_clases[2])
    contenido_4 =        Matematica(lista_de_clases[3])
    contenido_5 =        Matematica(lista_de_clases[4])



elif opcion==3:
    #================================Aquí va el enunciado================================================================
    enunciado += "La cantidad total de juguetes vendidos es"

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(cantidades_de_circulos[0]+cantidades_de_circulos[1]+cantidades_de_circulos[2]+cantidades_de_circulos[3]+cantidades_de_circulos[4])
    contenido_2 =        Matematica(cantidades_de_circulos[0])
    contenido_3 =        Matematica(cantidades_de_circulos[1])
    contenido_4 =        Matematica(cantidades_de_circulos[3])
    contenido_5 =        Matematica(cantidades_de_circulos[4])



enunciado_oculto = [opcion, sorted(cantidades_de_circulos)]











