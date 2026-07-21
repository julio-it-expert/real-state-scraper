import re
from bs4 import BeautifulSoup
from typing import List, Dict, Any

def extract_properties(html_content: str) -> List[Dict[str, Any]]:
    """
    Analiza el contenido HTML y extrae un listado de propiedades estructuradas.
    Retorna una lista de diccionarios siguiendo el diccionario de datos.
    """
    properties_list = []
    
    if not html_content:
        return properties_list
        
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Buscamos los bloques contenedores de cada inmueble
    # Usamos una clase genérica estándar simulando un portal inmobiliario
    cards = soup.find_all('div', class_='property-card')
    
    for card in cards:
        data = {}
        
        # 1. Identificador de la Propiedad (ID)
        try:
            data['property_id'] = card.get('data-id', 'N/A')
        except Exception:
            data['property_id'] = 'N/A'
            
        # 2. Título Comercial
        try:
            title_el = card.find('h2', class_='property-title')
            data['title'] = title_el.get_text(strip=True) if title_el else 'Sin Título'
        except Exception:
            data['title'] = 'Sin Título'
            
        # 3. Precio (Monto y Moneda)
        try:
            price_el = card.find('span', class_='property-price')
            if price_el:
                price_text = price_el.get_text(strip=True)
                # Extraemos la moneda (ej: USD o EUR)
                data['price_currency'] = 'USD' if 'USD' in price_text or '$' in price_text else 'EUR'
                # Limpiamos el texto para dejar solo el valor numérico
                clean_price = re.sub(r'[^\d.]', '', price_text.replace(',', '.'))
                data['price_amount'] = float(clean_price) if clean_price else 0.0
            else:
                data['price_currency'] = 'N/A'
                data['price_amount'] = 0.0
        except Exception:
            data['price_currency'] = 'N/A'
            data['price_amount'] = 0.0
            
        # 4. Ubicación Geográfica
        try:
            loc_el = card.find('div', class_='property-location')
            data['location'] = loc_el.get_text(strip=True) if loc_el else 'No Especificada'
        except Exception:
            data['location'] = 'No Especificada'
            
        # 5. Métricas Físicas: Área (m²), Habitaciones y Baños
        # Simulamos que vienen dentro de una lista de características (features)
        try:
            features_text = card.get_text()
            
            # Buscamos patrones numéricos usando expresiones regulares
            area_match = re.search(r'(\d+)\s*(m²|m2|mt2)', features_text, re.IGNORECASE)
            data['area_m2'] = int(area_match.group(1)) if area_match else None
            
            rooms_match = re.search(r'(\d+)\s*(hab|habi|room|cuarto)', features_text, re.IGNORECASE)
            data['rooms'] = int(rooms_match.group(1)) if rooms_match else None
            
            baths_match = re.search(r'(\d+)\s*(baño|bano|bath)', features_text, re.IGNORECASE)
            data['bathrooms'] = int(baths_match.group(1)) if baths_match else None
            
        except Exception:
            data['area_m2'] = None
            data['rooms'] = None
            data['bathrooms'] = None
            
        # 6. URL Fuente de Auditoría
        try:
            link_el = card.find('a', class_='property-link')
            data['source_url'] = link_el.get('href', 'N/A') if link_el else 'N/A'
        except Exception:
            data['source_url'] = 'N/A'
            
        properties_list.append(data)
        
    return properties_list