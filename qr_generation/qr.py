import qrcode
from PIL import Image
from pathlib import Path

DEFAULT_EXPORT_DIR_PATH = Path(__file__).parent / "output"
DEFAULT_OUTPUT_FILENAME = "output.png"

def qr_generate_image(parameters):
    
    qr = qrcode.QRCode(
        version=4,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    feed_data = parameters
    qr.add_data(feed_data)
    return qr.make_image(fill_color="black", back_color="white")

def qr_export_image(image, path=DEFAULT_EXPORT_DIR_PATH):
    '''y
    guarda 'image' como archivo en 'path'
    '''
    image.save((path / DEFAULT_OUTPUT_FILENAME).resolve())
