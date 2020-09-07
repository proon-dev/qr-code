import pyqrcode
import png
from pyqrcode import QRCode
QRstring = "https://github.com/diegosntts" # Coloque o link aqui
url = pyqrcode.create(QRstring)
url.png('Desktop\qr.png', scale = 8)