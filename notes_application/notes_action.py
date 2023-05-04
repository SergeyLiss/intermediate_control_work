#
import datetime

class ActNotes():

    def __init__(self, table):
        self.table = table
        pass

    # Add Note in Table
    def addNote(self, title, msg, id = None):
        if id == None:
            self.table += [datetime.now(), title, msg]
        else:
            self.table[id] = [datetime.now(), title, msg]
        pass

    # Read Note in Table
    def readNote(self, id):
        return self.table[id]
    
    # Delete Note in Table
    def delNote(self, id):
        self.table = self.table[:id] + self.table[(id+1):]
        pass
    
    # Change Note in Table
    def changeNote(self, id, newMsg):
        self.table[id] = newMsg
        pass
