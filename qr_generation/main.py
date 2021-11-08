from qr import *

if __name__ == "__main__":
    img = qr_generate_image("hola")
    qr_export_image(img)
