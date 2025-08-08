from pathlib import Path
from send2trash import send2trash

# Ruta de Descargas y carpeta a excluir
carpeta_descargas = Path.home() / "Downloads"
carpeta_excluir = carpeta_descargas / "Telegram"

# Contadores
archivos_enviados = 0
carpetas_enviadas = 0

# Verificar que la carpeta Telegram existe
if not carpeta_excluir.exists():
    print("⚠️ La carpeta 'Telegram' no existe. El script no continuará.")
    exit()

# Recorrer los elementos de la carpeta Descargas
for item in carpeta_descargas.iterdir():
    if item != carpeta_excluir:
        try:
            send2trash(str(item))
            if item.is_file():
                archivos_enviados += 1
                print(f"🗑️ Archivo enviado a la papelera: {item.name}")
            elif item.is_dir():
                carpetas_enviadas += 1
                print(f"🗑️ Carpeta enviada a la papelera: {item.name}")
        except Exception as e:
            print(f"⚠️ Error con {item.name}: {e}")

# Resultado
print(f"\n✅ Proceso completado.")
print(f"📌 Carpeta preservada: {carpeta_excluir}")
