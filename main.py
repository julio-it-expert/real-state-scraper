import os
from core.network import fetch_html
from core.parser import extract_properties
from core.pipeline import save_data

# HTML Simulado de un portal de bienes raíces para pruebas unitarias de arquitectura
MOCK_HTML_PORTAL = """
<!DOCTYPE html>
<html>
<head><title>Portal Inmobiliario de Prueba</title></head>
<body>
    <div class="properties-container">
        <!-- Propiedad 1: Completa -->
        <div class="property-card" data-id="RE-2026-001">
            <h2 class="property-title">Espectacular Apartamento Moderno Vista al Mar</h2>
            <span class="property-price">$145,000 USD</span>
            <div class="property-location">La Castellana, Caracas</div>
            <div class="property-features">3 hab | 2 baños | 120 m² de construcción</div>
            <a class="property-link" href="https://ejemplo-inmobiliaria.com/propiedad/RE-2026-001">Ver Detalles</a>
        </div>

        <!-- Propiedad 2: Variación de moneda y faltan baños -->
        <div class="property-card" data-id="RE-2026-002">
            <h2 class="property-title">Penthouse de Lujo Minimalista</h2>
            <span class="property-price">280.000 EUR</span>
            <div class="property-location">Las Mercedes, Caracas</div>
            <div class="property-features">4 habitaciones | 350mt2 construidos</div>
            <a class="property-link" href="https://ejemplo-inmobiliaria.com/propiedad/RE-2026-002">Ver Detalles</a>
        </div>

        <!-- Propiedad 3: Datos corruptos o mínimos (Prueba de robustez try-except) -->
        <div class="property-card">
            <h2 class="property-title">Casa de Campo a Remodelar</h2>
            <span class="property-price">Precio a consultar</span>
            <div class="property-location">El Hatillo</div>
            <div class="property-features">500 m2</div>
        </div>
    </div>
</body>
</html>
"""

def run_pipeline():
    print("=" * 60)
    print("[*] INICIANDO ORQUESTADOR CENTRAL - REAL ESTATE SCRAPER")
    print("=" * 60)
    
    # PASO 1: Simulación del Network Module
    # En producción usaríamos: html = fetch_html("https://portal-realestate.com/ventas")
    print("[1] Ejecutando módulo de red simulado...")
    html_content = MOCK_HTML_PORTAL
    
    if not html_content:
        print("[-] Error: No se obtuvo contenido HTML válido. Abortando.")
        return
        
    # PASO 2: Ejecución del Parser Module
    print("[2] Analizando DOM HTML con BeautifulSoup4 y Regex...")
    properties_extracted = extract_properties(html_content)
    
    print(f"[i] Se identificaron {len(properties_extracted)} estructuras de inmuebles.")
    
    # PASO 3: Ejecución del Data Pipeline con Pandas
    print("[3] Enviando datos al pipeline de exportación (Pandas)...")
    success = save_data(properties_extracted, "reporte_inmobiliario")
    
    if success:
        print("=" * 60)
        print("[+] SPRINT COMPLETADO EXITOSAMENTE: Datos listos para el portafolio.")
        print("=" * 60)
    else:
        print("[-] El pipeline falló en la fase de persistencia.")

if __name__ == "__main__":
    run_pipeline()