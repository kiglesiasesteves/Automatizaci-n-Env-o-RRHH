#!/bin/bash
# Script wrapper para ejecutar el envío de emails desde crontab
# Este script asegura que el entorno esté configurado correctamente

# Configurar directorio de trabajo
cd "$(dirname "$0")"

# Log file para registrar ejecuciones
LOG_FILE="logs/cron_email_$(date +%Y%m%d_%H%M%S).log"

# Crear directorio de logs si no existe
mkdir -p logs

# Función para logging
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

log "=== Iniciando envío automático de emails RRHH ==="

# Verificar que Python3 esté disponible
if ! command -v python3 &> /dev/null; then
    log "ERROR: python3 no está instalado"
    exit 1
fi

# Verificar que el archivo .env existe
if [ ! -f ".env" ]; then
    log "ERROR: Archivo .env no encontrado. Configurar credenciales SMTP."
    exit 1
fi

# Verificar que el script principal existe
if [ ! -f "src/email_sender.py" ]; then
    log "ERROR: Script src/email_sender.py no encontrado"
    exit 1
fi

# Ejecutar el script principal
log "Ejecutando envío de emails..."
python3 src/email_sender.py >> "$LOG_FILE" 2>&1

# Verificar resultado
if [ $? -eq 0 ]; then
    log "✅ Envío de emails completado exitosamente"
else
    log "❌ Error en el envío de emails"
fi

log "=== Finalizando envío automático ==="

# Limpiar logs antiguos (mantener solo los últimos 10 archivos)
cd logs
ls -t cron_email_*.log | tail -n +11 | xargs -r rm
cd ..

log "Log guardado en: $LOG_FILE"
