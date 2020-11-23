from PIL import Image
from PIL.ExifTags import TAGS

# read our image from current dir
my_img = Image.open("1.png")
# extract exif data
exif_data = my_img.getexif()
# iterrating over all exif data
for tagId in exif_data:
    # get the tag name
    tag = TAGS.get(tagId, tagId)
    data = exif_data.get(tagId)

    print(f"{tag:16}: {data}")