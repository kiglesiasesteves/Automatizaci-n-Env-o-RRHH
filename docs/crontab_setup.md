# 📅 Configuración de Crontab - Envío Automático

## 🕐 Programación Automática de Emails

Esta guía te ayuda a configurar el sistema para que envíe automáticamente recordatorios de vacaciones cada 3 meses.

### 📋 Configuraciones de Crontab Recomendadas

#### Cada 3 meses (trimestral)
```bash
# Ejecutar el 1 de enero, abril, julio y octubre a las 9:00 AM
0 9 1 1,4,7,10 * /ruta/completa/al/proyecto/run_cron.sh

# Ejecutar cada 3 meses el primer lunes del mes a las 8:30 AM
30 8 1-7 1,4,7,10 1 /ruta/completa/al/proyecto/run_cron.sh
```

#### Otras opciones útiles
```bash
# Cada mes (primer día del mes a las 9:00 AM)
0 9 1 * * /ruta/completa/al/proyecto/run_cron.sh

# Cada 6 meses (enero y julio)
0 9 1 1,7 * /ruta/completa/al/proyecto/run_cron.sh

# Prueba: cada día a las 10:00 AM (solo para testing)
0 10 * * * /ruta/completa/al/proyecto/run_cron.sh
```

### 🛠️ Instalación Paso a Paso

#### 1. Obtener ruta absoluta del proyecto
```bash
cd /ruta/a/tu/proyecto/PruebaE-mails
pwd
# Copiar la ruta completa que aparece
```

#### 2. Editar crontab del usuario
```bash
crontab -e
```

#### 3. Añadir la línea de configuración
Elegir una de las opciones de arriba y reemplazar `/ruta/completa/al/proyecto/` con tu ruta real.

**Ejemplo para envío trimestral:**
```bash
# Recordatorio de vacaciones RRHH - cada 3 meses
0 9 1 1,4,7,10 * /home/kiglesias/grd-data-platform/PruebaE-mails/run_cron.sh
```

#### 4. Verificar instalación
```bash
# Ver tareas programadas
crontab -l

# Verificar logs del sistema
tail -f /var/log/syslog | grep CRON
```

### 📝 Logging y Monitoreo

#### Ubicación de logs
- **Logs del script**: `logs/cron_email_YYYYMMDD_HHMMSS.log`
- **Logs del sistema**: `/var/log/syslog` (buscar "CRON")

#### Verificar última ejecución
```bash
# Ver logs más recientes
ls -la logs/cron_email_*.log | tail -5

# Ver contenido del último log
tail -20 logs/cron_email_$(ls logs/cron_email_*.log | sort | tail -1 | cut -d'/' -f2)
```

### 🧪 Testing

#### Prueba manual del script
```bash
# Ejecutar manualmente para probar
./run_cron.sh

# Verificar que no hay errores
echo $?
```

#### Programar prueba en crontab
```bash
# Añadir temporalmente una ejecución cada 5 minutos para probar
*/5 * * * * /ruta/completa/al/proyecto/run_cron.sh

# RECORDAR: Eliminar esta línea después de probar
```

### 🔧 Configuración Avanzada

#### Variables de entorno en crontab
Si necesitas variables específicas, añádelas al inicio del crontab:
```bash
# Editar crontab
crontab -e

# Añadir variables al inicio
PATH=/usr/local/bin:/usr/bin:/bin
MAILTO=admin@tuempresa.com

# Luego las tareas programadas
0 9 1 1,4,7,10 * /ruta/completa/al/proyecto/run_cron.sh
```

#### Notificaciones por email
```bash
# Recibir email solo si hay errores
0 9 1 1,4,7,10 * /ruta/completa/al/proyecto/run_cron.sh >/dev/null

# Recibir email siempre
0 9 1 1,4,7,10 * /ruta/completa/al/proyecto/run_cron.sh
```

### 📊 Programación Recomendada por Empresa

#### Empresa pequeña (< 50 empleados)
- **Frecuencia**: Cada 6 meses
- **Día**: Primer lunes de enero y julio
- **Hora**: 9:00 AM

#### Empresa mediana (50-200 empleados)
- **Frecuencia**: Cada 3 meses (trimestral)
- **Día**: Primer día del trimestre
- **Hora**: 8:30 AM

#### Empresa grande (> 200 empleados)
- **Frecuencia**: Mensual
- **Día**: Primer lunes del mes
- **Hora**: 8:00 AM

### 🚨 Solución de Problemas

#### Cron no ejecuta el script
1. Verificar permisos: `chmod +x run_cron.sh`
2. Verificar ruta absoluta en crontab
3. Verificar logs: `tail -f /var/log/syslog | grep CRON`

#### Emails no se envían
1. Verificar configuración `.env`
2. Ver logs del script: `tail logs/cron_email_*.log`
3. Probar ejecución manual: `./run_cron.sh`

#### Sin logs generados
1. Verificar permisos de escritura en directorio `logs/`
2. Crear directorio manualmente: `mkdir -p logs`
3. Verificar que crontab esté ejecutándose

### 📚 Referencias

- [Crontab Guru](https://crontab.guru) - Generador de expresiones cron
- [Documentación oficial de Cron](https://man7.org/linux/man-pages/man5/crontab.5.html)
- Logs del sistema: `/var/log/syslog`
