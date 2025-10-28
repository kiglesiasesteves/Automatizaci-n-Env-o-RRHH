"""
Configuraciones centralizadas para el sistema de envío de emails RRHH
"""
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# ==========================
# CONFIGURACIONES SMTP
# ==========================
SMTP_CONFIG = {
    'server': os.getenv("SMTP_SERVER", "smtp.gmail.com"),
    'port': int(os.getenv("SMTP_PORT", "587")),
    'user': os.getenv("SMTP_USER"),
    'password': os.getenv("SMTP_PASS"),
}

# ==========================
# CONFIGURACIONES DE BASE DE DATOS
# ==========================
DATABASE_CONFIG = {
    'url': os.getenv("DB_URL", "sqlite:///empleados.db"),
}

# ==========================
# CONFIGURACIONES DE ARCHIVOS
# ==========================
PATHS = {
    'logo': os.path.join(os.path.dirname(__file__), '..', 'assets', 'logo.png'),
    'templates': os.path.join(os.path.dirname(__file__), '..', 'templates'),
    'vacation_template': os.path.join(os.path.dirname(__file__), '..', 'templates', 'vacation_reminder.html'),
}

# ==========================
# CONFIGURACIONES DE EMAIL
# ==========================
EMAIL_CONFIG = {
    'subject': "📅 Recordatorio de tus vacaciones",
    'from_name': "Equipo RRHH",
}

# ==========================
# DATOS DE PRUEBA
# ==========================
SAMPLE_EMPLOYEES = [
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
