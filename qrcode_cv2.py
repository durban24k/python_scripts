from pyzbar.pyzbar import decode
from pyzbar.pyzbar import Decoded
import cv2
import os
import pprint

wifi_info=decode(cv2.imread(os.path.curdir+'/test_images/wifi.jpeg'))

print(wifi_info)
for info in wifi_info:
     pprint.pprint(info)