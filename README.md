# 📧 Automatización de Envío de Emails RRHH

Sistema automatizado para enviar recordatorios de vacaciones a empleados mediante email con plantillas HTML personalizadas.

## 📋 Descripción

Esta aplicación permite enviar automáticamente emails a empleados con información sobre sus vacaciones (días asignados, usados y restantes). Utiliza plantillas HTML profesionales y soporte para múltiples proveedores de email.

## 🚀 Características

- ✅ Envío automatizado de emails HTML
- ✅ Plantillas personalizables con Jinja2
- ✅ Soporte para múltiples proveedores SMTP (Gmail, Outlook, Yahoo)
- ✅ Configuración segura con variables de entorno
- ✅ Datos de prueba incluidos para testing
- ✅ Manejo de errores robusto
- ✅ Logo personalizable en emails

## 🛠️ Requisitos

### Dependencias de Python
```bash
python-dotenv>=1.0.0
jinja2>=3.0.0
Pillow>=9.0.0  # Para generar logo de prueba
```

### Configuración de Email
- Cuenta de email con autenticación SMTP habilitada
- Para Gmail: Contraseña de aplicación (2FA requerido)
- Para Outlook: SMTP AUTH habilitado en el tenant

## 📦 Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/kiglesiasesteves/Automatizaci-n-Env-o-RRHH.git
cd Automatizaci-n-Env-o-RRHH
```

### 2. Instalar dependencias
```bash
# Opción 1: Con pip (recomendado usar entorno virtual)
pip install python-dotenv jinja2 pillow

# Opción 2: Si hay problemas con entornos administrados
pip install python-dotenv jinja2 pillow --break-system-packages
```

### 3. Configurar variables de entorno
```bash
# Copiar archivo de ejemplo
cp .env.example .env

# Editar .env con tus credenciales
nano .env
```

## ⚙️ Configuración

### Archivo `.env`

Crea un archivo `.env` en la raíz del proyecto con la siguiente configuración:

```bash
# Configuración de base de datos (opcional)
DB_URL=sqlite:///empleados.db

# Configuración SMTP
# Para Gmail:
SMTP_SERVER=smtp.gmail.com
# Para Outlook/Hotmail:
# SMTP_SERVER=smtp-mail.outlook.com
# Para Yahoo:
# SMTP_SERVER=smtp.mail.yahoo.com

SMTP_PORT=587
SMTP_USER=tu_email@gmail.com
SMTP_PASS=tu_contraseña_de_aplicacion
```

### Configuración por Proveedor

#### 🔵 Gmail
1. Habilitar autenticación de 2 factores
2. Ir a [Contraseñas de aplicaciones](https://myaccount.google.com/apppasswords)
3. Generar nueva contraseña para "Correo"
4. Usar esa contraseña de 16 caracteres en `SMTP_PASS`

#### 🔷 Microsoft Outlook/Hotmail
1. Verificar que SMTP AUTH esté habilitado en tu organización
2. Usar tu email y contraseña normal
3. Si es cuenta empresarial, contactar al administrador de IT

#### 🟡 Yahoo
1. Habilitar "Aplicaciones menos seguras" o usar contraseña de aplicación
2. Configurar `SMTP_SERVER=smtp.mail.yahoo.com`

## 🏃‍♂️ Uso

### Instalación rápida
```bash
# Ejecutar script de instalación automática
./setup.sh
```

### Ejecución manual
```bash
# Script principal completo
python src/email_sender.py

