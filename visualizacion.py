"""
Script Adicional: Análisis Avanzado con Visualización
Para ver gráficos de los datos
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from analisis_sentimientos import (
    crear_dataframe_analisis, 
    obtener_palabras_frecuentes,
    comentarios
)

# Configurar estilo
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

def crear_visualizaciones(df):
    """
    Crea gráficos para visualizar el análisis
    """
    
    # Crear figura con 2 subplots
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Gráfico 1: Distribución de Sentimientos (Pie Chart)
    sentimientos = df['Sentimiento'].value_counts()
    colores = ['#2ecc71', '#e74c3c', '#95a5a6']  # Verde, Rojo, Gris
    
    axes[0].pie(sentimientos.values, 
                labels=sentimientos.index, 
                autopct='%1.1f%%',
                colors=colores,
                startangle=90,
                textprops={'fontsize': 12, 'weight': 'bold'})
    axes[0].set_title('Distribución de Sentimientos', fontsize=14, weight='bold')
    
    # Gráfico 2: Conteo de Sentimientos (Bar Chart)
    sentimientos.plot(kind='bar', ax=axes[1], color=colores, edgecolor='black')
    axes[1].set_title('Cantidad de Comentarios por Sentimiento', fontsize=14, weight='bold')
    axes[1].set_xlabel('Sentimiento', fontsize=12)
    axes[1].set_ylabel('Cantidad', fontsize=12)
    axes[1].set_xticklabels(axes[1].get_xticklabels(), rotation=45)
    axes[1].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('analisis_sentimientos.png', dpi=300, bbox_inches='tight')
    print("✅ Gráfico guardado como 'analisis_sentimientos.png'")
    plt.show()

def crear_grafico_palabras(comentarios, top=10):
    """
    Crea un gráfico de palabras más frecuentes
    """
    palabras_top = obtener_palabras_frecuentes(comentarios, top=top)
    
    if not palabras_top:
        print("No hay palabras para graficar")
        return
    
    palabras, frecuencias = zip(*palabras_top)
    
    plt.figure(figsize=(12, 6))
    plt.barh(palabras, frecuencias, color='#3498db', edgecolor='black')
    plt.xlabel('Frecuencia', fontsize=12, weight='bold')
    plt.ylabel('Palabras', fontsize=12, weight='bold')
    plt.title('Palabras Más Frecuentes en Comentarios', fontsize=14, weight='bold')
    plt.tight_layout()
    plt.savefig('palabras_frecuentes.png', dpi=300, bbox_inches='tight')
    print("✅ Gráfico guardado como 'palabras_frecuentes.png'")
    plt.show()

if __name__ == "__main__":
    print("=" * 60)
    print("VISUALIZACIÓN DE ANÁLISIS DE SENTIMIENTOS")
    print("=" * 60)
    print()
    
    # Crear DataFrame
    df = crear_dataframe_analisis(comentarios)
    
    # Crear visualizaciones
    print("📊 Generando gráficos...")
    crear_visualizaciones(df)
    print()
    
    print("📈 Generando gráfico de palabras...")
    crear_grafico_palabras(comentarios, top=8)
    print()
    
    print("✅ ¡Visualizaciones completadas!")
