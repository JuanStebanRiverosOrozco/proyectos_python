import pandas as pd

def estadisticas_columna(df, columna):
    """
    Recibe un DataFrame y el nombre de una columna numérica.
    Devuelve un DataFrame con las estadísticas: media, mediana y desviación estándar.
    """
    if columna not in df.columns:
        return f"La columna '{columna}' no existe en el DataFrame."
    
    # Asegurar que pandas maneje bien los datos numéricos
    serie = pd.to_numeric(df[columna], errors='coerce')
    
    resumen = {
        'media': [serie.mean()],
        'mediana': [serie.median()],
        'desviacion_estandar': [serie.std()]
    }
    
    return pd.DataFrame(resumen)


# Ejemplo de uso:
df = pd.DataFrame({
    'Nombre': ['Ana', 'Luis', 'María', 'Carlos'],
    'Edad': [23, 35, 29, 41]
})

resultado = estadisticas_columna(df, 'Edad')
print(resultado)
