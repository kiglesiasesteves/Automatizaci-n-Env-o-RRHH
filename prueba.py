import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from jinja2 import Template
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# ==========================
# CONFIGURACIONES
# ==========================
DB_URL = os.getenv("DB_URL", "sqlite:///empleados.db")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")

# ==========================
# PLANTILLA HTML DEL EMAIL
# ==========================
html_template = """
<!DOCTYPE html>
<html>
  <body style="font-family: Arial, sans-serif; color: #333;">
    <div style="max-width: 600px; margin: auto; padding: 20px; border-radius: 10px; background: #f9f9f9;">
      <div style="text-align:center;">
        <img src="cid:logo_empresa" alt="Logo" width="120" style="margin-bottom:20px;">
      </div>
      <h2 style="color: #2E86C1;">¡Hola {{ nombre }}!</h2>
      <p>Te recordamos el estado de tus vacaciones:</p>
      <ul>
        <li><strong>Asignados:</strong> {{ asignados }} días</li>
        <li><strong>Usados:</strong> {{ usados }} días</li>
        <li><strong>Restantes:</strong> <span style="color: #27AE60;">{{ restantes }} días</span></li>
      </ul>
      <p>Recuerda planificar tus vacaciones con anticipación 😊</p>
      <hr style="margin:30px 0;">
      <footer style="text-align:center; font-size: 12px; color: #888;">
        <p>Equipo de RRHH · Tu Empresa S.A.</p>
        <p><a href="https://www.tuempresa.com" style="color:#2E86C1; text-decoration:none;">www.tuempresa.com</a></p>
      </footer>
    </div>
  </body>
</html>
"""

# ==========================
# FUNCIÓN PARA ENVIAR EMAIL
# ==========================
def enviar_email(destinatario, asunto, html_content, imagen_logo):
    msg = MIMEMultipart("related")
    msg["Subject"] = asunto
    msg["From"] = SMTP_USER
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
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.sendmail(SMTP_USER, destinatario, msg.as_string())

# ==========================
# SCRIPT PRINCIPAL
# ==========================
def main():
    # Datos de prueba estáticos (sin usar base de datos)
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
        if not SMTP_USER or not SMTP_PASS:
            print(f"⚠️ No se pueden enviar emails: faltan credenciales SMTP en el archivo .env")
            print(f"   SMTP_USER: {'✅ Configurado' if SMTP_USER else '❌ Falta'}")
            print(f"   SMTP_PASS: {'✅ Configurado' if SMTP_PASS else '❌ Falta'}")
            print(f"📄 HTML generado correctamente para {nombre}")
            continue
            
        try:
            # Enviar email
            enviar_email(email, "📅 Recordatorio de tus vacaciones", html_content, "logo.png")
            print(f"✅ Email enviado exitosamente a {nombre} ({email})")
        except Exception as e:
            print(f"❌ Error enviando email a {nombre}: {str(e)}")

if __name__ == "__main__":
    if not os.path.exists("logo.png"):
        print("⚠️ Debes guardar un archivo 'logo.png' en la misma carpeta que este script.")
    else:
        main()
