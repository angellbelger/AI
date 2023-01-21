import qrcode
from PIL import Image

# lista com as páginas
paginas = ['http://exemplo2.com', 'http://exemplo3.com']

# cria o QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data('\n'.join(paginas))
qr.make(fit=True)

# salva a imagem
img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")
