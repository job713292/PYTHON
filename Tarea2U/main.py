import tkinter as tk
from tkinter import messagebox
from datetime import datetime


# ============================================================
# CLASE GESTIONCLIENTES
# ============================================================

class GestionClientes:

    def __init__(
        self,
        identificacion,
        nombre_completo,
        genero,
        tipo_menu,
        numero_sesiones,
        fecha_registro,
        precio_por_sesion
    ):
        self.identificacion = identificacion
        self.nombre_completo = nombre_completo
        self.genero = genero
        self.tipo_menu = tipo_menu
        self.numero_sesiones = numero_sesiones
        self.fecha_registro = fecha_registro
        self.precio_por_sesion = precio_por_sesion

    # Método para calcular el costo total
    def calcular_costo_total(self):
        return self.numero_sesiones * self.precio_por_sesion


# ============================================================
# VARIABLE GLOBAL PARA GUARDAR EL CLIENTE
# ============================================================

cliente_guardado = None


# ============================================================
# FUNCIÓN PARA VALIDAR CONTRASEÑA
# ============================================================

def verificar_contrasena():

    contrasena = entrada_contrasena.get()

    if contrasena == "1793":

        ventana.withdraw()
        ventana_registro()

    else:

        messagebox.showerror(
            "Error",
            "Contraseña incorrecta."
        )


# ============================================================
# VENTANA DE REGISTRO
# ============================================================

