import tkinter as tk  # Importa el módulo tkinter para la creación de la interfaz gráfica
from tkinter import ttk  # Importa ttk para widgets con estilos mejorados
from fresnel.calculator import calculate_fresnel_zone  # Importa la función para calcular la zona de Fresnel
from fresnel.utils import validate_input  # Importa la función para validar las entradas del usuario

class FresnelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fresnel Zone Calculator")  # Establece el título de la ventana
        self.root.geometry("400x350")  # Establece las dimensiones de la ventana
        # Configuración de estilos para los widgets
        style = ttk.Style()
        style.configure('TLabel', font=('Arial', 12))
        style.configure('TButton', font=('Arial', 12))
        style.configure('TEntry', font=('Arial', 12))
        style.configure('TOptionMenu', font=('Arial', 12))

        # Marco para la distancia
        distance_frame = ttk.Frame(root)
        distance_frame.pack(pady=10)  # Añade espacio vertical alrededor del marco

        # Etiqueta y campo de entrada para la distancia
        self.distance_label = ttk.Label(distance_frame, text="Distance:")
        self.distance_label.grid(row=0, column=0, padx=5)
        self.distance_entry = ttk.Entry(distance_frame)
        self.distance_entry.grid(row=0, column=1, padx=5)

        # Menú desplegable para la unidad de distancia
        self.distance_unit = tk.StringVar(value="m")  # Valor por defecto en metros
        self.distance_unit_menu = ttk.OptionMenu(distance_frame, self.distance_unit, "m", "m", "km", "mi")
        self.distance_unit_menu.grid(row=0, column=2, padx=5)

        # Marco para la frecuencia
        frequency_frame = ttk.Frame(root)
        frequency_frame.pack(pady=10)

        # Etiqueta y campo de entrada para la frecuencia
        self.frequency_label = ttk.Label(frequency_frame, text="Frequency:")
        self.frequency_label.grid(row=0, column=0, padx=5)
        self.frequency_entry = ttk.Entry(frequency_frame)
        self.frequency_entry.grid(row=0, column=1, padx=5)

        # Menú desplegable para la unidad de frecuencia
        self.frequency_unit = tk.StringVar(value="GHz")  # Valor por defecto en GHz
        self.frequency_unit_menu = ttk.OptionMenu(frequency_frame, self.frequency_unit, "GHz", "GHz", "MHz", "kHz")
        self.frequency_unit_menu.grid(row=0, column=2, padx=5)

        # Etiqueta para mostrar el resultado
        self.result_label = ttk.Label(root, text="")
        self.result_label.pack(pady=20)

        # Botón para calcular la zona de Fresnel
        self.calculate_button = ttk.Button(root, text="Calculate", command=self.calculate)
        self.calculate_button.pack()
        
        self.footer = ttk.Label(root, text="Create by Emanuel Diaz")
        self.footer.pack(pady=20)
        
    def calculate(self):
        try:
            # Validar y convertir la entrada de distancia
            distance = validate_input(self.distance_entry.get())
            frequency = validate_input(self.frequency_entry.get())

            # Calcular el radio de la zona de Fresnel
            result = calculate_fresnel_zone(distance, frequency)
            # Mostrar el resultado en la etiqueta
            self.result_label.config(text=f"Fresnel Zone Radius: {result} meters")
        except ValueError as e:
            # Mostrar el mensaje de error si la validación falla
            self.result_label.config(text=str(e))

if __name__ == "__main__":
    root = tk.Tk()  # Crear la ventana principal de la aplicación
    app = FresnelApp(root)  # Crear una instancia de la aplicación FresnelApp
    root.mainloop()  # Iniciar el bucle principal de la interfaz gráfica
