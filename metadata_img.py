import os
from PIL import Image
from PIL.ExifTags import TAGS

img_file='img2.jpeg'
image=Image.open(img_file)

exif={}
for tag,value in image._getexif().items():
     if tag in TAGS:
          exif[TAGS[tag]]=value

print(exif)