def ventana_registro():

    registro = tk.Toplevel(ventana)

    registro.title("Registro de Cliente - Sabor & Sazón")
    registro.geometry("700x700")

    # Color de fondo personalizado
    registro.configure(bg="#FFF4E6")

    # ========================================================
    # ENCABEZADO
    # ========================================================

    logo = tk.Label(
        registro,
        text="S&S",
        font=("Arial", 28, "bold"),
        bg="#FFF4E6",
        fg="#8B4513"
    )

    logo.pack(pady=(15, 0))

    titulo = tk.Label(
        registro,
        text="REGISTRO DE CLIENTE",
        font=("Arial", 20, "bold"),
        bg="#FFF4E6",
        fg="#8B4513"
    )

    titulo.pack(pady=10)

    subtitulo = tk.Label(
        registro,
        text="Sabor & Sazón - Sesiones Gastronómicas",
        font=("Arial", 11),
        bg="#FFF4E6",
        fg="#555555"
    )

    subtitulo.pack(pady=5)


    # ========================================================
    # IDENTIFICACIÓN
    # ========================================================

    tk.Label(
        registro,
        text="Identificación:",
        font=("Arial", 11, "bold"),
        bg="#FFF4E6"
    ).pack()

    entrada_identificacion = tk.Entry(
        registro,
        width=40
    )

    entrada_identificacion.pack(pady=5)


    # ========================================================
    # NOMBRE COMPLETO
    # ========================================================

    tk.Label(
        registro,
        text="Nombre completo:",
        font=("Arial", 11, "bold"),
        bg="#FFF4E6"
    ).pack()

    entrada_nombre = tk.Entry(
        registro,
        width=40
    )

    entrada_nombre.pack(pady=5)


    # ========================================================
    # GÉNERO
    # ========================================================

    tk.Label(
        registro,
        text="Género:",
        font=("Arial", 11, "bold"),
        bg="#FFF4E6"
    ).pack(pady=(5, 0))

    genero = tk.StringVar()
    genero.set("")

    marco_genero = tk.Frame(
        registro,
        bg="#FFF4E6"
    )

    marco_genero.pack()

    tk.Radiobutton(
        marco_genero,
        text="Masculino",
        variable=genero,
        value="Masculino",
        bg="#FFF4E6"
    ).pack(side="left", padx=10)

    tk.Radiobutton(
        marco_genero,
        text="Femenino",
        variable=genero,
        value="Femenino",
        bg="#FFF4E6"
    ).pack(side="left", padx=10)


    # ========================================================
    # TIPO DE MENÚ
    # ========================================================

    tk.Label(
        registro,
        text="Tipo de menú:",
        font=("Arial", 11, "bold"),
        bg="#FFF4E6"
    ).pack(pady=(10, 0))

    tipo_menu = tk.StringVar()

    tipo_menu.set("Seleccione un menú")

    menus = [
        "Menú ejecutivo",
        "Menú vegetariano",
        "Menú degustación",
        "Menú infantil",
        "Menú gourmet"
    ]

    menu = tk.OptionMenu(
        registro,
        tipo_menu,
        *menus
    )

    menu.config(
        width=25
    )

    menu.pack(pady=5)


    # ========================================================
    # PRECIO POR SESIÓN
    # ========================================================

    precio_var = tk.StringVar()

    precio_var.set("$0")

    tk.Label(
        registro,
        text="Precio por sesión:",
        font=("Arial", 11, "bold"),
        bg="#FFF4E6"
    ).pack(pady=(5, 0))

    entrada_precio = tk.Entry(
        registro,
        textvariable=precio_var,
        width=40,
        state="readonly",
        justify="center"
    )

    entrada_precio.pack(pady=5)


    # Diccionario con los precios
    precios = {
        "Menú ejecutivo": 35000,
        "Menú vegetariano": 28000,
        "Menú degustación": 75000,
        "Menú infantil": 20000,
        "Menú gourmet": 95000
    }


    # Función para actualizar precio
    def actualizar_precio(*args):

        precio = precios.get(
            tipo_menu.get(),
            0
        )

        precio_var.set(
            f"${precio:,.0f}"
        )


    # Detectar cambio de menú
    tipo_menu.trace_add(
        "write",
        actualizar_precio
    )


    # ========================================================
    # NÚMERO DE SESIONES
    # ========================================================

    tk.Label(
        registro,
        text="Número de sesiones:",
        font=("Arial", 11, "bold"),
        bg="#FFF4E6"
    ).pack(pady=(10, 0))

    entrada_sesiones = tk.Entry(
        registro,
        width=40
    )

    entrada_sesiones.pack(pady=5)


    # ========================================================
    # FECHA DE REGISTRO
    # ========================================================

    fecha_actual = datetime.now().strftime(
        "%d/%m/%Y %H:%M"
    )

    tk.Label(
        registro,
        text=f"Fecha de registro: {fecha_actual}",
        font=("Arial", 10),
        bg="#FFF4E6",
        fg="#555555"
    ).pack(pady=10)


    # ========================================================
    # FUNCIÓN GUARDAR REGISTRO
    # ========================================================

    def guardar_registro():

        global cliente_guardado

        identificacion = entrada_identificacion.get().strip()
        nombre = entrada_nombre.get().strip()
        genero_seleccionado = genero.get()
        menu_seleccionado = tipo_menu.get()
        sesiones = entrada_sesiones.get().strip()


        # Validación de identificación
        if identificacion == "":
            messagebox.showwarning(
                "Dato faltante",
                "Ingrese la identificación."
            )
            entrada_identificacion.focus()
            return


        # Validación de nombre
        if nombre == "":
            messagebox.showwarning(
                "Dato faltante",
                "Ingrese el nombre completo."
            )
            entrada_nombre.focus()
            return


        # Validación de género
        if genero_seleccionado == "":
            messagebox.showwarning(
                "Dato faltante",
                "Seleccione el género."
            )
            return


        # Validación del menú
        if menu_seleccionado == "Seleccione un menú":
            messagebox.showwarning(
                "Dato faltante",
                "Seleccione un tipo de menú."
            )
            return


        # Validación de sesiones
        if sesiones == "":
            messagebox.showwarning(
                "Dato faltante",
                "Ingrese el número de sesiones."
            )
            entrada_sesiones.focus()
            return


        try:

            numero_sesiones = int(sesiones)

            if numero_sesiones <= 0:

                messagebox.showwarning(
                    "Dato incorrecto",
                    "El número de sesiones debe ser mayor que cero."
                )

                entrada_sesiones.focus()

                return

        except ValueError:

            messagebox.showerror(
                "Error",
                "El número de sesiones debe ser un número entero."
            )

            entrada_sesiones.focus()

            return


        # Obtener precio real
        precio = precios[menu_seleccionado]


        # Crear objeto de la clase GestionClientes
        cliente_guardado = GestionClientes(
            identificacion,
            nombre,
            genero_seleccionado,
            menu_seleccionado,
            numero_sesiones,
            fecha_actual,
            precio
        )


        messagebox.showinfo(
            "Registro guardado",
            "El registro se guardó correctamente."
        )


    # ========================================================
    # FUNCIÓN MOSTRAR REPORTE
    # ========================================================

    def mostrar_reporte():

        global cliente_guardado

        if cliente_guardado is None:

            messagebox.showwarning(
                "Sin registro",
                "Primero debe guardar el registro del cliente."
            )

            return


        # Calcular costo total
        costo_total = cliente_guardado.calcular_costo_total()


        # Crear ventana de reporte
        reporte = tk.Toplevel(registro)

        reporte.title(
            "Reporte del Cliente"
        )

        reporte.geometry(
            "600x600"
        )

        reporte.configure(
            bg="#FFF4E6"
        )


        # ====================================================
        # TÍTULO
        # ====================================================

        tk.Label(
            reporte,
            text="REPORTE DEL CLIENTE",
            font=("Arial", 22, "bold"),
            bg="#FFF4E6",
            fg="#8B4513"
        ).pack(pady=20)


        tk.Label(
            reporte,
            text="SABOR & SAZÓN",
            font=("Arial", 16, "bold"),
            bg="#FFF4E6",
            fg="#8B4513"
        ).pack(pady=5)


        # ====================================================
        # INFORMACIÓN DEL CLIENTE
        # ====================================================

        informacion = (
            f"Identificación: {cliente_guardado.identificacion}\n\n"
            f"Nombre completo: {cliente_guardado.nombre_completo}\n\n"
            f"Género: {cliente_guardado.genero}\n\n"
            f"Tipo de menú: {cliente_guardado.tipo_menu}\n\n"
            f"Número de sesiones: "
            f"{cliente_guardado.numero_sesiones}\n\n"
            f"Fecha de registro: "
            f"{cliente_guardado.fecha_registro}\n\n"
            f"Precio por sesión: "
            f"${cliente_guardado.precio_por_sesion:,.0f}\n\n"
            f"COSTO TOTAL DEL SERVICIO:\n"
            f"${costo_total:,.0f}"
        )


        tk.Label(
            reporte,
            text=informacion,
            font=("Arial", 12),
            bg="#FFF4E6",
            justify="left"
        ).pack(
            pady=20,
            padx=30
        )


        # ====================================================
        # FÓRMULA
        # ====================================================

        formula = (
            f"Fórmula: {cliente_guardado.numero_sesiones} "
            f"sesiones × "
            f"${cliente_guardado.precio_por_sesion:,.0f}"
        )


        tk.Label(
            reporte,
            text=formula,
            font=("Arial", 11, "italic"),
            bg="#FFF4E6"
        ).pack(pady=10)


        # ====================================================
        # BOTÓN CERRAR REPORTE
        # ====================================================

        tk.Button(
            reporte,
            text="CERRAR REPORTE",
            command=reporte.destroy,
            width=25,
            height=2
        ).pack(pady=20)


    # ========================================================
    # FUNCIÓN SALIR
    # ========================================================

    def salir_aplicacion():

        respuesta = messagebox.askyesno(
            "Salir",
            "¿Está seguro de que desea salir de la aplicación?"
        )

        if respuesta:

            registro.destroy()
            ventana.destroy()


    # ========================================================
    # BOTONES
    # ========================================================

    marco_botones = tk.Frame(
        registro,
        bg="#FFF4E6"
    )

    marco_botones.pack(
        pady=20
    )


    # Botón guardar
    boton_guardar = tk.Button(
        marco_botones,
        text="GUARDAR REGISTRO",
        command=guardar_registro,
        width=20,
        height=2
    )

    boton_guardar.grid(
        row=0,
        column=0,
        padx=5,
        pady=5
    )


    # Botón calcular y mostrar reporte
    boton_reporte = tk.Button(
        marco_botones,
        text="CALCULAR / MOSTRAR REPORTE",
        command=mostrar_reporte,
        width=25,
        height=2
    )

    boton_reporte.grid(
        row=0,
        column=1,
        padx=5,
        pady=5
    )


    # Botón salir
    boton_salir = tk.Button(
        marco_botones,
        text="SALIR DE LA APLICACIÓN",
        command=salir_aplicacion,
        width=25,
        height=2
    )

    boton_salir.grid(
        row=1,
        column=0,
        columnspan=2,
        padx=5,
        pady=5
    )


