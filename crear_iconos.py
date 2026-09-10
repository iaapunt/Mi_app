from PIL import Image, ImageDraw, ImageFont

def crear_icono(tamano, archivo):
    imagen = Image.new("RGB", (tamano, tamano), "#111827")
    dibujo = ImageDraw.Draw(imagen)

    margen = tamano // 10

    dibujo.ellipse(
        (margen, margen, tamano - margen, tamano - margen),
        fill="#2563eb"
    )

    try:
        fuente = ImageFont.truetype(
            "/data/data/com.termux/files/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            tamano // 4
        )
    except:
        fuente = ImageFont.load_default()

    texto = "AI"

    caja = dibujo.textbbox((0, 0), texto, font=fuente)

    ancho = caja[2] - caja[0]
    alto = caja[3] - caja[1]

    x = (tamano - ancho) / 2
    y = (tamano - alto) / 2

    dibujo.text(
        (x, y),
        texto,
        fill="white",
        font=fuente
    )

    imagen.save(archivo)


crear_icono(192, "icons/icon-192.png")
crear_icono(512, "icons/icon-512.png")

print("Iconos creados correctamente")
0

