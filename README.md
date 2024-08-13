# Calculadora de Zona de Fresnel

Esta es una aplicación en Python que calcula el radio de la zona de Fresnel en función de la distancia y la frecuencia proporcionadas por el usuario. La aplicación está diseñada con una interfaz simple y fácil de usar utilizando `tkinter` y `ttk`.

## Explicación del Gráfico y la Zona de Fresnel

### ¿Qué es la Zona de Fresnel?

La zona de Fresnel es una región elipsoidal en el espacio alrededor de la línea de visión directa entre una antena transmisora y una antena receptora. Esta zona es crucial en los sistemas de comunicación inalámbrica, ya que cualquier obstrucción dentro de esta área puede afectar la calidad de la señal. La zona de Fresnel está compuesta por varias zonas, siendo la primera la más importante, ya que es donde la señal es más fuerte.

La fórmula para calcular el radio de la primera zona de Fresnel es:

![Texto alternativo](data:image/png;base64,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)

Donde:

- \( D \) es la distancia en km entre antenas
- \( f \) es la frecuencia en GHz de la señal transmitida

## Características

- **Conversión de Unidades:** Elige entre diferentes unidades para la distancia (metros, kilómetros, millas) y la frecuencia (GHz, MHz, kHz).
- **Interfaz:** La interfaz está construida usando `tkinter` y estilizada con `ttk` para un aspecto moderno.

### Explicación del Gráfico

El gráfico generado por la aplicación representa la zona de Fresnel como una elipse alargada entre las dos antenas. La línea central representa la línea de visión directa (LoS), y la región sombreada indica el área de la primera zona de Fresnel. Si existe alguna obstrucción dentro de esta zona sombreada, puede interferir con la señal y degradar la calidad de la comunicación.

Este gráfico es útil para visualizar cómo la zona de Fresnel varía en función de la distancia entre las antenas y la frecuencia utilizada, lo que ayuda en la planificación y optimización de sistemas de comunicación inalámbrica.

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
│   ├── design.py           # Configuración de estilo y temas
│
├── README.md               # Documentación del proyecto
└── requirements.txt        # Dependencias del proyecto
```
