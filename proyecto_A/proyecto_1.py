# Definimos la función
def calcular_promedio(lista_numeros):
    """
    Calcula el promedio de una lista de números.
    """
    if not lista_numeros:  # Verifica que la lista no esté vacía
        return "La lista está vacía"
    
    promedio = sum(lista_numeros) / len(lista_numeros)
    return promedio

# Ejemplo de uso:
numeros = [10, 20, 30, 40, 50]
resultado = calcular_promedio(numeros)

print(f"El promedio de {numeros} es: {resultado}")
