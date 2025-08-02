# 🔄 Sistema de Keep-Alive para Render

## 📋 Descripción
Este sistema evita que tu aplicación Flask se desactive en Render mediante múltiples estrategias de monitoreo y ping automático.

## 🚀 Características Implementadas

### 1. **Keep-Alive Interno**
- Ping automático cada 5 minutos (configurable)
- Múltiples endpoints de prueba (`/ping`, `/health`, `/`, `/status`)
- Manejo inteligente de errores y reintentos
- Logging detallado para debugging

### 2. **Endpoints de Monitoreo**
- `/health` - Health check completo con verificación de BD
- `/ping` - Ping simple para keep-alive
- `/status` - Status detallado del sistema

### 3. **Monitoreo Externo**
- Script `monitor.py` para servicios externos
- Configuración para UptimeRobot
- GitHub Actions workflow
- Soporte para cron jobs

## ⚙️ Configuración

### Variables de Entorno
```bash
# Habilitar/deshabilitar keep-alive
KEEP_ALIVE_ENABLED=true

# Intervalo en segundos (por defecto: 300 = 5 minutos)
KEEP_ALIVE_INTERVAL=300

# URL específica para keep-alive (opcional)
KEEP_ALIVE_URL=https://tu-app.onrender.com

# Token para cron jobs
CRON_SECRET_TOKEN=mi_token_super_secreto_1234567890
```

### En Render Dashboard
1. Ve a tu servicio en Render
2. En "Environment" agrega:
   ```
   KEEP_ALIVE_ENABLED=true
   KEEP_ALIVE_INTERVAL=300
   ```

## 🔧 Servicios de Monitoreo Externo

### 1. **UptimeRobot** (Recomendado)
- URL: `https://tu-app.onrender.com/health`
- Intervalo: 5 minutos
- Timeout: 30 segundos

### 2. **GitHub Actions**
- Configura el secret `APP_URL` en tu repositorio
- El workflow se ejecuta cada 5 minutos automáticamente

### 3. **Cron Job Local**
```bash
# Agregar a crontab
*/5 * * * * python /path/to/monitor.py https://tu-app.onrender.com
```

### 4. **Script Manual**
```bash
python monitor.py https://tu-app.onrender.com
```

## 📊 Verificación del Sistema

### 1. **Verificar Logs**
En Render Dashboard > Logs, busca:
```
🚀 KEEP-ALIVE: Iniciando con URL: https://tu-app.onrender.com
✅ KEEP-ALIVE: Ping exitoso - /ping - Status: 200
```

### 2. **Probar Endpoints**
```bash
# Health check
curl https://tu-app.onrender.com/health

# Ping simple
curl https://tu-app.onrender.com/ping

# Status detallado
curl https://tu-app.onrender.com/status
```

### 3. **Verificar Variables de Entorno**
```bash
# En Render Dashboard > Environment
KEEP_ALIVE_ENABLED=true
KEEP_ALIVE_INTERVAL=300
```

## 🛠️ Troubleshooting

### Problema: La app sigue durmiendo
**Soluciones:**
1. Verificar que `KEEP_ALIVE_ENABLED=true`
2. Revisar logs en Render Dashboard
3. Configurar monitoreo externo (UptimeRobot)
4. Verificar que los endpoints responden correctamente

### Problema: Errores de conexión
**Soluciones:**
1. Verificar que la URL es correcta
2. Aumentar el timeout en la configuración
3. Revisar si hay problemas de red

### Problema: Logs no aparecen
**Soluciones:**
1. Verificar que el hilo se inició correctamente
2. Revisar que no hay errores en el startup
3. Verificar variables de entorno

## 📈 Métricas de Rendimiento

El sistema incluye métricas automáticas:
- Tiempo de respuesta de endpoints
- Número de fallos consecutivos
- Estado de la base de datos
- Usuarios activos
- Uptime del sistema

## 🔒 Seguridad

- Los endpoints de monitoreo no exponen información sensible
- El token de cron está protegido
- Los logs no incluyen datos privados
- Timeouts configurados para evitar bloqueos

## 📞 Soporte

Si tienes problemas:
1. Revisa los logs en Render Dashboard
2. Verifica la configuración de variables de entorno
3. Prueba los endpoints manualmente
4. Configura monitoreo externo como respaldo

---

**Nota:** Este sistema es especialmente efectivo cuando se combina con monitoreo externo como UptimeRobot. 