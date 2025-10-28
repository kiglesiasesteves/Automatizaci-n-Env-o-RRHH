#!/bin/bash
# Script de instalación para el sistema de emails RRHH

echo "🚀 Instalando sistema de emails RRHH..."

# Crear archivo .env si no existe
if [ ! -f ".env" ]; then
    echo "📄 Creando archivo .env desde template..."
    cp config/.env.example .env
    echo "✅ Archivo .env creado. Recuerda configurar tus credenciales SMTP."
fi

# Instalar dependencias
echo "📦 Instalando dependencias de Python..."
pip install -r requirements.txt

# Generar logo si no existe
if [ ! -f "assets/logo.png" ]; then
    echo "🎨 Generando logo de ejemplo..."
    python3 -c "
from PIL import Image, ImageDraw, ImageFont
import os

# Crear directorio si no existe
os.makedirs('assets', exist_ok=True)

# Crear imagen simple
img = Image.new('RGB', (120, 60), color='#2E86C1')
draw = ImageDraw.Draw(img)

try:
    font = ImageFont.truetype('/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf', 20)
except:
    font = ImageFont.load_default()

text = 'RRHH'
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
x = (120 - text_width) // 2
y = (60 - text_height) // 2
draw.text((x, y), text, fill='white', font=font)

img.save('assets/logo.png')
print('✅ Logo generado en assets/logo.png')
" 2>/dev/null || echo "⚠️ No se pudo generar logo automáticamente. Agrega manualmente assets/logo.png"
fi

echo "✅ Instalación completada!"
echo ""
echo "📋 Próximos pasos:"
echo "1. Edita el archivo .env con tus credenciales SMTP"
echo "2. Ejecuta: python src/email_sender.py"
echo ""
echo "📖 Ver documentación completa en docs/setup_guide.md"
