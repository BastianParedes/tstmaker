from Definiciones import *

#Borra la carpeta temp
if os.path.exists("temp"):
    shutil.rmtree("temp")

#Genera la raiz
frame_base = tk.Tk()
frame_base.title("TstMaker")
frame_base.state("zoomed")

class Frame_datos(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        frame_base.frame_datos = self
        super().__init__(master, *args, **kwargs)

        self.canvas = tk.Canvas(self, highlightthickness=0, name="canvas")
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, name="scrollable_frame", bg=self["bg"])
        self.ventana = self.canvas.create_window((0, 0), window=self.scrollable_frame)

        self.canvas.propagate(True)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.bind("<MouseWheel>", self.mouse_wheel)
        self.scrollable_frame.bind("<Configure>", lambda _: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.bind("<MouseWheel>", self.mouse_wheel)

        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="top", fill="both", expand=True)

    def mouse_wheel(self, event):
        if not self.scrollable_frame.winfo_height() <= self.canvas.winfo_height():
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

class Frame_treeview(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        frame_base.frame_treeview = self
        super().__init__(master, *args, **kwargs)

        #Focus actual
        self.ejercicio_actual = None
        self.eje_tematico_actual = None
        self.unidad_actual = None
        self.contenido_actual = None

        #Treeview
        style = ttk.Style()
        style.configure("Treeview",
                background="white",
                foreground="black",
                rowheight=45,
                fieldbackground="white")
        style.map("Treeview", background=[("selected", "lightblue")])

        self.treeview = ttk.Treeview(self, show="tree", style="Treeview", selectmode="browse")
        self.treeview.tag_configure("mouse_over", background="#dfebf7")
        self.treeview.bind("<Motion>", self.mouse_over, add=True)
        self.treeview.tag_bind("Eje_temático", "<<TreeviewSelect>>", self.abrir_cerrar_actualizar)
        self.treeview.tag_bind("Unidad", "<<TreeviewSelect>>", self.abrir_cerrar_actualizar)
        self.treeview.tag_bind("Ejercicio", "<<TreeviewSelect>>", self.desplegar_spinboxs_poner_vista_previa)
        self.treeview.pack(fill="both", expand=True, side="left")

        #Scrollbar
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(fill="y", side="right")

    def mouse_over(self, event):
        event.widget.tk.call(self.treeview, "tag", "remove", "mouse_over")
        event.widget.tk.call(self.treeview, "tag", "add", "mouse_over", event.widget.identify_row(event.y))
        
    def abrir_cerrar_actualizar(self, event=None):
        self.ejercicio_actual = None

        #Abre o cierra
        iid = (self.treeview.focus())
        item = self.treeview.item(self.treeview.focus())
        self.treeview.item(iid, open=not item["open"])

        #Vacía la imagen previa
        frame_base.frame_vista_previa.poner_imagen_previa()
        
        #Vacía la descripción
        frame_base.frame_descripcion.poner_descripcion()

        #Deshabilita todos los spinbox
        for spinbox in frame_spinbox.lista_todos_los_spinbox:
            spinbox.variable.trace_vdelete("w", spinbox.id_trace)#quita el trace
            spinbox["state"] = "disabled"
            spinbox.variable.set("")
            int(spinbox["to"])
            spinbox.config(to=0)
            spinbox.label_max["text"] = "max 0"
            spinbox.id_trace = spinbox.variable.trace("w", spinbox.tratar_numeros)#repone el trace

    def desplegar_spinboxs_poner_vista_previa(self, event=None):
        #Busca los items
        item_contenido = self.treeview.item(self.treeview.focus())
        item_unidad = self.treeview.item(self.treeview.parent(self.treeview.focus()))
        item_eje_tematico = self.treeview.item(self.treeview.parent(self.treeview.parent(self.treeview.focus())))

        #Recolecta la informacion de los items
        contenido = item_contenido["text"]
        unidad = item_unidad["text"]
        eje_tematico = item_eje_tematico["text"]

        self.ejercicio_actual = ejercicios.buscar_ejercicio(eje_tematico, unidad, contenido)

        #Frame spinbox
        frame_spinbox = frame_base.frame_spinbox

        #Habilita los existentes y deshabilita los inexistentes. También establece la cantidad máxima
        for spinbox in frame_spinbox.lista_todos_los_spinbox:
            spinbox.variable.trace_vdelete("w", spinbox.id_trace)#quita el trace
            item, nivel = spinbox.item, spinbox.nivel
            if self.ejercicio_actual.existencias[item][nivel]:
                cantidad_guardada = int(self.ejercicio_actual.cantidades[item][nivel])
                spinbox["state"] = "normal"
                spinbox.config(to=self.ejercicio_actual.cantidades_disponibles[item][nivel])
                spinbox.variable.set( {cantidad_guardada:str(cantidad_guardada),0:""}[cantidad_guardada] )
                spinbox.label_max["text"] = f"max {self.ejercicio_actual.cantidades_disponibles[item][nivel]}"
            else:
                spinbox["state"] = "disabled"
                spinbox.variable.set("")
                spinbox.config(to=0)
                spinbox.label_max["text"] = "max 0"
            spinbox.id_trace = spinbox.variable.trace("w", spinbox.tratar_numeros)#repone el trace

        #Pone la descripción
        frame_base.frame_descripcion.poner_descripcion(self.ejercicio_actual)

        #Vacía la imagaen previa
        frame_base.frame_vista_previa.poner_imagen_previa()



class Frame_vista_previa(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        frame_base.frame_vista_previa = self
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
        self.poner_imagen_previa()
        self.boton_mas = tk.Button(self.frame_derecho, width=1, height=1, bg="black", text="+", font=("courier",16), command=lambda :self.zoom("+"), fg="white")
        self.boton_menos = tk.Button(self.frame_derecho, width=1, height=1, bg="black", text="-", font=("courier",16), command=lambda :self.zoom("-"), fg="white")

        self.canvas.propagate(False)
        self.canvas.configure(bg="white", width=self.imagen_tamaño_cambiado.size[0], xscrollcommand=self.scrollbar_x.set, yscrollcommand=self.scrollbar_y.set)

        self.bind("<MouseWheel>", self.mouse_wheel)
        self.scrollable_frame.bind("<Configure>", lambda _ : self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.bind("<MouseWheel>", self.mouse_wheel)
        self.label_imagen.bind("<MouseWheel>", self.mouse_wheel)

        self.scrollbar_x.pack(side="bottom", fill="x")
        self.scrollbar_y.pack(side="right", fill="y")
        self.frame_izquierdo.pack(side="left", fill="both", expand=True)
        self.frame_derecho.pack(side="right", fill="both", expand=True)
        self.canvas.pack(side="top", fill="y", expand=True)
        self.label_imagen.pack(fill="both")
        # self.boton_mas.grid(row=0, column=1, padx=0, pady=10, sticky="nswe")
        # self.boton_menos.grid(row=0, column=0, padx=10, pady=10, sticky="nswe")


    def poner_imagen_previa(self, ejercicio=None, item=None, level=None):
        #Deicide el path
        self.imagen_original = Image.open('Imagen previa inicial.jpg') if ejercicio==None else ejercicio.fotos[item][level]

        #Pone la nueva imagen previa
        self.imagen_tamaño_cambiado = self.imagen_original.resize((int(self.imagen_original.size[0]*self.factor),int(self.imagen_original.size[1]*self.factor)), Image.ANTIALIAS)
        self.imagen_nueva = ImageTk.PhotoImage(self.imagen_tamaño_cambiado)
        self.label_imagen["image"] = self.imagen_nueva
        if frame_base.winfo_ismapped()==1:#Evita que actualize si la ventana principal no aparece porque en caso contrario hay un delay raro en la carga de las pestañas
            self.label_imagen.update()
        self.canvas.yview_moveto("0")


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

class Frame_descripcion(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        frame_base.frame_descripcion = self
        kwargs["name"] = "frame descripción"
        super().__init__(master, *args, **kwargs)

        self.canvas = tk.Canvas(self, bg="orange", highlightthickness=0, name="canvas")
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="white", name="scrollable_frame")
        self.ventana = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.label_titulo = tk.Label(self.canvas, text="Descripción", bg="light grey")
        self.label_descripcion = tk.Label(self.scrollable_frame, justify="left", bg=self.canvas["bg"], fg="white")

        self.canvas.propagate(False)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.bind("<Configure>", lambda _ : threading.Thread(target=self.ajustar_label,daemon=True).start())
        self.canvas.bind("<MouseWheel>", self.mouse_wheel)
        self.scrollable_frame.bind("<Configure>", lambda _: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.label_descripcion.bind("<MouseWheel>", self.mouse_wheel)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        self.label_titulo.pack(fill="x", side="top")
        self.label_descripcion.pack(fill="both", expand=True, side="left")

    def poner_descripcion(self, ejercicio=None):
        self.label_descripcion["text"] = "" if ejercicio==None else ejercicio.descripcion
        self.canvas.yview_moveto("0")

    def mouse_wheel(self, event):
        if not self.scrollable_frame.winfo_height() <= self.canvas.winfo_height():
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def ajustar_label(self):
        self.label_descripcion["wraplength"] = self.canvas.winfo_width()*0.99


class Spinbox_ejercicio(tk.Spinbox):
    def __init__(self, master, item, nivel, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.config(
            width = 8,
            justify = "center",
            state = "disabled",
            background="white",
            disabledbackground="black",
            foreground="black",
            command=(frame_base.register(self.up_or_down), '%d'),
            from_=0,
            to=0
        )
        #Genera la variable
        self.variable = tk.StringVar(value="")
        self["textvariable"] = self.variable
        #Guarda los datos del ejercicio
        self.eje_tematico = None
        self.unidad = None
        self.contenido = None
        #Datos del spinbox
        self.item = item
        self.nivel = str(nivel)
        #Trace y Bind
        self.id_trace = self.variable.trace("w", self.tratar_numeros)
        self.bind("<FocusIn>", self.actualizar_vista_previa_y_descripcion)
        self.bind("<Key>", self.prevenir_letras)
        #Label que indica el máximo
        self.label_max = tk.Label(master, text="max 0", bg=master["bg"], justify="center")

    def up_or_down(self, direction):
        if direction=="up" and self.variable.get()=="":
            self.variable.set("1")
        self.actualizar_carrito()

    def prevenir_letras(self, event=None):
        if not event.char.isnumeric() and event.keysym not in ["BackSpace","Delete", "Up", "Down", "Right", "Left"]:
            return "break"

    def tratar_numeros(self, tipo="PY_VAR", vacio="", modo="w"):
        if self["state"]=="disabled":
            return None
        self.variable.set(str(min(int(f"0{self.variable.get()}"),int(self["to"]))))
        if self.variable.get()=="0":
            self.variable.set("")
        if frame_base.frame_treeview.ejercicio_actual==None:
            return None

        #Actualiza el carrito
        self.actualizar_carrito()

    def actualizar_vista_previa_y_descripcion(self, event):
        #Busca los datos del ejercicio
        ejercicio_actual = frame_base.frame_treeview.ejercicio_actual

        #Pone la nueva imagen previa
        frame_base.frame_vista_previa.poner_imagen_previa(ejercicio_actual, event.widget.item, event.widget.nivel)

        #Pone la desripción
        frame_base.frame_descripcion.poner_descripcion(ejercicio_actual)

    def actualizar_carrito(self):
        #Guarda la cantidad de ejercicios solicitados
        frame_base.frame_treeview.ejercicio_actual.cantidades[self.item][self.nivel] = int(self.get_especial())

        #Busca los datos del ejercicio y el frame de carrito
        ejercicio_actual = frame_base.frame_treeview.ejercicio_actual
        eje_tematico = ejercicio_actual.eje_tematico

        #Recolecta los datos
        unidad = ejercicio_actual.unidad
        contenido = ejercicio_actual.contenido
        item = self.item
        nivel = self.nivel
        cantidad = int(self.get_especial())
        largo_de_columnas = 50

        #Establece el treeview, iid y la cantidad de letras por columna
        frame_carrito = frame_base.frame_carrito
        treeview = frame_carrito.Treeview
        iid = f"{eje_tematico}/{unidad}/{contenido}/{item}/{nivel}".replace(" ","")
        largo_de_columnas = 50

        #Borra
        if treeview.exists(iid) and cantidad==0:
            treeview.delete(iid)

        #Actualiza
        elif treeview.exists(iid) and cantidad!=0:
            treeview.item(iid, values=(
                "\n".join(textwrap.wrap(eje_tematico, largo_de_columnas)),
                "\n".join(textwrap.wrap(unidad, largo_de_columnas)),
                "\n".join(textwrap.wrap(contenido, largo_de_columnas)),
                "\n".join(textwrap.wrap(item, largo_de_columnas)),
                nivel,
                cantidad,
                ))

        #Ingresa nuevo
        elif not treeview.exists(iid) and cantidad!=0:
            treeview.insert("", index="end", iid=iid, values=(
                "\n".join(textwrap.wrap(eje_tematico, largo_de_columnas)),
                "\n".join(textwrap.wrap(unidad, largo_de_columnas)),
                "\n".join(textwrap.wrap(contenido, largo_de_columnas)),
                "\n".join(textwrap.wrap(item, largo_de_columnas)),
                nivel,
                cantidad,
                ))
            treeview.tag_bind(iid, "<Motion>", frame_carrito.mouse_over)

    def get_especial(self):
        contenido_actual = self.variable.get()
        return {contenido_actual:contenido_actual, "":"0"}[contenido_actual]

    def __eq__(self, other):
        return self.eje_tematico==other.eje_tematico and self.unidad==other.unidad and self.contenido==other.contenido and self.item==other.item

class Frame_item(tk.Frame):
    def __init__(self, master, item, *args, **kwargs):
        kwargs["bg"] = master["bg"]
        super().__init__(master, *args, **kwargs)
        #Configura las columnas
        self.item = item
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        #Label de los items
        self.label_titulo = tk.Label(self, text=self.item, bg=master["bg"])

        self.font = font.Font(self.label_titulo, self.label_titulo.cget("font"))
        self.font.configure(underline=True)
        self.label_titulo.configure(font=self.font)

        #Labels niveles
        self.label_1 = tk.Label(self, text="Nivel 1", bg=master["bg"])
        self.label_2 = tk.Label(self, text="Nivel 2", bg=master["bg"])
        self.label_3 = tk.Label(self, text="Nivel 3", bg=master["bg"])

        #Spinboxs
        self.spinbox_1 = Spinbox_ejercicio(self, item=self.item, nivel="1")
        self.spinbox_2 = Spinbox_ejercicio(self, item=self.item, nivel="2")
        self.spinbox_3 = Spinbox_ejercicio(self, item=self.item, nivel="3")

        #POSICIONAMIENTO
        #Labels
        self.label_titulo.grid(row=0, column=0, columnspan=3)
        self.label_1.grid(row=1, column=0)
        self.label_2.grid(row=1, column=1)
        self.label_3.grid(row=1, column=2)

        #Spinboxs
        self.spinbox_1.grid(row=2, column=0)
        self.spinbox_2.grid(row=2, column=1)
        self.spinbox_3.grid(row=2, column=2)

        #Labels máximos
        self.spinbox_1.label_max.grid(row=3, column=0)
        self.spinbox_2.label_max.grid(row=3, column=1)
        self.spinbox_3.label_max.grid(row=3, column=2)

class Frame_spinbox(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        frame_base.frame_spinbox = self
        kwargs["bg"] = "light yellow"
        super().__init__(master, *args, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        #Crea los frames de los items
        self.frame_seleccion_multiple = Frame_item(self, item="Selección múltiple")
        self.frame_desarrollo = Frame_item(self, item="Desarrollo")
        self.frame_verdadero_y_falso = Frame_item(self, item="Verdadero y falso")

        #Pone los frames items
        self.frame_seleccion_multiple.grid(row=0, column=0, sticky="we")
        self.frame_desarrollo.grid(row=1, column=0, sticky="we")
        self.frame_verdadero_y_falso.grid(row=2, column=0, sticky="we")

        self.lista_todos_los_spinbox = [
            self.frame_seleccion_multiple.spinbox_1, self.frame_seleccion_multiple.spinbox_2, self.frame_seleccion_multiple.spinbox_3,
            self.frame_desarrollo.spinbox_1, self.frame_desarrollo.spinbox_2, self.frame_desarrollo.spinbox_3,
            self.frame_verdadero_y_falso.spinbox_1, self.frame_verdadero_y_falso.spinbox_2, self.frame_verdadero_y_falso.spinbox_3,
        ]


class Frame_carrito(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        frame_base.frame_carrito = self
        kwargs["name"] = "carrito"
        super().__init__(master, *args, **kwargs)
        self.grid_rowconfigure(0, minsize=100)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        #Todo del Treeview
        style = ttk.Style()
        style.configure("Treeview",
                background="white",
                foreground="black",
                rowheight=45,
                fieldbackground="white")
        style.map("Treeview", background=[("selected", "lightblue")])

        self.Treeview = ttk.Treeview(self, style="Treeview", columns=["#1", "#2", "#3", "#4", "#5", "#6"], show=["headings"])
        self.Treeview.tag_configure("mouse_over", background="#dfebf7")
        self.Treeview.bind("<Motion>", self.mouse_over)
        
        # self.Treeview.tag_configure("white", background="white")
        # self.Treeview.tag_configure("grey", background="grey")
        # self.Treeview.tag_configure("#adf4ff", background="#adf4ff")

        width_screen = frame_base.winfo_screenwidth()/100

        self.Treeview.column("#1", anchor="center", width=int(width_screen*19))
        self.Treeview.column("#2", anchor="center", width=int(width_screen*19))
        self.Treeview.column("#3", anchor="center", width=int(width_screen*24))
        self.Treeview.column("#4", anchor="center", width=int(width_screen*19))
        self.Treeview.column("#5", anchor="center", width=int(width_screen*5))
        self.Treeview.column("#6", anchor="center", width=int(width_screen*14))

        self.Treeview.heading("#1", text="Eje temático", anchor="center")
        self.Treeview.heading("#2", text="Unidad", anchor="center")
        self.Treeview.heading("#3", text="Contenido", anchor="center")
        self.Treeview.heading("#4", text="Item", anchor="center")
        self.Treeview.heading("#5", text="Nivel", anchor="center")
        self.Treeview.heading("#6", text="Cantidad solicitada", anchor="center")

        self.Treeview.grid(row=1, column=0, sticky="nswe", columnspan=2, rowspan=2)

        #Scrollbar
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.Treeview.yview)
        self.Treeview.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=1, column=2, sticky="ns")

    def borrar_fila_con_focus(self):
        #Trabaja con todas las filas que están seleccionadas
        for iid in self.Treeview.selection():
            #Obtiene la información de la fila que tiene el focus al liberar el click
            values = self.Treeview.item(iid)["values"]
            eje_tematico = values[0]
            unidad = values[1].replace("\n"," ")
            contenido = values[2].replace("\n"," ")
            item = values[3].replace("\n"," ")
            nivel = str(values[4])
            cantidad = values[5]

            #Establece la cantidad 0
            for ejercicio in ejercicios.lista:
                if ejercicio.eje_tematico==eje_tematico and ejercicio.unidad==unidad and ejercicio.contenido==contenido:
                    ejercicio.cantidades[item][nivel] = 0
                    break
            
            #Borra la fila
            self.Treeview.delete(iid)

    def mouse_over(self, event):
        self.Treeview.tk.call(self.Treeview, "tag", "remove", "mouse_over")
        self.Treeview.tk.call(self.Treeview, "tag", "add", "mouse_over", self.Treeview.identify_row(event.y))

    def limpiar(self):
        #Limpia el carrito
        self.Treeview.delete(*self.Treeview.get_children())
        #Pone ceros en los ejercicios
        for ejercicio in ejercicios.lista:
            for item in ejercicio.cantidades:
                for nivel in ejercicio.cantidades[item]:
                    ejercicio.cantidades[item][nivel] = 0
        
        for spinbox in frame_base.frame_spinbox.lista_todos_los_spinbox:
            if spinbox["state"] == "normal":
                spinbox.variable.set(0)


espacio_horizontal = 20
espacio_vertical = 2
class Entry_datos:
    def __init__(self, master, label, valor_inicial="", largo=40):
        #Genera lo necesario
        self.label = tk.Label(master, text=label, bg="#FFEEDD")
        self.variable = tk.StringVar(value=valor_inicial)
        self.entry = tk.Entry(master, textvariable=self.variable, width=largo)
        self.fila = master.grid_size()[1]-1

        #Posiciona todo
        self.label.grid(sticky="nw", row=master.grid_size()[1], column=0, padx=espacio_horizontal, pady=espacio_vertical)
        self.entry.grid(sticky="W", row=master.grid_size()[1]-1, column=1, pady=espacio_vertical)

    def get(self):
        return self.variable.get()

class Entry_numeros_datos:
    def __init__(self, master, label, valor_inicial="", largo=40):
        #Genera lo necesario
        self.label = tk.Label(master, text=label, bg="#FFEEDD")
        self.variable = tk.StringVar(value=valor_inicial)
        self.entry = tk.Entry(master, textvariable=self.variable, width=largo)
        self.fila = master.grid_size()[1]-1

        #Posiciona todo
        self.label.grid(sticky="nw", row=master.grid_size()[1], column=0, padx=espacio_horizontal, pady=espacio_vertical)
        self.entry.grid(sticky="W", row=master.grid_size()[1]-1, column=1, pady=espacio_vertical)
        
        #Trace y Bind
        self.variable.trace("w", self.poner_coma)
        self.entry.bind("<Key>", self.prevenir_letras)
        self.entry.bind("<FocusOut>", self.poner_ceros)

    def prevenir_letras(self, event):
        if not event.char.isnumeric() and event.keysym not in ["BackSpace","Delete"]:
            return "break"

    def poner_coma(self, *args, **kwargs):
        contenido = self.variable.get()
        if "," not in contenido:
            self.variable.set(contenido+",")

    def get(self):
        return self.variable.get().replace(",",".")

    def poner_ceros(self, event):
        contenido = self.variable.get()
        if contenido[0] == ",":
            contenido = "0" + contenido
        if contenido[-1] == ",":
            contenido = contenido + "0"
        self.variable.set(contenido)

class Text_datos:
    def __init__(self, master, label, ancho=30, alto=10, valor_inicial=""):
        #Genera lo necesario
        self.label = tk.Label(master, text=label, bg="#FFEEDD")
        self.text = tk.Text(master)
        self.fila = master.grid_size()[1]-1

        #Configura
        self.text.config(width=ancho, height=alto)
        self.text.insert("end", valor_inicial)

        #Posiciona todo
        self.label.grid(sticky="nw", row=master.grid_size()[1], column=0, padx=espacio_horizontal, pady=espacio_vertical)
        self.text.grid(sticky="W", row=master.grid_size()[1]-1, column=1, pady=espacio_vertical)
        
    def get(self):
        return self.text.get("0.0","end")

class Checkbutton_datos:
    def __init__(self, master, label, valor_inicial):
        #Genera lo necesario
        self.label = tk.Label(master, text=label, bg="#FFEEDD")
        self.variable = tk.BooleanVar(value=valor_inicial)
        self.ticket = tk.Checkbutton(master, variable=self.variable, onvalue=True, offvalue=False)
        self.fila = master.grid_size()[1]-1

        #Posiciona todo
        self.label.grid(sticky="nw", row=master.grid_size()[1], column=0, padx=espacio_horizontal, pady=espacio_vertical)
        self.ticket.grid(sticky="W", row=master.grid_size()[1]-1, column=1, pady=espacio_vertical)

    def get(self):
        return self.variable.get()

class Combobox_datos:
    def __init__(self, master, label, valor_inicial, lista_de_valores, largo_de_la_caja):
        #Genera lo necesario
        self.label = tk.Label(master, text=label, bg="#FFEEDD")
        self.variable = tk.StringVar()
        self.lista = ttk.Combobox(master, textvariable=self.variable, state="readonly")
        self.fila = master.grid_size()[1]-1

        #Configura        
        self.lista["values"] = lista_de_valores
        self.lista.set(valor_inicial)
        self.lista.config(width=largo_de_la_caja)

        #Posiciona todo
        self.label.grid(sticky="nw", row=master.grid_size()[1], column=0, padx=espacio_horizontal, pady=espacio_vertical)
        self.lista.grid(sticky="W", row=master.grid_size()[1]-1, column=1, pady=espacio_vertical)

    def get(self):
        return self.variable.get()

class Text_ajustable_datos:
    def __init__(self, master, label, valor_inicial=""):
        #Genera lo necesario
        self.label = tk.Label(master, text=label, bg="#FFEEDD")
        self.text = Text_ajustable(master, wrap="char")
        self.fila = master.grid_size()[1]-1

        #Configura 
        self.text.config(width=100, relief="groove", borderwidth=1)
        self.text.insert("end", valor_inicial+"\n")

        #Posiciona todo
        self.label.grid(sticky="nw", row=master.grid_size()[1], column=0, padx=espacio_horizontal, pady=espacio_vertical)
        self.text.grid(sticky="W", row=master.grid_size()[1]-1, column=1, pady=espacio_vertical)
        
    def get(self):
        return self.text.get("0.0","end")

class Imagen_datos:
    def __init__(self, master, label, ruta="", valor_inicial="", largo=40):
        if not os.path.exists(ruta):
            ruta = ""
        #Genera lo necesario
        self.label = tk.Label(master, text=label, bg="#FFEEDD")
        self.frame_grande = tk.Frame(master)
        self.label_imagen = tk.Label(self.frame_grande)
        self.ruta = ruta
        self.frame_botones = tk.Frame(self.frame_grande)
        self.fila = master.grid_size()[1]-1
        self.label_ruta = tk.Label(self.frame_grande, bg="#FFEEDD")
        self.boton = tk.Button(self.frame_grande, width=13, height=1, bg="#00CD63")
        if ruta=="":
            self.label_ruta.config(text="No se ha insertado una imagen")
            self.boton.config(text="Insertar imagen", command=self.buscar_imagen)
        else:
            self.label_ruta.config(text=ruta)
            self.boton.config(text="Quitar imagen", command=self.quitar_imagen)
            #Cargar imagen
            self.mostrar_imagen()

        #Crea los botones de align, con el centro elegido
        self.boton_izquierda = tk.Button(self.frame_botones, text="Izquierda", width=10, height=1, command=lambda:self.alinear("l"))
        self.boton_centro = tk.Button(self.frame_botones, text="Centro", width=10, height=1, command=lambda:self.alinear("c"), relief="sunken", state="disabled")
        self.boton_derecha = tk.Button(self.frame_botones, text="Derecha", width=10, height=1, command=lambda:self.alinear("r"))
        self.posicion = "c"

        #Configuraciones
        self.frame_botones.grid_columnconfigure(0, minsize=200)
        self.frame_grande.grid_rowconfigure(4, minsize=40)#Agrega el espacio en blanco debajo de la imagen

        #Posiciona
        self.label.grid(sticky="nw", row=master.grid_size()[1], column=0, padx=espacio_horizontal, pady=espacio_vertical)
        self.frame_grande.grid(sticky="W", row=master.grid_size()[1]-1, column=1, pady=espacio_vertical)
        self.boton.grid(row=0, column=0, sticky="w")
        self.frame_botones.grid(row=0, column=0, sticky="w")
        self.label_ruta.grid(row=1, column=0, sticky="w")
        if ruta != "":
            self.boton_izquierda.grid(row=0, column=1, padx=5, sticky="w")
            self.boton_centro.grid(row=0, column=2, padx=5, sticky="w")
            self.boton_derecha.grid(row=0, column=3, padx=5, sticky="w")

    def buscar_imagen(self):
        ruta_escritorio = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop") # determina la ruta del escritorio
        self.ruta = askopenfilename(title="Insertar imagen", initialdir=ruta_escritorio, initialfile="", filetypes=(("Formato jpg","*.jpg"),("Formato png","*.png"))) #abre el explorador
        if self.ruta != "":
            self.label_ruta.config(text=self.ruta)
            self.boton.config(text="Quitar imagen", command=self.quitar_imagen)

            #Pone y activa o desactiva los botones
            self.boton_izquierda.config(relief="raised", state="active")
            self.boton_centro.config(relief="sunken", state="disabled")
            self.boton_derecha.config(relief="raised", state="active")
            self.boton_izquierda.grid(row=0, column=1, padx=5)
            self.boton_centro.grid(row=0, column=2, padx=5)
            self.boton_derecha.grid(row=0, column=3, padx=5)
            self.posicion = "c"

            #Cargar imagen
            self.mostrar_imagen()

            #Pone el espacio extra debajo de la imagen mostrada
            self.frame_grande.grid_rowconfigure(4, minsize=40)

    def quitar_imagen(self):
        self.ruta = ""
        self.posicion = "c"
        self.label_ruta.config(text="No se ha insertado una imagen")
        self.boton.config(text="Insertar imagen", command=self.buscar_imagen)

        #Quita los botones de posicion
        self.boton_izquierda.grid_forget()
        self.boton_centro.grid_forget()
        self.boton_derecha.grid_forget()

        #Quita el label imagen
        self.label_imagen.config(image="")
        self.label_imagen.grid_forget()

    def alinear(self, posicion):
        self.posicion = posicion
        #Activa todos los botones
        for boton in [self.boton_izquierda, self.boton_centro, self.boton_derecha]:
            boton.config(relief="raised", state="active")

        #Desactiva el botón que fue apretado
        if posicion == "l":
            self.boton_izquierda.config(relief="sunken", state="disabled")
        elif posicion == "c":
            self.boton_centro.config(relief="sunken", state="disabled")
        elif posicion == "r":
            self.boton_derecha.config(relief="sunken", state="disabled")

    def mostrar_imagen(self):
        imagen_original = Image.open(self.ruta)
        imagen_nueva = ImageTk.PhotoImage(imagen_original)
        self.label_imagen.config(image=imagen_nueva)
        self.label_imagen.image = imagen_nueva
        self.label_imagen.grid(row=2, column=0, sticky="w")

    def get(self):
        return self.ruta





class Boton_align(tk.Button):
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
        #Ajusta el tamaño
        self["height"] = self.get("1.0","end").count("\n")
        altura_de_fila = 1
        
        for box in self.master.winfo_children():
            if isinstance(box, Text_ajustable):
                altura_de_fila = max([altura_de_fila, box["height"]])
        self.master["height"] = altura_de_fila *16 + 8

        #Posiciona el texto
        self.tag_configure("tag-posicion_del_texto", justify=self.posicion_del_texto)
        self.tag_add("tag-posicion_del_texto", "1.0", "end")

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

        self.boton_left = Boton_align(self.frame_botones_posicion_texto, posicion_del_texto="left")
        self.boton_center = Boton_align(self.frame_botones_posicion_texto, posicion_del_texto="center")



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


# Función usada en desarrollo
# def establecer_cantidad_general(boton_establecer):
#     #Desabilita el boton
#     boton_establecer["state"] = "disabled"
#     boton_establecer["text"] = "Estableciendo..."

#     cantidad_general = int(cantidad_a_establecer_para_todos.get())

#     #Establece el treeview, iid y la cantidad de letras por columna
#     frame_carrito = frame_base.frame_carrito
#     treeview = frame_carrito.Treeview
#     treeview.delete(*treeview.get_children())#Limpia el carrito
#     largo_de_columnas = 50


#     #Pone las cantidades
#     for ejercicio in ejercicios.lista:
#         eje_tematico = ejercicio.eje_tematico
#         unidad = ejercicio.unidad
#         contenido = ejercicio.contenido
#         for item in ejercicio.cantidades:
#             for nivel in "123":
#                 if ejercicio.existencias[item][nivel]:
#                     cantidad = min(cantidad_general, ejercicio.cantidades_disponibles[item][nivel])
#                     ejercicio.cantidades[item][nivel] = cantidad
#                     iid = f"{eje_tematico}/{unidad}/{contenido}/{item}/{nivel}".replace(" ","")

#                     #Pone en el carrito
#                     treeview.insert("", index="end", iid=iid, values=(
#                         "\n".join(textwrap.wrap(eje_tematico, largo_de_columnas)),
#                         "\n".join(textwrap.wrap(unidad, largo_de_columnas)),
#                         "\n".join(textwrap.wrap(contenido, largo_de_columnas)),
#                         "\n".join(textwrap.wrap(item, largo_de_columnas)),
#                         nivel,
#                         cantidad,
#                         ))

#     #Vuelve a habilitar el boton
#     boton_establecer.config(text="Establecer cantidad global", state="normal")

def agregar_preambulo_y_tabla_con_datos():
    #Pone en el preámbulo las dimensiones del papel y el margen
    paquete = fr"\usepackage[papersize={{{ancho_papel.get().replace(',','.')}cm, {alto_papel.get().replace(',','.')}cm}},tmargin={margen_superior.get()}cm,bmargin={margen_inferior.get()}cm,lmargin={margen_izquierdo.get()}cm,rmargin={margen_derecho.get()}cm]{{geometry}}"
    for doc in [frame_base.Doc, frame_base.Doc_respuestas, frame_base.Doc_procedimientos]:
        doc.preamble.append(pylatex.NoEscape(paquete))

    #Logo y Tabla con la información de la prueba y el alumno
    poner_primera_linea = True
    frame_base.Doc.append(pylatex.NoEscape(r"\begin{center} \begin{tabular}{c}"+"\n"))
    for fila in frame_base.frame_tabla.winfo_children():
        frame_base.Doc.append(pylatex.NoEscape(r"\begin{tabularx}{0.976\linewidth}{|"))

        #Calcula y establece porcentajes
        width_total = 0
        for box in fila.PanedWindow.winfo_children():
            width_total += box.winfo_width()
        for box in fila.PanedWindow.winfo_children():
            division = box.winfo_width()/width_total
            diccionario_de_posiciones = {"left": "", "center":r"\Centering ", "right":r"\raggedleft "}
            frame_base.Doc.append(pylatex.NoEscape(fr">{{{diccionario_de_posiciones[box.posicion_del_texto]}\hsize={division}\hsize}}X|"))
        frame_base.Doc.append(pylatex.NoEscape("}"))

        #Pone primera linea
        if poner_primera_linea:
            frame_base.Doc.append(pylatex.NoEscape(r"\hline"))
            poner_primera_linea = False

        #Pone unidades
        poner_separador_de_columnas = False
        for box in fila.PanedWindow.winfo_children():
            if poner_separador_de_columnas:
                frame_base.Doc.append(pylatex.NoEscape(r" & "))
            poner_separador_de_columnas = True
            #Arregla elementos especiales como °
            contenido = box.get("1.0", "end-1c")
            subContenidos = contenido.split("°")
            frame_base.Doc.append(subContenidos[0])
            for subContenido in subContenidos[1:]:
                frame_base.Doc.append(pylatex.NoEscape(r"$\degree$"))
                frame_base.Doc.append(subContenido)
                        
        #Cierra la tabla de la fila
        frame_base.Doc.append(pylatex.NoEscape(r" \\ \hline \end{tabularx} \\"))

    #Cierra la tabla más grande
    frame_base.Doc.append(pylatex.NoEscape(r"\end{tabular} \end{center}" + "\n"))



    
    #Agrega las instrucciones
    instrucciones = instrucciones_generales.get()
    while True:
        if len(instrucciones):
            if instrucciones[-1] in ["\n"," "]:
                instrucciones = instrucciones[:-1]
            else:
                break
        else:
            break
    if instrucciones != "":
        frame_base.Doc.append(pylatex.NoEscape(r"\textbf{Instrucciones generales:} "))
        frame_base.Doc.append(instrucciones)
        frame_base.Doc.append(pylatex.NoEscape(r"\hfill \break"*2))


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




def agregar_ejercicios_seleccion_multiple():
    print("Se inició el agregado de la selección múltiple")
    item = "Selección múltiple"
    respuestas = []
    numero_del_ejercicio = 1
    frame_base.Doc.append(pylatex.NoEscape(r"\textbf{Item selección múltiple:} "))
    instrucciones = instrucciones_seleccion_multiple.get()
    while True:
        if len(instrucciones):
            if instrucciones[-1] in ["\n"," "]:
                instrucciones = instrucciones[:-1]
            else:
                break
        else:
            break
    frame_base.Doc.append(instrucciones)
    frame_base.Doc.append(pylatex.NoEscape(r"\begin{longtable}{|p{0.475\linewidth}|p{0.475\linewidth}|} \hline"))

    #====================================Zona de importación====================================
    #Decide el ejercicio a usar
    for ejercicio in ejercicios.lista:
        for nivel in '123':
            if not ejercicio.existencias[item][nivel]:
                continue
            #Inicia el cambio de opcion a utilizar
            cantidad_opciones = ejercicio.opciones[item][nivel]
            lista_de_opciones_no_usadas = list(range(1,cantidad_opciones+1))

            for _ in range(0, ejercicio.cantidades[item][nivel]):
                print(f"Se está intentando importar {ejercicio.rutas[item][nivel]}")

                if nivel in "12":
                    while True:#Importa hasta que las alternativas sean distintas o el enunciado no haya sido usado
                        #Hace que las opciones se repitan solo al haber usado todas
                        if len(lista_de_opciones_no_usadas) == 0:
                            lista_de_opciones_no_usadas = list(range(1,cantidad_opciones+1))
                        opcion_a_usar = choice(lista_de_opciones_no_usadas)
                        lista_de_opciones_no_usadas.remove(opcion_a_usar)

                        #Importa
                        instrucciones = f"opcion={opcion_a_usar}\n"     + ejercicio.instrucciones[item][nivel] +   "\nejercicio.seleccion_multiple_enunciado, ejercicio.seleccion_multiple_contenido_correcto, ejercicio.seleccion_multiple_contenido_2, ejercicio.seleccion_multiple_contenido_3, ejercicio.seleccion_multiple_contenido_4, ejercicio.seleccion_multiple_contenido_5, ejercicio.enunciado_oculto_actual = enunciado, contenido_correcto, contenido_2, contenido_3, contenido_4, contenido_5, enunciado_oculto"
                        exec(instrucciones)

                        #Detecta si el enunciado oculto ya había sido usado
                        if ejercicio.enunciado_oculto_actual in ejercicio.enunciados_ocultos[item][nivel]:
                            print(f"En {ejercicio.eje_tematico} {ejercicio.unidad} {ejercicio.contenido} de tipo selección múltiple se repitió el enunciado. Opción {opcion_a_usar}")
                            print(ejercicio.seleccion_multiple_enunciado)
                            continue

                        #Detecta si hay alternativas repetidas
                        lista_de_contenidos = [ejercicio.seleccion_multiple_contenido_correcto, ejercicio.seleccion_multiple_contenido_2, ejercicio.seleccion_multiple_contenido_3, ejercicio.seleccion_multiple_contenido_4, ejercicio.seleccion_multiple_contenido_5]
                        lista_de_contenidos_reverso = lista_de_contenidos[::-1]
                        for contenido in lista_de_contenidos:
                            if lista_de_contenidos.count(contenido) != 1:
                                posicion_contenido_1 = 1 + lista_de_contenidos.index(ejercicio.seleccion_multiple_contenido_correcto)
                                posicion_contenido_2 = 5 - lista_de_contenidos_reverso.index(ejercicio.seleccion_multiple_contenido_correcto)
                                print(f"Alternativas {posicion_contenido_1} y {posicion_contenido_2} repetidas. Opción {opcion_a_usar}. Ejercicio {ejercicio.rutas[item][nivel]}")
                                # print(contenido)
                                break
                        else:
                            break

                    ejercicio.enunciados_ocultos[item][nivel].append(ejercicio.enunciado_oculto_actual)
                    #Pone el enunciado
                    frame_base.Doc.append(pylatex.NoEscape(r"\begin{enumerate}[label=\arabic*),start=" f"{numero_del_ejercicio}" "]"))
                    frame_base.Doc.append(pylatex.NoEscape(r"\item"))
                    frame_base.Doc.append(pylatex.NoEscape(ejercicio.seleccion_multiple_enunciado.replace("¿","?`")))
                    frame_base.Doc.append(pylatex.NoEscape(r"\end{enumerate}"))

                    #No tocar esto. Genera la lista con los contenidos
                    lista_contenidos = [ejercicio.seleccion_multiple_contenido_2, ejercicio.seleccion_multiple_contenido_3, ejercicio.seleccion_multiple_contenido_4, ejercicio.seleccion_multiple_contenido_5][0:int(cantidad_de_alternativas_por_pregunta.get())-1]
                    lista_contenidos.append(ejercicio.seleccion_multiple_contenido_correcto)

                    #Empiezan el entorno de las alternativas
                    frame_base.Doc.append(pylatex.NoEscape(r"\begin{enumerate}[label=\Alph*)]"))
                    numero_de_la_alternativa = 1
                    shuffle(lista_contenidos)
                    for contenido in lista_contenidos:
                        #Elije y establece los contenidos de las alternativas
                        frame_base.Doc.append(pylatex.NoEscape(r"\item"))
                        frame_base.Doc.append(pylatex.NoEscape(contenido))

                        #Guarda la alternativa correcta
                        if contenido == ejercicio.seleccion_multiple_contenido_correcto:
                            alternativa_correcta = {1:"A", 2:"B", 3:"C", 4:"D", 5:"E"}[numero_de_la_alternativa]

                        numero_de_la_alternativa += 1
                    frame_base.Doc.append(pylatex.NoEscape(r"\end{enumerate}"))
                    
                    #Agrega la respuesta a la lista de respuestas correctas
                    respuestas.append(f"{numero_del_ejercicio}) {alternativa_correcta}")



                    #Crea fotos de los ejercicios por separado
                    if separar_ejercicios_de_seleccion_multiple.get():
                        if not os.path.exists("temp\\Fotos"):
                            os.mkdir("temp\\Fotos")
                        foto = pylatex.Document(page_numbers=None, documentclass="standalone", document_options=pylatex.NoEscape(r"varwidth=true, border=0pt, convert={size=640x}"))
                        for paquete in [r"\usepackage{ragged2e}", r"\usepackage{setspace}", r"\usepackage{longtable}", r"\usepackage{tabularx}", r"\usepackage{gensymb}", r"\usepackage{amsmath}", r"\usepackage{amssymb}", r"\usepackage{enumitem}", r"\usepackage{graphicx}", r"\usepackage{tikz}", r"\usepackage{tkz-euclide}", r"\usepackage{siunitx}", r"\usepackage{fourier}", r"\usetikzlibrary{fit, shapes.geometric, quotes, angles, through, intersections}", r"\usepackage{fancyhdr}"]:
                            foto.preamble.append(pylatex.NoEscape(paquete))
                        #Pone el enunciado
                        foto.append(pylatex.NoEscape(r"\begin{longtable}{p{8.3 cm}}"))
                        foto.append(pylatex.NoEscape(ejercicio.seleccion_multiple_enunciado.replace("¿","?`")))

                        #Pone las alternativas
                        foto.append(pylatex.NoEscape(r"\begin{enumerate}[label=\Alph*)]"))
                        for contenido in lista_contenidos:
                            #Elije y establece los contenidos de las alternativas
                            foto.append(pylatex.NoEscape(r"\item"))
                            foto.append(pylatex.NoEscape(contenido))

                        foto.append(pylatex.NoEscape(r"\end{enumerate}"))
                        foto.append(pylatex.NoEscape(r"\end{longtable}"))

                        #Genera el .tex
                        foto.generate_tex(f"temp\\Fotos\\{numero_del_ejercicio}")
                        #Genera el pdf
                        current_path = os.path.abspath(__file__)
                        folder_container = os.path.dirname(current_path) + r"\temp\Fotos"
                        subprocess.run(f'lualatex -interaction=nonstopmode -output-directory="{folder_container}" "{folder_container}\\{numero_del_ejercicio}.tex"', shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
                        #Quita los restos
                        for formato in ["aux", "log", "tex"]:
                            os.remove(f"temp\\Fotos\\{numero_del_ejercicio}.{formato}")
                        #Crea la foto
                        pdf2image.convert_from_path(f"temp\\Fotos\\{numero_del_ejercicio}.pdf")[0].save(f"temp\\Fotos\\{numero_del_ejercicio}.jpg", 'JPEG')
                        #Quita el pdf
                        os.remove(f"temp\\Fotos\\{numero_del_ejercicio}.pdf")




                elif nivel == "3":
                    #Inicia el cambio de opcion a utilizar
                    cantidad_opciones = ejercicio.opciones[item][nivel]
                    lista_de_opciones_no_usadas = []

                    while True:#Importa hasta que el enunciado no haya sido usado
                        #Hace que las opciones se repitan solo al haber usado todas
                        if len(lista_de_opciones_no_usadas) == 0:
                            lista_de_opciones_no_usadas = list(range(1,cantidad_opciones+1))
                        opcion_a_usar = choice(lista_de_opciones_no_usadas)
                        lista_de_opciones_no_usadas.remove(opcion_a_usar)

                        #Importa
                        instrucciones = f"opcion={opcion_a_usar}\n"     + ejercicio.instrucciones[item][nivel] +    "\nejercicio.seleccion_multiple_enunciado, ejercicio.informacion_1, ejercicio.informacion_2, ejercicio.enunciado_oculto_actual, ejercicio.alternativa_correcta = enunciado, informacion_1, informacion_2, opcion, alternativa_correcta"
                        exec(instrucciones)
                        
                        if ejercicio.enunciado_oculto_actual in ejercicio.enunciados_ocultos[item][nivel]:
                            print(f"En {ejercicio.eje_tematico} {ejercicio.unidad} {ejercicio.contenido} de tipo selección múltiple se repitió el enunciado. Opción {opcion_a_usar}")
                            print(ejercicio.seleccion_multiple_enunciado)
                            print(ejercicio.informacion_1)
                            print(ejercicio.informacion_2)
                        else:
                            break

                    ejercicio.enunciados_ocultos[item][nivel].append(ejercicio.enunciado_oculto_actual)
                    #Pone el enunciado
                    #frame_base.Doc.append(f"{ejercicio.eje_tematico}\n{ejercicio.unidad}\n{ejercicio.contenido} {nivel}")
                    frame_base.Doc.append(pylatex.NoEscape(r"\begin{enumerate}[label=\arabic*),start=" f"{numero_del_ejercicio}" "]"))
                    frame_base.Doc.append(pylatex.NoEscape(r"\item"))
                    frame_base.Doc.append(pylatex.NoEscape(ejercicio.seleccion_multiple_enunciado.replace("¿","?`")))
                    #Pone las informaciones
                    frame_base.Doc.append(pylatex.NoEscape(r"\begin{enumerate}[label=(\arabic*),start=1]"))
                    frame_base.Doc.append(pylatex.NoEscape(r"\item"))
                    frame_base.Doc.append(pylatex.NoEscape(ejercicio.informacion_1))
                    frame_base.Doc.append(pylatex.NoEscape(r"\item"))
                    frame_base.Doc.append(pylatex.NoEscape(ejercicio.informacion_2))
                    frame_base.Doc.append(pylatex.NoEscape(r"\end{enumerate} \end{enumerate}"))

                    #Pone las alternativas
                    frame_base.Doc.append(pylatex.NoEscape(r"\begin{enumerate}[label=\Alph*)]"))
                    for contenido in ["(1) por sí sola", "(2) por sí sola", "Ambas juntas, (1) y (2)", "Cada una por sí sola, (1) ó (2)", "Se requiere información adicional"]:
                        frame_base.Doc.append(pylatex.NoEscape(r"\item"))
                        frame_base.Doc.append(pylatex.NoEscape(contenido))
                    frame_base.Doc.append(pylatex.NoEscape(r"\end{enumerate}"))
                    
                    #Agrega la alternativa correcta a la lista de respuestas correctas
                    respuestas.append(f"{numero_del_ejercicio}) {ejercicio.alternativa_correcta}")



                    #Crea fotos de los ejercicios por separado
                    if separar_ejercicios_de_seleccion_multiple.get():
                        if not os.path.exists("temp\\Fotos"):
                            os.mkdir("temp\\Fotos")
                        foto = pylatex.Document(page_numbers=None, documentclass="standalone", document_options=pylatex.NoEscape(r"varwidth=true, border=0pt, convert={size=640x}"))
                        for paquete in [r"\usepackage{ragged2e}", r"\usepackage{setspace}", r"\usepackage{longtable}", r"\usepackage{tabularx}", r"\usepackage{gensymb}", r"\usepackage{amsmath}", r"\usepackage{amssymb}", r"\usepackage{enumitem}", r"\usepackage{graphicx}", r"\usepackage{tikz}", r"\usepackage{tkz-euclide}", r"\usepackage{siunitx}", r"\usepackage{fourier}", r"\usetikzlibrary{fit, shapes.geometric, quotes, angles, through, intersections}"]:
                            foto.preamble.append(pylatex.NoEscape(paquete))

                        #Pone el enunciado
                        foto.append(pylatex.NoEscape(r"\begin{longtable}{p{8.3 cm}}"))
                        foto.append(pylatex.NoEscape(ejercicio.seleccion_multiple_enunciado.replace("¿","?`")))
                        #Pone las informaciones
                        foto.append(pylatex.NoEscape(r"\begin{enumerate}[label=(\arabic*),start=1]"))
                        foto.append(pylatex.NoEscape(r"\item"))
                        foto.append(pylatex.NoEscape(ejercicio.informacion_1))
                        foto.append(pylatex.NoEscape(r"\item"))
                        foto.append(pylatex.NoEscape(ejercicio.informacion_2))
                        foto.append(pylatex.NoEscape(r"\end{enumerate}"))
                        foto.append(pylatex.NoEscape(r"\end{longtable}"))

                        #Genera el .tex
                        foto.generate_tex(f"temp\\Fotos\\{numero_del_ejercicio}")
                        #Genera el pdf
                        current_path = os.path.abspath(__file__)
                        folder_container = os.path.dirname(current_path) + r"\temp\Fotos"
                        subprocess.run(f'lualatex -interaction=nonstopmode -output-directory="{folder_container}" "{folder_container}\\{numero_del_ejercicio}.tex"', shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
                        #Quita los restos
                        for formato in ["aux", "log", "tex"]:
                            os.remove(f"temp\\Fotos\\{numero_del_ejercicio}.{formato}")
                        #Crea la foto
                        pdf2image.convert_from_path(f"temp\\Fotos\\{numero_del_ejercicio}.pdf")[0].save(f"temp\\Fotos\\{numero_del_ejercicio}.jpg", 'JPEG')
                        #Quita el pdf
                        os.remove(f"temp\\Fotos\\{numero_del_ejercicio}.pdf")



                #Decide si la tabla sigue hacia al lado o hacia abajo
                if numero_del_ejercicio % 2 == 1:
                    frame_base.Doc.append(pylatex.NoEscape("&"))
                else:
                    frame_base.Doc.append(pylatex.NoEscape(r"\\"))
                    frame_base.Doc.append(pylatex.NoEscape(r"\hline"))

                #Suma 1 al numero del ejercicio en el documento
                numero_del_ejercicio += 1

                #Ctualiza la barra y el label de progreso
                barra_de_progreso["value"] += 1
                label_de_progreso["text"] = f"Ejercicios calculados: {barra_de_progreso['value']} de {barra_de_progreso['maximum']}"

    #================================Cierra item selección múltiple====================================
    print("Se terminó la zona de importación de selección múltiple")
    #Finaliza la tabla y completa el pdf
    if numero_del_ejercicio % 2 == 0:
        frame_base.Doc.append(pylatex.NoEscape(r"\\"))
        frame_base.Doc.append(pylatex.NoEscape(r"\hline \end{longtable}"))
    else:
        frame_base.Doc.append(pylatex.NoEscape(r"\end{longtable}"))

    #Genera otro pdf con las respuestas
    frame_base.Doc_respuestas.append(pylatex.NoEscape(r"Estas son las respuestas correctas del item de selección múltiple:\\\\"))
    frame_base.Doc_respuestas.append(pylatex.NoEscape(r"\begin{longtable}{|p{4 cm}|p{4 cm}|}"))
    frame_base.Doc_respuestas.append(pylatex.NoEscape(r"\hline"))

    for respuesta in respuestas:
        frame_base.Doc_respuestas.append(respuesta)
        if respuestas.index(respuesta) % 2 == 0:
            frame_base.Doc_respuestas.append(pylatex.NoEscape("&"))
        else:
            frame_base.Doc_respuestas.append(pylatex.NoEscape(r"\\"))
            frame_base.Doc_respuestas.append(pylatex.NoEscape(r"\hline"))

    if len(respuestas) % 2 == 0:
        frame_base.Doc_respuestas.append(pylatex.NoEscape(r"\end{longtable}"))    
    else:
        frame_base.Doc_respuestas.append(pylatex.NoEscape(r"\\"))
        frame_base.Doc_respuestas.append(pylatex.NoEscape(r"\hline"))
        frame_base.Doc_respuestas.append(pylatex.NoEscape(r"\end{longtable}"))

def agregar_ejercicios_desarrollo():
    print("Se inició el agregado de desarrollo")
    item = "Desarrollo"
    respuestas = []
    frame_base.Doc.append(pylatex.NoEscape(r"\textbf{Item desarrollo:} "))
    instrucciones = instrucciones_desarrollo.get()
    while True:
        if len(instrucciones):
            if instrucciones[-1] in ["\n"," "]:
                instrucciones = instrucciones[:-1]
            else:
                break
        else:
            break
    frame_base.Doc.append(instrucciones)
    frame_base.Doc.append(pylatex.NoEscape(r"\begin{enumerate}[label=\arabic*),start=1]"))

    #====================================Zona de importación====================================
    #Decide el ejercicio a usar
    for ejercicio in ejercicios.lista:
        for nivel in '123':
            if not ejercicio.existencias[item][nivel]:
                continue
            for _ in range(0, ejercicio.cantidades[item][nivel]):

                print(f"Se está intentando importar {ejercicio.rutas[item][nivel]} de tipo desarrollo")

                #Inicia el cambio de opcion a utilizar
                cantidad_opciones = ejercicio.opciones[item][nivel]
                lista_de_opciones_no_usadas = []

                while True:#Importa hasta que las alternativas sean distintas o el enunciado no haya sido usado
                    #Hace que las opciones se repitan solo al haber usado todas
                    if len(lista_de_opciones_no_usadas) == 0:
                        lista_de_opciones_no_usadas = list(range(1,cantidad_opciones+1))
                    opcion_a_usar = choice(lista_de_opciones_no_usadas)
                    lista_de_opciones_no_usadas.remove(opcion_a_usar)

                    #Importa hasta que las alternativas sean distintas o el enunciado no haya sido usado
                    espacio_para_el_desarrollo = 8
                    interior_de_ejercicio = f"opcion={opcion_a_usar}\n"     + ejercicio.instrucciones[item][nivel] +   "\nejercicio.desarrollo_enunciado, ejercicio.desarrollo_contenido_correcto, ejercicio.enunciado_oculto_actual, ejercicio.desarrollo_espacio_para_el_desarrollo = enunciado, contenido_correcto, enunciado_oculto, espacio_para_el_desarrollo"
                    exec(interior_de_ejercicio)

                    if ejercicio.enunciado_oculto_actual in ejercicio.enunciados_ocultos[item][nivel]:
                        print(f"En {ejercicio.eje_tematico} {ejercicio.unidad} {ejercicio.contenido} de tipo desarrollo se repitió el enunciado")
                        print(ejercicio.desarrollo_enunciado)
                        print(ejercicio.desarrollo_contenido_correcto)
                    else:
                        break

                ejercicio.enunciados_ocultos[item][nivel].append(ejercicio.enunciado_oculto_actual)

                #Pone el enunciado y el nombre del ejercicio
                frame_base.Doc.append(pylatex.NoEscape(r"\item"))

                frame_base.Doc.append(pylatex.NoEscape(ejercicio.desarrollo_enunciado.replace("¿","?`") + espacio_para_el_desarrollo*("\n"+r"\hfill \break")))
                # frame_base.Doc.append(pylatex.NoEscape(r"\hfill \break"))
                # frame_base.Doc.append(pylatex.NoEscape(r"\\"))

                #Agrega la respuesta a la lista de respuestas correctas
                respuestas.append(ejercicio.desarrollo_contenido_correcto)

                #Actualiza la barra y el label de progreso
                barra_de_progreso["value"] += 1
                label_de_progreso["text"] = f"Ejercicios calculados: {barra_de_progreso['value']} de {barra_de_progreso['maximum']}"

    #================================Cierra item desarrollo====================================
    print("Se terminó la zona de importación de desarrollo")

    #Finaliza la tabla y completa el pdf
    frame_base.Doc.append(pylatex.NoEscape(r"\end{enumerate}"))


    #Agrega las respuestas correctas
    frame_base.Doc_respuestas.append(pylatex.NoEscape(r"Estas son las respuestas correctas del item de desarrollo:"))
    frame_base.Doc_respuestas.append(pylatex.NoEscape(r"\begin{enumerate}[label=\arabic*),start=1]"))

    for respuesta in respuestas:
        frame_base.Doc_respuestas.append(pylatex.NoEscape(r"\item"))
        frame_base.Doc_respuestas.append(pylatex.NoEscape(respuesta))

    frame_base.Doc_respuestas.append(pylatex.NoEscape(r"\end{enumerate}"))

def agregar_ejercicios_verdadero_y_falso():
    print("Se inició el agregado de términos pareados")
    item = "Verdadero y falso"
    respuestas = []
    frame_base.Doc.append(pylatex.NoEscape(r"\textbf{Item verdadero y falso:} "))
    instrucciones = instrucciones_verdadero_y_falso.get()
    while True:
        if len(instrucciones):
            if instrucciones[-1] in ["\n"," "]:
                instrucciones = instrucciones[:-1]
            else:
                break
        else:
            break
    frame_base.Doc.append(instrucciones)
    frame_base.Doc.append(pylatex.NoEscape(r"\begin{enumerate}[label=\arabic*),start=1]"))

    #====================================Zona de importación====================================
    #Decide el ejercicio a usar
    for ejercicio in ejercicios.lista:
        for nivel in "123":
            if not ejercicio.existencias[item][nivel]:
                continue
            for _ in range(0, ejercicio.cantidades[item][nivel]):

                print(f"Se está intentando importar {ejercicio.rutas[item][nivel]} de tipo verdadero y falso")

                #Inicia el cambio de opcion a utilizar
                cantidad_opciones = ejercicio.opciones[item][nivel]
                lista_de_opciones_no_usadas = []

                while True:#Importa hasta que las alternativas sean distintas o el enunciado no haya sido usado
                    #Hace que las opciones se repitan solo al haber usado todas
                    if len(lista_de_opciones_no_usadas) == 0:
                        lista_de_opciones_no_usadas = list(range(1,cantidad_opciones+1))
                    opcion_a_usar = choice(lista_de_opciones_no_usadas)
                    lista_de_opciones_no_usadas.remove(opcion_a_usar)

                    #Importa hasta que las alternativas sean distintas o el enunciado no haya sido usado
                    tipo_de_ejercicio_a_incluir = choice([True,True,True,False,False,False,False,False,False,False])
                    espacio_para_el_desarrollo = 1
                    interior_de_ejercicio = f"opcion={opcion_a_usar}\n"     + ejercicio.instrucciones[item][nivel] +    "\nejercicio.verdadero_y_falso_enunciado_verdadero, ejercicio.verdadero_y_falso_enunciado_falso, ejercicio.enunciado_oculto_actual, ejercicio.verdadero_y_falso_espacio_para_el_desarrollo = enunciado_verdadero, enunciado_falso, enunciado_oculto, espacio_para_el_desarrollo"
                    exec(interior_de_ejercicio)

                    if ejercicio.enunciado_oculto_actual in ejercicio.enunciados_ocultos[item][nivel]:
                        print(f"En {ejercicio.eje_tematico} {ejercicio.unidad} {ejercicio.contenido} de tipo verdadero y falso se repitió el enunciado")
                        print(ejercicio.verdadero_y_falso_enunciado_verdadero)
                        print(ejercicio.verdadero_y_falso_enunciado_falso)
                    elif ejercicio.verdadero_y_falso_enunciado_verdadero==ejercicio.verdadero_y_falso_enunciado_falso:
                        print("El enunciado verdadero y el falso eran iguales")
                    else:
                        break

                ejercicio.enunciados_ocultos[item][nivel].append(ejercicio.enunciado_oculto_actual)

                #Pone el enunciado y el nombre del ejercicio
                frame_base.Doc.append(pylatex.NoEscape(r"\item"))


                #Pone el enunciado y agrega la respuesta a la lista de respuestas correctas
                if tipo_de_ejercicio_a_incluir==True:
                    frame_base.Doc.append(pylatex.NoEscape(r"V\ \ \ \ F\ \ \ \ "+ejercicio.verdadero_y_falso_enunciado_verdadero.replace("¿","?`")))
                    respuestas.append("Verdadero")
                elif tipo_de_ejercicio_a_incluir==False:
                    frame_base.Doc.append(pylatex.NoEscape(r"V\ \ \ \ F\ \ \ \ "+ejercicio.verdadero_y_falso_enunciado_falso.replace("¿","?`")))
                    respuestas.append(r"Falso\\Justificación: "+ejercicio.verdadero_y_falso_enunciado_verdadero)

                frame_base.Doc.append(pylatex.NoEscape(espacio_para_el_desarrollo*("\n"+r"\hfill \break")+"\n"+r"\hrule"))



                
                #Actualiza la barra y el label de progreso
                barra_de_progreso["value"] += 1
                label_de_progreso["text"] = f"Ejercicios calculados: {barra_de_progreso['value']} de {barra_de_progreso['maximum']}"

    #================================Fin Zona de importación====================================
    print("Se terminó la zona de importación de verdadero y falso")

    #Finaliza la tabla y completa el pdf
    frame_base.Doc.append(pylatex.NoEscape(r"\end{enumerate}"))

    #Agrega las respuestas correctas
    frame_base.Doc_respuestas.append(pylatex.NoEscape(r"Estas son las respuestas correctas del item de verdadero y falso:"))
    frame_base.Doc_respuestas.append(pylatex.NoEscape(r"\begin{enumerate}[label=\arabic*),start=1]"))

    for respuesta in respuestas:
        frame_base.Doc_respuestas.append(pylatex.NoEscape(r"\item"))
        frame_base.Doc_respuestas.append(pylatex.NoEscape(respuesta))

    frame_base.Doc_respuestas.append(pylatex.NoEscape(r"\end{enumerate}"))





def generar_pdf(ruta_carpeta, nombre_archivo):
    #Obtiene las cantidades de todos los ejercicios
    ejercicios.vaciar_enunciados_ocultos()

    #Genera las variables que contienen la información de los archivos fotmato .tex
    global barra_de_progreso, label_de_progreso
    frame_base.Doc = New_document(ruta_encabezado=imagen_encabezado.get(), ruta_pie=imagen_pie.get(), posicion_encabezado=imagen_encabezado.posicion, posicion_pie=imagen_pie.posicion)
    frame_base.Doc_respuestas = New_document(ruta_encabezado=imagen_encabezado.get(), ruta_pie=imagen_pie.get(), posicion_encabezado=imagen_encabezado.posicion, posicion_pie=imagen_pie.posicion)
    frame_base.Doc_procedimientos = New_document(ruta_encabezado=imagen_encabezado.get(), ruta_pie=imagen_pie.get(), posicion_encabezado=imagen_encabezado.posicion, posicion_pie=imagen_pie.posicion)

    ######################  NUEVO FRAME#################
    frame_base_progreso = tk.Toplevel()
    
    #Configura el frame
    frame_base_progreso.title("TstMaker")
    frame_base_progreso.protocol("WM_DELETE_WINDOW", lambda : None)
    frame_base_progreso.resizable(False, False)

    #Pone los widget en el frame
    barra_de_progreso = ttk.Progressbar(frame_base_progreso, length=350, style="Horizontal.TProgressbar", value=0, maximum=ejercicios.cantidad_ejercicios_solicitados())
    label_de_progreso = tk.Label(frame_base_progreso, text=f"Ejercicios calculados: 0 de {barra_de_progreso['maximum']}\n", bg="#FFEEDD")
    barra_de_progreso.grid(row=0, column=0)
    label_de_progreso.grid(row=1, column=0)

    #Centra el frame de progreso y lo levanta
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
    barra_de_progreso["maximum"] = ejercicios.cantidad_ejercicios_solicitados()
    
    #Importa los ejercicios
    funciones = (agregar_ejercicios_seleccion_multiple, agregar_ejercicios_desarrollo, agregar_ejercicios_verdadero_y_falso)
    for item, funcion in zip(ejercicios.items, funciones):
        if 0 < ejercicios.cantidades_ejercicios_por_item()[item]:
            funcion()

    #Llena el pdf de procedimientos
    if generar_pdf_con_procedimientos.get():
        frame_base.Doc_procedimientos.append(pylatex.NoEscape(r"A continuación se presentan los procedimientos para realizar los ejercicios:\hfill \break \hfill \break \hfill \break"+"\n"))
        for ejercicio in ejercicios.lista:
            salto_automatico, procedimiento = False, "No se ha creado esta explicación"
            if 0 < ejercicio.total_de_ejercicios:
                with open(ejercicio.ruta_procedimientos, "r", encoding="utf-8") as file:
                    interior_de_ejercicio = file.read()
                print(f"{ejercicio.unidad}, {ejercicio.contenido}")
                exec(interior_de_ejercicio+"\nejercicio.procedimiento_salto_automatico, ejercicio.procedimiento_procedimiento = salto_automatico, procedimiento")
                if ejercicio.procedimiento_salto_automatico:
                    ejercicio.procedimiento_procedimiento = ejercicio.procedimiento_procedimiento.replace("\n", "\n"+r"\hfill \break"+"\n")
                frame_base.Doc_procedimientos.append(pylatex.NoEscape(r"\begin{center}"))
                frame_base.Doc_procedimientos.append(ejercicio.contenido)
                frame_base.Doc_procedimientos.append(pylatex.NoEscape(r"\end{center}"))
                frame_base.Doc_procedimientos.append(pylatex.NoEscape(r"\hfill \break \hfill \break"))
                frame_base.Doc_procedimientos.append(pylatex.NoEscape(procedimiento+"\n"+r"\newpage"))

    #Se crean e inician las generaciones de los pdf
    hilo_Doc = threading.Thread(target=frame_base.Doc.generate_pdf, kwargs={"name":"Prueba", "generate_tex":False}, daemon=True)
    hilo_Doc_respuestas = threading.Thread(target=frame_base.Doc_respuestas.generate_pdf, kwargs={"name":"Respuestas"}, daemon=True)
    hilo_Doc_procedimientos = threading.Thread(target=frame_base.Doc_procedimientos.generate_pdf, kwargs={"name":"Procedimientos"}, daemon=True)


    frame_base.Doc.generate_tex("temp\\Prueba")
    hilo_Doc.start()
    if generar_pdf_con_respuestas.get() and ejercicios.cantidad_ejercicios_solicitados() != 0:
        hilo_Doc_respuestas.start()
    if generar_pdf_con_procedimientos.get():
        hilo_Doc_procedimientos.start()

    #Cambia la forma en que avanza la barra de progreso
    barra_de_progreso["value"] = 0
    tamaño_esperado = int(os.path.getsize("temp/Prueba.tex")*1.265839027)
    barra_de_progreso["maximum"] = tamaño_esperado
    label_de_progreso["text"] = f"Generando archivos. Esto puede tomar unos minutos.\n0 bytes  /  {tamaño_esperado} bytes"

    #Se espera que los pdf terminen de crearse, se sabe que terminó cicho proceso poeruq se borran los .bat
    #Aumenta la barra de progreso mientras se compilan los pdf's
    while hilo_Doc.is_alive() or hilo_Doc_respuestas.is_alive() or hilo_Doc_procedimientos.is_alive():
        time.sleep(0.5)
        if os.path.exists("temp/Prueba.pdf"):
            tamaño_actual = os.path.getsize("temp/Prueba.pdf")
            barra_de_progreso["value"] = tamaño_actual
            label_de_progreso["text"] = f"Generando archivos. Esto puede tomar unos minutos.\n{min(tamaño_actual,tamaño_esperado)} bytes  /  {tamaño_esperado} bytes"
    barra_de_progreso["value"] = barra_de_progreso["maximum"]
    label_de_progreso["text"] = f"Generando archivos. Esto puede tomar unos minutos.\n{tamaño_esperado} bytes  /  {tamaño_esperado} bytes"
    time.sleep(0.5)

    #Mueve los archivos a donde se pidió
    ruta_de_guardado = ruta_carpeta + '/' + nombre_archivo
    criterios = [True, mantener_archivo_tex.get(), generar_pdf_con_respuestas.get() and ejercicios.cantidad_ejercicios_solicitados() != 0, generar_pdf_con_procedimientos.get() and ejercicios.cantidad_ejercicios_solicitados() !=0]
    initial_paths = ["temp/Prueba.pdf", "temp/Prueba.tex", "temp/Respuestas.pdf", "temp/Procedimientos.pdf"]
    new_paths = [ruta_de_guardado+".pdf", ruta_de_guardado+".tex", ruta_de_guardado+" - Respuestas.pdf", ruta_de_guardado+" - Procedimientos.pdf"]
    file_names = [nombre_archivo+'.pdf', nombre_archivo+'.tex', nombre_archivo+' - Respuestas.pdf', nombre_archivo+' - Procedimientos.pdf']
    for criterio, initial_path, new_path, file_name in zip(criterios, initial_paths, new_paths, file_names):
        while criterio:
            try:
                shutil.move(initial_path, new_path)
                print(initial_path, new_path)
                break
            except:
                if not tk.messagebox.askretrycancel("TstMaker", f"No puede generarse \"{file_name}\" debido a que hay un archivo en la dirección de destino con el mismo nombre que no puede ser borrado ya que otro programa lo tiene abierto. Cierre dicho archivo e inténtelo de nuevo."):
                    break
    
    #Mueve la carpeta de fotos si se pidió
    if separar_ejercicios_de_seleccion_multiple.get():
        shutil.move("temp\\Fotos", ruta_carpeta+"/Fotos")

    if os.path.exists("temp"):
        shutil.rmtree("temp")

    frame_base_progreso.destroy()
    


def comenzar_generar_pdf():
    #Deshabilita el frame base
    frame_base.wm_attributes("-disabled", True)

    #Ventana emergente en caso de que la prueba esté vacía
    if ejercicios.cantidad_ejercicios_solicitados() == 0:
        if not tk.messagebox.askyesno("TstMaker", "No has seleccionado ejercicios, por lo que la evaluación estará vacía y no se generarán otros documentos.\n¿Deseas continuar de todas formas?"):
            frame_base.wm_attributes("-disabled", False)
            return None


    #Genera el nombre del archivo
    nombre_archivo = nombre_de_la_prueba.get()
    if nombre_archivo=="":
        nombre_archivo = "Sin nombre"

    #Abre el explorador y genera la ruta de guardado
    ruta_escritorio = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop") # determina la ruta del escritorio
    ruta_completa = asksaveasfilename(title="Guardar como", initialdir=ruta_escritorio, initialfile=nombre_archivo, filetypes=(("Formato pdf","*.pdf"),)) #abre el explorador

    #Detiene la creación si no se eligió una ruta. Esto puede ser porque se canceló o se cerró el explorador
    if ruta_completa=="":
        frame_base.wm_attributes("-disabled", False)
        return None

    # obtiene la ruta
    ruta_carpeta = ruta_completa[:ruta_completa.rfind("/")] # ruta carpeta sin último /
    nombre_archivo = ruta_completa.replace(ruta_carpeta, '')

    generar_pdf(ruta_carpeta, nombre_archivo)

    frame_base.wm_attributes("-disabled", False)
    tk.messagebox.showinfo("TstMaker", "Ha finalizado el proceso de creación de documentos.")

def guardar_confiruracion():
    with open("Configuracion.py", "w", encoding="utf-8") as file:
        Configuracion['cantidad_de_alternativas_por_pregunta'] = int(cantidad_de_alternativas_por_pregunta.get())
        Configuracion['generar_pdf_con_respuestas'] = generar_pdf_con_respuestas.get()
        Configuracion['generar_pdf_con_procedimientos'] = generar_pdf_con_procedimientos.get()
        Configuracion['mantener_archivo_tex'] = mantener_archivo_tex.get()
        Configuracion['ancho_papel'] = ancho_papel.get().replace('.',',')
        Configuracion['alto_papel'] = alto_papel.get().replace('.',',')
        Configuracion['margen_superior'] = margen_superior.get().replace('.',',')
        Configuracion['margen_inferior'] = margen_inferior.get().replace('.',',')
        Configuracion['margen_izquierdo'] = margen_derecho.get().replace('.',',')
        Configuracion['margen_derecho'] = margen_derecho.get().replace('.',',')
        Configuracion['imagen_encabezado'] = imagen_encabezado.get()
        Configuracion['imagen_pie'] = imagen_pie.get()

        for instruccion, box in zip(['instrucciones_generales', 'instrucciones_seleccion_multiple', 'instrucciones_desarrollo', 'instrucciones_verdadero_y_falso'], [instrucciones_generales, instrucciones_seleccion_multiple, instrucciones_desarrollo, instrucciones_verdadero_y_falso]):
            contenido = box.get()
            while contenido[-1] in [' ', '\n']:
                contenido = contenido[:-1]
            Configuracion[instruccion] = contenido

        Configuracion['tabla_inicial'] = []
        for row in frame_base.frame_tabla.winfo_children():
            contenido_de_la_fila = []
            for box in row.PanedWindow.winfo_children():
                contenido_de_la_fila.append({"contenido_de_la_caja":box.get("1.0", "end-1c"), "posicion_del_texto":box.posicion_del_texto})
            Configuracion['tabla_inicial'].append(contenido_de_la_fila)

        file.write(str(Configuracion))



style = ttk.Style()
style.theme_create("estilo", parent="alt", settings={
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
frame_datos = Frame_datos(notebook_principal)
notebook_principal.add(frame_datos, text="Datos de la evaluación")

#Frame donde irán las pociones de la prueba, pero no la tabla
sub_frame_1_datos = tk.Frame(frame_datos.scrollable_frame, bg=frame_datos["bg"])
sub_frame_1_datos.pack(fill="x", padx=40, pady=40)
#Opciones de la prueba
nombre_de_la_prueba = Entry_datos(sub_frame_1_datos, "Nombre del documento:", valor_inicial="", largo=40)
cantidad_de_alternativas_por_pregunta = Combobox_datos(sub_frame_1_datos, "Cantidad de alternativas por pregunta:", Configuracion['cantidad_de_alternativas_por_pregunta'], ["5","4"], 2)
generar_pdf_con_respuestas = Checkbutton_datos(sub_frame_1_datos, "Generar pdf con respuestas:", Configuracion['generar_pdf_con_respuestas'])
mantener_archivo_tex = Checkbutton_datos(sub_frame_1_datos, "Generar archivo .tex:", Configuracion['mantener_archivo_tex'])
separar_ejercicios_de_seleccion_multiple = Checkbutton_datos(sub_frame_1_datos, "Separar ejercicios de selección múltiple:", False)
# cantidad_a_establecer_para_todos = Entry_datos(sub_frame_1_datos, "Cantidad global:", 1, largo=6)         # Este input es usado en desarrollo
ancho_papel = Entry_numeros_datos(sub_frame_1_datos, "Ancho del papel (cm):", valor_inicial=Configuracion['ancho_papel'], largo=6)
alto_papel = Entry_numeros_datos(sub_frame_1_datos, "Alto del papel (cm):", valor_inicial=Configuracion['alto_papel'], largo=6)
margen_superior = Entry_numeros_datos(sub_frame_1_datos, "Margen superior (cm):", valor_inicial=Configuracion['margen_superior'], largo=6)
margen_inferior = Entry_numeros_datos(sub_frame_1_datos, "Margen inferior (cm):", valor_inicial=Configuracion['margen_inferior'], largo=6)
margen_izquierdo = Entry_numeros_datos(sub_frame_1_datos, "Margen izquierdo (cm):", valor_inicial=Configuracion['margen_izquierdo'], largo=6)
margen_derecho = Entry_numeros_datos(sub_frame_1_datos, "Margen derecho (cm):", valor_inicial=Configuracion['margen_derecho'], largo=6)
imagen_encabezado = Imagen_datos(sub_frame_1_datos, "Imagen del encabezado", ruta=Configuracion['imagen_encabezado'])
imagen_pie = Imagen_datos(sub_frame_1_datos, "Imagen de pie de página", ruta=Configuracion['imagen_pie'])
instrucciones_generales = Text_ajustable_datos(sub_frame_1_datos, "Instrucciones generales:", valor_inicial=Configuracion['instrucciones_generales'])
instrucciones_seleccion_multiple = Text_ajustable_datos(sub_frame_1_datos, "Instrucciones del item de selección múltiple:", valor_inicial=Configuracion['instrucciones_seleccion_multiple'])
instrucciones_desarrollo = Text_ajustable_datos(sub_frame_1_datos, "Instrucciones del item de desarrollo:", valor_inicial=Configuracion['instrucciones_desarrollo'])
instrucciones_verdadero_y_falso = Text_ajustable_datos(sub_frame_1_datos, "Instrucciones del item de verdadero y falso:", valor_inicial=Configuracion['instrucciones_verdadero_y_falso'])

#Se genera, pero no se muestra
generar_pdf_con_procedimientos = Checkbutton_datos(sub_frame_1_datos, "Generar pdf con procedimientos:", Configuracion['generar_pdf_con_procedimientos'])
generar_pdf_con_procedimientos.ticket.grid_forget()
generar_pdf_con_procedimientos.label.grid_forget()

#Genera el botón para establecer una cantidad general en todos los ejercicios. Este es un elemento de desarrollo
# boton_establecer = tk.Button(sub_frame_1_datos, text="Establecer cantidad global", width=20, height=2, bg="#00CD63")
# boton_establecer["command"] = lambda : threading.Thread(target=establecer_cantidad_general, kwargs={"boton_establecer":boton_establecer}, daemon=True).start()
# boton_establecer.grid(row=5, column=1, padx=0)

#Frame que contiene la tabla y los botones que agregan filas
frame_tabla_y_botones = tk.Frame(frame_datos.scrollable_frame, bg=frame_datos["bg"])
frame_tabla_y_botones.pack(pady=50)

#Frame de la tabla
frame_base.frame_tabla = tk.Frame(frame_tabla_y_botones, borderwidth=0, highlightthickness=0)
frame_base.frame_tabla.pack(pady=10)

#Llena la tabla con la guardada
for fila in Configuracion['tabla_inicial']:
    nueva_fila = Frame_row(frame_base.frame_tabla)
    for diccionario in fila:
        nueva_fila.agregar_caja(valor_inicial=diccionario["contenido_de_la_caja"], posicion_del_texto=diccionario["posicion_del_texto"])
    nueva_fila.pack(side="top", fill="x")
    for box in nueva_fila.PanedWindow.winfo_children():
        box.key()

#Función que crea las filas y las pone en la lista anterior
def crear_row():
    nueva_fila = Frame_row(frame_base.frame_tabla)
    nueva_fila.agregar_caja()
    nueva_fila.pack(side="top", fill="x")


#Frame donde irá el botón que agrega una fila
boton_crea_fila = tk.Button(frame_tabla_y_botones, bg="#00CD63", text=f"Agregar fila", height=2, command=crear_row)
boton_crea_fila.pack()

#linkea al scrollbar de frame_datos todos sus hijos y sub hijos y así
def linkear_al_scrollbar_de_frame_datos(frame):
    for widget in frame.winfo_children():
        widget.bind("<MouseWheel>", frame_base.frame_datos.mouse_wheel)
        if isinstance(widget , (tk.Frame, tk.Canvas, tk.PanedWindow, Frame_row)):
            linkear_al_scrollbar_de_frame_datos(widget)
linkear_al_scrollbar_de_frame_datos(frame_base.frame_datos)
##############TERMINÓ DE GENERAR EL FRAME DE DATOS







#Genera la interfaz de los ejercicios
tamaño_borde = 5
color_paneles = "black"
panel_completo = tk.PanedWindow(notebook_principal, bd=0, sashwidth=tamaño_borde, bg=color_paneles, orient="horizontal")
panel_izquierdo_horizontal = tk.PanedWindow(panel_completo, bd=0, sashwidth=tamaño_borde, bg=color_paneles, orient="horizontal")
panel_izquierdo_vertical = tk.PanedWindow(panel_izquierdo_horizontal, bd=0, sashwidth=tamaño_borde, bg=color_paneles, orient="vertical")

#Genera los frames
frame_vista_previa = Frame_vista_previa(panel_completo)
frame_treeview = Frame_treeview(panel_izquierdo_horizontal)
frame_spinbox = Frame_spinbox(panel_izquierdo_vertical)
frame_descripcion = Frame_descripcion(panel_izquierdo_vertical)

#Llena los panels y agrega la pestaña al notebook
width_screen = frame_base.winfo_screenwidth()
height_screen = frame_base.winfo_screenheight()
porcentaje_width_1 = 0.6
porcentaje_height_1 = 0.5
porcentaje_width_2 = 0.6

notebook_principal.add(panel_completo, text="Selección de ejercicios")
panel_completo.add(panel_izquierdo_horizontal, minsize=400, sticky="nswe", width=width_screen*porcentaje_width_1)
panel_completo.add(frame_vista_previa, minsize=400, sticky="nswe")
panel_izquierdo_horizontal.add(frame_treeview, minsize=200, sticky="nswe", width=width_screen*porcentaje_width_1*porcentaje_width_2)
panel_izquierdo_horizontal.add(panel_izquierdo_vertical, minsize=300, sticky="nswe")
panel_izquierdo_vertical.add(frame_spinbox, minsize=400, sticky="nswe", height=height_screen*porcentaje_height_1)
panel_izquierdo_vertical.add(frame_descripcion, minsize=250, sticky="nswe")




for eje_tematico in ejercicios.eje_unidad_contenido:
    eje_tematico_treeview = frame_treeview.treeview.insert(parent="", index="end", text=eje_tematico, tag="Eje_temático", iid=eje_tematico.replace(" ",""))
    for unidad in ejercicios.eje_unidad_contenido[eje_tematico]:
        unidad_eje_tematico = frame_treeview.treeview.insert(parent=eje_tematico_treeview, index="end", text=unidad, tag="Unidad", iid=f"{eje_tematico}/{unidad}".replace(" ",""))
        for contenido in ejercicios.eje_unidad_contenido[eje_tematico][unidad]:
            frame_treeview.treeview.insert(unidad_eje_tematico, index="end", text=contenido, tag="Ejercicio")






#Genera el frame carrito y los botones
frame_carrito = Frame_carrito(notebook_principal)
notebook_principal.add(frame_carrito, text="Carrito")

frame_carrito_botones = tk.Frame(frame_carrito, height=2)
frame_carrito_botones.grid(row=0, column=0, sticky="we")
frame_carrito_botones.grid_columnconfigure(0, weight=1)
frame_carrito_botones.grid_columnconfigure(1, weight=1)
frame_carrito_botones.grid_columnconfigure(2, weight=1)

boton_generar_pdf = tk.Button(frame_carrito_botones, text="Generar evaluación", width=30, height=2, command=lambda : threading.Thread(target=comenzar_generar_pdf,daemon=True).start(), bg="#00CD63")
boton_limpiar_carrito = tk.Button(frame_carrito_botones, text="Limpiar carrito", width=30, height=2, command=lambda : threading.Thread(target=frame_carrito.limpiar,daemon=True).start(), bg="#00CD63")
boton_eliminar_ejercicio = tk.Button(frame_carrito_botones, text="Eliminar ejercicios seleccionados", width=30, height=2, command=frame_carrito.borrar_fila_con_focus, bg="#00CD63")

boton_generar_pdf.grid(row=0, column=0, pady=20)
boton_limpiar_carrito.grid(row=0, column=1, pady=20)
boton_eliminar_ejercicio.grid(row=0, column=2, pady=20)





#Genera la barra de menú, los botones y sus comandos
Barra_menu = tk.Menu(frame_base)
frame_base.config(menu=Barra_menu)


Menu_1 = tk.Menu(Barra_menu, tearoff=0)
Menu_1.add_command(label="Guardar datos", command=guardar_confiruracion)
Menu_1.add_command(label="Generar evaluación", command=lambda : threading.Thread(target=comenzar_generar_pdf,daemon=True).start())
Menu_1.add_separator()
Menu_1.add_command(label="Salir", command=frame_base.destroy)
Barra_menu.add_cascade(label="Archivo", menu=Menu_1)




Menu_2 = tk.Menu(Barra_menu, tearoff=0)
Menu_2.add_command(label="Acerca de...", command=lambda : tk.messagebox.showinfo("TstMaker", f"""Nombre del programa: TstMaker
Autor: Bastián Gabriel Paredes Padget
Versión: Beta 12.5.7
Todos los derechos reservados."""))
Barra_menu.add_cascade(label="Ayuda", menu=Menu_2)









if __name__ == '__main__':
    frame_base.mainloop()



