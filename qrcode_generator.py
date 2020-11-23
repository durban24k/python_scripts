import qrcode

def qrCode():
     #data
     data='https://www.google.com'
     #filename
     file_name='qrcode.png'
     # function to generate the qrcode
     img=qrcode.make(data=data)
     #save as image
     img.save(file_name)

if __name__ == "__main__":
     qrCode()