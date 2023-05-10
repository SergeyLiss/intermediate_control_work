# Координация между элементами программы
from view import InterfaceConsoleNotes
from file_action import ActFileJson
from notes_action import ActNotes

class Models(InterfaceConsoleNotes, ActNotes, ActFileJson):

    def __init__(self):
        super().__init__()
        pass

    #
    def commandCicle(self):
        comm = 0
        while comm != 8:
            msg = self.commandView()
            msg = '.' + msg + '.'
            comm = self.commandList(msg)
            if comm != -1:
                self.commandSelection(comm)
            else:
                self.resultAllView(4)
    
    #
    def commandList(self, temp):
        listCommand = {0: '.o.open.',
                       1: '.s.save.c.close.',
                       2: '.a.add.',
                       3: '.r.read.',
                       4: '.w.write.',
                       5: '.d.del.delete.',
                       6: '.l.list.rl.readlist.',
                       7: '.h.help.',
                       8: '.e.exit.'}
        
        for i in range(9):
            if temp in listCommand[i]:
                return i
        
        return -1
    
    #
    def commandSelection(self, temp):
        if temp == 0:                           # open
            self.openFile()
        elif temp == 1:                         # save, close
            self.saveToFile()
        elif temp == 2:                         # add
            self.addToTable()
        elif temp == 3:                         # read
            self.readFromTable()
        elif temp == 4:                         # write
            self.writeToTable()
        elif temp == 5:                         # delete
            self.deleteFromTable()
        elif temp == 6:                         # read list
            self.readListFromTable()
        elif temp == 7:                         # help
            self.commandHelpView()
        elif temp == 8:                         # exit
            exit
        else:                                   # Непредвиденная ошибка
            self.resultAllView(41)
        pass

    # 0. open
    def openFile(self):
        ActFileJson.__init__(self, self.openFileView())
        temp = self.readFJ()
        if temp == 11:
            self.writeFJ()
        self.resultAllView(temp, self.nameFile)
        ActNotes.__init__(self, self.dataFile)
        pass
    
    # 1. save, close
    def saveToFile(self):
        self.dataFile = self.table
        self.writeFJ()
        self.resultAllView(2, self.id)
        pass

    # 2. add
    def addToTable(self):
        dataNote = ['','']
        j = 0

        for i in self.addNoteView():
            dataNote[j] = i
            j += 1
        self.id = len(self.table)
        self.addNote(dataNote[0], dataNote[1])
        self.resultAllView(5, self.id)
        pass
        
    # 3. read
    def readFromTable(self):
        self.readNoteView([self.id] + self.readNote())
        pass

    # 4. write
    def writeToTable(self):
        dataNote = ['','']
        j = 0

        for i in self.addNoteView():
            dataNote[j] = i
            j += 1
        self.id = len(self.table)
        self.addNote(dataNote[0], dataNote[1])
        self.resultAllView(5, self.id)
        pass

    # 5. delete
    def deleteFromTable(self):
        self.delNote()
        self.resultAllView(3, self.id)

    # 6. read list
    def readListFromTable(self):
        self.readAllNoteView(self.table)
        pass




            

    


test = Models()
test.commandCicle()
