from view import InterfaceConsoleNotes
from file_action import ActFileJson
from notes_action import ActNotes

class Models(InterfaceConsoleNotes, ActNotes, ActFileJson):

    def __init__(self):
        super().__init__()
        pass

    #
    def openFile(self):
        ActFileJson.__init__(self, self.openFileView())
        temp = self.readFJ()
        if temp == 11:
            self.writeFJ()
        self.resultAllView(temp, self.nameFile)
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
        if temp == 0:
            self.openFile()
        elif temp == 1:
            self.saveToFile()
        elif temp == 2:
            pass
        elif temp == 3:
            pass
        elif temp == 4:
            pass
        elif temp == 5:
            pass
        elif temp == 6:
            pass
        elif temp == 7:
            pass
        elif temp == 8:
            exit
        else:
            self.resultAllView(41)
    
    #
    def saveToFile(self, id='All'):
        self.dataFile = self.table
        self.writeFJ()
        self.resultAllView(id)



            

    


test = Models()
test.commandCicle()
