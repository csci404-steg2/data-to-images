# macos brew install libdmtx

import os
os.chdir("/Users/tateprice 1/Desktop/CSCI 404/steg")

textFile = open("./sample.txt", "r")
textFileContent = textFile.read()

splitLength = 45    # number split every n characters
textFileContentList = [textFileContent[i:i+splitLength] for i in range(0, len(textFileContent), splitLength)]
textFile.close()
print(textFileContentList)

