import qrcode
from PIL import Image

DEFAULT_EXPORT_PATH = "./output/qr1.png"

def qr_generate_image(parameters):
    '''
    genera una imagen de qr en base a 'parameters'
    retorna dicha imagen
    '''
    qr = qrcode.QRCode(
        version=8,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    feed_data = parameters
    qr.add_data(feed_data)
    return qr.make_image(fill_color="black", back_color="white")

def qr_export_image(image, path=DEFAULT_EXPORT_PATH):
    '''
    guarda 'image' como archivo en 'path'
    '''
    image.save(path)
