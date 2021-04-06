__author__ = "Dylan Martie, Tate Price"
__copyright__ = "Copyright 2021, Dylan Martie & Tate Price"
__credits__ = ["Jack Hance, Benjamin Harvey, Dylan Martie, James Palmer, Tate Price"]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Dylan Martie, Tate Price"
__email__ = "dylan.martie@ndsu.edu, tate.price@ndsu.edu"
__status__ = "Production"

# required packages:
# treepoem 3.9.0
# ghostscript 0.7
# pillow 8.2.0

import os
import string
import PIL
from PIL import Image
from pylibdmtx.pylibdmtx import decode
import treepoem

# @parameter p: textFile .txt
# @returns: imageFile .png
def createDataMatrix():

    # changing working direcotry to work with Tate's system
    os.chdir("/Users/tateprice 1/Desktop/CSCI 404/steg")

    # reading contents of text file
    textFile = open("./sample.txt", "r")
    textFileContent = textFile.read()

    splitLength = 40    # number split every n characters
    textFileContentList = [textFileContent[i:i+splitLength] for i in range(0, len(textFileContent), splitLength)]
    textFile.close()
      
    for i in range(0, len(textFileContentList)):
        #generating data matrices with treepoem    
        img = treepoem.generate_barcode(barcode_type='datamatrix', data=textFileContentList[i],)

        # removing white pixels from image
        img = img.convert("RGBA")
        datas = img.getdata()
        newData = []
        for item in datas:
            if item[0] == 255 and item[1] == 255 and item[2] == 255:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)

        # saving image to file       
        img.putdata(newData)
        img.save('./matricies/matrix' + str(i) + '.png')


def readDataMatrix():
   for i in range(0, len(textFileContentList)):
   decode(Image.open('./matricies/matrix' + str(i) + '.png'))
    
    print(decode(Image.open('./matricies/matrix0.png')))

createDataMatrix()
readDataMatrix()