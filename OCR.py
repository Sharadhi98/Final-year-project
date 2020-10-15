import pytesseract
from PIL import Image
import os

def createText():
#    os.system('./textcleaner ./images/funny.png ./images/funny1.png ')
    img = Image.open('./images/funny.png')
    print( img )
    result = pytesseract.image_to_string(img)
    with open("./texts/tts.txt",mode="w+") as file:

        file.write(result)
        print(result)

