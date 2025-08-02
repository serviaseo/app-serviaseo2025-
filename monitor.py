#!/usr/bin/env python3
"""
Script de monitoreo externo para mantener la aplicación activa en Render
Este script puede ejecutarse desde un servicio externo como UptimeRobot o cron
"""

import requests
import time
import os
import sys
from datetime import datetime

def ping_app(url):
    """Hace ping a la aplicación y verifica su estado"""
    try:
        # Intentar health check primero
        health_url = f"{url}/health"
        response = requests.get(health_url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Health check exitoso: {data.get('status', 'unknown')}")
            return True
        else:
            print(f"⚠️  Health check falló: Status {response.status_code}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error de conexión: {e}")
        return False

def main():
    # Obtener URL de la aplicación desde variable de entorno o argumento
    app_url = os.environ.get('APP_URL')
    
    if not app_url:
        if len(sys.argv) > 1:
            app_url = sys.argv[1]
        else:
            print("❌ Error: Debes especificar la URL de la aplicación")
            print("Uso: python monitor.py <URL_DE_LA_APP>")
            print("O configura la variable de entorno APP_URL")
            sys.exit(1)
    
    # Asegurar que la URL termine correctamente
    if not app_url.endswith('/'):
        app_url = app_url.rstrip('/')
    
    print(f"🚀 Iniciando monitoreo de: {app_url}")
    print(f"⏰ Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Hacer ping
    success = ping_app(app_url)
    
    if success:
        print("✅ Aplicación está activa y funcionando")
        sys.exit(0)
    else:
        print("❌ Aplicación no responde correctamente")
        sys.exit(1)

if __name__ == "__main__":
    main() 