# ============================================================
# VENTANA PRINCIPAL
# ============================================================

ventana = tk.Tk()

ventana.title(
    "Sabor & Sazón"
)

ventana.geometry(
    "600x450"
)

ventana.configure(
    bg="#FFF4E6"
)


# ============================================================
# LOGO / NOMBRE
# ============================================================

logo_principal = tk.Label(
    ventana,
    text="S&S",
    font=("Arial", 35, "bold"),
    bg="#FFF4E6",
    fg="#8B4513"
)

logo_principal.pack(
    pady=(30, 5)
)


# ============================================================
# TÍTULO
# ============================================================

titulo = tk.Label(
    ventana,
    text="SABOR & SAZÓN",
    font=("Arial", 26, "bold"),
    bg="#FFF4E6",
    fg="#8B4513"
)

titulo.pack(
    pady=5
)


# ============================================================
# AUTOR
# ============================================================

autor = tk.Label(
    ventana,
    text="Autor: Job Nuñez",
    font=("Arial", 12),
    bg="#FFF4E6"
)

autor.pack(
    pady=15
)


# ============================================================
# CONTRASEÑA
# ============================================================

texto_contrasena = tk.Label(
    ventana,
    text="Ingrese la contraseña:",
    font=("Arial", 11, "bold"),
    bg="#FFF4E6"
)

texto_contrasena.pack(
    pady=5
)


entrada_contrasena = tk.Entry(
    ventana,
    show="*",
    width=30
)

entrada_contrasena.pack(
    pady=5
)


# ============================================================
# BOTÓN INGRESAR
# ============================================================

boton_ingresar = tk.Button(
    ventana,
    text="INGRESAR",
    command=verificar_contrasena,
    width=20,
    height=2
)

boton_ingresar.pack(
    pady=20
)


# ============================================================
# EJECUTAR APLICACIÓN
# ============================================================

ventana.mainloop()