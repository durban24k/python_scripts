from pyzbar.pyzbar import decode
from PIL import Image
import os

info=decode(Image.open(os.path.curdir+'/test_images/wifi.jpeg'))
print(info)