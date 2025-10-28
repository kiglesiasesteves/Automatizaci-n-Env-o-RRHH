# 📖 Guía de Configuración Detallada

## 🔧 Configuración paso a paso

### 1. Gmail
1. **Habilitar 2FA:**
   - Ve a [Configuración de Google](https://myaccount.google.com/security)
   - Activa "Verificación en 2 pasos"

2. **Crear contraseña de aplicación:**
   - Ve a [Contraseñas de aplicación](https://myaccount.google.com/apppasswords)
   - Selecciona "Correo" y "Otro"
   - Copia la contraseña de 16 caracteres generada

3. **Configurar .env:**
   ```bash
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   SMTP_USER=tu_email@gmail.com
   SMTP_PASS=abcd efgh ijkl mnop
   ```

### 2. Microsoft Outlook
1. **Verificar configuración organizacional:**
   - Contacta a tu administrador de IT
   - Solicita habilitar SMTP AUTH

2. **Configurar .env:**
   ```bash
   SMTP_SERVER=smtp-mail.outlook.com
   SMTP_PORT=587
   SMTP_USER=tu_email@empresa.com
   SMTP_PASS=tu_contraseña_normal
   ```

### 3. Yahoo Mail
1. **Habilitar aplicaciones menos seguras o generar contraseña de aplicación**

2. **Configurar .env:**
   ```bash
   SMTP_SERVER=smtp.mail.yahoo.com
   SMTP_PORT=587
   SMTP_USER=tu_email@yahoo.com
   SMTP_PASS=tu_contraseña_aplicacion
   ```

## 🚀 Ejecución

### Desde la raíz del proyecto:
```bash
# Script completo
python src/email_sender.py

# Script simplificado
python src/email_sender_simple.py
```

## 🎨 Personalización

### Modificar plantilla de email:
Edita `templates/vacation_reminder.html`

### Cambiar datos de empleados:
Edita `config/settings.py` en la sección `SAMPLE_EMPLOYEES`

### Cambiar logo:
Reemplaza `assets/logo.png` con tu logo empresarial

## 🔍 Troubleshooting

### Errores comunes y soluciones:

**Error: No module named 'settings'**
- Asegúrate de ejecutar desde la raíz del proyecto
- Verifica que existe `config/settings.py`

**Error: Template not found**
- Verifica que existe `templates/vacation_reminder.html`
- Ejecuta desde la raíz del proyecto

**Error: Logo not found**
- Verifica que existe `assets/logo.png`
- O ejecuta el script para que genere uno automáticamente
