from exif import Image
with open('rename.png','rb') as image_file:
    my_image=Image(image_file)

print(my_image.has_exif)
dir(my_image)

# Read and modify image EXIF metadata using Python.
# Link: https://gitlab.com/TNThieding/exif/badges/master/pipeline.svg
# Link: https://gitlab.com/tnthieding/exif/badges/master/coverage.svg