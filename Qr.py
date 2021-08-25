import qrcode

img = qrcode.make("xxx")
f = open("output.png", "wb")
img.save(f)
f.close()