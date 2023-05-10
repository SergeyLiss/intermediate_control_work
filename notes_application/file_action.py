# Работа с файлом
import json

class ActFileJson():

    def __init__(self, nameFile) -> None:
        self.nameFile = nameFile + ".json"
        self.dataFile = []
        pass

    def readFJ(self):
        try:
            with open(self.nameFile, "r") as potokFile:
                temp = potokFile.readlines()
                if len(temp) > 0:
                    self.dataFile = json.loads(temp[0])
                return 1
        except FileNotFoundError:
            newFile = open(self.nameFile, "w")
            newFile.close()
            return 11
    
    def writeFJ(self):
        with open(self.nameFile, "w") as potokFile:
            potokFile.write(json.dumps(self.dataFile))
        pass
    