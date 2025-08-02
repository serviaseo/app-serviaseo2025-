#!/usr/bin/env python3
"""
Script de prueba para verificar el sistema de keep-alive
"""

import requests
import sys
from datetime import datetime

def test_endpoints(app_url):
    """Prueba todos los endpoints de monitoreo"""
    endpoints = [
        ('/ping', 'Ping simple'),
        ('/health', 'Health check'),
        ('/status', 'Status detallado'),
        ('/', 'Página principal')
    ]
    
    print(f"🔍 Probando endpoints de: {app_url}")
    print(f"⏰ Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    
    all_success = True
    
    for endpoint, description in endpoints:
        try:
            url = f"{app_url}{endpoint}"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                print(f"✅ {description}: OK (Status: {response.status_code})")
                
                # Mostrar respuesta para endpoints JSON
                if endpoint in ['/ping', '/health', '/status']:
                    try:
                        data = response.json()
                        if endpoint == '/health':
                            print(f"   📊 Status: {data.get('status', 'unknown')}")
                        elif endpoint == '/status':
                            print(f"   📊 Keep-alive: {data.get('system_stats', {}).get('keep_alive', 'unknown')}")
                    except:
                        pass
            else:
                print(f"❌ {description}: FAILED (Status: {response.status_code})")
                all_success = False
                
        except requests.exceptions.RequestException as e:
            print(f"❌ {description}: ERROR - {str(e)}")
            all_success = False
    
    print("-" * 50)
    
    if all_success:
        print("🎉 TODOS LOS ENDPOINTS FUNCIONAN CORRECTAMENTE")
        print("✅ Tu aplicación está activa y el sistema de keep-alive está operativo")
        return True
    else:
        print("⚠️  ALGUNOS ENDPOINTS FALLARON")
        print("🔧 Revisa la configuración de tu aplicación")
        return False

def main():
    # Obtener URL desde argumento o usar por defecto
    if len(sys.argv) > 1:
        app_url = sys.argv[1]
    else:
        app_url = "https://tu-app.onrender.com"  # Cambia por tu URL real
    
    # Asegurar que la URL termine correctamente
    if not app_url.endswith('/'):
        app_url = app_url.rstrip('/')
    
    print("🚀 SISTEMA DE VERIFICACIÓN DE KEEP-ALIVE")
    print("=" * 50)
    
    success = test_endpoints(app_url)
    
    if success:
        print("\n📋 PRÓXIMOS PASOS:")
        print("1. ✅ El sistema interno está funcionando")
        print("2. 🔧 Configura monitoreo externo (UptimeRobot)")
        print("3. 📊 Revisa logs en Render Dashboard")
        print("4. 🔄 La aplicación debería mantenerse activa")
    else:
        print("\n🔧 ACCIONES REQUERIDAS:")
        print("1. Verifica que la aplicación esté desplegada")
        print("2. Revisa las variables de entorno en Render")
        print("3. Verifica los logs en Render Dashboard")
        print("4. Asegúrate de que KEEP_ALIVE_ENABLED=true")
    
    print("\n" + "=" * 50)

if __name__ == "__main__":
    main() 