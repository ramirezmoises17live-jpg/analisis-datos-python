"""
Script de Análisis de Sentimientos en Redes Sociales
Para principiantes - Análisis básico de comentarios
"""

import pandas as pd
import numpy as np
from collections import Counter
import re

# ============================================
# DATOS DE EJEMPLO (Comentarios simulados)
# ============================================

comentarios = [
    "¡Me encanta este producto! Es increíble 😍",
    "Muy malo, no funciona como esperaba 😠",
    "Es aceptable, nada del otro mundo",
    "¡Excelente servicio! Totalmente recomendado",
    "Horrible experiencia, no lo compren",
    "Bueno, podría mejorar pero está bien",
    "¡Fantástico! Superó mis expectativas",
    "Decepcionante, esperaba más",
    "Normal, es lo que esperaba",
    "¡Perfecto! Volvería a comprar sin dudarlo"
]

# ============================================
# FUNCIÓN: Análisis de Sentimientos Simple
# ============================================

def analizar_sentimiento(texto):
    """
    Clasifica un comentario en: Positivo, Negativo o Neutral
    Usa palabras clave simples
    """
    
    # Convertir a minúsculas
    texto = texto.lower()
    
    # Palabras positivas
    positivas = ['excelente', 'increíble', 'fantástico', 'perfecto', 'bueno', 
                 'encanta', 'recomendado', 'superó', 'amor', 'amor', 'maravilloso']
    
    # Palabras negativas
    negativas = ['malo', 'horrible', 'decepcionante', 'decepción', 'peor', 
                 'no funciona', 'problema', 'error', 'feo', 'terrible']
    
    # Contar palabras positivas y negativas
    positivos_encontrados = sum(1 for palabra in positivas if palabra in texto)
    negativos_encontrados = sum(1 for palabra in negativas if palabra in texto)
    
    # Clasificar
    if positivos_encontrados > negativos_encontrados:
        return "Positivo"
    elif negativos_encontrados > positivos_encontrados:
        return "Negativo"
    else:
        return "Neutral"

# ============================================
# FUNCIÓN: Análisis de Frecuencia de Palabras
# ============================================

def obtener_palabras_frecuentes(texto_lista, top=5):
    """
    Obtiene las palabras más frecuentes en los comentarios
    """
    # Combinar todos los textos
    todo_texto = ' '.join(texto_lista).lower()
    
    # Remover caracteres especiales y emojis
    texto_limpio = re.sub(r'[^a-záéíóú\s]', '', todo_texto)
    
    # Palabras comunes a ignorar
    stop_words = {'es', 'de', 'la', 'el', 'y', 'que', 'un', 'una', 'los', 'las'}
    
    # Dividir en palabras y filtrar
    palabras = [p for p in texto_limpio.split() if p not in stop_words and len(p) > 3]
    
    # Contar frecuencias
    frecuencias = Counter(palabras)
    
    return frecuencias.most_common(top)

# ============================================
# FUNCIÓN: Crear DataFrame con Análisis
# ============================================

def crear_dataframe_analisis(comentarios):
    """
    Crea un DataFrame con el análisis completo
    """
    datos = []
    
    for i, comentario in enumerate(comentarios, 1):
        sentimiento = analizar_sentimiento(comentario)
        largo = len(comentario)
        
        datos.append({
            'ID': i,
            'Comentario': comentario,
            'Sentimiento': sentimiento,
            'Largo': largo
        })
    
    return pd.DataFrame(datos)

# ============================================
# MAIN: Ejecutar Análisis
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("ANÁLISIS DE SENTIMIENTOS EN REDES SOCIALES")
    print("=" * 60)
    print()
    
    # 1. Crear DataFrame
    df = crear_dataframe_analisis(comentarios)
    
    # 2. Mostrar datos
    print("📊 DATOS ANALIZADOS:")
    print(df.to_string(index=False))
    print()
    
    # 3. Estadísticas de Sentimientos
    print("📈 ESTADÍSTICAS DE SENTIMIENTOS:")
    print("-" * 40)
    conteos = df['Sentimiento'].value_counts()
    for sentimiento, cantidad in conteos.items():
        porcentaje = (cantidad / len(df)) * 100
        print(f"  {sentimiento}: {cantidad} comentarios ({porcentaje:.1f}%)")
    print()
    
    # 4. Palabras más frecuentes
    print("🔤 PALABRAS MÁS FRECUENTES:")
    print("-" * 40)
    palabras_top = obtener_palabras_frecuentes(comentarios, top=5)
    for palabra, freq in palabras_top:
        print(f"  '{palabra}': {freq} veces")
    print()
    
    # 5. Estadísticas de largo de comentarios
    print("📏 ESTADÍSTICAS DE COMENTARIOS:")
    print("-" * 40)
    print(f"  Promedio de caracteres: {df['Largo'].mean():.1f}")
    print(f"  Máximo: {df['Largo'].max()}")
    print(f"  Mínimo: {df['Largo'].min()}")
    print()
    
    print("✅ Análisis completado!")
