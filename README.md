# Calculadora de Zona de Fresnel

Esta es una aplicación en Python que calcula el radio de la zona de Fresnel en función de la distancia y la frecuencia proporcionadas por el usuario. La aplicación está diseñada con una interfaz simple y fácil de usar utilizando `tkinter` y `ttk`.

## Explicación del Gráfico y la Zona de Fresnel

### ¿Qué es la Zona de Fresnel?

La zona de Fresnel es una región elipsoidal en el espacio alrededor de la línea de visión directa entre una antena transmisora y una antena receptora. Esta zona es crucial en los sistemas de comunicación inalámbrica, ya que cualquier obstrucción dentro de esta área puede afectar la calidad de la señal. La zona de Fresnel está compuesta por varias zonas, siendo la primera la más importante, ya que es donde la señal es más fuerte.

La fórmula para calcular el radio de la primera zona de Fresnel es:

![Texto alternativo](https://www.prored.es/wp-content/uploads/2018/08/prored-formula-zona-primera-de-fresnel-en-metros-v2.png)

Donde:

- \( D \) es la distancia en km entre antenas
- \( f \) es la frecuencia en GHz de la señal transmitida

## Características

- **Conversión de Unidades:** Elige entre diferentes unidades para la distancia (metros, kilómetros, millas) y la frecuencia (GHz, MHz, kHz).
- **Interfaz:** La interfaz está construida usando `tkinter` y estilizada con `ttk` para un aspecto moderno.

## Instalación

1. **Clonar el Repositorio:**

   ```bash
   git clone https://github.com/tuusuario/fresnel_calculator.git
   cd fresnel_calculator
   ```

2. **Instalar Dependencias:**

   Asegúrate de tener Python 3 instalado y luego instala las dependencias requeridas:

   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar la Aplicación:**

   ```bash
   python3 main.py
   ```

## Uso

- **Distancia:** Ingresa la distancia en metros, kilómetros o millas.
- **Frecuencia:** Ingresa la frecuencia en GHz, MHz o kHz.
- **Calcular:** Haz clic en el botón "Calcular" para calcular el radio de la zona de Fresnel, que se mostrará en metros.

## Estructura del Proyecto

```plaintext
fresnel_calculator/
│
├── main.py                 # Punto de entrada principal para la aplicación
├── fresnel/
│   ├── __init__.py         # Inicializador del paquete
│   ├── calculator.py       # Lógica de cálculo para la zona de Fresnel
│   └── utils.py            # Funciones auxiliares para la validación de entradas
│
├── gui/
│   ├── __init__.py         # Inicializador del paquete
│   ├── interface.py        # Lógica y diseño de la interfaz gráfica
│   └── design.py           # Configuración de estilo y temas
│
├── README.md               # Documentación del proyecto
└── requirements.txt        # Dependencias del proyecto
```
