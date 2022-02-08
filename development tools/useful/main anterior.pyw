from Definiciones import *

if os.path.exists("temp"):
    shutil.rmtree("temp")

#Genera la raiz
frame_base = tk.Tk()
frame_base.title("TstMaker")
frame_base.state("zoomed")


class Frame_ejercicios(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        kwargs["name"] = "frame ejercicios"
        super().__init__(master, *args, **kwargs)

        #Crea canvas, frame scroleable y labels
        self.canvas = tk.Canvas(self, bg="light yellow", highlightthickness=0, name="canvas")
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.frame_pre_scroll = tk.Frame(self.canvas)
        self.scrollable_frame = tk.Frame(self.frame_pre_scroll, bg="light yellow", name="scrollable_frame", width=1500)
        self.ventana = self.canvas.create_window((0, 0), window=self.frame_pre_scroll, anchor="nw")
        self.label_0 = tk.Label(self.scrollable_frame, text="Completación", bg="light yellow")
        self.label_1 = tk.Label(self.scrollable_frame, text="Desarrollo", bg="light yellow")
        self.label_2 = tk.Label(self.scrollable_frame, text="Selección\nmúltiple", bg="light yellow")
        self.label_3 = tk.Label(self.scrollable_frame, text="Términos\npareados", bg="light yellow")
        self.label_4 = tk.Label(self.scrollable_frame, text="Verdadero\ny falso", bg="light yellow")
        self.label_5 = tk.Label(self.scrollable_frame, text="Nombre del ejercicio", bg="light yellow")

        #Ejecuta pack o grid en todo
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        self.scrollable_frame.pack()
        self.label_0.grid(sticky="N", row=0, column=0)
        self.label_1.grid(sticky="N", row=0, column=1)
        self.label_2.grid(sticky="N", row=0, column=2)
        self.label_3.grid(sticky="N", row=0, column=3)
        self.label_4.grid(sticky="N", row=0, column=4)
        self.label_5.grid(sticky="W", row=0, column=5)

        #Configuraciones y binds
        self.canvas.propagate(False)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.bind("<MouseWheel>", self.mouse_wheel)
        self.canvas.bind("<Configure>", self.ajustar_scrollable_frame)
        self.scrollable_frame.bind("<Configure>", lambda _: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.scrollable_frame.bind("<MouseWheel>", self.mouse_wheel)
        self.label_0.bind("<MouseWheel>", self.mouse_wheel)
        self.label_1.bind("<MouseWheel>", self.mouse_wheel)
        self.label_2.bind("<MouseWheel>", self.mouse_wheel)
        self.label_3.bind("<MouseWheel>", self.mouse_wheel)
        self.label_4.bind("<MouseWheel>", self.mouse_wheel)
        self.label_5.bind("<MouseWheel>", self.mouse_wheel)

        #Configuraciones de columnas
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame.grid_columnconfigure(1, weight=1)
        self.scrollable_frame.grid_columnconfigure(2, weight=1)
        self.scrollable_frame.grid_columnconfigure(3, weight=1)
        self.scrollable_frame.grid_columnconfigure(4, weight=1)
        self.scrollable_frame.grid_columnconfigure(5, weight=10)


    def mouse_wheel(self, event):
        if not self.scrollable_frame.winfo_height() <= self.canvas.winfo_height():
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def ajustar_scrollable_frame(self, event):
        self.scrollable_frame.configure(width=self.winfo_width())
        # self.canvas.configure(width=self.winfo_width())

class Frame_descripcion(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        kwargs["name"] = "frame descripción"
        super().__init__(master, *args, **kwargs)

        self.canvas = tk.Canvas(self, bg="white", highlightthickness=0, name="canvas")
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="white", name="scrollable_frame")
        self.ventana = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.label_titulo = tk.Label(self.canvas, text="Descripción", bg="light grey")
        self.label_descripcion = tk.Label(self.scrollable_frame, justify="left", bg="orange", fg="white")

        self.canvas.propagate(False)
        self.canvas.configure(yscrollcommand=self.scrollbar.set, bg="orange")

        self.canvas.bind("<Configure>", lambda _ : threading.Thread(target=self.ajustar_label,daemon=True).start())
        self.canvas.bind("<MouseWheel>", self.mouse_wheel)
        self.scrollable_frame.bind("<Configure>", lambda _: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.label_descripcion.bind("<MouseWheel>", self.mouse_wheel)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        self.label_titulo.pack(fill="x", side="top")
        self.label_descripcion.pack(fill="both", expand=True, side="left")

    def mouse_wheel(self, event):
        if not self.scrollable_frame.winfo_height() <= self.canvas.winfo_height():
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def ajustar_label(self):
        self.label_descripcion["wraplength"] = self.canvas.winfo_width()*0.99

class Frame_vista_previa(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        kwargs["name"] = "frame vista previa"
        super().__init__(master, *args, **kwargs)

        self.factor = 0.6

        self.frame_izquierdo = tk.Frame(self, bg="grey")
        self.frame_derecho = tk.Frame(self, bg="grey")

        self.canvas = tk.Canvas(self, highlightthickness=0, name="canvas")
        self.scrollbar_x = tk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.scrollbar_y = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, name="scrollable_frame")
        self.ventana = self.canvas.create_window((0, 0), window=self.scrollable_frame)
        self.label_imagen = tk.Label(self.scrollable_frame, bg="white", image="")
        self.imagen_original = Image.open(f"Imagen previa inicial.jpg")
        self.imagen_tamaño_cambiado = self.imagen_original.resize((int(self.imagen_original.size[0]*self.factor),int(self.imagen_original.size[1]*self.factor)), Image.ANTIALIAS)
        self.boton_mas = tk.Button(self.frame_derecho, width=1, height=1, bg="black", text="+", font=("courier",16), command=lambda :self.zoom("+"), fg="white")
        self.boton_menos = tk.Button(self.frame_derecho, width=1, height=1, bg="black", text="-", font=("courier",16), command=lambda :self.zoom("-"), fg="white")

        self.canvas.propagate(False)
        self.canvas.configure(bg="white", width=self.imagen_tamaño_cambiado.size[0], xscrollcommand=self.scrollbar_x.set, yscrollcommand=self.scrollbar_y.set)

        self.bind("<MouseWheel>", self.mouse_wheel)
        self.scrollable_frame.bind("<Configure>", lambda _: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.bind("<MouseWheel>", self.mouse_wheel)
        self.label_imagen.bind("<MouseWheel>", self.mouse_wheel)

        self.scrollbar_x.pack(side="bottom", fill="x")
        self.scrollbar_y.pack(side="right", fill="y")
        self.frame_izquierdo.pack(side="left", fill="both", expand=True)
        self.frame_derecho.pack(side="right", fill="both", expand=True)
        self.canvas.pack(side="top", fill="y", expand=True)
        self.label_imagen.pack(fill="both")
        self.boton_mas.grid(row=0, column=1, padx=0, pady=10, sticky="nswe")
        self.boton_menos.grid(row=0, column=0, padx=10, pady=10, sticky="nswe")

    def zoom(self, tipo):
        if self.label_imagen["image"]=="":
            return None
        if tipo=="+":
            self.factor = round(min(self.factor+0.1, 1), 1)
            self.imagen_tamaño_cambiado = self.imagen_original.resize((int(self.imagen_original.size[0]*self.factor),int(self.imagen_original.size[1]*self.factor)), Image.ANTIALIAS)
            self.imagen_nueva = ImageTk.PhotoImage(self.imagen_tamaño_cambiado)
            self.label_imagen["image"] = self.imagen_nueva
        elif tipo=="-":
            self.factor = round(max(self.factor-0.1, 0.3), 1)
            self.imagen_tamaño_cambiado = self.imagen_original.resize((int(self.imagen_original.size[0]*self.factor),int(self.imagen_original.size[1]*self.factor)), Image.ANTIALIAS)
            self.imagen_nueva = ImageTk.PhotoImage(self.imagen_tamaño_cambiado)
            self.label_imagen["image"] = self.imagen_nueva
        if self.factor==0.6:
            self.canvas.update()
            self.canvas.yview_moveto("0")

    def mouse_wheel(self, event):
        if not self.scrollable_frame.winfo_height() <= self.canvas.winfo_height():
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

class Entry_ejercicio(tk.Entry):
    def __init__(self,*args, **kwargs):
        #Genera la variable y su trace para que solo entren números
        self.variable = tk.StringVar(value="0")
        kwargs["textvariable"] = self.variable
        self.variable.trace("w", self.solo_numeros)
        
        #Guarda los datos del ejercicio
        self.eje_tematico = kwargs["eje_tematico"]
        self.unidad = kwargs["unidad"]
        self.nombre = kwargs["nombre"]
        self.item = kwargs["item"]
        kwargs.pop("eje_tematico")
        kwargs.pop("unidad")
        kwargs.pop("nombre")
        kwargs.pop("item")#No tiene uso por ahora

        #Carga todo el widget Entry y blindea para generar la imagen y la descripción
        super().__init__(*args, justify="center", **kwargs)
        self.bind("<FocusIn>", lambda event : threading.Thread(target=self.seleccionar_ejercicio,daemon=True).start())
        self.bind("<MouseWheel>", self.master.master.master.master.mouse_wheel)
        self.bind("<FocusOut>", lambda event : (self.insert("0","0"), self.actualizar_carrito(event)))

    def seleccionar_ejercicio(self):
        #Pone la nueva imagen previa
        frame_vista_previa = self.master.master.master.master.master.children["frame vista previa"]
        label_imagen = frame_vista_previa.label_imagen
        frame_vista_previa.factor = 0.6
        frame_vista_previa.cantidad_de_fotos = len(            os.listdir(f"Paquete/{self.eje_tematico}/{self.unidad}/{self.nombre}/Fotos")        )
        frame_vista_previa.ruta_actual = f"Paquete/{self.eje_tematico}/{self.unidad}/{self.nombre}/Fotos/Foto {randrange(frame_vista_previa.cantidad_de_fotos)+1}.jpg"
        frame_vista_previa.imagen_original = Image.open(frame_vista_previa.ruta_actual)
        frame_vista_previa.imagen_tamaño_cambiado = frame_vista_previa.imagen_original.resize((int(frame_vista_previa.imagen_original.size[0]*frame_vista_previa.factor),int(frame_vista_previa.imagen_original.size[1]*frame_vista_previa.factor)), Image.ANTIALIAS)
        frame_vista_previa.imagen_nueva = ImageTk.PhotoImage(frame_vista_previa.imagen_tamaño_cambiado)
        label_imagen["image"] = frame_vista_previa.imagen_nueva
        label_imagen.update()
        frame_vista_previa.canvas.yview_moveto("0")
        
        #Pone la desripción
        label_descripcion = self.master.master.master.master.master.children["frame descripción"].label_descripcion
        file = open(f"Paquete/{self.eje_tematico}/{self.unidad}/{self.nombre}/Descripción.py", "r", encoding="utf-8")
        label_descripcion["text"] = "\n\n"+file.read()
        file.close()
        canvas = self.master.master.master.master.master.children["frame descripción"].canvas
        canvas.yview_moveto("0")

    def solo_numeros(self, tipo="PY_VAR", vacio="", modo="w"):
        #Quita lo no numérico
        contenido = ""
        for letra_numero in self.variable.get():
            if letra_numero in "0123456789":
                contenido += letra_numero
        self.variable.set(contenido)
        #Quita los ceros extras
        for numero in self.variable.get():
            if numero=="0" and len(self.variable.get())>1:
                self.variable.set(self.variable.get()[1:])
            else:
                break
        #Pone el limitador hasta 50
        if self.variable.get()!="" and 50<int(self.variable.get()):
            self.variable.set("50")

    def actualizar_carrito(self, event=None):
        frame_carrito = self.master.master.master.master.master.master.master.master.winfo_children()[-1]
        Treeview = frame_carrito.Treeview
        iid = f"{self.eje_tematico}/{self.unidad}/{self.nombre}/{self.item}".replace(" ","")
        largo_de_columnas = 50

        #Borra
        if Treeview.exists(iid) and int(self.variable.get())==0:
            Treeview.delete(iid)

        #Actualiza
        elif Treeview.exists(iid) and int(self.variable.get())!=0:
            Treeview.item(iid, values=(
                "\n".join(textwrap.wrap(self.eje_tematico, largo_de_columnas)),
                "\n".join(textwrap.wrap(self.unidad, largo_de_columnas)),
                "\n".join(textwrap.wrap(self.nombre, largo_de_columnas)),
                "\n".join(textwrap.wrap(self.item, largo_de_columnas)),
                "\n".join(textwrap.wrap(self.variable.get(), largo_de_columnas)),
                ))
            

        #Ingresa nuevo
        elif not Treeview.exists(iid) and int(self.variable.get())!=0:
            Treeview.insert("", index="end", iid=iid, values=(
                "\n".join(textwrap.wrap(self.eje_tematico, largo_de_columnas)),
                "\n".join(textwrap.wrap(self.unidad, largo_de_columnas)),
                "\n".join(textwrap.wrap(self.nombre, largo_de_columnas)),
                "\n".join(textwrap.wrap(self.item, largo_de_columnas)),
                "\n".join(textwrap.wrap(self.variable.get(), largo_de_columnas)),
                ))
            Treeview.tag_bind(iid, "<Motion>", frame_carrito.mouse_over)

    def __eq__(self, other):
        return self.eje_tematico==other.eje_tematico and self.unidad==other.unidad and self.nombre==other.nombre and self.item==other.item


class Frame_carrito(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        kwargs["name"] = "carrito"
        super().__init__(master, *args, **kwargs)
        self.grid_rowconfigure(0, minsize=100)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        #Todo del Treeview
        style = ttk.Style()
        style.configure("Treeview",
                background="white",
                foreground="black",
                rowheight=45,
                fieldbackground="white")
        style.map("Treeview", background=[("selected", "lightblue")])

        self.Treeview = ttk.Treeview(self, style="Treeview", columns=["#1", "#2", "#3", "#4", "#5"], show=["headings"])
        self.Treeview.tag_configure("mouse_over", background="#dfebf7")
        self.Treeview.bind("<Motion>", self.mouse_over)
        # self.Treeview.tag_configure("white", background="white")
        # self.Treeview.tag_configure("grey", background="grey")
        # self.Treeview.tag_configure("#adf4ff", background="#adf4ff")

        width_screen = frame_base.winfo_screenwidth()/100

        self.Treeview.column("#1", anchor="center", width=int(width_screen*20))
        self.Treeview.column("#2", anchor="center", width=int(width_screen*20))
        self.Treeview.column("#3", anchor="center", width=int(width_screen*25))
        self.Treeview.column("#4", anchor="center", width=int(width_screen*20))
        self.Treeview.column("#5", anchor="center", width=int(width_screen*15))

        self.Treeview.heading("#1", text="Eje temático", anchor="center")
        self.Treeview.heading("#2", text="Unidad", anchor="center")
        self.Treeview.heading("#3", text="Contenido", anchor="center")
        self.Treeview.heading("#4", text="Item", anchor="center")
        self.Treeview.heading("#5", text="Cantidad solicitada", anchor="center")

        self.Treeview.grid(row=1, column=0, sticky="nswe", columnspan=2, rowspan=2)

        #Scrollbar
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.Treeview.yview)
        self.Treeview.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=1, column=2, sticky="ns")

    def mouse_over(self, event):
        self.Treeview.tk.call(self.Treeview, "tag", "remove", "mouse_over")
        self.Treeview.tk.call(self.Treeview, "tag", "add", "mouse_over", self.Treeview.identify_row(event.y))

    def limpiar(self):
        #Limpia el carrito
        self.Treeview.delete(*self.Treeview.get_children())
        #Pone ceros en todos los Entry
        for ejercicio in lista_de_todos_los_ejercicios:
            if ejercicio.existe_completacion:
                ejercicio.entry_completacion.variable.set("0")
            if ejercicio.existe_desarrollo:
                ejercicio.entry_desarrollo.variable.set("0")
            if ejercicio.existe_seleccion_multiple:
                ejercicio.entry_seleccion_multiple.variable.set("0")
            if ejercicio.existe_terminos_pareados:
                ejercicio.entry_terminos_pareados.variable.set("0")
            if ejercicio.existe_verdadero_y_falso:
                ejercicio.entry_verdadero_y_falso.variable.set("0")


espacio_horizontal = 20
espacio_vertical = 2
class Entry_datos:
    def __init__(self, master, label, fila, valor_inicial="", mostrar=True, largo=40):
        self.label = tk.Label(master, text=label, bg="#FFEEDD")
        self.mostrar = mostrar
        if mostrar==True:
            self.label.grid(sticky="nw", row=fila, column=0, padx=espacio_horizontal, pady=espacio_vertical)
        self.variable = tk.StringVar(value=valor_inicial)
        self.entry = tk.Entry(master, textvariable=self.variable, width=largo)
        if mostrar==True:
            self.entry.grid(sticky="W", row=fila, column=1, pady=espacio_vertical)
        self.fila = fila
    def get(self):
        return self.variable.get()

class Text_datos:
    def __init__(self, master, label, fila, ancho=30, alto=10, valor_inicial="", mostrar=True):
        self.label = tk.Label(master, text=label, bg="#FFEEDD")
        self.mostrar = mostrar
        if mostrar==True:
            self.label.grid(sticky="nw", row=fila, column=0, padx=espacio_horizontal, pady=espacio_vertical)
        self.variable = tk.StringVar(value=valor_inicial)
        self.text = tk.Text(master)
        self.text.config(width=ancho, height=alto)
        self.text.insert("end", valor_inicial)
        if mostrar==True:
            self.text.grid(sticky="W", row=fila, column=1, pady=espacio_vertical)
        self.fila = fila
    def get(self):
        return self.text.get("0.0","end")

class Checkbutton_datos:
    def __init__(self, master, label, fila, valor_inicial, mostrar=True):
        self.label = tk.Label(master, text=label, bg="#FFEEDD")
        self.mostrar = mostrar        
        if mostrar==True:
            self.label.grid(sticky="nw", row=fila, column=0, padx=espacio_horizontal, pady=espacio_vertical)
        self.variable = tk.BooleanVar(value=valor_inicial)
        self.ticket = tk.Checkbutton(master, variable=self.variable, onvalue=True, offvalue=False)
        if mostrar==True:
            self.ticket.grid(sticky="W", row=fila, column=1, pady=espacio_vertical)
        self.fila = fila
    def get(self):
        return self.variable.get()

class Combobox_datos:
    def __init__(self, master, label, fila, valor_inicial, lista_de_valores, largo_de_la_caja, mostrar=True):
        self.label = tk.Label(master, text=label, bg="#FFEEDD")
        self.mostrar = mostrar
        if mostrar==True:
            self.label.grid(sticky="nw", row=fila, column=0, padx=espacio_horizontal, pady=espacio_vertical)
        self.variable = tk.StringVar()
        self.lista = ttk.Combobox(master, textvariable=self.variable, state="readonly")
        self.lista["values"] = lista_de_valores
        self.lista.set(valor_inicial)
        self.lista.config(width=largo_de_la_caja)
        if mostrar==True:
            self.lista.grid(sticky="W", row=fila, column=1, pady=espacio_vertical)
        self.fila = fila
    def get(self):
        return self.variable.get()



class Ejercicio:
    """self
    eje_tematico
    unidad
    nombre
    lista_de_enunciados_ocultos
    existe_seleccion_multiple
    existe_desarrollo
    ruta_seleccion_multiple
    ruta_desarrollo
    """
    def __init__(self, eje_tematico, unidad, nombre):
        self.eje_tematico=eje_tematico
        self.unidad=unidad
        self.nombre=nombre

        self.cantidad_completacion = 0
        self.cantidad_desarrollo = 0
        self.cantidad_seleccion_multiple = 0
        self.cantidad_terminos_pareados = 0
        self.cantidad_verdadero_y_falso = 0

        self.lista_de_enunciados_ocultos_completacion = []
        self.lista_de_enunciados_ocultos_desarrollo = []
        self.lista_de_enunciados_ocultos_seleccion_multiple = []
        self.lista_de_enunciados_ocultos_terminos_pareados = []
        self.lista_de_enunciados_ocultos_verdadero_y_falso = []

        self.ruta_completacion = f"Paquete/{eje_tematico}/{unidad}/{nombre}/Completación.py"
        self.ruta_desarrollo = f"Paquete/{eje_tematico}/{unidad}/{nombre}/Desarrollo.py"
        self.ruta_seleccion_multiple = f"Paquete/{eje_tematico}/{unidad}/{nombre}/Selección múltiple.py"
        self.ruta_terminos_pareados = f"Paquete/{eje_tematico}/{unidad}/{nombre}/Términos pareados.py"
        self.ruta_verdadero_y_falso = f"Paquete/{eje_tematico}/{unidad}/{nombre}/Verdadero y falso.py"
        self.ruta_procedimientos = f"Paquete/{eje_tematico}/{unidad}/{nombre}/Procedimientos.py"
        self.ruta_fotos = f"Paquete/{eje_tematico}/{unidad}/{nombre}/Fotos"

        self.existe_completacion = os.path.exists(self.ruta_completacion)
        self.existe_desarrollo = os.path.exists(self.ruta_desarrollo)
        self.existe_seleccion_multiple = os.path.exists(self.ruta_seleccion_multiple)
        self.existe_terminos_pareados = os.path.exists(self.ruta_terminos_pareados)
        self.existe_verdadero_y_falso = os.path.exists(self.ruta_verdadero_y_falso)

        self.nombre_para_ordenar = self.nombre.lower().replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")

        self.entry_completacion = None
        self.entry_desarrollo= None
        self.entry_seleccion_multiple = None
        self.entry_terminos_pareados = None
        self.entry_verdadero_y_falso = None

    def __lt__(self, other):
        if self.eje_tematico!=other.eje_tematico:
            return {"Números":1, "Álgebra y funciones":2, "Geometría":3, "Estadística y probabilidades":4}[self.eje_tematico] < {"Números":1, "Álgebra y funciones":2, "Geometría":3, "Estadística y probabilidades":4}[other.eje_tematico]
        else:
            return self.unidad+self.nombre < other.unidad+other.nombre

    def __eq__(self, other):
        return self.eje_tematico==other.eje_tematico and self.unidad==other.unidad and self.nombre==other.nombre

    def __str__(self):
        return self.eje_tematico+" "+self.unidad+" "+self.nombre

    def actualizar_cantidades(self):
        if self.existe_completacion:
            self.cantidad_completacion = int(self.entry_completacion.get())
        if self.existe_desarrollo:
            self.cantidad_desarrollo = int(self.entry_desarrollo.get())
        if self.existe_seleccion_multiple:
            self.cantidad_seleccion_multiple = int(self.entry_seleccion_multiple.get())
        if self.existe_terminos_pareados:
            self.cantidad_terminos_pareados = int(self.entry_terminos_pareados.get())
        if self.existe_verdadero_y_falso:
            self.cantidad_verdadero_y_falso = int(self.entry_verdadero_y_falso.get())



class boton_align(tk.Button):
    def __init__(self, master, posicion_del_texto, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self["command"] = self.apretar
        self["text"] = {"left":"Izquierda", "center":"Centrar"}[posicion_del_texto]
        self.posicion_del_texto = posicion_del_texto

    
    def apretar(self):
        #Activa todos los botones
        for boton in self.master.winfo_children():
            boton["relief"] = "raised"
            boton["state"] = "active"
        #Desactiva el botón que fue apretado
        self["relief"] = "sunken"
        self["state"] = "disabled"

        #Tag que establece la posición del texto
        caja_con_focus = self.master.master.PanedWindow.focus_get()
        caja_con_focus.posicion_del_texto = self.posicion_del_texto
        caja_con_focus.tag_configure("tag-posicion_del_texto", justify=self.posicion_del_texto)
        caja_con_focus.tag_add("tag-posicion_del_texto", "1.0", "end")

class Text_ajustable(tk.Text):
    #https://es.stackoverflow.com/questions/362762/entry-multil%C3%ADnea-en-tkinter-o-text-con-textvariable
    def __init__(self, master, valor_inicial="", posicion_del_texto="left", *args, **kwargs):
        kwargs["relief"] = "solid"
        kwargs["borderwidth"] = 0
        super().__init__(master, *args, **kwargs)
        self._textvariable = tk.StringVar(self, value=valor_inicial)
        self._on_var_change()

        self.tk.eval("""proc widget_proxy {widget widget_command args} {

                # call the real tk widget command with the real args
                set result [uplevel [linsert $args 0 $widget_command]]

                # if the contents changed, generate an event we can bind to
                if {([lindex $args 0] in {insert replace delete})} {
                    event generate $widget <<Change>> -when tail
                }
                # return the result from the real widget command
                return $result
            }""")

        self.tk.eval(f"""rename {self} _{self}
            interp alias {{}} ::{self} {{}} widget_proxy {self} _{self}""")

        self.bind("<<Change>>", self._on_widget_change)
        self._textvariable.trace_add(("write", "unset"), self._on_var_change)
        self._textvariable.trace_add(("write", "unset"), self.key)

        #Tag que establece la posición del texto
        self.posicion_del_texto = posicion_del_texto
        self.tag_configure("tag-posicion_del_texto", justify=self.posicion_del_texto)
        self.tag_add("tag-posicion_del_texto", "1.0", "end")

    def key(self, *args):
        try:
            #Ajusta el tamaño
            self["height"] = self.get("1.0","end").count("\n")
            altura_de_fila = 1
            for box in self.master.winfo_children():
                altura_de_fila = max([altura_de_fila, box["height"]])
            self.master["height"] = altura_de_fila *16 + 8

            #Posiciona el texto
            self.tag_configure("tag-posicion_del_texto", justify=self.posicion_del_texto)
            self.tag_add("tag-posicion_del_texto", "1.0", "end")
        except:
            pass

    def _on_var_change(self, *args):
        """Change the text widget when the associated textvariable changes"""
        text_current = self.get("1.0", "end-1c")
        var_current = self._textvariable.get()
        if text_current != var_current:
            self.delete("1.0", "end")
            self.insert("1.0", var_current)
    def _on_widget_change(self, event=None):
        """Change the variable when the widget changes"""
        if self._textvariable is not None:
            self._textvariable.set(self.get("1.0", "end-1c"))

class Frame_row(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self["bg"] = master.master["bg"]
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)

        #Crea el paned window
        self.PanedWindow = tk.PanedWindow(self, bg="black", relief="solid", borderwidth=1, width=1000)
        self.PanedWindow.grid(row=0, column=1)

        #Crea los botones que agregan y quitan cajas
        self.frame_botones = tk.Frame(self, bg=master["bg"], borderwidth=0, highlightthickness=0, width=82, height=0)
        self.frame_botones.grid(row=0, column=2, padx=5, pady=5)
        self.frame_botones.propagate(False)

        self.boton_quitar_caja = tk.Button(self.frame_botones, command=self.quitar_caja, text="-1", width=3, height=1)
        self.boton_agregar_caja = tk.Button(self.frame_botones, command=self.agregar_caja, text="+1", width=3, height=1)
        
        #Crea los botones que cambian la posición del texto
        self.frame_botones_posicion_texto = tk.Frame(self, bg=master["bg"], borderwidth=0, highlightthickness=0, width=129, height=0)
        self.frame_botones_posicion_texto.grid(row=0, column=0, padx=5, pady=5)
        self.frame_botones_posicion_texto.propagate(False)

        self.boton_left = boton_align(self.frame_botones_posicion_texto, posicion_del_texto="left")
        self.boton_center = boton_align(self.frame_botones_posicion_texto, posicion_del_texto="center")



    def agregar_caja(self, valor_inicial="", posicion_del_texto="left"):
        if len(self.PanedWindow.winfo_children()) == 5:
            tk.messagebox.showinfo("TstMaker", "No se pueden crear más de 5 columnas por fila.")
            return None
        posicion = len(self.PanedWindow.winfo_children())
        self.PanedWindow.grid_columnconfigure(posicion, weight=1)
        text = Text_ajustable(self.PanedWindow, valor_inicial, posicion_del_texto, height=0.1)
        self.PanedWindow.add(text, minsize=100, sticky="nswe", stretch="always")

        #Bindea las cajas para mostrar o dejar de mostrar los botones que agregan o quitan cajas
        text.bind("<FocusIn>", self.FocusIn)
        text.bind("<FocusOut>", self.FocusOut)

    def FocusIn(self, event):
        #Activa o desactiva los botones en función del box que tiene focus
        for boton in self.frame_botones_posicion_texto.winfo_children():
            if boton.posicion_del_texto==event.widget.posicion_del_texto:
                boton["relief"] = "sunken"
                boton["state"] = "disabled"
            else:
                boton["relief"] = "raised"
                boton["state"] = "active"
        
        #Pone los botones de posición de texto y los botones de agregar o quitar cajas
        self.boton_left.grid(row=0, column=0, padx=5)
        self.boton_center.grid(row=0, column=1, padx=5)
        self.boton_quitar_caja.grid(row=0, column=0, padx=5)
        self.boton_agregar_caja.grid(row=0, column=1, padx=5)

    def FocusOut(self, event=None):
        for widget in [self.boton_quitar_caja, self.boton_agregar_caja, self.boton_left, self.boton_center]:
            widget.grid_forget()
        for frame in [self.frame_botones_posicion_texto, self.frame_botones]:
            frame["height"] = 0

    def quitar_caja(self):
        if len(self.master.winfo_children())==1 and len(self.PanedWindow.winfo_children())==1:
            tk.messagebox.showinfo("TstMaker", "No se puede quitar la tabla completa.\nSi necesitas ingresar más información puedes agregar más filas a la tabla o cambiar el tamaño de cada fila.")
            return None
        if len(self.PanedWindow.winfo_children()) == 1:
            self.destroy()
            return None
        else:
            self.PanedWindow.winfo_children()[-1].destroy()
            posicion = len(self.PanedWindow.winfo_children())
            self.PanedWindow.grid_columnconfigure(posicion, weight=0)
        
        #Esconde botones de posición de texto ya que se pierde focus, pero no se van dichos botones sin lo que viene
        self.boton_left.grid_forget()
        self.boton_center.grid_forget()
        self.frame_botones_posicion_texto["height"] = 0




def enviar_mensaje_a_servidor():
    #Prueba conexión a internet
    try:
        requests.get("http://www.google.com")
    except:
        tk.messagebox.showinfo("TstMaker", "No cuenta con conexión a internet. Revise su conexión a internet e inténtelo más tarde.")
        return None


    ####################    Genera interfaz    ####################
    frame_base.wm_attributes("-disabled", True)
    frame_base_retroalimentacion = tk.Toplevel()
    frame_base_retroalimentacion.title("TstMaker")
    frame_base_retroalimentacion.protocol("WM_DELETE_WINDOW", lambda : (frame_base.wm_attributes("-disabled", False), frame_base_retroalimentacion.destroy()))
    frame_base_retroalimentacion.geometry("500x500")
    frame_base_retroalimentacion.resizable(False, False)

    label_titulo = tk.Label(frame_base_retroalimentacion, text="Escribe aquí tu mensaje:", anchor="w")
    textbox = tk.Text(frame_base_retroalimentacion)
    boton_enviar = tk.Button(frame_base_retroalimentacion, text="Enviar", width=20, height=2, bg="#00CD63")
    label_titulo.pack(fill="x")
    textbox.pack()
    boton_enviar.pack(expand=True)

    #Función del borón
    def conectar_a_servidor():
        #Bloquea el frame de la retroalimentación
        frame_base_retroalimentacion.wm_attributes("-disabled", True)
        #Modifica el botón y lo deshabilita
        boton_enviar["state"] = "disabled"
        boton_enviar["text"] = "Enviando..."
        #Sube el archivo
        try:
            requests.post(url+"/send", data={"message":textbox.get("0.0", "end")})
            #Quita el frame de retroalimentación y activa el frame base
            frame_base.wm_attributes("-disabled", False)
            frame_base_retroalimentacion.destroy()
            tk.messagebox.showinfo("TstMaker", "Gracias por ayudar a que TstMaker sea mejor cada día.")
        except:
            #Quita el frame de retroalimentación y activa el frame base
            frame_base.wm_attributes("-disabled", False)
            frame_base_retroalimentacion.destroy()
            tk.messagebox.showinfo("TstMaker", "No se ha podido enviar tu mensaje debido a un eror inesperado. Revise su conexión a internet e inténtelo más tarde.")


    boton_enviar["command"] = conectar_a_servidor

    #Centra el frame de retroalimentacion y lo levanta
    frame_base_retroalimentacion.update_idletasks()
    width = frame_base_retroalimentacion.winfo_width()
    frm_width = frame_base_retroalimentacion.winfo_rootx() - frame_base_retroalimentacion.winfo_x()
    win_width = width + 2 * frm_width
    height = frame_base_retroalimentacion.winfo_height()
    titlebar_height = frame_base_retroalimentacion.winfo_rooty() - frame_base_retroalimentacion.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = frame_base_retroalimentacion.winfo_screenwidth() // 2 - win_width // 2
    y = frame_base_retroalimentacion.winfo_screenheight() // 2 - win_height // 2
    frame_base_retroalimentacion.geometry(f"{width}x{height}+{x}+{y}")
    frame_base_retroalimentacion.deiconify()
    frame_base_retroalimentacion.lift()

def actualizar_programa(mostrar_resultado_de_busqueda=True):
    #Prueba conexión a internet
    try:
        requests.get("http://www.google.com")
    except:
        if mostrar_resultado_de_busqueda:
            tk.messagebox.showinfo("TstMaker", "No se ha podido contactar con el servidor. Revise su conexión a internet e inténtelo más tarde.")
        return None

    #Permite paso si ya se abrió el frame_base
    while not frame_base.winfo_ismapped()==1:
        time.sleep(0.5)

    #Consulta la verisón en el servidor
    try:
        version_en_internet = requests.get(url+"/version").text
    except:
        if mostrar_resultado_de_busqueda:
            tk.messagebox.showinfo("TstMaker", "No se pudo establecer la conexión con el servidor.\nRevise su conexión a internet e inténtelo más tarde.")
        return None

    #Detiene la actualización si la versión instalada es la misma que está en el servidor
    if  open("version.txt","r").read() == version_en_internet:
        if mostrar_resultado_de_busqueda:
            tk.messagebox.showinfo("TstMaker", "TstMaker ya es encuentra en su versión más actual.")
        return None

    #Hay una actualización en el servidor. Pregunta si quiere instalarla
    if not tk.messagebox.askyesno("TstMaker", "Se ha encontrado una actualización disponible.\n¿Deseas instalarla ahora?"):
        return None

    #Pregunta si quiere actualizar
    if open("version.txt","r").read() != requests.get(url+"/version").text:
        while not frame_base.winfo_ismapped()==1:
            time.sleep(0.5)

    #Genera segunda ventana
    frame_base.wm_attributes("-disabled", True)
    frame_base_actualizacion = tk.Toplevel()
    frame_base_actualizacion.title("TstMaker")
    frame_base_actualizacion.geometry("300x60")
    frame_base_actualizacion.resizable(False, False)
    frame_base_actualizacion.protocol("WM_DELETE_WINDOW", lambda : (frame_base.wm_attributes("-disabled", False), frame_base_actualizacion.destroy()))

    barra_actualizacion = ttk.Progressbar(frame_base_actualizacion, length=350, style="Horizontal.TProgressbar", value=0, maximum=5)
    label_informacion_actualizacion = tk.Label(frame_base_actualizacion, text="Conectando con el servidor")
    label_puntos = tk.Label(frame_base_actualizacion, text="")

    barra_actualizacion.pack(expand=True)
    label_informacion_actualizacion.pack()
    label_puntos.pack()

    #Centra el frame de actualizacion y lo levanta
    frame_base_actualizacion.update_idletasks()
    width = frame_base_actualizacion.winfo_width()
    frm_width = frame_base_actualizacion.winfo_rootx() - frame_base_actualizacion.winfo_x()
    win_width = width + 2 * frm_width
    height = frame_base_actualizacion.winfo_height()
    titlebar_height = frame_base_actualizacion.winfo_rooty() - frame_base_actualizacion.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = frame_base_actualizacion.winfo_screenwidth() // 2 - win_width // 2
    y = frame_base_actualizacion.winfo_screenheight() // 2 - win_height // 2
    frame_base_actualizacion.geometry(f"{width}x{height}+{x}+{y}")
    frame_base_actualizacion.deiconify()
    frame_base_actualizacion.lift()

    #Cambia los puntos constantamente
    def cambiar_puntos():
        while True:
            try:
                cantidad_puntos = len(label_puntos["text"])
                label_puntos["text"] = "."*((cantidad_puntos+1)%4)
            except:
                return None
            time.sleep(0.5)
    threading.Thread(target=cambiar_puntos, daemon=True).start()

    #Descargar el rar
    try:
        barra_actualizacion["value"], barra_actualizacion["maximum"] = 0, 100
        label_informacion_actualizacion["text"] = "Descargando archivos de la nueva versión"
        respuesta = requests.get(url+"/download", stream=True)
        tamaño_descarga = int(respuesta.headers.get("content-length"))
        total_descargado = 0
        size_chunks = 2048
        with open("new_version.zip", "wb") as file:
            for data in respuesta.iter_content(size_chunks):
                file.write(data)
                total_descargado += size_chunks
                barra_actualizacion["value"] = min([int(total_descargado*100/tamaño_descarga), 100])
        barra_actualizacion["value"], barra_actualizacion["maximum"] = 2, 5
    except:
        if os.path.exists("new_version.zip"):
            os.remove("new_version.zip")
        frame_base.wm_attributes("-disabled", False)
        tk.messagebox.showinfo("TstMaker", "La actualización ha sido interrumpida.")
        frame_base_actualizacion.destroy()
        return None
    

    #Crea la carpeta "temp" y extrae el rar
    label_informacion_actualizacion["text"] = "Extrayendo archivos"
    if os.path.exists("temp"):
        shutil.rmtree("temp")
    shutil.unpack_archive("new_version.zip", "temp")
    try:
        barra_actualizacion["value"] = barra_actualizacion["maximum"]
    except:
        if os.path.exists("temp"):
            shutil.rmtree("temp")
        os.remove("new_version.zip")
        frame_base.wm_attributes("-disabled", False)
        tk.messagebox.showinfo("TstMaker", "La actualización ha sido interrumpida por del usuario.")
        frame_base_actualizacion.destroy()
        return None

    #Desactiva la salida para que la actualización no se pueda detener
    frame_base_actualizacion.wm_attributes("-disabled", True)

    ###################CREA EL .bat PARA TERMINAR LA OPERACION#############
    #Carpeta contenedora
    current_path = os.path.abspath(__file__)
    folder_container = os.path.dirname(current_path)
    with open("replacer.bat", "w", encoding="utf-8") as file:
        #Se pone en la ubicación de tstmaker
        file.write("cd "+folder_container+"\n\n")

        #Mata el proceso
        file.write(f"taskkill /F /PID {os.getpid()}\n\n")

        #Elimina los archivos actuales
        for archivo in os.listdir():
            if archivo not in ["temp", "replacer.bat", "version.txt"]:
                if "." in archivo:
                    file.write("DEL /F /Q \""+archivo+"\"\n")
                else:
                    file.write("Rmdir /Q /S \""+archivo+"\"\n")
        file.write("\n")

        #Se posiciona en la carpeta del tstmaker
        file.write("cd \""+folder_container+"\\temp"+"\"\n")

        #Mueve la versión nueva
        for archivo in os.listdir("temp"):
            if archivo not in ["version.txt"]:
                file.write("move \""+archivo+"\" \""+folder_container+"\"\n")
        file.write("\n")

        #Vuelve a la carpeta de tstmaker
        file.write("cd "+folder_container+"\n")

        #Elimina la carpeta temporal y el bat
        file.write("Rmdir /Q /S  \"temp\"\n")
        file.write("DEL /F /Q \"replacer.bat\"\n")
        file.write("exit")
        file.close()
        while not os.path.exists("replacer.bat"):
            pass

    #Crea el version.txt
    file = open("version.txt","w",encoding="utf-8")
    file.write(version_en_internet)
    file.close()

    #Mensaje final de actualización, pide reboot
    label_informacion_actualizacion["text"] = "Esperando aceptación de usuario"

    #Avisa que se completó la actualización y abre el replacer.bat
    frame_base_actualizacion.destroy()
    tk.messagebox.showinfo("TstMaker", "La actualización se ha completado exitosamente.\nPor favor reinicie TstMaker para hacer efectivo el cambio.")
    os.startfile(folder_container+r"\replacer.bat")




def mostrar_ocultar_extra_de_tamaño_de_papel(nombre, vacio, modo):
    if tamaño_del_papel.get() == "Otro":
        alto.mostrar = True
        alto.label.grid(sticky="W", row=alto.fila, column=0, padx=50)
        alto.entry.grid(sticky="W", row=alto.fila, column=1, padx=50)
        ancho.mostrar = True
        ancho.label.grid(sticky="W", row=ancho.fila, column=0, padx=50)
        ancho.entry.grid(sticky="W", row=ancho.fila, column=1, padx=50)
    else:
        alto.mostrar = False
        alto.label.grid_forget()
        alto.entry.grid_forget()
        ancho.mostrar = False
        ancho.label.grid_forget()
        ancho.entry.grid_forget()

def determinar_ancho_alto(nombre, vacio, modo):
    if tamaño_del_papel.get() == "Carta":
        ancho.entry.delete(0,"end")
        ancho.entry.insert(0,"21,59")
        alto.entry.delete(0,"end")
        alto.entry.insert(0,"27,94")
    elif tamaño_del_papel.get() == "Oficio":
        ancho.entry.delete(0,"end")
        ancho.entry.insert(0,"21,59")
        alto.entry.delete(0,"end")
        alto.entry.insert(0,"35.56")
    else:
        ancho.entry.delete(0,"end")
        ancho.entry.insert(0,"21,59")
        alto.entry.delete(0,"end")
        alto.entry.insert(0,"33")

def establecer_cantidad_general(boton_establecer):
    boton_establecer["state"] = "disabled"
    boton_establecer["text"] = "Estableciendo..."
    for ejercicio in lista_de_todos_los_ejercicios:
        if ejercicio.existe_completacion:
            ejercicio.entry_completacion.variable.set(cantidad_a_establecer_para_todos.get())
            ejercicio.entry_completacion.insert(0,"0")
            ejercicio.entry_completacion.actualizar_carrito()

        if ejercicio.existe_desarrollo:
            ejercicio.entry_desarrollo.variable.set(cantidad_a_establecer_para_todos.get())
            ejercicio.entry_desarrollo.insert(0,"0")
            ejercicio.entry_desarrollo.actualizar_carrito()

        if ejercicio.existe_seleccion_multiple:
            ejercicio.entry_seleccion_multiple.variable.set(cantidad_a_establecer_para_todos.get())
            ejercicio.entry_seleccion_multiple.insert(0,"0")
            ejercicio.entry_seleccion_multiple.actualizar_carrito()

        if ejercicio.existe_terminos_pareados:
            ejercicio.entry_terminos_pareados.variable.set(cantidad_a_establecer_para_todos.get())
            ejercicio.entry_terminos_pareados.insert(0,"0")
            ejercicio.entry_terminos_pareados.actualizar_carrito()

        if ejercicio.existe_verdadero_y_falso:
            ejercicio.entry_verdadero_y_falso.variable.set(cantidad_a_establecer_para_todos.get())
            ejercicio.entry_verdadero_y_falso.insert(0,"0")
            ejercicio.entry_verdadero_y_falso.actualizar_carrito()
    boton_establecer["text"] = "Establecer cantidad global"
    boton_establecer["state"] = "normal"

def agregar_preambulo_y_tabla_con_datos():
    global frame_tabla
    #Preámbulo
    doc.preamble.append(pylatex.NoEscape(r"\usepackage{ragged2e}"+"\n"+r"\usepackage{setspace}"+"\n"+r"\usepackage{longtable}"+"\n"+r"\usepackage{tabularx}"+"\n"+r"\usepackage{gensymb}"+"\n"+r"\usepackage{amsmath}"+"\n"+r"\usepackage{enumitem}"+"\n"+r"\usepackage{graphicx}"+"\n"+r"\usepackage{tikz}"+"\n"+r"\usepackage{tkz-euclide}"+"\n"+r"\usepackage{siunitx}"+"\n"+r"\usepackage{fourier}"+"\n"+r"\usetikzlibrary{fit, shapes.geometric, quotes, angles, through, intersections}"+"\n"+fr"\usepackage[papersize={{{ancho.get().replace(',','.')}cm, {alto.get().replace(',','.')}cm}},tmargin=2cm,bmargin=2cm,lmargin=2cm,rmargin=2cm]{{geometry}}"))
    #doc.preamble.append(pylatex.NoEscape(r"\usepgfplotslibrary{external}"+"\n"+r"\tikzexternalizer"))


    #Logo y Tabla con la información de la prueba y el alumno
    poner_primera_linea = True
    doc.append(pylatex.NoEscape(r"\begin{center} \begin{tabular}{p{17 cm}}"+"\n"))
    for fila in frame_tabla.winfo_children():
        doc.append(pylatex.NoEscape(r"\begin{tabularx}{\linewidth}{|"))

        #Calcula y establece porcentajes
        width_total = 0
        for box in fila.PanedWindow.winfo_children():
            width_total += box.winfo_width()
        for box in fila.PanedWindow.winfo_children():
            division = box.winfo_width()/width_total
            diccionario_de_posiciones = {"left": "", "center":r"\Centering ", "right":r"\raggedleft "}
            doc.append(pylatex.NoEscape(fr">{{{diccionario_de_posiciones[box.posicion_del_texto]}\hsize={division}\hsize}}X|"))
        doc.append(pylatex.NoEscape("}"))

        #Pone primera linea
        if poner_primera_linea:
            doc.append(pylatex.NoEscape(r"\hline"))
            poner_primera_linea = False

        #Pone unidades
        poner_separador_de_columnas = False
        for box in fila.PanedWindow.winfo_children():
            if poner_separador_de_columnas:
                doc.append(pylatex.NoEscape(r" & "))
            poner_separador_de_columnas = True
            doc.append(box.get("1.0", "end-1c"))
        #Cierra la tabla de la fila
        doc.append(pylatex.NoEscape(r" \\ \hline \end{tabularx} \\"))

    #Cierra la tabla más grande
    doc.append(pylatex.NoEscape(r"\end{tabular} \end{center}" + "\n"))




    #Agrega las instrucciones
    # if instrucciones.get() != "\n":
    #     doc.append("Instrucciones:")
    #     doc.append(pylatex.NoEscape(r"\begin{itemize} \item"))
    #     linea = ""
    #     cantidad_de_saltos = instrucciones.get().count("\n")-1
    #     saltos_utilizados = 0
    #     for letra in instrucciones.get():
    #         if not letra=="\n":
    #             linea += letra
    #         else:
    #             doc.append(linea)
    #             linea=""
    #             if saltos_utilizados<cantidad_de_saltos:
    #                 doc.append(pylatex.NoEscape(r"\item"))
    #                 saltos_utilizados +=1
    #     doc.append(pylatex.NoEscape(r"\end{itemize}"))


    #Instrucciones mías

    # Lee la evaluación completa antes de contestar.
    # Responda con letra clara y legible.
    # Utiliza solo lápiz de pasta azul o negro o lápiz grafito.
    # Las respuestas escritas con grafito o con presencia de corrector no podrán ser reclamadas en caso de error en la corrección por parte del docente.
    # Tienes 75 minutos para responder.
    # El uso de cuadernos, libros, teléfonos o cualquier otro material no necesario para el desarrollo de la evaluación será considerado copia.
    # Compartir materiales será considerado copia.
    # Cualquier tipo de comunicación con otro compañero será considerado copia.
    # El uso de calculadora será permitido, siempre y cuando el docente lo establezca verbalmente.
    # Sólo habrá dos instancias, indicadas por el docente, de 5 minutos cada una, para realizar preguntas.
    # La copia tendrá como consecuencia el inmediato retiro de la prueba y corrección con nota máxima 40.

    doc_respuestas.preamble.append(pylatex.NoEscape(r"\usepackage{ragged2e}"+"\n"+r"\usepackage{setspace}"+"\n"+r"\usepackage{longtable}"+"\n"+r"\usepackage{gensymb}"+"\n"+r"\usepackage{amsmath}"+"\n"+r"\usepackage{enumitem}"+"\n"+r"\usepackage{graphicx}"+"\n"+r"\usepackage{tikz}"+"\n"+r"\usepackage{tkz-euclide}"+"\n"+r"\usepackage{siunitx}"+"\n"+r"\usepackage{fourier}"+"\n"+r"\usetikzlibrary{fit, shapes.geometric, quotes, angles, through, intersections}"+"\n"+fr"\usepackage[papersize={{{ancho.get().replace(',','.')}cm, {alto.get().replace(',','.')}cm}},tmargin=2cm,bmargin=2cm,lmargin=2cm,rmargin=2cm]{{geometry}}"))
    # doc_respuestas.preamble.append(pylatex.NoEscape(r"\usepgfplotslibrary{external}"+"\n"+r"\tikzexternalizer"))
    doc_procedimientos.preamble.append(pylatex.NoEscape(r"\usepackage{ragged2e}"+"\n"+r"\usepackage{setspace}"+"\n"+r"\usepackage{longtable}"+"\n"+r"\usepackage{gensymb}"+"\n"+r"\usepackage{amsmath}"+"\n"+r"\usepackage{enumitem}"+"\n"+r"\usepackage{graphicx}"+"\n"+r"\usepackage{tikz}"+"\n"+r"\usepackage{tkz-euclide}"+"\n"+r"\usepackage{siunitx}"+"\n"+r"\usepackage{fourier}"+"\n"+r"\usetikzlibrary{fit, shapes.geometric, quotes, angles, through, intersections}"+"\n"+fr"\usepackage[papersize={{{ancho.get().replace(',','.')}cm, {alto.get().replace(',','.')}cm}},tmargin=2cm,bmargin=2cm,lmargin=2cm,rmargin=2cm]{{geometry}}"))
    # doc_procedimientos.preamble.append(pylatex.NoEscape(r"\usepgfplotslibrary{external}"+"\n"+r"\tikzexternalizer"))

def agregar_ejercicios_completacion(lista_de_ejercicios):
    print("Se inició el agregado de completación")
    doc.append(pylatex.NoEscape(r"Item Completación: Responde cada pregunta. No es necesario que la respuesta incluya desarrollo."))
    barra_de_progreso["value"] += 1
    label_de_progreso["text"] = f"Ejercicios calculados: {barra_de_progreso['value']} de {barra_de_progreso['maximum']}"
    print("Se terminó la zona de importación de completación")

def agregar_ejercicios_desarrollo(lista_de_ejercicios):
    print("Se inició el agregado de desarrollo")
    respuestas = []
    doc.append(pylatex.NoEscape(r"Item Desarrollo: Responde lo pedido en cada caso. Debe haber desarrollo que justifique cada respuesta."))
    doc.append(pylatex.NoEscape(r"\begin{enumerate}[label=\arabic*),start=1]"))

    #====================================Zona de importación====================================
    #Decide el ejercicio a usar
    while 0 < len(lista_de_ejercicios):
        if desordenar_ejercicios.get()==True:
            ejercicio = choice(lista_de_ejercicios)
        else:
            ejercicio = lista_de_ejercicios[0]



        print(f"Se está intentando importar {ejercicio.ruta_desarrollo} de tipo desarrollo")



        #Importa hasta que las alternativas sean distintas o el enunciado no haya sido usado
        espacio_para_el_desarrollo = 8
        file = open(ejercicio.ruta_desarrollo, "r", encoding="utf-8")
        interior_de_ejercicio = file.read()
        file.close()
        exec(interior_de_ejercicio+"\nejercicio.desarrollo_enunciado, ejercicio.desarrollo_contenido_correcto, ejercicio.desarrollo_enunciado_oculto, ejercicio.desarrollo_espacio_para_el_desarrollo = enunciado, contenido_correcto, enunciado_oculto, espacio_para_el_desarrollo")

        while ejercicio.desarrollo_enunciado_oculto in ejercicio.lista_de_enunciados_ocultos_desarrollo:
            if ejercicio.desarrollo_enunciado_oculto in ejercicio.lista_de_enunciados_ocultos_desarrollo:
                print(f"En {ejercicio.eje_tematico} {ejercicio.unidad} {ejercicio.nombre} de tipo desarrollo se repitió el enunciado")
                print(ejercicio.desarrollo_enunciado)
                print(ejercicio.desarrollo_contenido_correcto)
                pass

            exec(interior_de_ejercicio+"\nejercicio.desarrollo_enunciado, ejercicio.desarrollo_contenido_correcto, ejercicio.desarrollo_enunciado_oculto, ejercicio.desarrollo_espacio_para_el_desarrollo = enunciado, contenido_correcto, enunciado_oculto, espacio_para_el_desarrollo")
        ejercicio.lista_de_enunciados_ocultos_desarrollo.append(ejercicio.desarrollo_enunciado_oculto)

        #Pone el enunciado y el nombre del ejercicio
        doc.append(pylatex.NoEscape(r"\item"))

        doc.append(pylatex.NoEscape(ejercicio.desarrollo_enunciado + espacio_para_el_desarrollo*("\n"+r"\hfill \break")))
        # doc.append(pylatex.NoEscape(r"\hfill \break"))
        # doc.append(pylatex.NoEscape(r"\\"))

        #Agrega la respuesta a la lista de respuestas correctas
        respuestas.append(ejercicio.desarrollo_contenido_correcto)


        #Reduce en 1 la cantidad de ejercicios a importar y lo elimina de la lista si ya no quedan
        ejercicio.cantidad_desarrollo -= 1
        if ejercicio.cantidad_desarrollo == 0:
            lista_de_ejercicios.remove(ejercicio)
        barra_de_progreso["value"] += 1
        label_de_progreso["text"] = f"Ejercicios calculados: {barra_de_progreso['value']} de {barra_de_progreso['maximum']}"

    #================================Fin Zona de importación====================================
    print("Se terminó la zona de importación de desarrollo")

    #Finaliza la tabla y completa el pdf
    doc.append(pylatex.NoEscape(r"\end{enumerate}"))


    #Agrega las respuestas correctas
    doc_respuestas.append(pylatex.NoEscape(r"Estas son las respuestas correctas del item de desarrollo:"))
    doc_respuestas.append(pylatex.NoEscape(r"\begin{enumerate}[label=\arabic*),start=1]"))

    for respuesta in respuestas:
        doc_respuestas.append(pylatex.NoEscape(r"\item"))
        doc_respuestas.append(pylatex.NoEscape(respuesta))

    doc_respuestas.append(pylatex.NoEscape(r"\end{enumerate}"))

def agregar_ejercicios_seleccion_multiple(lista_de_ejercicios):
    print("Se inició el agregado de la selección múltiple")
    respuestas = []
    numero_del_ejercicio = 1
    doc.append(pylatex.NoEscape(r"""Item Selección multiple: Encierra en un círculo la alternativa correcta en cada caso.
    \begin{longtable}{|p{8.3 cm}|p{8.3 cm}|}
    \hline"""))

    #====================================Zona de importación====================================
    #Decide el ejercicio a usar
    while 0 < len(lista_de_ejercicios):
        if desordenar_ejercicios.get()==True:
            ejercicio = choice(lista_de_ejercicios)
        else:
            ejercicio = lista_de_ejercicios[0]



        print(f"Se está intentando importar {ejercicio.ruta_seleccion_multiple} de tipo selección múltiple")



        #Importa hasta que las alternativas sean distintas o el enunciado no haya sido usado
        file = open(ejercicio.ruta_seleccion_multiple, "r", encoding="utf-8")
        interior_de_ejercicio = file.read()
        file.close()
        exec(interior_de_ejercicio+"\nejercicio.seleccion_multiple_enunciado, ejercicio.seleccion_multiple_contenido_correcto, ejercicio.seleccion_multiple_contenido_2, ejercicio.seleccion_multiple_contenido_3, ejercicio.seleccion_multiple_contenido_4, ejercicio.seleccion_multiple_contenido_5, ejercicio.seleccion_multiple_enunciado_oculto = enunciado, contenido_correcto, contenido_2, contenido_3, contenido_4, contenido_5, enunciado_oculto")


        while ejercicio.seleccion_multiple_contenido_correcto==ejercicio.seleccion_multiple_contenido_2 or ejercicio.seleccion_multiple_contenido_correcto==ejercicio.seleccion_multiple_contenido_3 or ejercicio.seleccion_multiple_contenido_correcto==ejercicio.seleccion_multiple_contenido_4 or ejercicio.seleccion_multiple_contenido_correcto==ejercicio.seleccion_multiple_contenido_5 or ejercicio.seleccion_multiple_contenido_2==ejercicio.seleccion_multiple_contenido_3 or ejercicio.seleccion_multiple_contenido_2==ejercicio.seleccion_multiple_contenido_4 or ejercicio.seleccion_multiple_contenido_2==ejercicio.seleccion_multiple_contenido_5 or ejercicio.seleccion_multiple_contenido_3==ejercicio.seleccion_multiple_contenido_4 or ejercicio.seleccion_multiple_contenido_3==ejercicio.seleccion_multiple_contenido_5 or ejercicio.seleccion_multiple_contenido_4==ejercicio.seleccion_multiple_contenido_5 or ejercicio.seleccion_multiple_enunciado_oculto in ejercicio.lista_de_enunciados_ocultos_seleccion_multiple:
            if ejercicio.seleccion_multiple_enunciado_oculto in ejercicio.lista_de_enunciados_ocultos_seleccion_multiple:
                print(f"En {ejercicio.eje_tematico} {ejercicio.unidad} {ejercicio.nombre} de tipo selección múltiple se repitió el enunciado")
                pass
            else:
                if ejercicio.seleccion_multiple_contenido_correcto==ejercicio.seleccion_multiple_contenido_2:
                    print(f"1 y 2")
                    pass
                elif ejercicio.seleccion_multiple_contenido_correcto==ejercicio.seleccion_multiple_contenido_3:
                    print(f"1 y 3")
                    pass
                elif ejercicio.seleccion_multiple_contenido_correcto==ejercicio.seleccion_multiple_contenido_4:
                    print(f"1 y 4")
                    pass
                elif ejercicio.seleccion_multiple_contenido_correcto==ejercicio.seleccion_multiple_contenido_5:
                    print(f"1 y 5")
                    pass
                elif ejercicio.seleccion_multiple_contenido_2==ejercicio.seleccion_multiple_contenido_3:
                    print(f"2 y 3")
                    pass
                elif ejercicio.seleccion_multiple_contenido_2==ejercicio.seleccion_multiple_contenido_4:
                    print(f"2 y 4")
                    pass
                elif ejercicio.seleccion_multiple_contenido_2==ejercicio.seleccion_multiple_contenido_5:
                    print(f"2 y 5")
                    pass
                elif ejercicio.seleccion_multiple_contenido_3==ejercicio.seleccion_multiple_contenido_4:
                    print(f"3 y 4")
                    pass
                elif ejercicio.seleccion_multiple_contenido_3==ejercicio.seleccion_multiple_contenido_5:
                    print(f"3 y 5")
                    pass
                elif ejercicio.seleccion_multiple_contenido_4==ejercicio.seleccion_multiple_contenido_5:
                    print(f"4 y 5")
                    pass
                
                print(ejercicio.seleccion_multiple_enunciado)
                print(ejercicio.seleccion_multiple_contenido_correcto)
                print(ejercicio.seleccion_multiple_contenido_2)
                print(ejercicio.seleccion_multiple_contenido_3)
                print(ejercicio.seleccion_multiple_contenido_4)
                print(ejercicio.seleccion_multiple_contenido_5)
            exec(interior_de_ejercicio+"\nejercicio.seleccion_multiple_enunciado, ejercicio.seleccion_multiple_contenido_correcto, ejercicio.seleccion_multiple_contenido_2, ejercicio.seleccion_multiple_contenido_3, ejercicio.seleccion_multiple_contenido_4, ejercicio.seleccion_multiple_contenido_5, ejercicio.seleccion_multiple_enunciado_oculto = enunciado, contenido_correcto, contenido_2, contenido_3, contenido_4, contenido_5, enunciado_oculto")

        ejercicio.lista_de_enunciados_ocultos_seleccion_multiple.append(ejercicio.seleccion_multiple_enunciado_oculto)
        #Pone el enunciado
        doc.append(pylatex.NoEscape(r"\begin{enumerate}[label=\arabic*),start=" f"{numero_del_ejercicio}" "]"))
        doc.append(pylatex.NoEscape(r"\item"))
        doc.append(pylatex.NoEscape(ejercicio.seleccion_multiple_enunciado))
        doc.append(pylatex.NoEscape(r"\end{enumerate}"))

        #No tocar esto. Genera la lista con los contenidos
        lista_contenidos = [ejercicio.seleccion_multiple_contenido_2, ejercicio.seleccion_multiple_contenido_3, ejercicio.seleccion_multiple_contenido_4, ejercicio.seleccion_multiple_contenido_5][0:int(cantidad_de_alternativas_por_pregunta.get())-1]
        lista_contenidos.append(ejercicio.seleccion_multiple_contenido_correcto)

        #Empiezan el entorno de las alternativas
        doc.append(pylatex.NoEscape(r"\begin{enumerate}[label=\Alph*)]"))
        numero_de_la_alternativa = 1
        shuffle(lista_contenidos)
        for contenido in lista_contenidos:
            #Elije y establece los contenidos de las alternativas
            doc.append(pylatex.NoEscape(r"\item"))
            doc.append(pylatex.NoEscape(contenido))

            #Guarda la alternativa correcta
            if contenido == ejercicio.seleccion_multiple_contenido_correcto:
                alternativa_correcta = {1:"A", 2:"B", 3:"C", 4:"D", 5:"E"}[numero_de_la_alternativa]

            numero_de_la_alternativa += 1
        doc.append(pylatex.NoEscape(r"\end{enumerate}"))
        
        #Agrega la respuesta a la lista de respuestas correctas
        respuestas.append(f"{numero_del_ejercicio}) {alternativa_correcta}")
        
        #Decide si la tabla sigue hacia al lado o hacia abajo
        if numero_del_ejercicio % 2 == 1:
            doc.append(pylatex.NoEscape("&"))
        else:
            doc.append(pylatex.NoEscape(r"\\"))
            doc.append(pylatex.NoEscape(r"\hline"))

        numero_del_ejercicio += 1


        #Reduce en 1 la cantidad de ejercicios a importar y lo elimina de la lista si ya no quedan
        ejercicio.cantidad_seleccion_multiple -= 1
        if ejercicio.cantidad_seleccion_multiple == 0:
            lista_de_ejercicios.remove(ejercicio)
        barra_de_progreso["value"] += 1
        label_de_progreso["text"] = f"Ejercicios calculados: {barra_de_progreso['value']} de {barra_de_progreso['maximum']}"

    #================================Fin Zona de importación====================================
    print("Se terminó la zona de importación de selección múltiple")



    #Finaliza la tabla y completa el pdf
    if numero_del_ejercicio % 2 == 0:
        doc.append(pylatex.NoEscape(r"\\"))
        doc.append(pylatex.NoEscape(r"\hline \end{longtable}"))
    else:
        doc.append(pylatex.NoEscape(r"\end{longtable}"))



    #Genera otro pdf con las respuestas
    doc_respuestas.append(pylatex.NoEscape(r"Estas son las respuestas correctas del item de selección múltiple:\\\\"))
    doc_respuestas.append(pylatex.NoEscape(r"\begin{longtable}{|p{4 cm}|p{4 cm}|}"))
    doc_respuestas.append(pylatex.NoEscape(r"\hline"))

    for respuesta in respuestas:
        doc_respuestas.append(respuesta)
        if respuestas.index(respuesta) % 2 == 0:
            doc_respuestas.append(pylatex.NoEscape("&"))
        else:
            doc_respuestas.append(pylatex.NoEscape(r"\\"))
            doc_respuestas.append(pylatex.NoEscape(r"\hline"))

    if len(respuestas) % 2 == 0:
        doc_respuestas.append(pylatex.NoEscape(r"\end{longtable}"))    
    else:
        doc_respuestas.append(pylatex.NoEscape(r"\\"))
        doc_respuestas.append(pylatex.NoEscape(r"\hline"))
        doc_respuestas.append(pylatex.NoEscape(r"\end{longtable}"))

def agregar_ejercicios_terminos_pareados(lista_de_ejercicios):
    print("Se inició el agregado de términos pareados")
    doc.append(pylatex.NoEscape(r"Item Términos pareados: Relaciona los elementos escribiendo la letra correspondiente."))
    barra_de_progreso["value"] += 1
    label_de_progreso["text"] = f"Ejercicios calculados: {barra_de_progreso['value']} de {barra_de_progreso['maximum']}"
    print("Se terminó la zona de importación de términos pareados")

def agregar_ejercicios_verdadero_y_falso(lista_de_ejercicios):
    print("Se inició el agregado de términos pareados")
    respuestas = []
    doc.append(pylatex.NoEscape(r"Item Verdadero y falso: Encierra en un círculo la letra V si el enunciado es verdadero o la letra F si el enunciado es falso. Debes justificar las falsas."))
    doc.append(pylatex.NoEscape(r"\begin{enumerate}[label=\arabic*),start=1]"))

    #====================================Zona de importación====================================
    #Decide el ejercicio a usar
    while 0 < len(lista_de_ejercicios):
        if desordenar_ejercicios.get()==True:
            ejercicio = choice(lista_de_ejercicios)
        else:
            ejercicio = lista_de_ejercicios[0]



        print(f"Se está intentando importar {ejercicio.ruta_verdadero_y_falso} de tipo verdadero y falso")



        #Importa hasta que las alternativas sean distintas o el enunciado no haya sido usado
        tipo_de_ejercicio_a_incluir = choice([True,True,True,False,False,False,False,False,False,False])
        espacio_para_el_desarrollo = 1
        file = open(ejercicio.ruta_verdadero_y_falso, "r", encoding="utf-8")
        interior_de_ejercicio = file.read()
        file.close()
        exec(interior_de_ejercicio+"\nejercicio.verdadero_y_falso_enunciado_verdadero, ejercicio.verdadero_y_falso_enunciado_falso, ejercicio.verdadero_y_falso_enunciado_oculto, ejercicio.verdadero_y_falso_espacio_para_el_desarrollo = enunciado_verdadero, enunciado_falso, enunciado_oculto, espacio_para_el_desarrollo")
        while ejercicio.verdadero_y_falso_enunciado_verdadero==ejercicio.verdadero_y_falso_enunciado_falso or ejercicio.verdadero_y_falso_enunciado_oculto in ejercicio.lista_de_enunciados_ocultos_verdadero_y_falso:

            if ejercicio.verdadero_y_falso_enunciado_oculto in ejercicio.lista_de_enunciados_ocultos_verdadero_y_falso:
                print(f"En {ejercicio.eje_tematico} {ejercicio.unidad} {ejercicio.nombre} de tipo verdadero y falso se repitió el enunciado")
                print(ejercicio.verdadero_y_falso_enunciado_verdadero)
                print(ejercicio.verdadero_y_falso_enunciado_falso)
                pass

            elif ejercicio.verdadero_y_falso_enunciado_verdadero==ejercicio.verdadero_y_falso_enunciado_falso:
                print("El enunciado verdadero y el falso eran iguales")
                pass
            tipo_de_ejercicio_a_incluir = choice([True,True,True,False,False,False,False,False,False,False])
            exec(interior_de_ejercicio+"\nejercicio.verdadero_y_falso_enunciado_verdadero, ejercicio.verdadero_y_falso_enunciado_falso, ejercicio.verdadero_y_falso_enunciado_oculto, ejercicio.verdadero_y_falso_espacio_para_el_desarrollo = enunciado_verdadero, enunciado_falso, enunciado_oculto, espacio_para_el_desarrollo")
        ejercicio.lista_de_enunciados_ocultos_verdadero_y_falso.append(ejercicio.verdadero_y_falso_enunciado_oculto)

        #Pone el enunciado y el nombre del ejercicio
        doc.append(pylatex.NoEscape(r"\item"))


        #Pone el enunciado y agrega la respuesta a la lista de respuestas correctas
        if tipo_de_ejercicio_a_incluir==True:
            doc.append(pylatex.NoEscape(r"V\ \ \ \ F\ \ \ \ "+ejercicio.verdadero_y_falso_enunciado_verdadero))
            respuestas.append("Verdadero")
        elif tipo_de_ejercicio_a_incluir==False:
            doc.append(pylatex.NoEscape(r"V\ \ \ \ F\ \ \ \ "+ejercicio.verdadero_y_falso_enunciado_falso))
            respuestas.append(r"Falso\\Justificación: "+ejercicio.verdadero_y_falso_enunciado_verdadero)

        doc.append(pylatex.NoEscape(espacio_para_el_desarrollo*("\n"+r"\hfill \break")+"\n"+115*r"\_"))



        #Reduce en 1 la cantidad de ejercicios a importar y lo elimina de la lista si ya no quedan
        ejercicio.cantidad_verdadero_y_falso -= 1
        if ejercicio.cantidad_verdadero_y_falso == 0:
            lista_de_ejercicios.remove(ejercicio)
        barra_de_progreso["value"] += 1
        label_de_progreso["text"] = f"Ejercicios calculados: {barra_de_progreso['value']} de {barra_de_progreso['maximum']}"

    #================================Fin Zona de importación====================================
    print("Se terminó la zona de importación de verdadero y falso")

    #Finaliza la tabla y completa el pdf
    doc.append(pylatex.NoEscape(r"\end{enumerate}"))

    #Agrega las respuestas correctas
    doc_respuestas.append(pylatex.NoEscape(r"Estas son las respuestas correctas del item de verdadero y falso:"))
    doc_respuestas.append(pylatex.NoEscape(r"\begin{enumerate}[label=\arabic*),start=1]"))

    for respuesta in respuestas:
        doc_respuestas.append(pylatex.NoEscape(r"\item"))
        doc_respuestas.append(pylatex.NoEscape(respuesta))

    doc_respuestas.append(pylatex.NoEscape(r"\end{enumerate}"))

def generar_pdf():
    #Deshabilita el frame base
    frame_base.wm_attributes("-disabled", True)
    #En estas listas se meterán los ejercicios a importar
    lista_de_ejercicios_completacion_a_incluir = []
    lista_de_ejercicios_desarrollo_a_incluir = []
    lista_de_ejercicios_terminos_pareados_a_incluir = []
    lista_de_ejercicios_seleccion_multiple_a_incluir = []
    lista_de_ejercicios_verdadero_y_falso_a_incluir = []

    #Obtiene las cantidades de todos los ejercicios
    cantidad_total_de_ejercicios_en_archivo = 0
    for ejercicio in lista_de_todos_los_ejercicios:
        ejercicio.lista_de_enunciados_ocultos_completacion = []
        ejercicio.lista_de_enunciados_ocultos_desarrollo = []
        ejercicio.lista_de_enunciados_ocultos_seleccion_multiple = []
        ejercicio.lista_de_enunciados_ocultos_terminos_pareados = []
        ejercicio.lista_de_enunciados_ocultos_verdadero_y_falso = []

        ejercicio.actualizar_cantidades()

        if 0 < ejercicio.cantidad_completacion:
            lista_de_ejercicios_completacion_a_incluir.append(ejercicio)
        if 0 < ejercicio.cantidad_desarrollo:
            lista_de_ejercicios_desarrollo_a_incluir.append(ejercicio)
        if 0 < ejercicio.cantidad_terminos_pareados:
            lista_de_ejercicios_terminos_pareados_a_incluir.append(ejercicio)
        if 0 < ejercicio.cantidad_seleccion_multiple:
            lista_de_ejercicios_seleccion_multiple_a_incluir.append(ejercicio)
        if 0 < ejercicio.cantidad_verdadero_y_falso:
            lista_de_ejercicios_verdadero_y_falso_a_incluir.append(ejercicio)
        
        ejercicio.total_de_ejercicios = ejercicio.cantidad_completacion + ejercicio.cantidad_desarrollo + ejercicio.cantidad_terminos_pareados + ejercicio.cantidad_seleccion_multiple + ejercicio.cantidad_verdadero_y_falso
        cantidad_total_de_ejercicios_en_archivo += ejercicio.total_de_ejercicios

    #Ventana emergente en caso de que la prueba esté vacía
    if cantidad_total_de_ejercicios_en_archivo == 0:
        if not tk.messagebox.askyesno("TstMaker", "No has seleccionado ejercicios, por lo que la evaluación estará vacía y no se generarán otros documentos.\n¿Deseas continuar de todas formas?"):
            frame_base.wm_attributes("-disabled", False)
            return None

    #Genera el nombre del archivo
    nombre_del_archivo = nombre_de_la_prueba.get()
    if nombre_del_archivo=="":
        nombre_del_archivo = "Sin nombre"

    #Abre el explorador y genera la ruta de guardado
    ruta_escritorio = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop") # determina la ruta del escritorio
    ruta_completa = asksaveasfilename(title="Guardar como", initialdir=ruta_escritorio, initialfile=nombre_del_archivo, filetypes=(("Formato pdf","*.pdf"),)) #abre el explorador

    #Detiene la creación si no se eligió una ruta. Esto puede ser porque se canceló o se cerró el explorador
    if ruta_completa=="":
        frame_base.wm_attributes("-disabled", False)
        return None
    ruta_incompleta = ruta_completa[:ruta_completa.rfind("/")+1] #se quita desde el siguiente del último / en adelante
    archivo_con_formato = ruta_completa[ruta_completa.rfind("/")+1:] #nombre del archivo con el .pdf
    if "." in archivo_con_formato:
        archivo_sin_formato = archivo_con_formato[:archivo_con_formato.find(".")]
    else:
        archivo_sin_formato = archivo_con_formato
    if archivo_sin_formato.replace(" ","")=="":
        archivo_sin_formato = "Sin nombre"
    ruta_de_guardado = ruta_incompleta+archivo_sin_formato

    #Comienza a tomar el tiempo
    inicio_cronometro = time.time()

    #Genera las variables que contienen la información de los archivos fotmato .tex
    global doc, doc_respuestas, doc_procedimientos, barra_de_progreso, label_de_progreso, interrumpido
    doc = pylatex.Document(page_numbers=None)
    doc_respuestas = pylatex.Document(page_numbers=None)
    doc_procedimientos = pylatex.Document(page_numbers=None)


    ######################  NUEVO FRAME#################
    frame_base_progreso = tk.Toplevel()
    interrumpido = False
    
    def interrumpir_generacion_pdf():
        # global interrumpido
        frame_base.wm_attributes("-disabled", False)
        global doc, doc_respuestas, doc_procedimientos, interrumpido
        interrumpido = True
        del doc, doc_respuestas, doc_procedimientos
        frame_base_progreso.destroy()
        #Mata el proceso lualatex.exe
        for _ in range(3):
            for process in psutil.process_iter():
                if process.name() == "lualatex.exe":
                    process.kill()
        tk.messagebox.showinfo("TstMaker", "La creación de los archivos ha sido interrumpida.")
        if os.path.exists("temp"):
            shutil.rmtree("temp")


    #Configura el frame
    frame_base_progreso.title("TstMaker")
    frame_base_progreso.protocol("WM_DELETE_WINDOW", interrumpir_generacion_pdf)
    frame_base_progreso.resizable(False, False)

    #Pone los widget en el frame
    barra_de_progreso = ttk.Progressbar(frame_base_progreso, length=350, style="Horizontal.TProgressbar", value=0)
    label_de_progreso = tk.Label(frame_base_progreso, text=f"Ejercicios calculados: 0 de {barra_de_progreso['maximum']}\n", bg="#FFEEDD")
    barra_de_progreso.grid(row=0, column=0)
    label_de_progreso.grid(row=1, column=0)

    # #Centra el frame de progreso y lo levanta
    frame_base_progreso.update_idletasks()
    width = frame_base_progreso.winfo_width()
    frm_width = frame_base_progreso.winfo_rootx() - frame_base_progreso.winfo_x()
    win_width = width + 2 * frm_width
    height = frame_base_progreso.winfo_height()
    titlebar_height = frame_base_progreso.winfo_rooty() - frame_base_progreso.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = frame_base_progreso.winfo_screenwidth() // 2 - win_width // 2
    y = frame_base_progreso.winfo_screenheight() // 2 - win_height // 2
    frame_base_progreso.geometry(f"{width}x{height}+{x}+{y}")
    frame_base_progreso.deiconify()
    frame_base_progreso.lift()



    #Genera la carpeta que contiene los archivos y genera los hilos que generan los archivos
    if os.path.exists("temp"):
        shutil.rmtree("temp")
    os.mkdir("temp")

    #######################AQUI VA EL TRY#########
    #Agrega preámbulos a los tres archivos
    #Agrega la tabla de información en la guía
    agregar_preambulo_y_tabla_con_datos()

    #Configura la barra de progreso
    barra_de_progreso["maximum"] = int(cantidad_total_de_ejercicios_en_archivo)
    #Importa los ejercicios Completación
    if len(lista_de_ejercicios_completacion_a_incluir) != 0:
        agregar_ejercicios_completacion(lista_de_ejercicios_completacion_a_incluir)
    #Importa los ejercicios Desarrollo
    if len(lista_de_ejercicios_desarrollo_a_incluir) != 0:
        agregar_ejercicios_desarrollo(lista_de_ejercicios_desarrollo_a_incluir)
    #Importa los ejercicios Términos pareados
    if len(lista_de_ejercicios_terminos_pareados_a_incluir) != 0:
        agregar_ejercicios_terminos_pareados(lista_de_ejercicios_terminos_pareados_a_incluir)
    #Importa los ejercicios Selección múltiple
    if len(lista_de_ejercicios_seleccion_multiple_a_incluir) != 0:
        agregar_ejercicios_seleccion_multiple(lista_de_ejercicios_seleccion_multiple_a_incluir)
    #Establece las cantidades. Verdadero y falso
    if len(lista_de_ejercicios_verdadero_y_falso_a_incluir) != 0:
        agregar_ejercicios_verdadero_y_falso(lista_de_ejercicios_verdadero_y_falso_a_incluir)

    #Llena el pdf de procedimientos
    if generar_pdf_con_procedimientos.get() and not interrumpido:
        doc_procedimientos.append(pylatex.NoEscape(r"A continuación se presentan los procedimientos para realizar los ejercicios:\hfill \break \hfill \break \hfill \break"+"\n"))
        for ejercicio in lista_de_todos_los_ejercicios:
            salto_automatico, procedimiento = False, "No se ha creado esta explicación"
            if 0 < ejercicio.total_de_ejercicios:
                file = open(ejercicio.ruta_procedimientos, "r", encoding="utf-8")
                interior_de_ejercicio = file.read()
                file.close()
                print(f"{ejercicio.unidad}, {ejercicio.nombre}")
                exec(interior_de_ejercicio+"\nejercicio.procedimiento_salto_automatico, ejercicio.procedimiento_procedimiento = salto_automatico, procedimiento")
                if ejercicio.procedimiento_salto_automatico:
                    ejercicio.procedimiento_procedimiento = ejercicio.procedimiento_procedimiento.replace("\n", "\n"+r"\hfill \break"+"\n")
                doc_procedimientos.append(pylatex.NoEscape(r"\begin{center}"))
                doc_procedimientos.append(ejercicio.nombre)
                doc_procedimientos.append(pylatex.NoEscape(r"\end{center}"))
                doc_procedimientos.append(pylatex.NoEscape(r"\hfill \break \hfill \break"))
                doc_procedimientos.append(pylatex.NoEscape(procedimiento+"\n"+r"\newpage"))

    #Se inician las generaciones de los pdf
    current_path = os.path.abspath(__file__)
    folder_container = os.path.dirname(current_path).replace("\\","/")
    #vbs y bat de prueba
    if not interrumpido:
        doc.generate_tex("temp/Prueba")
        with open("temp/Prueba.vbs", "w", encoding="utf-8") as file:
            file.write('Set WshShell = CreateObject("WScript.Shell")'+"\n")
            file.write(f'WshShell.Run chr(34) & "{folder_container}\\temp\\Prueba.bat" & Chr(34), 0'+"\n")
            file.write("Set WshShell = Nothing"+"\n")
            file.close()
        with open("temp/Prueba.bat", "w", encoding="utf-8") as file:
            file.write(f'cd "{folder_container}\\temp"' + "\n")
            file.write(f'lualatex "Prueba.tex"' + "\n")
            file.write(f'DEL /F /Q "Prueba.vbs"' + "\n")
            file.write(f'DEL /F /Q "Prueba.bat"' + "\n")
            file.write("exit"+"\n")
            file.close()
        os.startfile(f'"{folder_container}\\temp\\Prueba.vbs"')
    #vbs y bat de respuestas
    if generar_pdf_con_respuestas.get() and cantidad_total_de_ejercicios_en_archivo!=0 and not interrumpido:
        doc_respuestas.generate_tex("temp/Respuestas")
        with open("temp/Respuestas.vbs", "w", encoding="utf-8") as file:
            file.write('Set WshShell = CreateObject("WScript.Shell")'+"\n")
            file.write(f'WshShell.Run chr(34) & "{folder_container}\\temp\\Respuestas.bat" & Chr(34), 0'+"\n")
            file.write("Set WshShell = Nothing"+"\n")
        with open("temp/Respuestas.bat", "w", encoding="utf-8") as file:
            file.write(f'cd "{folder_container}\\temp"' + "\n")
            file.write(f'lualatex "Respuestas.tex"' + "\n")
            file.write(f'DEL /F /Q "Respuestas.vbs"' + "\n")
            file.write(f'DEL /F /Q "Respuestas.bat"' + "\n")
            file.write("exit"+"\n")
            file.close()
        os.startfile(f'"{folder_container}\\temp\\Respuestas.vbs"')
    #vbs y bat de procedimientos
    if generar_pdf_con_procedimientos.get() and not interrumpido:
        doc.generate_tex("temp/Procedimiento")
        with open("temp/Procedimientos.vbs", "w", encoding="utf-8") as file:
            file.write('Set WshShell = CreateObject("WScript.Shell")'+"\n")
            file.write(f'WshShell.Run chr(34) & "{folder_container}\\temp\\Procedimientos.bat" & Chr(34), 0'+"\n")
            file.write("Set WshShell = Nothing"+"\n")
            file.close()
        with open("temp/Procedimientos.bat", "w", encoding="utf-8") as file:
            file.write(f'cd "{folder_container}\\temp"' + "\n")
            file.write(f'lualatex "Procedimientos.tex"' + "\n")
            file.write(f'DEL /F /Q "Procedimientos.vbs"' + "\n")
            file.write(f'DEL /F /Q "Procedimientos.bat"' + "\n")
            file.write("exit"+"\n")
            file.close()
        os.startfile(f'"{folder_container}\\temp\\Procedimientos.vbs"')

    #Cambia la forma en que avanza la barra de progreso
    tiempo_calculo = time.time()-inicio_cronometro    
    barra_de_progreso["value"] = 0
    tamaño_esperado = int(os.path.getsize("temp/Prueba.tex")*1.265839027)
    barra_de_progreso["maximum"] = tamaño_esperado
    label_de_progreso["text"] = f"Generando archivos. Esto puede tomar unos minutos.\n0 bytes  /  {tamaño_esperado} bytes"

    #Se espera que los pdf terminen de crearse, se sabe que terminó cicho proceso poeruq se borran los .bat
    #Aumenta la barra de progreso mientras se compilan los pdf's
    while os.path.exists("temp/Prueba.bat") or os.path.exists("temp/Respuestas.bat") or os.path.exists("temp/Procedimientos.bat"):
        time.sleep(0.2)
        if os.path.exists("temp/Prueba.pdf"):
            tamaño_actual = os.path.getsize("temp/Prueba.pdf")
            barra_de_progreso["value"] = tamaño_actual
            label_de_progreso["text"] = f"Generando archivos. Esto puede tomar unos minutos.\n{min(tamaño_actual,tamaño_esperado)} bytes  /  {tamaño_esperado} bytes"
    barra_de_progreso["value"] = barra_de_progreso["maximum"]
    label_de_progreso["text"] = f"Generando archivos. Esto puede tomar unos minutos.\n{tamaño_esperado} bytes  /  {tamaño_esperado} bytes"
    time.sleep(1)
    
    #Mueve los archivos a donde se pidió
    while not interrumpido:
        if interrumpido:
            break
        try:
            shutil.move("temp/Prueba.pdf", ruta_de_guardado+".pdf")
            break
        except:
            if not tk.messagebox.askretrycancel("TstMaker", f"No puede generarse \"{nombre_del_archivo}.pdf\" debido a que hay un archivo en la dirección de destino con el mismo nombre que no puede ser borrado ya que otro programa lo tiene abierto. Cierre dicho archivo e inténtelo de nuevo."):
                break

    if mantener_archivo_tex.get():
        while not interrumpido:
            if interrumpido:
                break
            try:
                shutil.move("temp/Prueba.tex", ruta_de_guardado+".tex")
                break
            except:
                if not tk.messagebox.askretrycancel("TstMaker", f"No puede generarse \"{nombre_del_archivo}.tex\" debido a que hay un archivo en la dirección de destino con el mismo nombre que no puede ser borrado ya que otro programa lo tiene abierto. Cierre dicho archivo e inténtelo de nuevo."):
                    break

    if generar_pdf_con_respuestas.get() and cantidad_total_de_ejercicios_en_archivo!=0:
        while not interrumpido:
            if interrumpido:
                break
            try:
                shutil.move("temp/Respuestas.pdf", ruta_de_guardado+" - Respuestas.pdf")
                break
            except:
                if not tk.messagebox.askretrycancel("TstMaker", f"No puede generarse \"{nombre_del_archivo} - Respuestas.pdf\" debido a que hay un archivo en la dirección de destino con el mismo nombre que no puede ser borrado ya que otro programa lo tiene abierto. Cierre dicho archivo e inténtelo de nuevo."):
                    break

    if generar_pdf_con_procedimientos.get() and cantidad_total_de_ejercicios_en_archivo!=0:
        while not interrumpido:
            try:
                shutil.move("temp/Procedimientos.pdf", ruta_de_guardado+" - Procedimientos.pdf")
                break
            except:
                if not tk.messagebox.askretrycancel("TstMaker", f"No puede generarse \"{nombre_del_archivo} - Procedimientos.pdf\" debido a que hay un archivo en la dirección de destino con el mismo nombre que no puede ser borrado ya que otro programa lo tiene abierto. Cierre dicho archivo e inténtelo de nuevo."):
                    break
    if os.path.exists("temp"):
        shutil.rmtree("temp")

    #Calcula tiempo que demoró la compilación
    tiempo_total = time.time()-inicio_cronometro
    tiempo_compilacion = tiempo_total - tiempo_calculo
    print(f"Tiempo de cálculo {tiempo_calculo}")
    print(f"Tiempo de compilación {tiempo_compilacion}")
    print(f"Tiempo total {tiempo_total}")
    print(f"compilacion/calculo {(tiempo_compilacion)/(tiempo_calculo)}")
    print(f"Tiempo total/Cantidad total {(tiempo_total)/(tiempo_calculo)}")

    frame_base.wm_attributes("-disabled", False)
    if not interrumpido:
        frame_base_progreso.destroy()
        tk.messagebox.showinfo("TstMaker", "Ha finalizado el proceso de creación de documentos.")



def generador_fila_frame_datos():
    fila_generada = 0
    while True:
        yield fila_generada
        fila_generada+=1
fila_de_frame_datos = generador_fila_frame_datos()

def guardar_confiruracion():
    global frame_tabla
    file = open("Configuracion.py", "w", encoding="utf-8")
    file.write(f"""cantidad_de_alternativas_por_pregunta = "{cantidad_de_alternativas_por_pregunta.get()}"\ndesordenar_ejercicios = {desordenar_ejercicios.get()}\ngenerar_pdf_con_respuestas = {generar_pdf_con_respuestas.get()}\ngenerar_pdf_con_procedimientos = {generar_pdf_con_procedimientos.get()}\nmantener_archivo_tex = {mantener_archivo_tex.get()}\ncantidad_a_establecer_para_todos = "{cantidad_a_establecer_para_todos.get()}"\ninstrucciones = \"\"\"{instrucciones.get()[:-1]}\"\"\"\n""")
    file.write("tabla_inicial = [\n")
    for row in frame_tabla.winfo_children():
        contenido_de_la_fila = []
        for box in row.PanedWindow.winfo_children():
            contenido_de_la_fila.append(
                {"contenido_de_la_caja":box.get("1.0", "end-1c"), "posicion_del_texto":box.posicion_del_texto}
                )
        file.write("    "+str(contenido_de_la_fila)+",\n")
    file.write("    ]\n")
    file.close()

def test_lualatex():
    #Deshabilita el frame base
    frame_base.wm_attributes("-disabled", True)

    #Configura el frame
    frame_base_progreso = tk.Toplevel()
    frame_base_progreso.title("TstMaker")
    frame_base_progreso.protocol("WM_DELETE_WINDOW", lambda : None)
    frame_base_progreso.resizable(False, False)

    #Configura los label
    label_de_progreso = tk.Label(frame_base_progreso, text="Buscando distribución de TeX/LaTeX en su sistema.", bg=frame_base_progreso["bg"], width=70)
    label_de_progreso.grid(row=0, column=0, pady=4)
    label_puntos = tk.Label(frame_base_progreso, text="", bg=frame_base_progreso["bg"])
    label_puntos.grid(row=1, column=0, pady=2, sticky="nswe")
    def cambiar_puntos():
        while True:
            try:
                cantidad_puntos = len(label_puntos["text"])
                label_puntos["text"] = "."*((cantidad_puntos+1)%4)
            except:
                return None
            time.sleep(0.2)
    threading.Thread(target=cambiar_puntos, daemon=True).start()

    # #Centra el frame de progreso y lo levanta
    frame_base_progreso.update_idletasks()
    width = frame_base_progreso.winfo_width()
    frm_width = frame_base_progreso.winfo_rootx() - frame_base_progreso.winfo_x()
    win_width = width + 2 * frm_width
    height = frame_base_progreso.winfo_height()
    titlebar_height = frame_base_progreso.winfo_rooty() - frame_base_progreso.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = frame_base_progreso.winfo_screenwidth() // 2 - win_width // 2
    y = frame_base_progreso.winfo_screenheight() // 2 - win_height // 2
    frame_base_progreso.geometry(f"{width}x{height}+{x}+{y}")
    frame_base_progreso.deiconify()
    frame_base_progreso.lift()
    #Determina el path
    current_path = os.path.abspath(__file__)
    folder_container = os.path.dirname(current_path)

    #Recarga la carpeta temporal
    if os.path.exists("temp"):
        shutil.rmtree("temp")  
    os.mkdir("temp")

    #Revisa si lualatex está instalado
    file = open("temp/test_1.vbs", "w", encoding="utf-8")
    file.write('Set WshShell = CreateObject("WScript.Shell")'+"\n")
    file.write(f'WshShell.Run chr(34) & "{folder_container}\\temp\\test_1.bat" & Chr(34), 0'+"\n")
    file.write("Set WshShell = Nothing"+"\n")
    file.close()
    file = open("temp/test_1.tex", "w", encoding="utf-8")
    file.write(r"\documentclass{article}"+"\n"+r"\begin{document}"+"\n"+r"test"+"\n"+r"\end{document}")
    file.close()
    file = open("temp/test_1.bat", "w", encoding="utf-8")
    file.write(f"cd {folder_container}\\temp\nlualatex --interaction=nonstopmode test_1.tex" + "\n" + "DEL /F /Q test_1.bat")
    file.close()
    os.startfile(folder_container+"\\temp\\test_1.vbs")
    while os.path.exists("temp/test_1.bat"):
        time.sleep(0.5)

    if not os.path.exists("temp/test_1.pdf"):
        frame_base.wm_attributes("-disabled", False)
        frame_base_progreso.destroy()
        tk.messagebox.showinfo("TstMaker", "No se encuentra instalada ninguna distribución de TeX/LaTeX en su sistema.\nSe le recomienda descargar e instalar MiKTeX desde la página oficial https://miktex.org con la instalación de paquetes configurada en el modo \"on the fly\".\nDe no hacerlo, TstMaker no podrá generar sus documentos.")
    #lualatex está instalado, pero ahora revisa si los paquetes están instalados, o bien si se pueden isntalar los paquetes "on the fly"
    else:
        label_de_progreso["text"] = "Revisando configuración de paquetes de su distribución de TeX/LaTeX en su sistema."
        file = open("temp/test_2.vbs", "w", encoding="utf-8")
        file.write('Set WshShell = CreateObject("WScript.Shell")'+"\n")
        file.write(f'WshShell.Run chr(34) & "{folder_container}\\temp\\test_2.bat" & Chr(34), 0'+"\n")
        file.write("Set WshShell = Nothing"+"\n")
        file.close()
        file = open("temp/test_2.tex", "w", encoding="utf-8")
        file.write(r"\documentclass{article}"+"\n"+r"\usepackage[T1]{fontenc}"+"\n"+r"\usepackage[utf8]{inputenc}"+"\n"+r"\usepackage{lmodern}"+"\n"+r"\usepackage{textcomp}"+"\n"+r"\usepackage{ragged2e}"+"\n"+r"\usepackage{setspace}"+"\n"+r"\usepackage{longtable}"+"\n"+r"\usepackage{tabularx}"+"\n"+r"\usepackage{gensymb}"+"\n"+r"\usepackage{amsmath}"+"\n"+r"\usepackage{enumitem}"+"\n"+r"\usepackage{graphicx}"+"\n"+r"\usepackage{tikz}"+"\n"+r"\usepackage{tkz-euclide}"+"\n"+r"\usepackage{siunitx}"+"\n"+r"\usepackage{fourier}"+"\n"+r"\usetikzlibrary{fit, shapes.geometric, quotes, angles, through, intersections}"+"\n"+fr"\usepackage[papersize={{{ancho.get().replace(',','.')}cm, {alto.get().replace(',','.')}cm}},tmargin=2cm,bmargin=2cm,lmargin=2cm,rmargin=2cm]{{geometry}}"+"\n"+r"\begin{document}"+"\n"+"test\n"+r"\end{document}")
        file.close()
        file = open("temp/test_2.bat", "w", encoding="utf-8")
        file.write(f"cd {folder_container}\\temp\nlualatex --interaction=nonstopmode test_2.tex" + "\n" + "DEL /F /Q test_2.bat")
        file.close()
        os.startfile(folder_container+"\\temp\\test_2.vbs")
        while os.path.exists("temp/test_2.bat"):
            time.sleep(0.5)
        frame_base.wm_attributes("-disabled", False)
        if os.path.exists("temp/test_2.pdf"):
            frame_base_progreso.destroy()
            tk.messagebox.showinfo("TstMaker", "Su distribución de TeX/LaTeX se encuentra correctamente instalada y configurada en su sistema.")
        else:
            frame_base_progreso.destroy()
            tk.messagebox.showinfo("TstMaker", "Su distribución de TeX/LaTeX se encuentra correctamente instalada, pero no los paquetes.\nConfigure la instalación de paquetes de su distribución en el modo \"on the fly\", esto puede hacerlo reinstalándola.\nDe no hacerlo, TstMaker no podrá generar sus documentos.")
    #Borra la carpeta temporal
    shutil.rmtree("temp")

style = ttk.Style()
style.theme_create( "estilo", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
        "TNotebook.Tab": {
            "configure": {"padding": [5, 1], "background": "light green" },
            "map":       {"background": [("selected", "red"), ("active", "#fc9292")],
                          "foreground": [("selected", "#ffffff"), ("active", "#000000")],
                          "expand": [("selected", [1, 1, 1, 0])] 
                         }
                         }
                                                    }
                   )
style.theme_use("estilo")
style.configure("Horizontal.TProgressbar", foreground='blue', background='red')








#Construye la interfaz
notebook_principal = ttk.Notebook(frame_base, name="notebook_principal")
notebook_principal.pack(fill="both", expand="yes")

#Aquí se crea el panel llamado Inicio
frame_datos = tk.Frame(notebook_principal)
notebook_principal.add(frame_datos, text="Datos")

#Frame donde irán las pociones de la prueba, pero no la tabla
sub_frame_1_datos = tk.Frame(frame_datos)
sub_frame_1_datos.pack(fill="x", padx=40, pady=40)
#Opciones de la prueba
nombre_de_la_prueba = Entry_datos(sub_frame_1_datos, "Nombre del documento", next(fila_de_frame_datos), valor_inicial="", mostrar=True, largo=40)
cantidad_de_alternativas_por_pregunta = Combobox_datos(sub_frame_1_datos, "Cantidad de alternativas por pregunta", next(fila_de_frame_datos), Configuracion.cantidad_de_alternativas_por_pregunta, ["5","4","3","2"], 2)
desordenar_ejercicios = Checkbutton_datos(sub_frame_1_datos, "Desordenar ejercicios", next(fila_de_frame_datos), Configuracion.desordenar_ejercicios)
generar_pdf_con_respuestas = Checkbutton_datos(sub_frame_1_datos, "Generar pdf con respuestas", next(fila_de_frame_datos), Configuracion.generar_pdf_con_respuestas)
mantener_archivo_tex = Checkbutton_datos(sub_frame_1_datos, "Generar archivo .tex", next(fila_de_frame_datos), Configuracion.mantener_archivo_tex)
cantidad_a_establecer_para_todos = Entry_datos(sub_frame_1_datos, "Cantidad global", next(fila_de_frame_datos), Configuracion.cantidad_a_establecer_para_todos, largo=6)
tamaño_del_papel = Combobox_datos(sub_frame_1_datos, "Tamaño de papel", next(fila_de_frame_datos), "Carta", ["Carta", "Oficio", "Otro"], 8)
#Se genera, pero no se muestra
generar_pdf_con_procedimientos = Checkbutton_datos(sub_frame_1_datos, "Generar pdf con procedimientos", next(fila_de_frame_datos), Configuracion.generar_pdf_con_procedimientos, mostrar=False)
ancho = Entry_datos(sub_frame_1_datos, "Ancho (cm)", next(fila_de_frame_datos), "21,59", mostrar=False)
alto = Entry_datos(sub_frame_1_datos, "Alto (cm)", next(fila_de_frame_datos), "27,94", mostrar=False)
instrucciones = Text_datos(sub_frame_1_datos, "Instrucciones", next(fila_de_frame_datos), 140, valor_inicial=Configuracion.instrucciones, mostrar=False)

tamaño_del_papel.variable.trace("w", mostrar_ocultar_extra_de_tamaño_de_papel)
tamaño_del_papel.variable.trace("w", determinar_ancho_alto)
#Genera el botón para establecer una cantidad general en todos los ejercicios
boton_establecer = tk.Button(sub_frame_1_datos, text="Establecer cantidad global", width=20, height=2, bg="#00CD63")
boton_establecer["command"] = lambda : threading.Thread(target=establecer_cantidad_general, kwargs={"boton_establecer":boton_establecer}, daemon=True).start()
boton_establecer.grid(row=5, column=1, padx=0, sticky="e")












#Frame que contiene la tabla y los botones que agregan filas
frame_tabla_y_botones = tk.Frame(frame_datos)
frame_tabla_y_botones.pack()

#Frame de la tabla
frame_tabla = tk.Frame(frame_tabla_y_botones, borderwidth=0, highlightthickness=0)
frame_tabla.pack(pady=10)

#Llena la tabla con la guardada
for fila in Configuracion.tabla_inicial:
    nueva_fila = Frame_row(frame_tabla)
    for diccionario in fila:
        nueva_fila.agregar_caja(valor_inicial=diccionario["contenido_de_la_caja"], posicion_del_texto=diccionario["posicion_del_texto"])
    nueva_fila.pack(side="top", fill="x")
    for box in nueva_fila.PanedWindow.winfo_children():
        box.key()

#Función que crea las filas y las pone en la lista anterior
def crear_row():
    nueva_fila = Frame_row(frame_tabla)
    nueva_fila.agregar_caja()
    nueva_fila.pack(side="top", fill="x")


#Frame donde irá el botón que agrega una fila
boton_crea_fila = tk.Button(frame_tabla_y_botones, bg="green", text=f"Agregar fila", height=2, command=crear_row)
boton_crea_fila.pack()

#Genera la interfaz de los ejercicios
lista_de_todos_los_ejercicios = []
for eje_tematico in ["Números", "Álgebra y funciones", "Geometría", "Estadística y probabilidades"]:
    #Genera el frame de la eje_tematico y agrega la pestaña al notebook_principal
    frame = tk.Frame(notebook_principal, name="frame "+eje_tematico)
    # exit()
    notebook_principal.add(frame, text=eje_tematico)

    #Genera el notebook para la eje_tematico
    notebook = ttk.Notebook(frame, name="sub_notebook "+eje_tematico)
    notebook.pack(fill="both", expand="yes")

    for unidad in os.listdir(f"Paquete/{eje_tematico}"):
        #Genera el frame del notebook y agrega la pestaña
        frame_base_unidad = tk.Frame(notebook, name="frame "+unidad)
        frame_base_unidad.pack(fill="both")
        notebook.add(frame_base_unidad, text=unidad)

        frame_base_unidad.grid_columnconfigure(0, weight=70)
        frame_base_unidad.grid_columnconfigure(1, weight=30)
        frame_base_unidad.grid_rowconfigure(0, weight=1)

        #Genera el frame donde se eligen los ejercicios
        frame_ejercicios_unidad = Frame_ejercicios(frame_base_unidad, bg="white")
        frame_ejercicios_unidad.grid(row=0 ,column=0, sticky="nsew")

        #Genera el frame donde está la descripción
        frame_descripcion_unidad = Frame_descripcion(frame_base_unidad, bg="white")
        frame_descripcion_unidad.grid(row=1 ,column=0, sticky="nsew")

        #Genera el frame de vista previa
        frame_vista_previa_unidad = Frame_vista_previa(frame_base_unidad)
        frame_vista_previa_unidad.grid(row=0, column=1, rowspan=2, sticky="nsew")

        x = 1
        for contenido in os.listdir(f"Paquete/{eje_tematico}/{unidad}"):
            ejercicio = Ejercicio(eje_tematico, unidad, contenido)
            lista_de_todos_los_ejercicios.append(ejercicio)
            y = 0
            largo_entrys = 8
            #Genera la variable y entry de completación
            if ejercicio.existe_completacion:
                ejercicio.entry_completacion = Entry_ejercicio(frame_ejercicios_unidad.scrollable_frame, width=largo_entrys, eje_tematico=ejercicio.eje_tematico, unidad=ejercicio.unidad, nombre=ejercicio.nombre, item="Completación")
                ejercicio.entry_completacion.grid(row=x, column=0)
            #Genera la variable y entry de desarrollo
            if ejercicio.existe_desarrollo:
                ejercicio.entry_desarrollo = Entry_ejercicio(frame_ejercicios_unidad.scrollable_frame, width=largo_entrys, eje_tematico=ejercicio.eje_tematico, unidad=ejercicio.unidad, nombre=ejercicio.nombre, item="Desarrollo")
                ejercicio.entry_desarrollo.grid(row=x, column=1)
            #Genera la variable y entry de selección múltiple
            if ejercicio.existe_seleccion_multiple:
                ejercicio.entry_seleccion_multiple = Entry_ejercicio(frame_ejercicios_unidad.scrollable_frame, width=largo_entrys, eje_tematico=ejercicio.eje_tematico, unidad=ejercicio.unidad, nombre=ejercicio.nombre, item="Selección múltiple")
                ejercicio.entry_seleccion_multiple.grid(row=x, column=2)
            #Genera la variable y entry de términos pareados
            if ejercicio.existe_terminos_pareados:
                ejercicio.entry_terminos_pareados = Entry_ejercicio(frame_ejercicios_unidad.scrollable_frame, width=largo_entrys, eje_tematico=ejercicio.eje_tematico, unidad=ejercicio.unidad, nombre=ejercicio.nombre, item="Términos pareados")
                ejercicio.entry_terminos_pareados.grid(row=x, column=3)
            #Genera la variable y entry de verdadero y falso
            if ejercicio.existe_verdadero_y_falso:
                ejercicio.entry_verdadero_y_falso = Entry_ejercicio(frame_ejercicios_unidad.scrollable_frame, width=largo_entrys, eje_tematico=ejercicio.eje_tematico, unidad=ejercicio.unidad, nombre=ejercicio.nombre, item="Verdadero y falso")
                ejercicio.entry_verdadero_y_falso.grid(row=x, column=4)
            #Genera las labels de los ejercicios considerando la cantidad de tipos de item
            ejercicio.label = tk.Label(frame_ejercicios_unidad.scrollable_frame, text=ejercicio.nombre, bg="light yellow")
            ejercicio.label.grid(sticky="W", row=x, column=5)
            ejercicio.label.bind("<MouseWheel>", frame_ejercicios_unidad.mouse_wheel)
            x+=1










frame_carrito = Frame_carrito(notebook_principal)
notebook_principal.add(frame_carrito, text="Carrito")

boton_generar_pdf = tk.Button(frame_carrito, text="Generar evaluación", width=20, height=2, command=lambda : threading.Thread(target=generar_pdf,daemon=True).start(), bg="#00CD63")

boton_limpiar_carrito = tk.Button(frame_carrito, text="Limpiar carrito", width=20, height=2, command=lambda : threading.Thread(target=frame_carrito.limpiar,daemon=True).start(), bg="#00CD63")

boton_generar_pdf.grid(row=0, column=0, pady=20)
boton_limpiar_carrito.grid(row=0, column=1, pady=20)









Barra_menu = tk.Menu(frame_base)
frame_base.config(menu=Barra_menu)

Menu_1 = tk.Menu(Barra_menu, tearoff=0)
Menu_1.add_command(label="Guardar datos", command=guardar_confiruracion)
Menu_1.add_command(label="Generar evaluación", command=lambda : threading.Thread(target=generar_pdf,daemon=True).start())
Menu_1.add_separator()
Menu_1.add_command(label="Salir", command=frame_base.destroy)
Barra_menu.add_cascade(label="Archivo", menu=Menu_1)

Menu_2 = tk.Menu(Barra_menu, tearoff=0)
Menu_2.add_command(label="Enviar comentarios", command=enviar_mensaje_a_servidor)
Menu_2.add_separator()
Menu_2.add_command(label="Buscar actualizaciones...", command=lambda:threading.Thread(target=actualizar_programa).start())
Menu_2.add_command(label="Hacer diagnóstico de lualatex", command=lambda:threading.Thread(target=test_lualatex).start())
Menu_2.add_separator()
Menu_2.add_command(label="Acerca de", command=lambda : tk.messagebox.showinfo("TstMaker", f"""Nombre del programa: TstMaker
Autor: Bastián Gabriel Paredes Padget
Versión: {open("version.txt","r").read()}
Todos los derechos reservados."""))
Barra_menu.add_cascade(label="Ayuda", menu=Menu_2)








threading.Thread(target=actualizar_programa, kwargs={"mostrar_resultado_de_busqueda":False}).start()
frame_base.mainloop()



