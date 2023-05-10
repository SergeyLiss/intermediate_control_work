#
from datetime import datetime

class ActNotes():

    def __init__(self, table):
        self.table = table
        self.id = 0
        pass

    # Add Note in Table
    def addNote(self, title, msg, id=None):
        timeNow = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if id == None:
            self.table += [[timeNow, title, msg]]
        else:
            self.table[id] = [[timeNow, title, msg]]
        pass

    # Read Note in Table
    def readNote(self):
        return self.table[self.id]
    
    # Delete Note in Table
    def delNote(self):
        self.table = self.table[:self.id] + self.table[(self.id+1):]
        pass
    
    # Change Note in Table
    def changeNote(self, newMsg):
        self.table[self.id] = newMsg
        pass
