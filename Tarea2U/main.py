import tkinter as tk
from tkinter import messagebox

class GestionClientes:
    def __init__(self,identificacion, nombre_completo, genero, tipo_menu, numero_sesiones, fecha_registro,precio_por_sesion):
        self.identificacion = identificacion
        self.nombre_completo = nombre_completo
        self.genero = genero
        self.tipo_menu = tipo_menu
        self.numero_sesiones = numero_sesiones
        self.fecha_registro = fecha_registro
        self.precio_por_sesion = precio_por_sesion

    def calcular_costo_total(self):
        return self.numero_sesiones * self.precio_por_sesion

def verificar_contrasena():
    contrasena = entrada_contrasena.get()

    if contrasena == "1793":
        ventana.withdraw()
        ventana_registro()

    else:
        messagebox.showerror("Error", "Contraseña incorrecta")

def ventana_registro():

    registro = tk.Toplevel(ventana)

    registro.title("Registro de Cliente")
    registro.geometry("600x500")

    titulo = tk.Label(
        registro,
        text="REGISTRO DE CLIENTE",
        font=("Arial", 20, "bold")
    )
    titulo.pack(pady=20)

    # Identificación
    tk.Label(registro, text="Identificación:").pack()
    entrada_identificacion = tk.Entry(registro)
    entrada_identificacion.pack(pady=5)

    # Nombre completo
    tk.Label(registro, text="Nombre completo:").pack()
    entrada_nombre = tk.Entry(registro)
    entrada_nombre.pack(pady=5)

    # Género
    tk.Label(registro, text="Género:").pack()

    genero = tk.StringVar()

    tk.Radiobutton(
        registro,
        text="Masculino",
        variable=genero,
        value="Masculino"
    ).pack()

    tk.Radiobutton(
        registro,
        text="Femenino",
        variable=genero,
        value="Femenino"
    ).pack()

    # Tipo de menú
    tk.Label(registro, text="Tipo de menú:").pack(pady=5)

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

    menu.pack()

    # Número de sesiones
    tk.Label(registro, text="Número de sesiones:").pack(pady=5)

    entrada_sesiones = tk.Entry(registro)
    entrada_sesiones.pack()

    # Fecha
    tk.Label(
        registro,
        text="Fecha de registro: Automática"
    ).pack(pady=10)


ventana = tk.Tk()

ventana.title("Sabor & Sazón")
ventana.geometry("600x400")


titulo = tk.Label(
    ventana,
    text="SABOR & SAZÓN",
    font=("Arial", 24, "bold")
)

titulo.pack(pady=30)


# Nombre del autor

autor = tk.Label(
    ventana,
    text="Autor: JOB NUÑEZ",
    font=("Arial", 12)
)

autor.pack(pady=10)


# Texto contraseña

texto_contrasena = tk.Label(
    ventana,
    text="Ingrese la contraseña:"
)

texto_contrasena.pack(pady=5)


# Campo contraseña

entrada_contrasena = tk.Entry(
    ventana,
    show="*",
    width=25
)

entrada_contrasena.pack(pady=5)


# Botón ingresar

boton_ingresar = tk.Button(
    ventana,
    text="INGRESAR",
    command=verificar_contrasena
)

boton_ingresar.pack(pady=20)


ventana.mainloop()