# Script simplificado
python src/email_sender_simple.py
```

### Comandos de Django (si aplica)
```bash
# Si tienes configuración de Django
python manage.py send_vacation_summary
```

## 📁 Estructura del Proyecto

```
📦 PruebaE-mails/
├── � src/                          # Código fuente principal
│   ├── 📄 email_sender.py           # Script principal completo
│   ├── 📄 email_sender_simple.py    # Versión simplificada
│   └── 📄 models.py                 # Modelos de datos (Django)
├── � templates/                    # Plantillas de email
│   └── 📄 vacation_reminder.html    # Plantilla HTML para emails
├── 📁 assets/                       # Recursos (imágenes, etc.)
│   ├── 🖼️ logo.png                  # Logo para emails
│   └── 📄 logo_instructions.txt     # Instrucciones para el logo
├── 📁 config/                       # Configuraciones
│   ├── 📄 .env.example              # Plantilla de configuración
│   └── 📄 settings.py               # Configuraciones centralizadas
├── � docs/                         # Documentación adicional
│   └── 📄 setup_guide.md            # Guía detallada de configuración
├── � .env                          # Variables de entorno (NO subir a git)
├── 📄 .gitignore                    # Archivos ignorados por git
├── 📄 README.md                     # Este archivo
├── 📄 requirements.txt              # Dependencias de Python
├── � setup.sh                      # Script de instalación automática
└── 📁 venv/                         # Entorno virtual (opcional)
```

## 🧪 Testing

### Datos de Prueba
El script incluye datos de prueba por defecto:

```python
empleados_prueba = [
    {
        'nombre': 'Keyla Anais',
        'email': 'keylaanais15@gmail.com',
        'vacaciones_asignadas': 30,
        'vacaciones_usadas': 10
    },
    {
        'nombre': 'Juan Pérez', 
        'email': 'juan.perez@ejemplo.com',
        'vacaciones_asignadas': 25,
        'vacaciones_usadas': 5
    }
]
```

### Probar sin enviar emails
Para probar sin enviar emails reales, puedes:
1. Usar emails de prueba (ejemplo@test.com)
2. Modificar el script para guardar HTML en archivos
3. Verificar configuración SMTP con credenciales vacías

## 🎨 Personalización

### Modificar Plantilla HTML
Edita la variable `html_template` en `prueba.py`:

```python
html_template = """
<!DOCTYPE html>
<html>
<body style="font-family: Arial, sans-serif;">
    <h2>¡Hola {{ nombre }}!</h2>
    <p>Tu información de vacaciones:</p>
    <!-- Personaliza aquí -->
</body>
</html>
"""
```

### Cambiar Logo
Reemplaza `logo.png` con tu logo empresarial (recomendado: 120x60 píxeles, formato PNG).

### Agregar Empleados
Modifica la lista `empleados_prueba` en el script o conecta con una base de datos real.

## 🔒 Seguridad

- ⚠️ **NUNCA** subas el archivo `.env` al repositorio
- ✅ Usa contraseñas de aplicación, no contraseñas normales
- ✅ El archivo `.env` está incluido en `.gitignore`
- ✅ Usa `.env.example` para compartir la estructura de configuración

## 🚨 Solución de Problemas

### Error: "Username and Password not accepted"
- **Gmail**: Necesitas contraseña de aplicación, no contraseña normal
- **Outlook**: Verificar que SMTP AUTH esté habilitado

### Error: "SmtpClientAuthentication is disabled"
- Problema común en cuentas empresariales de Microsoft
- Contactar administrador de IT para habilitar SMTP AUTH

### Error: "No module named 'dotenv'"
```bash
pip install python-dotenv
```

### Error: "No such file: logo.png"
```bash
# El script generará automáticamente un logo de prueba
python3 prueba.py
```

## 📝 Logs y Monitoreo

El script muestra información detallada:
```
🔄 Procesando empleados con datos de prueba...

📋 Procesando empleado: Keyla Anais
   📧 Email: keylaanais15@gmail.com
   📅 Vacaciones: 10/30 usadas, 20 restantes
✅ Email enviado exitosamente a Keyla Anais
```

## 🤝 Contribución

1. Fork el proyecto
2. Crea tu rama de características (`git checkout -b feature/nueva-caracteristica`)
3. Commit tus cambios (`git commit -am 'Agregar nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver archivo `LICENSE` para más detalles.

## 👥 Autor

- **Keyla Iglesias** - [kiglesiasesteves](https://github.com/kiglesiasesteves)

## 📞 Soporte

Si tienes problemas o preguntas:
1. Revisa la sección de solución de problemas
2. Abre un issue en GitHub
3. Contacta al equipo de desarrollo

---

⭐ Si este proyecto te fue útil, ¡no olvides darle una estrella en GitHub!
>>>>>>> Stashed changes
