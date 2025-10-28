import smtplib
import os
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from jinja2 import Template

# Agregar el directorio config al path para importar settings
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'config'))
from settings import SMTP_CONFIG, PATHS, EMAIL_CONFIG, SAMPLE_EMPLOYEES

# ==========================
# FUNCIÓN PARA CARGAR PLANTILLA
# ==========================
def cargar_plantilla():
    """Carga la plantilla HTML desde archivo"""
    with open(PATHS['vacation_template'], 'r', encoding='utf-8') as f:
        return f.read()

# ==========================
# FUNCIÓN PARA ENVIAR EMAIL
# ==========================
def enviar_email(destinatario, asunto, html_content, imagen_logo):
    msg = MIMEMultipart("related")
    msg["Subject"] = asunto
    msg["From"] = SMTP_CONFIG['user']
    msg["To"] = destinatario

    # Alternativas (texto + HTML)
    msg_alternative = MIMEMultipart("alternative")
    msg.attach(msg_alternative)

    # Adjuntar HTML
    msg_alternative.attach(MIMEText(html_content, "html"))

    # Adjuntar imagen como logo
    with open(imagen_logo, "rb") as f:
        logo = MIMEImage(f.read())
        logo.add_header("Content-ID", "<logo_empresa>")
        msg.attach(logo)

    # Enviar correo
    with smtplib.SMTP(SMTP_CONFIG['server'], SMTP_CONFIG['port']) as server:
        server.starttls()
        server.login(SMTP_CONFIG['user'], SMTP_CONFIG['password'])
        server.sendmail(SMTP_CONFIG['user'], destinatario, msg.as_string())

# ==========================
# SCRIPT PRINCIPAL
# ==========================
def main():
    # Cargar plantilla HTML
    html_template = cargar_plantilla()
    
    # Usar datos de prueba estáticos
    empleados_prueba = SAMPLE_EMPLOYEES

    print("🔄 Procesando empleados con datos de prueba...")
    
    # Procesar cada empleado
    for emp in empleados_prueba:
        nombre = emp['nombre']
        email = emp['email']
        asignados = emp['vacaciones_asignadas']
        usados = emp['vacaciones_usadas']
        restantes = asignados - usados

        print(f"\n📋 Procesando empleado: {nombre}")
        print(f"   📧 Email: {email}")
        print(f"   📅 Vacaciones: {usados}/{asignados} usadas, {restantes} restantes")

        # Renderizar HTML
        template = Template(html_template)
        html_content = template.render(
            nombre=nombre,
            asignados=asignados,
            usados=usados,
            restantes=restantes
        )

        # Verificar configuración SMTP antes de enviar
        if not SMTP_CONFIG['user'] or not SMTP_CONFIG['password']:
            print(f"⚠️ No se pueden enviar emails: faltan credenciales SMTP en el archivo .env")
            print(f"   SMTP_USER: {'✅ Configurado' if SMTP_CONFIG['user'] else '❌ Falta'}")
            print(f"   SMTP_PASS: {'✅ Configurado' if SMTP_CONFIG['password'] else '❌ Falta'}")
            print(f"📄 HTML generado correctamente para {nombre}")
            continue
            
        try:
            # Enviar email
            enviar_email(email, EMAIL_CONFIG['subject'], html_content, PATHS['logo'])
            print(f"✅ Email enviado exitosamente a {nombre} ({email})")
        except Exception as e:
            print(f"❌ Error enviando email a {nombre}: {str(e)}")

if __name__ == "__main__":
    if not os.path.exists(PATHS['logo']):
        print("⚠️ Debes guardar un archivo 'logo.png' en la carpeta assets/")
    else:
        main()
