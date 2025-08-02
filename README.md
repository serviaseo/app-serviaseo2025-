# Sistema de Gestión de Planillas - Grupo Servis Aseo S.L

## Descripción
Sistema web para la gestión de planillas de control de servicios de aseo para Salud Casanare y Laboratorio, desarrollado con Flask.

## Características
- Gestión de usuarios y autenticación
- Planillas de control por mes y año
- Descarga de documentos en múltiples formatos (Excel, PDF, Word)
- Panel de administración
- Usuarios temporales con códigos QR
- Sistema de tareas y actividades

## Despliegue en Render

### Configuración Actual
- **Python**: 3.10.13 (compatible con pandas y numpy)
- **Framework**: Flask 2.3.3
- **Servidor**: Gunicorn
- **Base de datos**: SQLite

### Archivos de Configuración
- `runtime.txt`: Especifica Python 3.10.13
- `requirements.txt`: Dependencias con versiones compatibles
- `build.sh`: Script de construcción optimizado
- `render.yaml`: Configuración de Render
- `Procfile`: Comando de inicio para Gunicorn

### Pasos para Desplegar
1. Conectar el repositorio a Render
2. Crear un nuevo Web Service
3. Render detectará automáticamente la configuración
4. El build se ejecutará automáticamente
5. La aplicación estará disponible en la URL proporcionada

### Usuarios por Defecto
- **admin**: admin123
- **root**: aseo2025slclabor
- **julio**: julio21200521A

## Desarrollo Local

### Instalación
```bash
# Crear entorno virtual
python -m venv entorno8080

# Activar entorno (Windows)
entorno8080\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
python app.py
```

### Variables de Entorno
- `FLASK_ENV`: development (para debug local)
- `PORT`: 5000 (puerto por defecto)

## Estructura del Proyecto
```
├── app.py                 # Aplicación principal
├── requirements.txt       # Dependencias
├── runtime.txt           # Versión de Python
├── build.sh              # Script de construcción
├── render.yaml           # Configuración de Render
├── Procfile              # Comando de inicio
├── templates/            # Plantillas HTML
├── static/               # Archivos estáticos
└── uploads/              # Archivos subidos
```

## Notas Importantes
- La aplicación usa Python 3.10.13 para compatibilidad con pandas y numpy
- El modo debug está desactivado en producción
- Se incluye un sistema de keep-alive para evitar que Render duerma la aplicación
- Los usuarios temporales se limpian automáticamente

## Soporte
Para problemas técnicos, contactar al administrador del sistema.
