import os
import string
import PIL
from PIL import Image
from pylibdmtx.pylibdmtx import encode
from pylibdmtx.pylibdmtx import decode

def createDataMatrix():
    
    os.chdir("/Users/tateprice 1/Desktop/CSCI 404/steg")

    textFile = open("./sample.txt", "r")
    textFileContent = textFile.read()

    splitLength = 40    # number split every n characters
    textFileContentList = [textFileContent[i:i+splitLength] for i in range(0, len(textFileContent), splitLength)]
    textFile.close()
    
    encoded = encode('hello world')
    img = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)
    img.save('./matricies/dmtx.png')
    
#    for i in range(0, len(textFileContentList)):
#        encoded = encode(textFileContentList[i])
        
        
#        img = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)
#        img = img.convert("RGBA")

#        datas = img.getdata()
#
#        newData = []
#        for item in datas:
#            if item[0] == 255 and item[1] == 255 and item[2] == 255:
#                newData.append((255, 255, 255, 0))
#            else:
#                newData.append(item)
                
#        img.putdata(newData)
#        img.save('./matricies/matrix' + str(i) + '.png')

def readDataMatrix():
#    for i in range(0, len(textFileContentList)):
#    decode(Image.open('./matricies/matrix' + str(i) + '.png'))
    
    print(decode(Image.open('./matricies/dmtx.png')))

createDataMatrix()
readDataMatrix()
