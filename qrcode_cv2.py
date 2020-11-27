from pyzbar.pyzbar import decode
import cv2
import os
import pprint

wifi_info=decode(cv2.imread(os.path.curdir+'/test_images/wifi.jpeg'))
pprint.pprint(wifi_info)