from send2trash import send2trash
from pathlib import Path

# Ruta correcta a la carpeta "Screenshots"
carpeta_screenshots = Path("C:/Users/ocioc/Pictures/Screenshots")

# Verificar si existe
if not carpeta_screenshots.exists():
    print(f"⚠️ La carpeta '{carpeta_screenshots}' no existe.")
    exit()

# Eliminar contenido enviándolo a la papelera
archivos_enviados = 0
carpetas_enviadas = 0

for item in carpeta_screenshots.iterdir():
    try:
        send2trash(str(item))
        if item.is_file():
            archivos_enviados += 1
            print(f"🗑️ Archivo enviado a papelera: {item.name}")
        elif item.is_dir():
            carpetas_enviadas += 1
            print(f"🗑️ Carpeta enviada a papelera: {item.name}")
    except Exception as e:
        print(f"⚠️ Error al eliminar {item.name}: {e}")

# Resultado
print(f"\n✅ Limpieza completa.")

