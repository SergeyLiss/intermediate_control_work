import json

class ActFileJson():

    def __init__(self, nameFile) -> None:
        self.nameFile = nameFile + ".json"
        self.dataFile = []
        pass

    def readFJ(self):
        potokFile = open(self.nameFile, "r")
        self.dataFile = json.loads(potokFile.readlines()[0])
        potokFile.close()
        pass
    
    def writeFJ(self):
        potokFile = open(self.nameFile, "w")
        potokFile.write(json.dumbs(self.dataFile))
        potokFile.close()
        pass