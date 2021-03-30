import os
from pylibdmtx.pylibdmtx import encode
from PIL import Image
import random
import string
from pylibdmtx.pylibdmtx import encode

os.chdir("/Users/tateprice 1/Desktop/CSCI 404/steg")

textFile = open("./sample.txt", "r")
textFileContent = textFile.read()

splitLength = 35    # number split every n characters
textFileContentList = [textFileContent[i:i+splitLength] for i in range(0, len(textFileContent), splitLength)]
textFile.close()

#letters = string.ascii_lowercase

for i in range(20):
#    random_data = ''.join(random.choice(letters) for i in range(10))
    encoded = encode(textFileContentList[i])
    img = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
            
    img.putdata(newData)
    img.save('/Users/tateprice 1/Desktop/CSCI 404/steg/matricies/test' + str(i) + '.png')
