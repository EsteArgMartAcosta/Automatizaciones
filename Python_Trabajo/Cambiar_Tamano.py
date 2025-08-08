from PIL import Image
from pathlib import Path

# === CONFIGURACIÓN ===
ANCHO, ALTO = 1280, 720
CALIDAD = 80  # Entre 1 y 100 (recomendado 70–85 para buena compresión)

# Carpetas
carpeta_origen = Path.home() / "Downloads" / "Telegram"
carpeta_salida = carpeta_origen / "Redimensionadas"
carpeta_salida.mkdir(exist_ok=True)

# Extensiones válidas
extensiones = ['.jpg', '.jpeg', '.png', '.bmp']

contador = 1

for archivo in carpeta_origen.iterdir():
    if archivo.suffix.lower() in extensiones:
        try:
            with Image.open(archivo) as img:
                img_convertida = img.convert("RGB")
                img_redimensionada = img_convertida.resize((ANCHO, ALTO))

                nombre_nuevo = f"portada_{contador}.jpg"
                ruta_salida = carpeta_salida / nombre_nuevo

                # Guardar con compresión y calidad ajustada
                img_redimensionada.save(
                    ruta_salida,
                    format='JPEG',
                    quality=CALIDAD,
                    optimize=True
                )

                print(f"✅ {archivo.name} → {nombre_nuevo} (calidad: {CALIDAD})")
                contador += 1

        except Exception as e:
            print(f"⚠️ Error procesando {archivo.name}: {e}")

print(f"\n✅ {contador - 1} imagen(es) optimizadas y guardadas en: {carpeta_salida}")
