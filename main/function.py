from generate.settings import BASE_DIR, BASE_URL
import pyqrcode
import png


def create_qrcode(request, link):
    message = link.url
    text = pyqrcode.create(message)
    text.png(f"{BASE_DIR}/media/img/{link.id}.png", scale=8)
    return f"{BASE_URL}/media/img/{link.id}.png"




