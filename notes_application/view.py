#

class InterfaceConsoleNotes():

    def __init__(self) -> None:
        pass

    # Открытие файла
    def openFileView(self):
        flag = False
        msg = ''
        while flag != True:
            msg = input("Введите имя файла (без расширения): ")
            flag = self.controlInput(msg)
        return msg
    
    # Результаты работы методов: открыть файл, сохранить заметку, удалить заметку
    def resultAllView(self, cod, id=None):
        if cod == 0:
            print(f"Файл {id}.json открыт.")
        elif cod == 2:
            print(f"Заметка id={id} сохранена.")
        elif cod == 4:
            print(f"Заметка id={id} удалена.")
        else:
            print(f"Проблемка: {cod}...{id}")
    
    # Добавление заметки
    def addNoteView(self):
        listMsg = ['Введите заголовок заметки: ', 'Введите тело заметки: ']
        for i in listMsg:
            yield input(i)
    
    # Чтение заметки
    def readNoteView(self, note):
        listMsg = ['Заметка id=','Заголовок заметки: ','Тело заметки: ','Дата создания/изменения: ']
        for i in range(4):
            print(listMsg[i] + note[i])
        pass
    
    # Проверка на отсутствие пустой строки
    def controlInput(self, temp) -> bool:
        if temp != '':
            return True
        else:
            print("Вы ничего не ввели. Попробуйте снова...")
            return False