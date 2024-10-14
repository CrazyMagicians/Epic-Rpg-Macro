optionsFilePath = __file__.replace("options_resolver.py","options.ini")

def importData(filePath=optionsFilePath):
    retList = {}
    with open(filePath,"r") as optionsFile:
        optionsData = optionsFile.read().splitlines()
    for line in optionsData:
        option,value = line.split("=")
        retList[option] = value
    
    return retList

def editData(option,value,filePath=optionsFilePath): #unused
    newOptionsData = ""
    with open(filePath,"r") as optionsFile:
        optionsData = optionsFile.read()
    for line in optionsData.splitlines():
        key = line.split("=")[0]
        if key == option:
            newOptionsData += option+"="+value+"\n"
        else:
            newOptionsData += line + "\n"

    newOptionsData = newOptionsData[:-1]
    with open(filePath,"w") as optionsFile:
        optionsFile.write(newOptionsData)
      
