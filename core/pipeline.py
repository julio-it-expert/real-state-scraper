import os
import pandas as pd
from typing import List, Dict, Any

def save_data(data: List[Dict[str, Any]], filename_base: str) -> bool:
    """
    Recibe un listado de propiedades, lo transforma en un DataFrame de Pandas
    y lo exporta de manera eficiente a formatos CSV y Excel respetando los tipos de datos.
    """
    if not data:
        print("[!] Advertencia: No hay datos disponibles para exportar.")
        return False
        
    output_dir = "data"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    try:
        # Cargamos los datos crudos en un DataFrame estructurado de Pandas
        df = pd.DataFrame(data)
        
        # Corrección de Ingeniería: En lugar de usar un fillna global que rompe tipos numéricos,
        # limpiamos los nulos de texto y numéricos por separado de forma segura.
        
        # Para las columnas de texto que tengan None, ponemos "N/A"
        text_cols = ['property_id', 'title', 'price_currency', 'location', 'source_url']
        for col in text_cols:
            if col in df.columns:
                df[col] = df[col].fillna("N/A")
                
        # Para las columnas numéricas que tengan None, ponemos un valor neutro (0 o 0.0)
        num_cols = ['price_amount', 'area_m2', 'rooms', 'bathrooms']
        for col in num_cols:
            if col in df.columns:
                df[col] = df[col].fillna(0)
        
        # Definimos las rutas de salida
        csv_path = os.path.join(output_dir, f"{filename_base}.csv")
        excel_path = os.path.join(output_dir, f"{filename_base}.xlsx")
        
        # Exportación con Pandas
        df.to_csv(csv_path, index=False, encoding='utf-8')
        df.to_excel(excel_path, index=False)
        
        print(f"[+] Éxito (Pandas Pipeline):")
        print(f"    -> CSV generado en: {csv_path}")
        print(f"    -> Excel generado en: {excel_path}")
        print(f"    Registros totales procesados: {len(df)}")
        return True
        
    except Exception as e:
        print(f"[-] Error crítico en el pipeline de Pandas al exportar datos: {e}")
        return False