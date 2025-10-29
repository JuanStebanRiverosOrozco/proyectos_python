import pandas as pd

def crear_dataframe():
    """
    Crea un DataFrame de ejemplo con nombres, edades y ciudades.
    """
    datos = {
        'Nombre': ['Ana', 'Luis', 'María', 'Carlos'],
        'Edad': [23, 35, 29, 41],
        'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia']
    }
    df = pd.DataFrame(datos)
    return df

# Ejemplo de uso
print(crear_dataframe())
