import pyqrcode as qr
from pyqrcode import QRCode


Url = 'vijay'

qr_code = qr.create(Url)

qr_code.png("myTrebas", scale=8)

qr_code.show()