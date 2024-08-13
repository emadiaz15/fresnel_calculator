import tkinter as tk  # Importa el módulo tkinter para crear la interfaz gráfica
from tkinter import ttk  # Importa ttk, que es una versión mejorada de los widgets de tkinter

def apply_theme(root):
    """
    Aplica un tema personalizado a la aplicación.
    """
    style = ttk.Style(root)  # Crea un objeto Style que permite configurar estilos para widgets
    
    # Establece el tema a 'clam', 'alt', 'default', o 'classic'
    style.theme_use('clam')
    
    # Configura un estilo personalizado para el widget TLabel
    style.configure('TLabel', font=('Helvetica', 12), foreground='blue')
    
    # Configura un estilo personalizado para el widget TButton
    style.configure('TButton', font=('Helvetica', 12), background='lightblue')
    
    # Se pueden añadir configuraciones de estilo adicionales aquí
