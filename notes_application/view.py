# Ввод/вывод в консоль

class InterfaceConsoleNotes():

    def __init__(self) -> None:
        pass

    #
    def commandView(self):
        flag = False
        msg = ''
        while flag != True:
            msg = input("\nВведите команду: ")
            flag = self.controlInput(msg)
        return msg

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
        if cod == 1:
            print(f"Файл {id} открыт.")
        elif cod == 11:
            print(f"Файл {id} создан.")
        elif cod == 2:
            print(f"Заметка id={id} сохранена.")
        elif cod == 3:
            print(f"Заметка id={id} удалена.")
        elif cod == 4:
            print("Неправильная команда. Чтобы узнать список команд, введите команду 'h' или 'help' ...")
        elif cod == 41:
            print("Какая-то ошибка в commandSelection()")
        elif cod == 5:
            print(f"Заметка id={id} создана.")
        elif cod == 6:
            print(f"Заметка id={id} изменена.")
        else:
            print(f"Проблемка: {cod}...{id}")
    
    # Добавление заметки
    def addNoteView(self):
        listMsg = ['Введите заголовок заметки: ', 'Введите тело заметки: ']
        for i in listMsg:
            yield input(i)
    
    # Чтение заметки
    def readNoteView(self, note):
        listMsg = ['Заметка id=','Дата создания/изменения: ','Заголовок заметки: ','Тело заметки: ']
        for i in range(4):
            print(listMsg[i] + str(note[i]))
        pass
    
    # Чтение всех заметок
    def readAllNoteView(self, notes):
        print(notes)
        print(' id   Дата созд./изм.       Заголовок     Тело заметки    ') # 4 20 12 16 by 2
        print('{:>4}{:>20}{:>16}{:>20}'.format('id','Дата созд./изм.','Заголовок','Тело заметки'))

        for i in range(len(notes)):
            titleFormat = notes[i][1]
            if len(titleFormat) > 12:
                titleFormat = titleFormat[:9] + '...'
            msgFormat = notes[i][2]
            if len(msgFormat) > 16:
                msgFormat = msgFormat[:9] + '...'
            print('{:>4}{:>20}{:>16}{:>20}'.format(i,notes[i][0],titleFormat,msgFormat))
        pass
    
    # Проверка на отсутствие пустой строки
    def controlInput(self, temp) -> bool:
        if temp != '':
            return True
        else:
            print("Вы ничего не ввели. Попробуйте снова...")
            return False
    
    #
    def commandHelpView(self):
        print()