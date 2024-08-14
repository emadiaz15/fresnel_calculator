def validate_input(value):
    # Valida que la entrada sea un número
    try:
        # Intenta convertir el valor de entrada a un número real
        return float(value.replace(",","."))
    except ValueError:
        # Si la conversión falla, lanza un error indicando que la entrada no es válida
        raise ValueError("Entrada no válida, debe ser un número.")
