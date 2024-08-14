import math  # Importa la libreria matemática estándar de Python

def calculate_fresnel_zone(distance, frequency):
    # Calcula el radio de la zona de Fresnel utilizando la fórmula dada
    # La fórmula utilizada es una aproximación común para la zona de Fresnel:
    # R = 17.32 * sqrt((d / 1000) / (4 * f))
    # Donde:
    # - R es el radio de la zona de Fresnel en metros.
    # - d es la distancia entre las antenas en metros.
    # - f es la frecuencia en GHz.
    return 8.656 * (math.sqrt(float(distance) / float(frequency)))
