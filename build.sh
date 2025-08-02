#!/bin/bash
echo "🚀 Iniciando construcción de la aplicación..."

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno para keep-alive
export KEEP_ALIVE_ENABLED=true
export KEEP_ALIVE_INTERVAL=300

echo "✅ Construcción completada"