import time
import random
import requests

# Database of real user-agents for rotation and to mitigate blocks (Anti-Scraping)
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
]

def fetch_html(url: str, max_retries: int = 3) -> str:
    """
    Performs a secure HTTP GET request to a specific URL.
    Implements header rotation, dynamic delays, and exception handling.
    """
    headers = {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept-Language": "es-ES,es;q=0.9,en;q=0.8",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Connection": "keep-alive"
    }
    
    # Controlled dynamic delay t_delay ∈ [1.5, 3.5] seconds (Human Behavior)
    time.sleep(random.uniform(1.5, 3.5))
    
    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers, timeout=15)
            
            # Si el servidor responde con códigos 4xx o 5xx, lanza una excepción
            response.raise_for_status()
            
            return response.text
            
        except requests.exceptions.RequestException as e:
            print(f"[!] Error de red en intento {attempt + 1}/{max_retries} para {url}: {e}")
            if attempt < max_retries - 1:
                time.sleep(5)  # Espera un poco más antes de reintentar si falló
            else:
                print(f"[-] Error crítico: Se agotaron los intentos de conexión para {url}")
                return ""